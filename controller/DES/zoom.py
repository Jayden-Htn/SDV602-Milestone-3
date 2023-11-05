"""
Register button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import model.data.accounts as accounts


def accept(event, values, instance):
    if event == '':
        pass
    return True