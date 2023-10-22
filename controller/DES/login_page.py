"""
Login page button controller
"""
import sys
sys.dont_write_bytecode = True
import view.data_explorer_view as view

def accept(event, values, instance):
    print('login_page.py: accept()', event)
    # Change window 1 layout to login layout
    if event == '-LOGIN_PAGE-':
        instance.window[f'-COL_WELCOME-'].update(visible=False)
        instance.window[f'-COL_LOGIN-'].update(visible=True)
    return True
