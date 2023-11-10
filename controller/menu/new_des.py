"""
New DES button controller
"""
import sys
sys.dont_write_bytecode = True
from view.explorer_view import DES_View


def accept(event, values, state):
    if event == '-OTHER_DES-':
        # Get selected user
        des_owner = values['-DES_DROPDOWN-']
        if des_owner != 'Select a DES':
            # Create window
            des_obj = DES_View(des_owner)
            des_obj.set_layout()
            des_obj.render()
            des_obj.set_data()
    return True 