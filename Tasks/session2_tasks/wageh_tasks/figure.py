def draw_pyramid():
    rows = int(input("Enter a number between 1 and 20: "))
    
    if rows < 1 or rows > 20:
        print("Please enter a number from 1 to 20.")
        return
    
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

draw_pyramid()
