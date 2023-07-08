def calculate_gift_tax(value_of_gift):
    if value_of_gift < 5000:
        print("No tax!")
    elif 5000 <= value_of_gift < 25000:
        tax = 100 + (value_of_gift - 5000) * 0.08
        print(f"Amount of tax: {tax} euros")
    elif 25000 <= value_of_gift < 55000:
        tax = 1700 + (value_of_gift - 25000) * 0.10
        print(f"Amount of tax: {tax} euros")
    elif 55000 <= value_of_gift < 200000:
        tax = 4700 + (value_of_gift - 55000) * 0.12
        print(f"Amount of tax: {tax} euros")
    elif 200000 <= value_of_gift < 1000000:
        tax = 22100 + (value_of_gift - 200000) * 0.15
        print(f"Amount of tax: {tax} euros")
    else:
        tax = 142100 + (value_of_gift - 1000000) * 0.17
        print(f"Amount of tax: {tax} euros")

def main():
    value_of_gift = float(input("Value of gift: "))
    calculate_gift_tax(value_of_gift)

main()
