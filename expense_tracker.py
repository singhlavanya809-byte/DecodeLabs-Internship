print("================================")
print("      EXPENSE TRACKER")
print("================================")

filename = "expenses.txt"
total = 0
entries = []

while True:
    try:
        num_expenses = int(input("How many expenses do you want to enter? "))
        if num_expenses > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid whole number.")

for i in range(num_expenses):
    while True:
        try:
            expense = float(input(f"Enter expense {i+1}: "))
            break
        except ValueError:
            print("Please enter a valid number for the expense.")

    description = input("Description (optional): ").strip()
    entries.append((expense, description))
    total += expense

with open(filename, "a", encoding="utf-8") as file:
    for expense, description in entries:
        file.write(f"{expense:.2f}\t{description}\n")

print("\n================================")
print("Expense Summary")
print("================================")
print(f"Total Spent: {total:.2f}")
print(f"Entries saved to {filename}")
