# SDV602-Milestone-3

Python data set explorer for NMIT SDV602 milestone 3 2023. This program is based of the work done for milestone 2.

Please read this document before setting up and using the program. 


## Installation

How to run the game:

1. Download the repository and open in VS Code.
2. Run `python -m venv venv` to install a virtual environment if you do not already have one set up.
3. Run `source venv/Scripts/activate` in the terminal to start the virtual environment if it is not active.
4. Run `pip install -r requirements.txt` in the terminal to install dependancies.
5. Run the main.py script.


## Dependancies

- Python V3.11.4
- PySimpleGUI V4.60.5

These can be installed by running the command `pip install -r requirements.txt` in the terminal.

Requirements.txt is generated by running `pip freeze > requirements.txt` in the terminal.


## Venv

Venv terminal commands:
- Create new venv: `python -m venv venv`
- Activate venv: `source venv/Scripts/activate`
- Exit errors: `exit()`


## Code Style

This code is formatted in accordance to the PEP8 and PEP257 style guides.

I have developed my own convention for PySimpleGUI (PSG) keys based on the recommended convention. PSG recommends following the most recent convention of '-BUTTON_1-'. Since I am having multiple screens display off one window and have duplicated button names (e.g. multiple login buttons across pages), I have decied to use the mofiied convention of '-TYPE_PAGE_NAME-', e.g. '-BTN_LOGIN_BACK-'. This will allow me to differentiate between pages. Like how the input convention is to use '-IN_NAME-', adding the type for buttons ('btn') will help to identify between buttons and inputs.
