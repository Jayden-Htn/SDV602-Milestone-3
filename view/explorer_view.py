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

from view.window_view import Window_View
from view.layouts.layout_des import layout as layout_des
import view.chart_examples as ce 


# Procedures
class DES_View(Window_View):
    def __init__(self, name):
        super().__init__()
        self.user = name
        self.figure_agg = None
        self.my_lastfig = None
        self.fig_dict = {'Line Plot': (ce.line_plot,{}), 'Plot Dots(discrete plot)': (ce.discrete_plot,{}),
                         'Name and Label': (ce.names_labels,{}), 'Plot many Lines': (ce.multiple_plots,{}),
                         'Bar Chart': (ce.bar_chart,{}), 'Histogram': (ce.histogram,{'title':'Our Histogram Name'}),
                         'Scatter Plots': (ce.scatter_plots,{}), 'Stack Plot': (ce.stack_plot,{}),
                         'Pie Chart 1': (ce.pie_chart1,{}), 'Pie Chart 2': (ce.pie_chart2,{})}


    def set_layout(self):
        self.current_layout = layout_des(self)


    def set_data(self):
        # Set user
        self.window['-USER-'].update(f'Managed by {self.user}')

        # Disable owner controls
        if self.user != Window_View.user:
            self.window['-DATASET-'].update(disabled=True)
            self.window['-DATASET-'].update(button_color=('#e6e6e6','#e6e6e6'))
            # Add edit title and description button, will be disabled if not owner too

        # Get chart data

        # Set chart data


    def have_selected_graph(self, values):
        return len(values['-LISTBOX-']) > 0


    def update_current_data(self, values, file_name=None, **kwargs):
        if self.have_selected_graph(values): 
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

        
    def draw_figure(self, canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg


    def delete_figure_agg(self, figure_agg):
        if self.figure_agg:
            self.figure_agg.get_tk_widget().forget()
        plt.close('all')


    def figure_list_draw(self, values):
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
    
