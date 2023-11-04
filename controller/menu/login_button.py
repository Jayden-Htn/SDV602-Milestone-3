"""
Login button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import model.data.accounts as accounts
import view.menu_view as view

def accept(event, values, instance):
    keep_going = True
    if event == '-LOGIN_BUTTON-':
        accounts_exists = accounts.verify_account(values['-EMAIL-'], values['-PASSWORD-'])
        if accounts_exists:
            # Add current user
            view.Menu_View.set_user(accounts.get_display_name(values['-EMAIL-']))
            # Switch screen
            instance.window['-COL_LOGIN-'].update(visible=False)
            instance.window['-COL_HOME-'].update(visible=True)
            # Update name on home screen
            view.Menu_View.load_home_page(instance)
        else:
            sg.Popup('Login failed. Incorrect email or password.')
    return keep_going

