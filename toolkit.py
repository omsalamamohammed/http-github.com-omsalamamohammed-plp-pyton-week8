import random

def guessing_game():
    """Tool 1: Number Guessing Game"""
    secret_number = random.randint(1, 100)
    attempts = 0
    print("\n--- Number Guessing Game ---")
    print("I picked a number from 1 to 100. Try to guess!")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try higher.")
            elif guess > secret_number:
                print("Too high! Try lower.")
            else:
                print(f"Correct! You won in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number!")

def todo_list():
    """Tool 2: Simple To-Do List Manager"""
    tasks = []
    print("\n--- To-Do List Manager ---")
    
    while True:
        print("\n1. Add Task  2. View Tasks  3. Remove Task  4. Back to Main Menu")
        choice = input("Choose: ")

        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
            print(f"Added: {task}")
        elif choice == '2':
            if not tasks:
                print("No tasks yet!")
            else:
                print("\nYour Tasks:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
        elif choice == '3':
            if not tasks:
                print("No tasks to remove!")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
                try:
                    num = int(input("Enter task number to remove: ")) - 1
                    removed = tasks.pop(num)
                    print(f"Removed: {removed}")
                except:
                    print("Invalid number!")
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

def calculator():
    """Tool 3: Simple Calculator"""
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif op == '/':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Cannot divide by zero!")
        else:
            print("Invalid operation!")
    except ValueError:
        print("Please enter valid numbers!")

# Main Menu Loop
while True:
    print("\n==============================")
    print("  ADAM'S PERSONAL MINI-TOOLKIT")
    print("==============================")
    print("1. Number Guessing Game")
    print("2. To-Do List Manager")
    print("3. Calculator")
    print("4. Exit")
    
    main_choice = input("Choose tool (1-4): ")

    if main_choice == '1':
        guessing_game()
    elif main_choice == '2':
        todo_list()
    elif main_choice == '3':
        calculator()
    elif main_choice == '4':
        print("Goodbye! Thanks for using the toolkit.")
        break
    else:
        print("Invalid choice! Please choose 1-4.")