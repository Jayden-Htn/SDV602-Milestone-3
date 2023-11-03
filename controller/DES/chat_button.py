"""
Chat button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def accept(event, values, instance):
    keep_going = True
    if event == '--':
        pass
        # Get input values and add to chat
    return keep_going

