"""
Details button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import model.data.data_scan as data
from view.window_view import Window_View


def accept(event, values, instance):
    if event == '-DETAILS-':
        # Popup for changing title and description
        layout = [[sg.Text('Chart Title:', pad=((19,0),0)), sg.InputText(key='-TITLE-', size=(50,1), default_text=instance.window['-TITLE-'].get(), )],
                  [sg.Text('Description:'), sg.Multiline(key='-DESCRIPTION-', size=(50,5), default_text=instance.window['-DESCRIPTION-'].get())],
                  [sg.Button('Ok', pad=((230,10),20)), sg.Button('Cancel', pad=((10,220),20))]]
        popup = sg.Window('Update DES Details', layout, modal=True, size=(600, 200), finalize=True)
        while True:
            event, values = popup.read()
            if event == 'Ok' and values['-TITLE-'] != '' and values['-DESCRIPTION-'] != '':
                # Update chart title and description
                instance.window['-TITLE-'].update(values['-TITLE-'])
                instance.window['-DESCRIPTION-'].update(values['-DESCRIPTION-'])
                # Find des_view instance where window matches
                data_manager = data.Data_Manager()
                data_manager.update_des_info(instance.owner, values['-TITLE-'], values['-DESCRIPTION-'])
                del data_manager
                popup.close()
                break
            elif event == 'Cancel':
                popup.close()
                break
            elif event == sg.WIN_CLOSED:
                popup.close()
                break
    return True

