"""
figure list controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import view.charts as charts

def accept(event, values, state):
    view = state['view']
    view.figure_list_draw(values)
    return True


