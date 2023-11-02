"""
This file is used to define the layouts of the windows.
"""


# Imports
import sys 
sys.dont_write_bytecode = True

import PySimpleGUI as sg

import controller.exit_button as exit_button
import controller.menu.new_des as new_des
import controller.menu.login_page as login_page
import controller.menu.register_page as register_page
import controller.menu.login_button as login_button
import controller.menu.register_button as register_button
import controller.menu.back_button as back_button


# Procedures
def layout(view):
    # Welcome screen layout
    view.components['title'] = sg.Text('Data Scout: Data Set Explorer', font='Any 28', size=(700,1), justification='center')
    view.components['welcome_text'] = sg.Text('Explore large data sets with ease', font='Any 16', pad=(0,(0,20)))
    view.components['login_button'] = sg.Button(button_text='Login', key='-LOGIN_PAGE-', size=(20,1))
    view.components['register_button'] = sg.Button(button_text='Register', key='-REGISTER_PAGE-', size=(20,1))
    view.components['exit_button'] = sg.Button(button_text='Exit', key='-EXIT-', size=(20,1))
    view.controls += [login_page.accept]
    view.controls += [register_page.accept]
    view.controls += [exit_button.accept]

    layout_welcome = [
        [sg.Column(
            layout=[
                [view.components['title']],
                [view.components['welcome_text']],
                [view.components['login_button']],
                [view.components['register_button']],
                [view.components['exit_button']],
            ],
            element_justification='center'
        )]
    ]

    # Login screen layout
    view.components['title'] = sg.Text('Data Scout: Data Set Explorer', font='Any 28', size=(700,1), justification='center')
    view.components['page_name'] = sg.Text('Login', font='Any 18', justification='right', pad=(0,(0,20)))
    view.components['email_text'] = sg.Text('Email', size=(8,1), justification='right')
    view.components['email_input'] = sg.Input(size=(25,1), key='-EMAIL-')
    view.components['password_text'] = sg.Text('Password', size=(8,1), justification='right')
    view.components['password_input'] = sg.Input(size=(25,1), key='-PASSWORD-')
    view.components['login_button'] = sg.Button('Login', size=(15,1), key='-LOGIN_BUTTON-', pad=(0,(20,0)))
    view.components['back_button'] = sg.Button('Back', key='-BACK_BUTTON-', size=(15,1))
    view.controls += [login_button.accept]
    view.controls += [back_button.accept]

    layout_login = [
        [sg.Column(
            layout=[
                [view.components['title']],
                [view.components['page_name']],
                [view.components['email_text'], view.components['email_input']],
                [view.components['password_text'], view.components['password_input']],
                [view.components['login_button']],
                [view.components['back_button']],
            ],
            element_justification='center'
        )]
    ]

    # Register screen layout
    view.components['title'] = sg.Text('Data Scout: Data Set Explorer', font='Any 28', size=(700,1), justification='center')
    view.components['page_name'] = sg.Text('Register', font='Any 18', justification='right', pad=(0,(0,20)))
    view.components['name_text'] = sg.Text('Name', size=(8,1), justification='right')
    view.components['name_input'] = sg.Input(size=(25,1), key='-NAME-')
    view.components['email_text'] = sg.Text('Email', size=(8,1), justification='right')
    view.components['email_input'] = sg.Input(size=(25,1), key='-EMAIL_2-')
    view.components['password_text'] = sg.Text('Password', size=(8,1), justification='right')
    view.components['password_input'] = sg.Input(size=(25,1), key='-PASSWORD_2-')
    view.components['register_button'] = sg.Button('Register', key='-REGISTER_BUTTON-', size=(15,1), pad=(0,(20,0)))
    view.components['back_button'] = sg.Button('Back', key='-BACK_BUTTON_2-', size=(15,1))
    view.controls += [register_button.accept]
    view.controls += [back_button.accept]

    layout_register = [
        [sg.Column(
            layout=[
                [view.components['title']],
                [view.components['page_name']],
                [view.components['name_text'], view.components['name_input']],
                [view.components['email_text'], view.components['email_input']],
                [view.components['password_text'], view.components['password_input']],
                [view.components['register_button']],
                [view.components['back_button']],
            ],
            element_justification='center'
        )]
    ]

    # Home screen layout
    view.components['title'] = sg.Text('Data Scout: Data Set Explorer', font='Any 28', 
                                       size=(700,1), justification='center')
    view.components['page_name'] = sg.Text('Welcome User', font='Any 18', justification='right', 
                                           pad=(0,(0,20)), key='-PAGE_NAME-')
    view.components['my_des'] = sg.Button('My DES', key='-MY_DES-', size=(15,1))
    view.components['des_dropdown'] = sg.Combo(['Select a DES'], key='-DES_DROPDOWN-',
                                                size=(15,1), default_value='Select a DES')
    view.components['other_des'] = sg.Button('Open DES', key='-OTHER_DES-', size=(15,1))
    view.components['exit_button'] = sg.Button('Exit', key='-EXIT_2-', size=(15,1))
    view.controls += [new_des.accept]
    view.controls += [exit_button.accept]

    frame_layout = [
        [view.components['des_dropdown']],
        [view.components['other_des']]
    ]

    view.components['des_list'] = sg.Frame(title='DES', layout=frame_layout, size=(140, 80), 
                                           title_color='#2D6A4F', background_color='#95D0B3')

    layout_home = [
        [sg.Column(
            layout=[
                [view.components['title']],
                [view.components['page_name']],
                [view.components['my_des']],
                [view.components['des_list']],
                [view.components['exit_button']],
            ],
            element_justification='center'
        )]
    ]

    # Full screen layout
    return [[
        sg.VPush(),
        sg.Column(layout_welcome, key='-COL_WELCOME-'), 
        sg.Column(layout_login, visible=False, key='-COL_LOGIN-'), 
        sg.Column(layout_register, visible=False, key='-COL_REGISTER-'),
        sg.Column(layout_home, visible=False, key='-COL_HOME-'),
        sg.VPush()
    ]]
