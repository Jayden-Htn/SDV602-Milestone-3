"""
Register button controller
"""
import sys
sys.dont_write_bytecode = True
import view.explorer_view as des_view


def accept(event, values, instance):
    if event == '-PAN-':
        # Regenerate chart with new pan
        des_view.DES_View.set_data(instance)
    return True