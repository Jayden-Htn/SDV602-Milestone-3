"""
Chat button controller to send messages in the chat.
"""
import sys
sys.dont_write_bytecode = True
import datetime

def accept(event, values, instance):
    if event == '-CHAT_SEND-':
        # Get input message
        message = values['-CHAT_INPUT-']
        if message != '':
            # Send message to chat manager
            instance.chat_manager.send_chat(message)
            # Clear input field
            instance.window['-CHAT_INPUT-'].update('')
    return True

