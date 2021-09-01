# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
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
    print('please input sales data from the last market')
    print('data should be six numbers, separated by commas')
    print('for example: 20,18,30,25,22,15\n')

    data_str = input('Enter your data here: ')
    sales_data = data_str.split(',')
    validate_data(sales_data)

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


get_sales_data()
