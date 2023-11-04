"""
This module contains the Window_View superclass for the PySimpleGUI window.
"""


# Imports
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg


# Procedures
class Window_View():
    user = None
    view_list = []
    def __init__(self):
        self.window = None
        self.current_layout = []
        self.components = {"has_components":False}
        self.controls = []
        Window_View.view_list += [self]
   

    def set_theme():
        """
        This function sets the default PySimpleGUI theme for the program.
        """
        sg.SetOptions(
            background_color='#95D0B3', 
            text_element_background_color='#95D0B3',
            text_color="#2D6A4F",
            font='Any 12',
            element_background_color='#D0E9DD',
            input_elements_background_color='#F7F3EC',
            button_color=('white','#2D6A4F'),
            titlebar_background_color='red',
            titlebar_text_color='black'
        )


    def render(self):
        # create the form and show it without the plot
        if self.current_layout != [] :
            self.window = sg.Window('Data Scout: Data Set Explorer', self.current_layout, size=(900, 500), finalize=True)
      

    # class static method, level reading
    def accept_input():
        keep_going = True  
        active_view = None     
        while keep_going:
            # print("----- New Loop -----")
            window, event, values = sg.read_all_windows()
            # print("event: ", event)
            # Find class from window
            for view in Window_View.view_list:
                if view.window == window:
                    active_view = view
                    # Active view is the window that the event came from
            # Check for window close
            if event == sg.WIN_CLOSED or event == 'Exit':
                    keep_going = False
            for accept_control in active_view.controls:
                # Determine loop and handle event
                keep_going = accept_control(event, values, active_view)            
            if active_view != None:
                active_view.window.refresh()


            
       
