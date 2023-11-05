"""
Chat button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def accept(event, values, instance):
    if event == '--':
        pass
        # Get input values and add to chat
        return True

