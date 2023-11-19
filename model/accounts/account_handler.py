"""
    This module contains the functions that handle the accounts.

    Functions:
        verify_account(email, password): This function checks if the account exists with the correct password.
        check_for_item(item, item_type): This function checks if the item exists in the csv file (e.g. username, email).
        get_display_name(user_email): This function gets the display name of the account.
        add_account(name, email, password): This function adds an account to the csv file.
        get_account_names(): This function gets the names of the accounts.
        get_other_names(name): This function gets the names of the other accounts.
"""


# Imports
import model.accounts.database_reader as files


# Procedures
def verify_account(email, password):
    """
        This function checks if the account exists with the correct password.

        Parameters:
            email (str): The email of the account.
            password (str): The password of the account.

        Returns:
            Exists (bool): If the account exists or not.
    """
    # Retrieve the data from the csv file
    data = files.read_csv_file()
    
    # Check if the account exists
    for account in data:
        if account[1] == email and account[2] == password:
            return True
    return False


def check_for_item(item, item_type):
    """
        This function checks if the item exists in the csv file (e.g. username, email).

        Parameters:
            item (str): The item to be checked.
            item_type (str): The type of item to be checked.

        Returns:
            Exists (bool): Returns true if the item exists, false otherwise.
    """
    # Retrieve the data from the csv file
    data = files.read_csv_file()

    # Identify the column to check
    if item_type == 'name':
        col = 0
    elif item_type == 'email':
        col = 1
    else:
        col = 2

    # Check if the item exists
    for account in data:
        if account[col].lower() == item.lower():
            return True
    return False


def get_display_name(user_email):
    """
        This function gets the display name of the account.

        Parameters:
            email (str): The email of the account.

        Returns:
            display_name (str): The display name of the account.
    """
    data = files.read_csv_file()
    for name, email, password in data:
        if email == user_email:
            return name


def add_account(name, email, password):
    """
        This function adds an account to the csv file.

        Parameters:
            name (str): The name of the account.
            email (str): The email of the account.
            password (str): The password of the account.
    """
    global username
    
    data = files.read_csv_file()
    data.append([name, email, password])
    files.write_csv_file(data)
    username = name


def get_account_names():
    """
        This function gets the names of the accounts.

        Returns:
            names (list): The names of the accounts.
    """
    data = files.read_csv_file()
    names = [account[0] for account in data]
    return names


def get_other_names(name):
    """
        This function gets the names of the other accounts.

        Parameters:
            name (str): The username of the active account.

        Returns:
            names (list): The names of the other accounts.
    """
    # Get the names of the accounts
    names = get_account_names()
    # Remove the active account as it is displayed separately from the other accounts
    names.remove(name)
    return names