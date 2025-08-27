while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Average")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "6":
        print("Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            if b == 0:
                print("Error: Division by zero")
            else:
                print("Result:", a / b)

    elif choice == "5":
        nums = input("Enter numbers separated by spaces: ")
        num_list = [float(n) for n in nums.split()]
        if len(num_list) == 0:
            print("Error: No numbers provided")
        else:
            print("Average:", sum(num_list) / len(num_list))

    else:
        print("Invalid option. Try again.")
