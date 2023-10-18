"""
    This is the main module for the program. It handles the windows and display.

    Functions:
        set_window_1(): This function sets the layout for the first window.
        make_my_des_window(): This function sets the layout for the user's personal DES window.
        make_des_window(user): This function sets the layout for each other DES window.
        set_theme(): This function sets the default PySimpleGUI theme for the program.
        update_des_list(window, username): This function updates the list of other DES screens.
"""


# Import libraries
import PySimpleGUI as psg

# Import modules
import logic_processor.event_handler as events
import logic_processor.request_handler as requests


# Functions
def set_window_1():
    """
        This function sets the layout for the first window.

        Returns:
            window (PySimpleGUI.Window): The window object.
    """
    # Layout for the welcome screen
    layout_welcome = [
        [psg.Column(
            layout=[
                [psg.Text('Data Scout: Data Set Explorer', font='Any 28', size=(700,1), justification='center')],
                [psg.Text('Explore large data sets with ease', font='Any 16', pad=(0,(0,20)))],
                [psg.Button('Login', key='-BTN_WELCOME_LOGIN-', size=(20,1))],
                [psg.Button('Register', key='-BTN_WELCOME_REGISTER-', size=(20,1))],
                [psg.Button('Exit', key='-BTN_WELCOME_EXIT-', size=(20,1))],
            ],
            element_justification='center'
        )]
    ]
    # Layout for the login screen
    layout_login = [
        [psg.Column(
            layout=[
                [psg.Text('Data Scout: Data Set Explorer', font='Any 20', size=(700,1), justification='center')],
                [psg.Text('Login', font='Any 18', justification='right', pad=(0,(0,20)))],
                [psg.Text('Email', size=(8,1), justification='right'), psg.Input(key='-IN_LOGIN_EMAIL-', size=(25,1))],
                [psg.Text('Password', size=(8,1), justification='right'), psg.Input(key='-IN_LOGIN_PASSWORD-', size=(25,1))],
                [psg.Button('Login', key='-BTN_LOGIN_LOGIN-', size=(15,1), pad=(0,(20,0)))],
                [psg.Button('Back', key='-BTN_LOGIN_BACK-', size=(15,1))],
            ],
            element_justification='center'
        )]
    ]
    # Layout for the register screen
    layout_register = [
        [psg.Column(
            layout=[
                [psg.Text('Data Scout: Data Set Explorer', font='Any 20', size=(700,1), justification='center')],
                [psg.Text('Register', font='Any 18', pad=(0,(0,20)))],
                [psg.Text('Username', size=(8,1), justification='right'), psg.Input(key='-IN_REGISTER_NAME-', size=(25,1))],
                [psg.Text('Email', size=(8,1), justification='right'), psg.Input(key='-IN_REGISTER_EMAIL-', size=(25,1))],
                [psg.Text('Password', size=(8,1), justification='right'), psg.Input(key='-IN_REGISTER_PASSWORD-', size=(25,1))],
                [psg.Button('Register', key='-BTN_REGISTER_REGISTER-', size=(15,1), pad=(0,(20,0)))],
                [psg.Button('Back', key='-BTN_REGISTER_BACK-', size=(15,1))],
            ],
            element_justification='center'
        )]
    ]
    # Scrollable container for other user's DES buttons
    des_container = [
        [psg.Column([], key='-DES_COL-', scrollable=True, vertical_scroll_only=True, size=(180, 120))]
    ]
    # Layout for the home screen
    layout_home = [
        [psg.Column(
            layout=[
                [psg.Text('Data Scout: Data Set Explorer', font='Any 20', size=(700,1), justification='center')],
                [psg.Text('Welcome User', font='Any 18', key='-TXT_HOME_WELCOME-', pad=(0,(0,40)))],
                [psg.Button('My DES', key='-BTN_HOME_MY_DES-', size=(15,1))],
                [psg.Frame(title='Other DES', layout=des_container, key='-DES_COL-', size=(184, 140), title_color='#2D6A4F', background_color='#95D0B3')],
                [psg.Button('Exit', key='-BTN_HOME_EXIT-', size=(15,1))]
            ],
            element_justification='center'
        )]
    ]
    # Full layout for the window, includes all possible screens
    # Navigation between screens is handled by changing the visibility of the columns
    layout = [[
        psg.VPush(),
        psg.Column(layout_welcome, key='-COL_WELCOME-'), 
        psg.Column(layout_login, visible=False, key='-COL_LOGIN-'), 
        psg.Column(layout_register, visible=False, key='-COL_REGISTER-'),
        psg.Column(layout_home, visible=False, key='-COL_HOME-'),
        psg.VPush()
    ]]
    return psg.Window('Data Scout: Data Set Explorer', layout, size=(700, 400), finalize=True)


def make_my_des_window():
    """
        This function sets the layout for the user's personal DES window.

        Returns:
            window (PySimpleGUI.Window): The window object.
    """
    # Note: my des is separate as it will have additional control such as selecting data sets to display,
    # which will be added in the next version

    # Left column contains chart display and title
    display_column = [
        [psg.Column(
            layout=[
                [psg.Text('My Personal DES', font='Any 20', justification='center', pad=(0,0))],
                [psg.Text('DES Title', font='Any 16', pad=(0,(0,10)))],
                [psg.Text('Chart goes here', pad=(0,(0,20)), size=(45,15), background_color='lightgrey')]
            ],
            element_justification='left'
        )]
    ]

    # Right column contains chart controls
    # Note: open chat button functionality will be implemented in the next version
    # and possibly integrated into the DES window instead of a separate window

    control_column = [
        [psg.Column(
            layout=[
                [psg.Button('Close', key='-DES_EXIT-', size=(10,1), pad=(0,(0,50)))],
                [psg.Text('Description', font='Any 12', size=(25,5), pad=(0,(0,20)), background_color='#D0E9DD')],
                [psg.Text('Zoom', size=(5,1)), psg.Slider(range=(1,100), default_value=1, orientation='h', key='-ZOOM-', enable_events=True)],
                [psg.Text('Pan', size=(5,1)), psg.Slider(range=(1,100), default_value=1, orientation='h', key='-PAN-', enable_events=True)],
                [psg.Button('Open chat', key='-CHAT-', size=(10,1), pad=((0, 50),(10,10)))]
            ],
            element_justification='right'
        )]
    ]

    # Full layout
    layout = [[
            psg.Column(display_column), 
            psg.Column(control_column)
        ]]
    return psg.Window('Data Explorer 1', layout, size=(700, 400), finalize=True)


def make_des_window(user):
    """
        This function sets the layout for each DES window.

        Parameters:
            user (str): The user to display the DES for.

        Returns:
            window (PySimpleGUI.Window): The window object.
    """
    # Left column contains chart display and title
    display_column = [
        [psg.Column(
            layout=[
                [psg.Text(f'{user}\'s DES', font='Any 20', justification='center', pad=(0,0))],
                [psg.Text('DES Title', font='Any 16', pad=(0,(0,10)))],
                [psg.Text('Chart goes here', pad=(0,(0,20)), size=(45,15), background_color='lightgrey')]
            ],
            element_justification='left'
        )]
    ]

    # Right column contains chart controls
    control_column = [
        [psg.Column(
            layout=[
                [psg.Button('Close', key='-DES_EXIT-', size=(10,1), pad=(0,(0,50)))],
                [psg.Text('Description', font='Any 12', size=(25,5), pad=(0,(0,20)), background_color='#D0E9DD')],
                [psg.Text('Zoom', size=(5,1)), psg.Slider(range=(1,100), default_value=1, orientation='h', key='-ZOOM-', enable_events=True)],
                [psg.Text('Pan', size=(5,1)), psg.Slider(range=(1,100), default_value=1, orientation='h', key='-PAN-', enable_events=True)],
                [psg.Button('Open chat', key='-CHAT-', size=(10,1), pad=((0, 50),(10,10)))]
            ],
            element_justification='right'
        )]
    ]

    # Full layout
    layout = [[
            psg.Column(display_column), 
            psg.Column(control_column)
        ]]
    return psg.Window('Data Explorer 1', layout, size=(700, 400), finalize=True)


def set_theme():
    """
    This function sets the default PySimpleGUI theme for the program.
    """
    psg.SetOptions(
        background_color='#95D0B3', 
        text_element_background_color='#95D0B3',
        text_color="#2D6A4F",
        font='Any 12',
        element_background_color='#D0E9DD',
        input_elements_background_color='#F7F3EC',
        button_color=('white','#2D6A4F'),
        titlebar_background_color='red',
        titlebar_text_color='black'
    )


def update_des_list(window, username):
    """
        This function updates the list of other DES screens.

        Parameters:
            window (PySimpleGUI.Window): The window object.
            username (str): The username of the active account.
    """
    # Get all DES names except the user's
    des_list = requests.get_other_names(username) 

    # Placeholder text if no DES screens available
    if len(des_list) == 0:
        window.extend_layout(
            window['-DES_COL-'], [[psg.Text('No DES screens available.')]]
        )
        
    # Add DES buttons to the list
    else:
        for des in des_list:
            window.extend_layout(
                window['-DES_COL-'], [[psg.Button(des, 
                key=f'-BTN_HOME_DES_{des}-', size=(15,1))]]
            )


def main():
    """
        This is the main function for the program. It handles the windows and display.
    """
    # Set theme and create initial windows
    set_theme()
    window_1, des_windows = set_window_1(), []
    active_screen = 'WELCOME'
    username = None

    # Main event loop
    while True:
        # Get events from all active windows
        window, event, values = psg.read_all_windows()
        # Handle any window 1 events
        if window == window_1:
            # Close program on exit
            if event in (psg.WIN_CLOSED, '-BTN_WELCOME_EXIT-', '-BTN_HOME_EXIT-'):
                break

            # Handle event
            new_active, kwargs = events.event_processor(event, values, 1)

            # Create new DES window if required
            if new_active == 'MYDES':
                des_windows.append(make_my_des_window())
                new_active = 'HOME'
            elif new_active == 'DES':
                des_windows.append(make_des_window(kwargs['user']))
                new_active = 'HOME'

            # Tasks on first home screen load
            if new_active == 'HOME' and username == None:
                # Add username to home screen
                username = kwargs['username']
                window_1['-TXT_HOME_WELCOME-'].update(f'Welcome {username}!')
                
                # Update DES list with other DES screens
                update_des_list(window_1, username)

            # Update screen if required
            if active_screen != new_active:
                window_1[f'-COL_{active_screen}-'].update(visible=False)
                active_screen = new_active
                window_1[f'-COL_{active_screen}-'].update(visible=True)

        # Handle any DES window events
        else:
            # Identify which DES window the event came from
            for des_window in des_windows:
                if des_window == window:
                    # Handle exit event
                    if event in (psg.WIN_CLOSED, '-DES_EXIT-'): # to be fixed
                        des_window.close()
                        des_windows.remove(des_window)
                        break 
                    # Event will be handled by the DES window handler
                    # once implemented in the next version

    # Close windows on exit
    window_1.close()
    if des_windows:
        for des_window in des_windows:
            des_window.close()


if __name__ == '__main__':
    main()