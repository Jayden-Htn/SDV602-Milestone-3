"""
This file is used to define the layouts of the windows.
"""


# Imports
import sys 
sys.dont_write_bytecode = True

import PySimpleGUI as sg

import controller.exit_button as exit_button
import controller.des.figure_list_select as figure_list_select
import controller.des.open_csv as open_csv
import controller.des.zoom as zoom
import controller.des.pan as pan
import controller.des.chat as chat


# Procedures
def layout(view):
    # Left column contains chart display and title
    view.components['title'] = sg.Text('Data Scout: Data Set Explorer', font='Any 28', size=(700,1), justification='center')
    view.components['user'] = sg.Text('User\'s name', font='Any 18', justification='right', pad=(0,(0,20)))
    view.components['chart'] = sg.Text('Chart goes here', pad=(0,(0,20)), size=(5,3), background_color='lightgrey')
    # 45 x 15 is the size of the chart display 

    # Right column contains chart controls
    view.components['exit_button'] = sg.Button(button_text='Exit', key='-EXIT-', size=(20,1))
    view.components['description'] = sg.Text('Description goes here', font='Any 12', size=(45,15), pad=(0,(0,20)), background_color='#D0E9DD')
    view.components['figure_list'] = sg.Listbox(values=[], size=(45,15), key='-FIGURE_LIST-', enable_events=True)
    view.components['open_csv'] = sg.Button('Open CSV', key='-OPEN_CSV-', size=(10,1), pad=(0,(0,50)))
    view.components['zoom'] = sg.Text('Zoom', size=(5,1))
    view.components['zoom_slider'] = sg.Slider(range=(1,100), default_value=1, orientation='h', key='-ZOOM-', enable_events=True)
    view.components['pan'] = sg.Text('Pan', size=(5,1))
    view.components['pan_slider'] = sg.Slider(range=(1,100), default_value=1, orientation='h', key='-PAN-', enable_events=True)
    view.components['chat'] = sg.Button('Open chat', key='-CHAT-', size=(10,1), pad=((0, 50),(10,10)))
    view.controls += [exit_button.accept]
    view.controls += [figure_list_select.accept]
    view.controls += [open_csv.accept]
    view.controls += [zoom.accept]
    view.controls += [pan.accept]
    view.controls += [chat.accept]


    # Full layout
    return [[
        sg.Column(
            layout=[
                [view.components['title']],
                [view.components['user']],
                [view.components['chart']],
            ],
            element_justification='left',
            background_color='red'
        ),
        sg.Column(
            layout=[
                [view.components['exit_button']],
                [view.components['description']],
                [view.components['figure_list']],
                [view.components['open_csv']],
                [view.components['zoom'], view.components['zoom_slider']],
                [view.components['pan'], view.components['pan_slider']],
                [view.components['chat']]
            ],
            element_justification='right',
            background_color='blue'
        )
    ]]


def des_layout(view):
    pass