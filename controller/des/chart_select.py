"""
Chart list controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import view.charts as charts

def accept(event, values, state):
    if event == '-CHART_LIST-':
        print("Chart list controller")
        pass
        # Redraw chart
    return True


