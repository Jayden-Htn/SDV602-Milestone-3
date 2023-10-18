"""
    Data Explorer
    An example module. 
"""


# Import libraries
import sys
sys.dont_write_bytecode = True # Don't write bytecode files to disk (pyc)

# Import modules
from view.data_explorer_view import DES_View


# Main code
if __name__ == "__main__" :
    """
        Code that runs when this is the main module.
    """
    des_obj = DES_View()
    des_obj.set_up_layout()
    des_obj.render()
    DES_View.accept_input()
