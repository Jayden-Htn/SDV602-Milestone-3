"""
Login page button controller
"""
import sys
sys.dont_write_bytecode = True

def accept(event, values, instance):
    print('login_page.py: accept()', event)
    # Change window 1 layout to login layout
    if event == '-LOGIN_PAGE-':
        instance.window['-COL_WELCOME-'].update(visible=False)
        instance.window['-COL_LOGIN-'].update(visible=True)
    return True
