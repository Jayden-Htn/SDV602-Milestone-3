"""
New DES button controller
"""
import sys
sys.dont_write_bytecode = True
from view.data_explorer_view import DES_View


def accept(event, values, state):
    keep_going = True
    if event == '-MY_DES-':
        des_obj = DES_View()
        des_obj.set_up_layout('des')
        des_obj.render()
    return keep_going