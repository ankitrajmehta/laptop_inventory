from datetime import datetime

class Home():
    def __init__(self) :
        self.current_mode = 'home'
        id = 1
        self.data = []
        with open("laptop.txt") as file:
            for i, line in enumerate(file): #enumerate gives index as well as the element
                tmp = line.strip().split(', ')
                tmp.insert(0, str(i + 1))  # Add the ID number at the beginning of the row
                self.data.append(tmp)

               
        

    def display_home(self):
        print("\t \t Laptop Store Menu")
        for i in range(30):
            print(" =",end="")
        print("")

        for row in self.data:
            for element in row:
                print(element, end="  ")
            print("")

        print("Press 'o' to order new laptop")
        print("Press 's' to sell new laptop")
        print("Press 'e' to exit")
        inp = input("Press:")
        return inp
    
    def update_txt(self):
        with open("laptop.txt", "w") as edit_file:
            for row in self.data:
                line = ', '.join(row[1:])  # Join the elements of the row with a comma and space
                edit_file.write(line + '\n')  # Write the line to the file with a newline character


    def buy(self, id, quantity):
        self.data[id - 1][4] = int(self.data[id - 1][4])
        if self.data[id - 1][4] <= 0:
            print("No more remaining")
            return
        self.data[id - 1][4] -= quantity
        self.data[id - 1][4] = str(self.data[id - 1][4])
        self.update_txt()

    def buy_receipt(self, id, quantity):
        current_datetime = datetime.now()
        current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        name = input("Enter customer name: ")
        lap_name = self.data[id - 1][1]
        brand = self.data[id - 1][2]
        price = str(self.data[id - 1][3]).replace("$", "")
        total = quantity * int(price)
        total_shipping = total + 25


        receipt_data = "\t \t Laptop Sale Receipt \n \n"\
                    "--------------------------------------------\n"\
                    f"Receipt for: {name}\n\n" \
                    f"Date and Time: {current_datetime}\n" \
                    f"Laptop Name: {lap_name}\n" \
                    f"Brand: {brand}\n" \
                    f"Total: ${total}\n" \
                    f"Total (including shipping): ${total_shipping}"


        with open(f"{name}_sale_receipt_{current_datetime}.txt", 'w') as rec:
            rec.write(receipt_data)

    def order(self,id , quantity):
        self.data[id - 1][4] = int(self.data[id - 1][4])
        self.data[id - 1][4] += quantity
        self.data[id - 1][4] = str(self.data[id - 1][4])
        self.update_txt()

    def order_receipt(self,id , quantity):
        current_datetime = datetime.now()
        current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        lap_name = self.data[id - 1][1]
        brand = self.data[id - 1][2]
        price = str(self.data[id - 1][3]).replace("$", "")
        total = quantity * int(price)
        vat = (13 * total)/100
        total_vat = total + vat

        order_data = "\t \t Laptop Order Receipt \n \n"\
                    "--------------------------------------------\n"\
                    f"Date and Time: {current_datetime}\n" \
                    f"Laptop Name: {lap_name}\n" \
                    f"Brand: {brand}\n" \
                    f"Total (without VAT): ${total}\n" \
                    f"VAT: {vat} \n"\
                    f"Total (including shipping): ${total_vat}"
        with open(f"order_receipt_{current_datetime}.txt", 'w') as rec:
            rec.write(order_data)


    def run(self):
        running = True
        while running:
            inp = self.display_home()
            if inp == 'e':
                running= False
            elif inp == 's':
                try:
                    b = int(input("Enter id of Laptop You Want To sell:"))
                    q = int(input("Enter quantity of Laptop You Want To sell:"))
                    confirm = input(f"Are You sure you want to sell { q } units of { self.data[b - 1][1]} (Y/n)")
                    if confirm == "y" or confirm == "Y":
                        self.buy(b, q)
                        self.buy_receipt(b, q)
                except:
                    print("Invalid inputs")
            elif inp == 'o':
                try:
                    o = int(input("Enter id of Laptop You Want To order:"))
                    q_2 = int(input("Enter quantity of Laptop You Want To order:"))
                    confirm = input(f"Are You sure you want to order { q_2 } units of { self.data[o - 1][1]} (Y/n)")
                    if confirm == "y" or confirm == "Y":
                        self.order(o, q_2)
                        self.order_receipt(o, q_2)
                except:
                    print("Invalid inputs")
            else:
                print("None valid key clicked")


if __name__=="__main__":
    home = Home()
    home.run()