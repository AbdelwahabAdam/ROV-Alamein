def calc():
    print("Operations: +, -, *, /, avg")
    operation = input("Enter operation: ").strip()

    if operation == "avg":
        numbers = input("Enter the numbers separated by space: ").split()
        numbers = [float(x) for x in numbers]
        answer = sum(numbers) / len(numbers)

    else:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the 2nd number: "))

        if operation == "+":
            answer = first + second
        elif operation == "-":
            answer = first - second
        elif operation == "*":
            answer = first * second
        elif operation == "/":
            if second != 0:
                answer = first / second
            else:
                answer = "Error: can't divide by zero"
        else:
            answer = "Invalid choice"

    print("Answer:", answer)


calc()
