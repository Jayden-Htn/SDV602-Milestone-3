"""
    Description: This file contains the functions that handle the events from GUI inputs.

    Functions:
        validate_login(values): This function gets the login details from the login form.
        register_screen(values): This function gets the register details from the registration form.
        window_1_handler(event, values): This function handles the input from the first window.
        window_2_handler(event, values): This function handles the input from the second window.
        event_processor(event, values, window): This function processes the events from the window and passes to the specifc window handler.
""" 


# Import modules
import account_manager.account_handler as accounts


# Functions
def validate_login(values):
    """
        This function gets the login details from the login form and checks if the account exists.

        Parameters:
            values (dict): The values from the window.

        Returns:
            screen (str): The screen to go to.
            username (dict): The username to be displayed on the next screen (if applicable).
    """
    # Get the values from the window
    email = values['-IN_LOGIN_EMAIL-'].lower()
    password = values['-IN_LOGIN_PASSWORD-']
    # Check if the account exists
    response = accounts.verify_correct_account(email, password)
    # Return the screen to go to
    if response:
        return 'HOME', {'username': accounts.get_display_name()}
    return 'LOGIN', {}


def register_screen(values):
    """
        This function gets the register details from the registration form and checks if the account exists.

        Parameters:
            values (dict): The values from the window.
            
        Returns:
            screen (str): The screen to go to.
            username (dict): The username to be displayed in the welcome message (if applicable).
    """
    # Get the values from the window
    username = values['-IN_REGISTER_NAME-']
    email = values['-IN_REGISTER_EMAIL-'].lower()
    password = values['-IN_REGISTER_PASSWORD-']

    # Check if either the username or email already exists (must be unique)
    if accounts.check_for_item(username, 'name') or accounts.check_for_item(email, 'email'):
        return 'REGISTER', {}
    # Add the account to the csv file
    accounts.add_account(username, email, password)
    return 'HOME', {'username': username}


def window_1_handler(event, values):
    """
        This function handles the input from the first window.

        Parameters:
            event (str): The event from the window.
            values (dict): The values from the window.

        Returns:
            screen (str): The screen to go to.
            user (dict): Username to open DES screen for (if applicable).
    """
    # Back buttons
    if event in ('-BTN_LOGIN_BACK-', '-BTN_REGISTER_BACK-'):
        return 'WELCOME', {}
    
    # Welcome page
    elif event == '-BTN_WELCOME_LOGIN-':
        return 'LOGIN', {}
    elif event == '-BTN_WELCOME_REGISTER-':
        return 'REGISTER', {}
    
    # Login page
    elif event == '-BTN_LOGIN_LOGIN-':
        return validate_login(values)
    
    # Register page
    elif event == '-BTN_REGISTER_REGISTER-':
        return register_screen(values)
    
    # Home page
    elif event == '-BTN_HOME_MY_DES-':
        return 'MYDES', {}
    
    # Check if the event is to open a user DES window
    des_list = [ f'-BTN_HOME_DES_{a}-' for a in accounts.get_account_names()]
    if event in des_list:
        return 'DES', {'user': event.split('_')[-1].split('-')[0]}
    
    # General catch all
    return 'HOME'


def window_2_handler(event, values):
    # Implemented in the next version
    pass


def event_processor(event, values, window):
    """
        This function processes the events from the window and passes to the specifc window handler.

        Parameters:
            event (str): The event from the window.
            values (dict): The values from the window.
            window (int): The window to process the event for.

        Returns:
            screen (str): The screen to go to.
            kwargs (dict): Optional values to be passed to the next screen.
                username: The username to be displayed in the welcome message.
                user: The DES screen to open.
    """
    # Pass the event to the correct window handler
    if window == 1:
        return window_1_handler(event, values)
    else:
        return window_2_handler(event, values)
    