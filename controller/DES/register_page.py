"""
Register page button controller
"""
import sys
sys.dont_write_bytecode = True

def accept(event, values, instance):
    print('register_page.py: accept()', event)
    # Change window 1 layout to register layout
    if event == '-REGISTER_PAGE-':
        instance.window[f'-COL_WELCOME-'].update(visible=False)
        instance.window[f'-COL_REGISTER-'].update(visible=True)
    return True