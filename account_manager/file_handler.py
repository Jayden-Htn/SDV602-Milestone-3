"""
    This module handles the reading and writing of the csv file.

    Functions:
        read_csv_file(): This function reads the csv file and returns the data.
        write_csv_file(data): This function writes the data to the csv file.
"""


# Import libraries
import csv


# Set global variables
global file_path 
file_path = './database/accounts.csv'


# Functions
def read_csv_file():
    """
        This function reads the csv file and returns the data.

        Returns:
            data (list): The data from the csv file.
    """
    global file_path

    # Read the csv file
    with open(file_path) as f:
        data = list(csv.reader(f))
    data.pop(0) # Remove the header
    return data


def write_csv_file(data):
    """
        This function writes the data to the csv file.

        Parameters:
            data (list): The data to be written to the csv file.
    """
    global filepath

    # Write the data to the csv file
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Email', 'Password']) # Add the header
        writer.writerows(data)


if __name__ == '__main__':
    # check that read and write work
    data = read_csv_file()
    print(data)
    data.append(['Jayden', 'j@email.com', 'password123'])
    write_csv_file(data)
    data = read_csv_file()
    print(data)


