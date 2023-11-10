"""
Exit button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
from view.window_view import Window_View


def accept(event, values, state):
    if event in (sg.WIN_CLOSED, '-EXIT-', '-EXIT_2-'):   
        return False
    return True