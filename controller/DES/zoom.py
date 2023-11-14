"""
Register button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import view.explorer_view as des_view


def accept(event, values, instance):
    if event == '-ZOOM-':
        # Regenerate chart with new zoom
        des_view.DES_View.set_data(instance)

        pass
    return True