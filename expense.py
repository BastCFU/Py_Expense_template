from PyInquirer import prompt
import csv

def load_users():
    users = []
    with open("users.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            users.append(row[0])  # Assuming the name is in the first column
    return users

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": load_users()
    },
    {
        "type":"list",
        "name":"involved_people",
        "message":"New Expense - Involved People : ",
        "choices": load_users()
    }
]

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]


def new_expense(*args):
    # Prompt the user for expense information
    expense_data = prompt(expense_questions)
    # Save the expense data to the CSV file
    with open("expense_report.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([expense_data['amount'], expense_data['label'], expense_data['spender'], expense_data['involved_people']])
    print("Expense Added!")
    return True

def new_user(*args):
    # Prompt the user for expense information
    user_data = prompt(user_questions)
    # Save the expense data to the CSV file
    with open("users.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([user_data['name']])
    print("User Added!")
    return True

