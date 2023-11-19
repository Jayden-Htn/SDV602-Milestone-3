"""
This file contains the view for the data explorer screen, sets up the layout and creates the window controls.

Classes:
    DES_View: The view for the data explorer screen.
"""


# Imports
import sys
sys.dont_write_bytecode = True

from view.window_view import Window_View
from view.layouts.layout_menu import layout as layout_menu
import model.accounts.account_handler as accounts


# Procedures
class Menu_View(Window_View):
    """
    The view for the data explorer screen.

    Functions:
        set_layout(): Sets the layout for the DES screen.
        set_data(): Sets the data for the DES screen.
        set_chat(): Sets the chat for the DES screen.
        disable_owner_controls(): Disables the owner controls (e.g. data and detail setting).
        get_selected_chart(): Gets the selected chart.
        prepare_chart_data(): Prepares the chart data for drawing and sets the chart details on the DES screen.
        chart_draw_handler(): Handles the drawing of new charts on the canvas.
        draw_figure(): Draws the chart on the canvas.
        delete_chart_agg(): Deletes the chart from the canvas.
    """

    def __init__(self):
        super().__init__()


    def set_layout(self):
        self.current_layout = layout_menu(self)

    
    def load_home_page(instance):
        """
        This function loads the home page.
        """
        window = instance.window
        # Update name on home screen
        window['-PAGE_NAME-'].update(f'Welcome, {instance.user}!')
        # Update DES dropdown
        des_list = accounts.get_other_names(instance.user)
        window['-DES_DROPDOWN-'].update(values=des_list)
        window['-DES_DROPDOWN-'].update(value='Select a DES')  


    def set_user(name):
        Window_View.user = name
       
