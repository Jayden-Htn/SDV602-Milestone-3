"""
Register page button controller
"""
import sys
sys.dont_write_bytecode = True

def accept(event, values, instance):
    # Change window 1 layout to register layout
    if event == '-REGISTER_PAGE-':
        instance.window['-COL_WELCOME-'].update(visible=False)
        instance.window['-COL_REGISTER-'].update(visible=True)
    return True