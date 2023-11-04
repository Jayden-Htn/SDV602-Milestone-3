"""
This file contains the view for the data explorer screen, sets up the layout and creates the window controls.
"""


# Imports
import sys
sys.dont_write_bytecode = True

from view.window_view import Window_View
from view.layouts.layout_menu import layout as layout_menu
import model.data.accounts as accounts


# Procedures
class Menu_View(Window_View):
    def __init__(self):
        super().__init__()


    def set_layout(self):
        self.current_layout = layout_menu(self)

    
    def load_home_page(instance):
        window = instance.window
        # Update name on home screen
        window['-PAGE_NAME-'].update(f'Welcome, {instance.user}!')
        # Update DES dropdown
        des_list = accounts.get_other_names(instance.user)
        window['-DES_DROPDOWN-'].update(values=des_list)
        window['-DES_DROPDOWN-'].update(value='Select a DES')  


    def set_user(name):
        Window_View.user = name
       
