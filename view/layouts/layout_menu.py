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
    components = view.components
    controls = view.controls
    # Welcome screen layout
    components['title'] = sg.Text('Data Scout: Data Set Explorer', font='Any 28', size=(700,1), justification='center')
    components['welcome_text'] = sg.Text('Explore large data sets with ease', font='Any 16', pad=(0,(0,20)))
    components['login_button'] = sg.Button(button_text='Login', key='-LOGIN_PAGE-', size=(20,1))
    components['register_button'] = sg.Button(button_text='Register', key='-REGISTER_PAGE-', size=(20,1))
    components['exit_button'] = sg.Button(button_text='Exit', key='-EXIT-', size=(20,1))
    controls += [login_page.accept]
    controls += [register_page.accept]
    controls += [exit_button.accept]

    layout_welcome = [
        [sg.Column(
            layout=[
                [components['title']],
                [components['welcome_text']],
                [components['login_button']],
                [components['register_button']],
                [components['exit_button']],
            ],
            element_justification='center'
        )]
    ]

    # Login screen layout
    components['title'] = sg.Text('Data Scout: Data Set Explorer', font='Any 28', size=(700,1), justification='center')
    components['page_name'] = sg.Text('Login', font='Any 18', justification='right', pad=(0,(0,20)))
    components['email_text'] = sg.Text('Email', size=(8,1), justification='right')
    components['email_input'] = sg.Input(size=(25,1), key='-EMAIL-')
    components['password_text'] = sg.Text('Password', size=(8,1), justification='right')
    components['password_input'] = sg.Input(size=(25,1), key='-PASSWORD-')
    components['login_button'] = sg.Button('Login', size=(15,1), key='-LOGIN_BUTTON-', pad=(0,(20,0)))
    components['back_button'] = sg.Button('Back', key='-BACK_BUTTON-', size=(15,1))
    controls += [login_button.accept]
    controls += [back_button.accept]

    layout_login = [
        [sg.Column(
            layout=[
                [components['title']],
                [components['page_name']],
                [components['email_text'], components['email_input']],
                [components['password_text'], components['password_input']],
                [components['login_button']],
                [components['back_button']],
            ],
            element_justification='center'
        )]
    ]

    # Register screen layout
    components['title'] = sg.Text('Data Scout: Data Set Explorer', font='Any 28', size=(700,1), justification='center')
    components['page_name'] = sg.Text('Register', font='Any 18', justification='right', pad=(0,(0,20)))
    components['name_text'] = sg.Text('Name', size=(8,1), justification='right')
    components['name_input'] = sg.Input(size=(25,1), key='-NAME-')
    components['email_text'] = sg.Text('Email', size=(8,1), justification='right')
    components['email_input'] = sg.Input(size=(25,1), key='-EMAIL_2-')
    components['password_text'] = sg.Text('Password', size=(8,1), justification='right')
    components['password_input'] = sg.Input(size=(25,1), key='-PASSWORD_2-')
    components['register_button'] = sg.Button('Register', key='-REGISTER_BUTTON-', size=(15,1), pad=(0,(20,0)))
    components['back_button'] = sg.Button('Back', key='-BACK_BUTTON_2-', size=(15,1))
    controls += [register_button.accept]
    controls += [back_button.accept]

    layout_register = [
        [sg.Column(
            layout=[
                [components['title']],
                [components['page_name']],
                [components['name_text'], components['name_input']],
                [components['email_text'], components['email_input']],
                [components['password_text'], components['password_input']],
                [components['register_button']],
                [components['back_button']],
            ],
            element_justification='center'
        )]
    ]

    # Home screen layout
    components['title'] = sg.Text('Data Scout: Data Set Explorer', font='Any 28', 
                                       size=(700,1), justification='center')
    components['page_name'] = sg.Text('Welcome User', font='Any 18', justification='right', 
                                           pad=(0,(0,20)), key='-PAGE_NAME-')
    components['my_des'] = sg.Button('My DES', key='-MY_DES-', size=(15,1))
    components['des_dropdown'] = sg.Combo(['Select a DES'], key='-DES_DROPDOWN-',
                                                size=(15,1), default_value='Select a DES')
    components['other_des'] = sg.Button('Open DES', key='-OTHER_DES-', size=(15,1))
    components['exit_button'] = sg.Button('Exit', key='-EXIT_2-', size=(15,1))
    controls += [new_des.accept]
    controls += [exit_button.accept]

    frame_layout = [
        [components['des_dropdown']],
        [components['other_des']]
    ]

    components['des_list'] = sg.Frame(title='DES', layout=frame_layout, size=(140, 80), 
                                           title_color='#2D6A4F', background_color='#95D0B3')

    layout_home = [
        [sg.Column(
            layout=[
                [components['title']],
                [components['page_name']],
                [components['my_des']],
                [components['des_list']],
                [components['exit_button']],
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
