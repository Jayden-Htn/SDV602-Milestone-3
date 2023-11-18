"""
Dataset Button Controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg


def accept(event, values, instance):
    if event == '-DATASET-':
        # Popup for changing title and description
        layout = [[sg.Text('Warning: Any new data will be merged into the matching columns', pad=((18,0),0))],
                  [sg.Text('of existing data. All file must have headers.', pad=((18,0),(0,20)))],
                  [sg.Text('CSV URL:', pad=((18,0),0)), sg.InputText(key='-URL-', size=(50,1))],
                  [sg.Text('Local CSV:'), sg.Input(default_text='No file selected', size=(30,1), disabled=True), sg.FileBrowse(key='-FILE-', size=(10,1), file_types=(("CSV Files", "*.csv"),))],
                  [sg.Button('Clear All Data', pad=((185,0),(20,0)))],
                  [sg.Button('Ok', pad=((185,10),(20,0))), sg.Button('Cancel', pad=((10,20),(20,0)))]]
        popup = sg.Window('Update DES Details', layout, modal=True, size=(500, 250), finalize=True)
        while True:
            event, values = popup.read()
            if event == 'Ok' and (values['-URL-'] != '' or values['-FILE-'] != ''):
                # Temp code below
                if values['-URL-'] != '':
                    pass # Sort later
                    # Can set file_path by storing URL file locally temporarily for merge
                elif values['-FILE-'] != '':
                    file_path = values['-FILE-']
                    instance.data_manager.merge_data(file_path, instance.owner)
                    instance.prepare_chart_data()
                else:
                    sg.popup_error('Error: No file selected')
                    continue
                popup.close()
                break
            elif event == 'Clear All Data':
                # Clear all data
                instance.data_manager.clear_data(instance.owner)               
                instance.set_data()
            elif event == 'Cancel':
                popup.close()
                break
            elif event == sg.WIN_CLOSED:
                popup.close()
                break
    return True

