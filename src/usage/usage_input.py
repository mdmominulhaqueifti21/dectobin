from dectobin import decimal_to_binary

num = input("Enter decimal number: ")

try:
    if '.' in num:
        num = float(num)
    else:
        num = int(num)

    print("Binary:", decimal_to_binary(num))

except:
    print("Please enter a valid number.")
