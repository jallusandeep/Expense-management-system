import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

# Create logger at the module level
logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    try:
        # Add logging for connection attempts
        logger.info("Attempting database connection")
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="expense_manager"
        )
        if connection.is_connected():
            logger.info("MySQL Connected successfully")
            print("MySQL Connected successfully")
        
        cursor = connection.cursor(dictionary=True)
        yield cursor
        
        if commit:
            connection.commit()
            logger.info("Transaction committed")
    except mysql.connector.Error as err:
        logger.error(f"Database error: {err}")
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()
            logger.info("Database connection closed")

# Rest of your functions with added logging
def fetch_all_records():
    logger.info("Fetching all records")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        logger.info(f"Retrieved {len(expenses)} records")
        return expenses

def fetch_expenses_for_date(expense_date):
    logger.info(f"Fetching expenses for date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        logger.info(f"Retrieved {len(expenses)} records for date {expense_date}")
        for i in expenses:
            print(i)
        return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Inserting expense: date={expense_date}, amount={amount}, category={category}, notes={notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )
        logger.info("Expense added successfully")
        print("Expense added successfully!")

def delete_expense_for_date(expense_date):
    logger.info(f"Deleting expenses for date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))
        logger.info(f"Expenses for {expense_date} deleted successfully")
        print(f"Expenses for {expense_date} deleted successfully!")

def fetch_expense_summary(start_date, end_date):
    logger.info(f"Fetching expense summary from {start_date} to {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''
            SELECT category, SUM(amount) as total 
            FROM expenses 
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category;
            ''',
            (start_date, end_date)
        )
        summary = cursor.fetchall()
        logger.info(f"Retrieved summary with {len(summary)} categories")
        return summary

#if __name__ == "__main__":
    #logger.info("Starting application")
    #fetch_expenses_for_date("2024-08-01")
    #insert_expense("2024-08-01", 1227.0, "Rent","Monthly rent payment")
    #delete_expense_for_date("2022-08-02")
    #fetch_expense_summary("2024-08-01", "2024-08-05")
    #logger.info("Application finished")