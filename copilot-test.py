# Create a function that extracts text from a csv file. Include any libraries that may be needed. The function should output a python dictionary with the key being the column name and value being the text from the cell.

import csv  # import csv library

def extract_text_from_csv(csv_file):
    """
    Extract text from a csv file and return a dictionary with the key being the column name and value being the text from the cell.
    """
    with open(csv_file, newline='') as csvfile:  # open csv file
        reader = csv.DictReader(csvfile)  # read csv file
        for row in reader:  # iterate through rows
            print(row)  # print row

extract_text_from_csv('copilot-test.csv')  # call function  # output: {'name': 'John', 'age': '25', 'city': 'New York'}

