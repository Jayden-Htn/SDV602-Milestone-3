"""
New DES button controller
"""
import sys
sys.dont_write_bytecode = True
from view.data_explorer_view import DES_View


def accept(event, values, state):
    keep_going = True
    if event == '-OTHER_DES-':
        # Get selected user
        des_owner = values['-DES_DROPDOWN-']
        if des_owner != 'Select a DES':
            # Create window
            des_obj = DES_View()
            des_obj.set_up_layout('other_des', des_owner)
            des_obj.render()
    return keep_going 