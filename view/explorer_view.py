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
import view.charts as charts
from model.data.data_scan import Data_Manager


# Procedures
class DES_View(Window_View):
    def __init__(self, name):
        super().__init__()
        self.owner = name
        self.chart_agg = None
        self.last_chart = None
        self.chart_dict = {'Line Plot': (charts.line_plot,{}), 'Plot Dots (discrete plot)': (charts.discrete_plot,{}),
                         'Name and Label': (charts.names_labels,{}), 'Plot many Lines': (charts.multiple_plots,{}),
                         'Bar Chart': (charts.bar_chart,{}), 'Histogram': (charts.histogram,{'title':'Our Histogram Name'}),
                         'Scatter Plots': (charts.scatter_plots,{}), 'Stack Plot': (charts.stack_plot,{}),
                         'Pie Chart 1': (charts.pie_chart1,{}), 'Pie Chart 2': (charts.pie_chart2,{})}


    def set_layout(self):
        self.current_layout = layout_des(self)


    def set_data(self):
        # Set owner
        self.window['-USER-'].update(f'Managed by {self.owner}')

        # Set chart options
        self.window['-CHART_LIST-'].update(values=list(self.chart_dict))
        self.window['-CHART_LIST-'].update(value=list(self.chart_dict)[0])

        # Disable owner controls
        if self.owner != Window_View.user:
            self.window['-DATASET-'].update(disabled=True)
            self.window['-DATASET-'].update(button_color=('#D0E9DD','#D0E9DD'))
            self.window['-DETAILS-'].update(disabled=True)
            self.window['-DETAILS-'].update(button_color=('#D0E9DD','#D0E9DD'))

        # Get chart data
        data = Data_Manager.get_data(self.owner)
        if data != None:
            # Set chart data
            self.update_current_data(self.window, file_name=data.file_name, data=data.data, title=data.title, x_label=data.x_label, y_label=data.y_label)

        # Update title to display no data
        self.window['-TITLE-'].update('No Data Set')


    def have_selected_graph(self, values):
        return len(values['-LISTBOX-']) > 0


    def update_current_data(self, values, file_name=None, **kwargs):
        if self.have_selected_graph(values): 
            the_file_name = file_name
            choice = values['-LISTBOX-'][0] 
            (func,args) = self.chart_dict[choice]
            for arg_name in kwargs:
                args[arg_name] = kwargs[arg_name]
            
            if 'file_name' in args :
                the_file_name = args['file_name']
            if the_file_name != None :
                args['file_name'] = the_file_name
            else:
                the_file_name = "No data"
            self.update_component_text('data_file_name',the_file_name)
            self.chart_dict[choice] = (func,args)
            self.chart_list_draw(values)

        
    def draw_chart(self, canvas, chart):
        chart_canvas_agg = FigureCanvasTkAgg(chart, canvas)
        chart_canvas_agg.draw()
        chart_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return chart_canvas_agg


    def delete_chart_agg(self, chart_agg):
        if self.chart_agg:
            self.chart_agg.get_tk_widget().forget()
        plt.close('all')


    def chart_list_draw(self, values):
        if self.have_selected_graph(values) :
            choice = values['-LISTBOX-'][0]                 # get first listbox item chosen (returned as a list)
            func_tuple = self.chart_dict[choice]                         # get function to call from the dictionary
            kwargs = func_tuple[1]
            
            func = func_tuple[0]
            
            self.window['-MULTILINE-'].update(inspect.getsource(func))  # show source code to function in multiline
            
            chart = func(**kwargs)                                    # call function to get the chart
            
            # ** IMPORTANT ** Clean up previous drawing before drawing again
            self.delete_chart_agg(self.chart_agg)

            the_file_name = "No Data"
            if 'file_name' in kwargs:
                the_file_name = kwargs['file_name']
            self.update_component_text('data_file_name',the_file_name)
            
            self.chart_agg = self.draw_chart(self.window['-CANVAS-'].TKCanvas, chart)  # draw the chart
    
