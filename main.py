from utils import add, sub, multiply, divide, exponent, modulo, floor_divide, absolute

def main():
    while True:
        
        print("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):")
        opcion = input().lower().strip()
        
        if opcion == "exit":
            break
            
        opciones_validas = ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute"]
        if opcion not in opciones_validas:
            print("Invalid option!")
            continue
            
        if opcion == "absolute":
           
            num = float(input("Enter the number: "))
            result = absolute(num)
        else:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if opcion == "add":
                result = add(num1, num2)
            elif opcion == "subtract":
                result = sub(num1, num2)
            elif opcion == "multiply":
                result = multiply(num1, num2)
            elif opcion == "divide":
                result = divide(num1, num2)
            elif opcion == "exponent":
                result = exponent(num1, num2)
            elif opcion == "modulo":
                result = modulo(num1, num2)
            elif opcion == "floor_divide":
                result = floor_divide(num1, num2)
        
        if isinstance(result, str):
            print(result)
        else:
            
            print(f"The result is: {result}")

if __name__ == "__main__":
    main()