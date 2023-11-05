"""
Data set controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def accept(event, values, instance):
    if event == '--':
        pass
        # Popup for data set updating
        # Local or url
        return True

