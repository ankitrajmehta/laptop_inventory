from datetime import datetime

def update_txt(data):
    with open("laptop.txt", "w") as edit_file:
        for row in data:
            line = ', '.join(row[1:])  # Join the elements of the row with a comma and space
            edit_file.write(line + '\n')  # Write the line to the file with a newline character


def buy_receipt(data, id, quantity):
    current_datetime = datetime.now()
    current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    name = input("Enter customer name: ")
    lap_name = data[id - 1][1]
    brand = data[id - 1][2]
    price = str(data[id - 1][3]).replace("$", "")
    total = quantity * int(price)
    total_shipping = total + 25 * quantity


    receipt_data = "\t \t Laptop Sale Receipt \n \n"\
                "--------------------------------------------\n"\
                f"Receipt for: {name}\n\n" \
                f"Date and Time: {current_datetime}\n" \
                f"Laptop Name: {lap_name}\n" \
                f"Brand: {brand}\n" \
                f"Total: ${total}\n" \
                f"Total (including shipping): ${total_shipping}"

    current_datetime = str(current_datetime)
    current_datetime = current_datetime.replace(" ","_")
    current_datetime = current_datetime.replace(":","_")
    current_datetime = current_datetime.replace("-","_")
    name = name.replace(" ","_")
    with open(f"{name}_sale_receipt_{current_datetime}.txt", 'w') as rec:
        rec.write(receipt_data)

    return receipt_data


def order_receipt(data,id , quantity):
    current_datetime = datetime.now()
    current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    lap_name = data[id - 1][1]
    brand = data[id - 1][2]
    price = str(data[id - 1][3]).replace("$", "")
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
    
    current_datetime = str(current_datetime)
    current_datetime = current_datetime.replace(" ","_")
    current_datetime = current_datetime.replace(":","_")
    current_datetime = current_datetime.replace("-","_")

    with open(f"order_receipt_{current_datetime}.txt", 'w') as rec:
        rec.write(order_data)

    return order_data