#CRUD operations here.
import mysql.connector
from contextlib import contextmanager
import os
import sys


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="iknowmypass",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    print("Closing cursor")
    cursor.close()
    connection.close()


def fetch_all_records():
    query = "SELECT * from expenses"

    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def insert_expense(expense_date, amount, category, notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expense_summary(start_date,end_date):
    with get_db_cursor() as cursor:
        cursor.execute(
            '''select category,SUM(amount) as total
                from expenses
                where expense_date
                between %s and %s
                group by category;''',
            (start_date,end_date)
        )
        data=cursor.fetchall()
        return data
if __name__ == "__main__":
    # project_root=os.path.join(os.path.dirname(__file__),'..')
    # print("**Project Root: ",project_root)
    # fetch_all_records()
    # expenses=fetch_expenses_for_date("2024-08-01")
    # delete_expenses_for_date("2024-08-25")
    # # delete_expenses_for_date("2024-08-20")
    # # fetch_expenses_for_date("2024-08-20")
    # print(expenses)
    summary=fetch_expense_summary("2024-08-01","2024-08-05")
    for record in summary:
        print(record)

    
