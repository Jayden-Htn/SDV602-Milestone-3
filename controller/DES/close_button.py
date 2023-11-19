"""
Exit button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
from view.window_view import Window_View


def accept(event, values, state):
    if event in (sg.WIN_CLOSED, '-CLOSE-'):   
        state.window.close()
        Window_View.view_list.remove(state)
        # Stop chat thread
        state.chat_manager.stop()
        # If main menu is not open, exit program
        if len(Window_View.view_list) == 0:
            sys.exit()
    return True