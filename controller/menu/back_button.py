"""
Back button controller
"""
import sys
sys.dont_write_bytecode = True

def accept(event, values, instance):
    # Change window 1 layout back to welcome layout
    if event == '-BACK_BUTTON-' or event == '-BACK_BUTTON_2-':
        instance.window[f'-COL_LOGIN-'].update(visible=False)
        instance.window[f'-COL_REGISTER-'].update(visible=False)
        instance.window[f'-COL_WELCOME-'].update(visible=True)
    return True
