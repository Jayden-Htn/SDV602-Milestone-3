"""
    Description: This file contains the functions that handle the independant data requests from the GUI process.

    Functions:
        get_other_names(username): This function gets the names of the other accounts.
""" 


# Import modules
import account_manager.account_handler as accounts


def get_other_names(username):
    """
        This function gets the names of the other accounts.

        Parameters:
            username (str): The username of the active account.

        Returns:
            names (list): The names of the other accounts.
    """
    # Get the names of the accounts
    names = accounts.get_account_names()
    
    # Remove the active account as it is displayed separately from the other accounts
    names.remove(username)
    return names