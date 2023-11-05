"""
This file is used to define the layouts of the windows.
"""


# Imports
import sys 
sys.dont_write_bytecode = True

import PySimpleGUI as sg

import controller.exit_button as exit_button
import controller.des.dataset_button as dataset_button
import controller.des.details_button as details_button
import controller.des.chart_list_select as chart_list
import controller.des.open_csv as open_csv
import controller.des.zoom as zoom
import controller.des.pan as pan
import controller.des.chat_button as chat_button


# Procedures
def layout(view):
    components = view.components
    controls = view.controls

    # Left column contains chart display and title
    components['title'] = sg.Text('Title of the data', font='Any 24', size=(25,1))
    components['user'] = sg.Text('Managed by {User\'s name}', font='Any 14', justification='right', pad=((5,0),(0,10)), key='-USER-')
    components['chart'] = sg.Canvas(size=(550,500), background_color='#D0E9DD', key='-CANVAS-')
    # 45 x 15 is the size of the chart display 

    # Right column contains chart controls
    components['exit_button'] = sg.Button(button_text='Exit', key='-EXIT-', size=(8,1), pad=((0, 10),(27,0)))
    components['dataset_button'] = sg.Button(button_text='Dataset', key='-DATASET-', size=(8,1), pad=((0,30),(27,0)))
    components['details_button'] = sg.Button(button_text='Details', key='-DETAILS-', size=(8,1), pad=((0,30),(27,0)))
    components['description'] = sg.Text('Description goes here', font='Any 12', size=(35,7), pad=(0,(30,10)), background_color='#D0E9DD')
    components['chart_label'] = sg.Text('Charts', font='Any 12', size=(5,1), pad=(0,(0,0)))
    components['chart_list'] = sg.Combo(values=['Chart 1', 'Chart 2'], size=(23,1), key='-CHART_LIST-', enable_events=True)
    components['zoom_label'] = sg.Text('Zoom', size=(5,1))
    components['zoom_slider'] = sg.Slider(range=(1,100), default_value=1, orientation='h', key='-ZOOM-', enable_events=True)
    components['pan_label'] = sg.Text('Pan', size=(5,1))
    components['pan_slider'] = sg.Slider(range=(1,100), default_value=1, orientation='h', key='-PAN-', enable_events=True)
    components['chat'] = sg.Output(size=(35,5), background_color='#D0E9DD', key='-CHAT-', pad=(0,(10,0)))
    components['chat_input'] = sg.InputText(size=(25,1), key='-CHAT_INPUT-')
    components['chat_button'] = sg.Button('Send', key='-CHAT_BUTTON-', size=(10,1))
    controls += [exit_button.accept]
    controls += [dataset_button.accept]
    controls += [details_button.accept]
    controls += [chart_list.accept]
    controls += [open_csv.accept]
    controls += [zoom.accept]
    controls += [pan.accept]
    controls += [chat_button.accept]

    # Full layout
    return [[
        sg.Column(
            layout=[
                [components['title']],
                [components['user']],
                [components['chart']],
            ],
            element_justification='left',
            size=(550,500)
        ),
        sg.Column(
            layout=[
                [components['dataset_button'], components['details_button'], components['exit_button']],
                [components['description']],
                [components['chart_label'], components['chart_list']],
                [components['zoom_label'], components['zoom_slider']],
                [components['pan_label'], components['pan_slider']],
                [components['chat']],
                [components['chat_input'], components['chat_button']],
            ],
            element_justification='right',
        )
    ]]
