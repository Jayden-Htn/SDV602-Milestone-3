"""
This file contains the view for the data explorer screen, sets up the layout and creates the window controls.
"""


# Imports
import sys
sys.dont_write_bytecode = True
from typing import Dict
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import inspect

import view.chart_examples as ce 
import view.layouts as layouts
import model.data.accounts as accounts


# Procedures
class DES_View(object):
    des_list = [] # change to a dict, store window instance and and class instance
    user = None
    def __init__(self):
        self.window = None
        self.figure_agg = None
        self.current_layout = []
        self.components = {"has_components":False}
        self.controls = []
        self.my_lastfig = None
        self.fig_dict = {'Line Plot': (ce.line_plot,{}), 'Plot Dots(discrete plot)': (ce.discrete_plot,{}),
                         'Name and Label': (ce.names_labels,{}), 'Plot many Lines': (ce.multiple_plots,{}),
                         'Bar Chart': (ce.bar_chart,{}), 'Histogram': (ce.histogram,{'title':'Our Histogram Name'}),
                         'Scatter Plots': (ce.scatter_plots,{}), 'Stack Plot': (ce.stack_plot,{}),
                         'Pie Chart 1': (ce.pie_chart1,{}), 'Pie Chart 2': (ce.pie_chart2,{})}
        DES_View.des_list += [self] # add to list of des objects


    def have_selected_graph(self,values):
        return len(values['-LISTBOX-']) > 0
  

    def update_component_text(self,component_name, text):
        if component_name in self.components:
            self.components[component_name].update(text)


    def update_current_data(self,values,file_name=None, **kwargs):
        if self.have_selected_graph(values) : 
            the_file_name = file_name
            choice = values['-LISTBOX-'][0] 
            (func,args) = self.fig_dict[choice]
            for arg_name in kwargs:
                args[arg_name] = kwargs[arg_name]
            
            if 'file_name' in args :
                the_file_name = args['file_name']
            if the_file_name != None :
                args['file_name'] = the_file_name
            else:
                the_file_name = "No data"
            self.update_component_text('data_file_name',the_file_name)
            self.fig_dict[choice] = (func,args)
            self.figure_list_draw(values)

        
    def draw_figure(self,canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg


    def delete_figure_agg(self,figure_agg):
        if self.figure_agg:
            self.figure_agg.get_tk_widget().forget()
        plt.close('all')


    def figure_list_draw(self,values):
        if self.have_selected_graph(values) :
            choice = values['-LISTBOX-'][0]                 # get first listbox item chosen (returned as a list)
            func_tuple = self.fig_dict[choice]                         # get function to call from the dictionary
            kwargs = func_tuple[1]
            
            func = func_tuple[0]
            
            self.window['-MULTILINE-'].update(inspect.getsource(func))  # show source code to function in multiline
            
            fig = func(**kwargs)                                    # call function to get the figure
            
            # ** IMPORTANT ** Clean up previous drawing before drawing again
            self.delete_figure_agg(self.figure_agg)

            the_file_name = "No Data"
            if 'file_name' in kwargs:
                the_file_name = kwargs['file_name']
            self.update_component_text('data_file_name',the_file_name)
            
            self.figure_agg = self.draw_figure(self.window['-CANVAS-'].TKCanvas, fig)  # draw the figure
    

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


    def set_up_layout(self, type):
        if type == 'main':
            self.current_layout = layouts.main_layout(self)
        elif type == 'des':
           self.current_layout = layouts.des_layout(self)
        else:
           print("Error: Unknown layout type")


    def load_home_page(instance):
        window = instance.window
        # Update name on home screen
        window['-PAGE_NAME-'].update(f'Welcome, {instance.user}!')
        # Update DES dropdown
        des_list = accounts.get_other_names(instance.user)
        window['-DES_DROPDOWN-'].update(values=des_list)
        window['-DES_DROPDOWN-'].update(value='Select a DES')


    def render(self):
        # create the form and show it without the plot
        if self.current_layout != [] :
            self.window = sg.Window('Data Scout: Data Set Explorer', self.current_layout, size=(700, 400), finalize=True)
            

    # class static method, level reading
    def accept_input():
        keep_going = True  
        active_view = None     
        while keep_going:
            # print("----- New Loop -----")
            window, event, values = sg.read_all_windows()
            # print("event: ", event)
            # Find class from window
            for view in DES_View.des_list:
                if view.window == window:
                    active_view = view
            # Check for window close
            if event == sg.WIN_CLOSED or event == 'Exit':
                    keep_going = False
            for accept_control in active_view.controls:
                # Determine loop and handle event
                keep_going = accept_control(event, values, active_view)            
            if active_view != None:
                active_view.window.refresh()

            
       
