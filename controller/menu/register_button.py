"""
Register button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import model.data.accounts as accounts
import view.menu_view as view


def accept(event, values, instance):
    if event == '-REGISTER_BUTTON-':
        email_exists = accounts.check_for_item(values['-EMAIL_2-'], 'email')
        name_exists = accounts.check_for_item(values['-NAME-'], 'name')
        if not email_exists and not name_exists:
            # Add account
            accounts.add_account(values['-NAME-'], values['-EMAIL_2-'], values['-PASSWORD_2-'])
            # Add current user
            view.Menu_View.user = values['-NAME-']
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