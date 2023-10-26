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
        accounts_exists = accounts.check_for_item('email', values['-EMAIL_2-'])
        accounts_exists_2 = accounts.check_for_item('name', values['-NAME-'])
        print("values: ", values)
        if not accounts_exists and not accounts_exists_2:
            # Add account
            accounts.add_account(values['-NAME-'], values['-EMAIL_2-'], values['-PASSWORD_2-'])
            # Add current user
            view.DES_View.user = values['-NAME-']
            print("view.DES_View.user: ", view.DES_View.user)
            # Switch screen
            instance.window[f'-COL_REGISTER-'].update(visible=False)
            instance.window[f'-COL_HOME-'].update(visible=True)
        else:
            sg.Popup('Login failed. Email or name already in use.')
    return keep_going