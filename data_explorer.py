"""
    Data Explorer
    An example module. 
"""


# Imports
import sys
sys.dont_write_bytecode = True # Don't write bytecode files to disk (pyc)

from view.window_view import Window_View
from view.menu_view import Menu_View


# Main code
if __name__ == "__main__" :
    """
        Code that runs when this is the main module.
    """
    Window_View.set_theme()
    des_obj = Menu_View()
    des_obj.set_layout()
    des_obj.render()
    Window_View.accept_input()
