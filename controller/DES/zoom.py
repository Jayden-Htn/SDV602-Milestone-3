"""
Register button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import model.data.accounts as accounts


def accept(event, values, instance):
    keep_going = True
    if event == '':
        pass
    return keep_going