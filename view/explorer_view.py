"""
This file contains the view for the data explorer screen, sets up the layout and creates the window controls.
"""


# Imports
import sys
sys.dont_write_bytecode = True
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
                         'Bar Chart': (charts.bar_chart,{}), 'Histogram': (charts.histogram,{}),
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
        disabled_color = ('#D0E9DD','#D0E9DD')
        if self.owner != Window_View.user:
            self.window['-DATASET-'].update(disabled=True)
            self.window['-DATASET-'].update(button_color=disabled_color)
            self.window['-DETAILS-'].update(disabled=True)
            self.window['-DETAILS-'].update(button_color=disabled_color)

        # Get chart data
        print("BEFORE")
        data_manager = Data_Manager()
        data = None
        info = None
        if data_manager.get_data(self.owner) != None:
            print("TWO")
            data = data_manager.values_list
            print("THREE")
            info = data_manager.get_chart_info(self.owner) # Title, description, etc.

        # Set chart data
        print("FOUR")
        self.update_current_chart(data, info)


    def get_selected_chart(self):
        # Check if user selected a chart
        if self.window['-CHART_LIST-'] in self.chart_dict:
            print("returning", self.chart_dict['-CHART_LIST-'] in self.chart_dict)
            return self.chart_dict['-CHART_LIST-'].get() in self.chart_dict
        # If not, set to default
        return self.chart_dict['Line Plot']


    def update_current_chart(self, data, info):
        # Get selected chart type function
        func, args = self.get_selected_chart()
        
        # Set details
        if info != None:
            self.window['-TITLE-'].update(info['title'])
            self.window['-DESCRIPTION-'].update(info['description'])
        else:
            self.window['-TITLE-'].update('No Data Set')
            self.window['-DESCRIPTION-'].update('No Data Set')

        # Set title
        self.chart_draw_handler(data, func, args)


    def chart_draw_handler(self, values, func, kwargs):
        """
        Handles the drawing of new charts on the canvas.

        Parameters
            values (dict): The values from the window.
        """
        # Multiline
        # self.window['-MULTILINE-'].update(inspect.getsource(func)) # show source code to function in multiline
        
        # Get chart
        chart = func(**kwargs)
        
        # Clean up previous drawing before drawing again
        self.delete_chart_agg()
        
        # Draw the chart
        self.chart_agg = self.draw_chart(self.window['-CANVAS-'].TKCanvas, chart)  # draw the chart


    def draw_chart(self, canvas, chart):
        chart_canvas_agg = FigureCanvasTkAgg(chart, canvas)
        chart_canvas_agg.draw()
        chart_canvas_agg.get_tk_widget().pack(side='left', fill='none', expand=0)
        return chart_canvas_agg


    def delete_chart_agg(self):
        if self.chart_agg:
            self.chart_agg.get_tk_widget().forget()
        plt.close('all')
    
