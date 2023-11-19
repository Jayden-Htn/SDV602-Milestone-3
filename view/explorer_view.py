"""
This file contains the view for the data explorer screen, sets up the layout and creates the window controls.
"""


# Imports
import sys
sys.dont_write_bytecode = True
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,  NavigationToolbar2Tk
import datetime

from view.window_view import Window_View
from view.layouts.layout_des import layout as layout_des
import view.charts as charts
from model.data.data_scan import Data_Manager
from model.chat_manager import Chat_Manager


# Procedures
class DES_View(Window_View):
    def __init__(self, name):
        super().__init__()
        self.owner = name
        self.data_manager = Data_Manager()
        self.chat_manager = Chat_Manager(self.user, self.owner)
        self.chart_agg = None
        self.last_chart = None
        self.chart_dict = {'Line Plot': (charts.line_plot), 'Plot Dots (discrete plot)': (charts.discrete_plot),
                         'Name and Label': (charts.names_labels), 'Plot many Lines': (charts.multiple_plots),
                         'Bar Chart': (charts.bar_chart), 'Histogram': (charts.histogram),
                         'Scatter Plots': (charts.scatter_plots), 'Stack Plot': (charts.stack_plot),
                         'Pie Chart 1': (charts.pie_chart1), 'Pie Chart 2': (charts.pie_chart2)}


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
            self.disable_owner_controls()

        # Set chat
        self.set_chat()

        # Set chart data
        self.prepare_chart_data()


    def set_chat(self):
        # Send chat component to chat manager
        self.chat_manager.set_chat_component(self.window['-CHAT-'])

        # Set chat log
        # self.chat_manager.set_test_messages()
        chat_log = self.chat_manager.get_chat()
        if chat_log == None:
            self.window['-CHAT-'].print("No messages available")
        else:
            for message in chat_log:
                datetime_str = datetime.datetime.utcfromtimestamp(message['Time'])
                time = datetime_str.strftime('%H:%M')
                self.window['-CHAT-'].print(f"<{message['UserName']} {time} UTC> {message['Message']}")
        self.window['-CHAT-'].update()


    def disable_owner_controls(self):
        """
        Disables the owner controls (e.g. data and detail setting).
        """
        disabled_color = ('#D0E9DD','#D0E9DD')
        if self.owner != Window_View.user:
            self.window['-DATASET-'].update(disabled=True)
            self.window['-DATASET-'].update(button_color=disabled_color)
            self.window['-DETAILS-'].update(disabled=True)
            self.window['-DETAILS-'].update(button_color=disabled_color)


    def get_selected_chart(self):
        # Check if user selected a chart
        if self.window['-CHART_LIST-'] in self.chart_dict:
            return self.chart_dict['-CHART_LIST-'].get() in self.chart_dict
        # If not, set to default
        return self.chart_dict['Line Plot']


    def prepare_chart_data(self):
        """
        Prepares the chart data for drawing and sets the chart details on the DES screen.
        """
        # Get selected chart type function
        func = self.get_selected_chart()

        # Get chart data
        data_manager = self.data_manager
        data = None
        info = None
        if data_manager.get_data(self.owner):
            data = data_manager.dict_list
            info = data_manager.get_chart_info(self.owner) # Title, description, etc.
        
        # Set details
        if info != None:
            title = info['title']
            self.window['-TITLE-'].update(title)
            self.window['-DESCRIPTION-'].update(info['description'])
        else:
            title = "No Data Set"
            self.window['-TITLE-'].update(title)
            self.window['-DESCRIPTION-'].update('No Data Set')

        # Set title
        self.chart_draw_handler(data, func, title)


    def chart_draw_handler(self, data, func, title):
        """
        Handles the drawing of new charts on the canvas.

        Parameters
            values (dict): The values from the window.
        """
        # Setup kwargs dict
        kwargs = {}
        if not(data == {'': []} or data == None):
            list_values = list(data.values())
            kwargs['x_values'] = list_values[0]
            for i in range(1, len(data)):
                kwargs[f'y_values_{i}'] = list(data.values())[i]
        if not(data == None or list(data.keys()) == ['']):
            kwargs['x_label'] = list(data.keys())[0]
            kwargs['y_label'] = list(data.keys())[1]
        if title != None:
            kwargs['title_label'] = title

        # Get chart
        figure = func(**kwargs)
        
        # Clean up previous drawing before drawing again
        self.delete_chart_agg()
        
        # Draw the chart
        self.chart_agg = self.draw_figure(self.window['-CANVAS-'].TKCanvas, figure)  # draw the chart


    def draw_figure(self, canvas, figure):
        chart_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        chart_canvas_agg.draw()
        # Add toolbar to canvas
        toolbar = NavigationToolbar2Tk(
            chart_canvas_agg, self.window['-CANVAS TOOLS-'].TKCanvas)
        toolbar.update()
        chart_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return chart_canvas_agg


    def delete_chart_agg(self):
        if self.chart_agg:
            self.chart_agg.get_tk_widget().forget()
        plt.close('all')
    
