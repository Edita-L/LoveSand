# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    get sales input data from the user
    """
    while True:
      print('please input sales data from the last market')
      print('data should be six numbers, separated by commas')
      print('for example: 20,18,30,25,22,15\n')

      data_str = input('Enter your data here: ')
      sales_data = data_str.split(',')
      if validate_data(sales_data):
          print('data is valid')
          break
    return sales_data

def validate_data(values):
    """
    converts string values into integers or raisers valueError if string cannot be converted, or the number of values is not 6
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError (f'Exactly 6 values are required. you have provided {len(values)}')
    except ValueError as e:
        print(f'invalid data: {e}. please try again. \n')
        return False
    return True


def update_sales_worksheet(data):
    """
    update sales worksheet with a new row of the values provided
    """
    print("Updating sales worksheet..\n")

    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales worksheet updated successfully.\n")

def calculate_surplus_data(sales_row):
    """
    compare sales values with stock and calculate surplus number
    """
    print("calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(f'stock row {stock_row}')
    print(f'sales row {sales_row}')

    surplus_data = []
    for stock, sales in zip (stock_row,sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    return surplus_data

def update_surplus_worksheet(data):
    """
    update surplus worksheet with a new row of the values calculated
    """
    print("Updating surplus worksheet..\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("surplus worksheet updated successfully.\n")

def main():
    """
    run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_surplus_worksheet(new_surplus_data)

print("Welcome to love sandwiches\n")
main()