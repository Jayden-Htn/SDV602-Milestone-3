"""
This file is used to define the layouts of the windows.
"""


# Imports
import sys 
sys.dont_write_bytecode = True

import PySimpleGUI as sg

import controller.exit_button as exit_button
import controller.des.dataset_button as dataset_button
import controller.des.chart_list_select as chart_list
import controller.des.open_csv as open_csv
import controller.des.zoom as zoom
import controller.des.pan as pan
import controller.des.chat_button as chat_button


# Procedures
def layout(view):
    # Left column contains chart display and title
    view.components['title'] = sg.Text('Title of the data', font='Any 24', size=(25,1))
    view.components['user'] = sg.Text('Managed by {User\'s name}', font='Any 14', justification='right', pad=((5,0),(0,10)))
    view.components['chart'] = sg.Canvas(size=(550,500), background_color='#D0E9DD', key='-CANVAS-')
    # 45 x 15 is the size of the chart display 

    # Right column contains chart controls
    view.components['exit_button'] = sg.Button(button_text='Exit', key='-EXIT-', size=(10,1), pad=(0,(27,0)))
    view.components['dataset_button'] = sg.Button(button_text='Dataset', key='-DATASET-', size=(10,1), pad=((0,30),(27,0)))
    view.components['description'] = sg.Text('Description goes here', font='Any 12', size=(35,7), pad=(0,(30,10)), background_color='#D0E9DD')
    view.components['chart_label'] = sg.Text('Charts', font='Any 12', size=(5,1), pad=(0,(0,0)))
    view.components['chart_list'] = sg.Combo(values=['Chart 1', 'Chart 2'], size=(23,1), key='-FIGURE_LIST-', enable_events=True)
    view.components['zoom_label'] = sg.Text('Zoom', size=(5,1))
    view.components['zoom_slider'] = sg.Slider(range=(1,100), default_value=1, orientation='h', key='-ZOOM-', enable_events=True)
    view.components['pan_label'] = sg.Text('Pan', size=(5,1))
    view.components['pan_slider'] = sg.Slider(range=(1,100), default_value=1, orientation='h', key='-PAN-', enable_events=True)
    view.components['chat'] = sg.Output(size=(35,5), background_color='#D0E9DD', key='-CHAT-', pad=(0,(10,0)))
    view.components['chat_input'] = sg.InputText(size=(25,1), key='-CHAT_INPUT-')
    view.components['chat_button'] = sg.Button('Send', key='-CHAT_BUTTON-', size=(10,1))
    view.controls += [exit_button.accept]
    view.controls += [dataset_button.accept]
    view.controls += [chart_list.accept]
    view.controls += [open_csv.accept]
    view.controls += [zoom.accept]
    view.controls += [pan.accept]
    view.controls += [chat_button.accept]


    # Full layout
    return [[
        sg.Column(
            layout=[
                [view.components['title']],
                [view.components['user']],
                [view.components['chart']],
            ],
            element_justification='left',
            size=(550,500)
        ),
        sg.Column(
            layout=[
                [view.components['dataset_button'], view.components['exit_button']],
                [view.components['description']],
                [view.components['chart_label'], view.components['chart_list']],
                [view.components['zoom_label'], view.components['zoom_slider']],
                [view.components['pan_label'], view.components['pan_slider']],
                [view.components['chat']],
                [view.components['chat_input'], view.components['chat_button']],
            ],
            element_justification='right',
        )
    ]]


def des_layout(view):
    pass