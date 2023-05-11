from time import sleep
from read import *
from write import *
from operations import *

class Home():
    def __init__(self) :
        self.data = readfile()
        self.disp = ""
        self.mode = "home"

    def display(self):
        if self.mode == "home":
            print("\t \t Laptop Store Menu")
            for i in range(30):
                print(" =",end="")
            print("")

            print("ID |Name    |Price |Quantity |Processor |Graphic card")

            for row in self.data:
                for element in row:
                    print(element, end="  ")
                print("")

            print("Press 'o' to order new laptop")
            print("Press 's' to sell new laptop")
            print("Press 'e' to exit")
            inp = input("Press:")
            return inp
        elif self.mode == "receipt":
            print(self.disp)
            input("Press Enter(RETURN) to continue")

    def run(self):
        running = True
        while running:
            self.mode = "home"
            inp = self.display()
            if inp == 'e':
                running= False
            elif inp == 's':
                try:
                    b = int(input("Enter id of Laptop You Want To sell:"))
                    if b > len(self.data):
                        raise KeyError
                    q = int(input("Enter quantity of Laptop You Want To sell:"))
                    if q < 0 :
                        print("Quantity must be over 0")
                        input("Press Enter(RETURN) to continue")
                        continue
                    if (int(self.data[b - 1][4]) - q) <= 0:
                        print("Not enough laptops")
                        input("Press Enter(RETURN) to continue")
                        continue
                    confirm = input(f"Are You sure you want to sell { q } units of { self.data[b - 1][1]} (Y/n)")
                    if confirm == "y" or confirm == "Y":
                        self.data = buy(self.data, b, q)
                        update_txt(self.data)
                        self.disp = buy_receipt(self.data, b, q)
                        self.mode = "receipt"
                        self.display()

                except ValueError:
                    print("Invalid inputs")
                    input("Press Enter(RETURN) to continue")
                except KeyError:
                    print("Invalid ID number")
                    input("Press Enter(RETURN) to continue")
                except KeyboardInterrupt:
                    running = False
                except :
                    print("Application Error")
                    input("Press Enter(RETURN) to continue")

            elif inp == 'o':
                try:
                    buy_list = []
                    o = int(input("Enter id of Laptop You Want To order:"))
                    if o > len(self.data):
                        raise KeyError
                    q_2 = int(input("Enter quantity of Laptop You Want To order:"))
                    confirm = input(f"Are You sure you want to order { q_2 } units of { self.data[o - 1][1]} (Y/n)")
                    if confirm == "y" or confirm == "Y":
                        order(self.data, o, q_2)
                        update_txt(self.data)
                        self.disp = order_receipt(self.data, o, q_2)
                        self.mode = "receipt"
                        self.display()
                except ValueError:
                    print("Invalid inputs")
                    input("Press Enter(RETURN) to continue")
                except KeyError:
                    print("Invalid ID number")
                    input("Press Enter(RETURN) to continue")
                except KeyboardInterrupt:
                    running = False
                except :
                    print("Application Error")
                    input("Press Enter(RETURN) to continue")
            else:
                print("None valid key clicked")
                input("Press Enter(RETURN) to continue")


if __name__=="__main__":
    home = Home()
    home.run()