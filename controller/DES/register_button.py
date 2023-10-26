"""
Register button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import model.data.accounts as accounts
import view.data_explorer_view as view


def accept(event, values, instance):
    keep_going = True
    if event == '-REGISTER_BUTTON-':
        email_exists = accounts.check_for_item(values['-EMAIL_2-'], 'email')
        print("email_exists: ", email_exists)
        name_exists = accounts.check_for_item(values['-NAME-'], 'name')
        print("name_exists: ", name_exists)
        print("values: ", values)
        if not email_exists and not name_exists:
            # Add account
            accounts.add_account(values['-NAME-'], values['-EMAIL_2-'], values['-PASSWORD_2-'])
            # Add current user
            view.DES_View.user = values['-NAME-']
            print("view.DES_View.user: ", view.DES_View.user)
            # Switch screen
            instance.window[f'-COL_REGISTER-'].update(visible=False)
            instance.window[f'-COL_HOME-'].update(visible=True)
        elif email_exists:
            sg.Popup('Register failed. Email already in use.')
        elif name_exists:
            sg.Popup('Register failed. Name already in use.')
    return keep_going