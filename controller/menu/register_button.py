"""
Register button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import model.accounts.account_handler as accounts
import view.menu_view as view


def accept(event, values, instance):
    if event == '-REGISTER_BUTTON-':
        email_exists = accounts.check_for_item(values['-EMAIL_2-'], 'email')
        name_exists = accounts.check_for_item(values['-NAME-'], 'name')
        # Note: the name 'des' would conflict with internal file names
        if not email_exists and not name_exists and values['-NAME-'] != 'des':
            # Add account
            accounts.add_account(values['-NAME-'], values['-EMAIL_2-'], values['-PASSWORD_2-'])
            # Add current user
            view.Menu_View.set_user(accounts.get_display_name(values['-EMAIL_2-']))
            # Switch screen
            instance.window['-COL_REGISTER-'].update(visible=False)
            instance.window['-COL_HOME-'].update(visible=True)
            # Update name on home screen
            view.Menu_View.load_home_page(instance)
        elif email_exists:
            sg.Popup('Register failed. Email already in use.')
        elif name_exists:
            sg.Popup('Register failed. Name already in use.')
    return True