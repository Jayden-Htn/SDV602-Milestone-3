"""
This module contains the Chat_Manager class for the chat feature.

Classes:
    Chat_Manager: This class handles the chat feature.
"""


# Imports
from model.network.jsn_drop_service import jsnDrop
from datetime import datetime
from threading import Thread
from time import sleep


class Chat_Manager(object):
    """
    This class handles the chat feature.

    Init:
        active_user (str): The name of the active user.
        des_name (str): The name of the DES owner.
        chat_component (sg.Multiline): The chat component.

    Functions:
        send_chat(message): This function sends a chat message to the chat table.
        get_chat(): This function gets the chat messages from the chat table.
        set_test_messages(): This function sets test messages in the chat table.
    """
    jsn_tok = "14419e82-082e-4ae7-a128-ef0118e9d483"


    def now_time_stamp(self):
        time_now = datetime.now()
        # Must be timestamped to be encoded for JsnDrop
        return time_now.timestamp()
    

    def set_chat_component(self, chat_component):
        """
        Sets the chat component.

        Parameters:
            chat_component (sg.Multiline): The chat component.
        """
        self.chat_component = chat_component
 

    def __init__(self, active_user, des_name) -> None:
        super().__init__()
        self.current_status = None
        self.chat_list = []
        self.current_user = active_user
        self.current_des = des_name
        self.chat_component = None
        self.thread = Thread(target=self.thread_updater)
        self.run_thread = True

        self.jsnDrop = jsnDrop(Chat_Manager.jsn_tok,"https://newsimland.com/~todd/JSON")

        # Optional clear tables
        # self.jsnDrop.drop('tblChat')
        
        # Schema for tables, will not wipe existing data
        result = self.jsnDrop.create("tblChat", {"Time PK": self.now_time_stamp(),
                                                "UserName": "A_LOOONG_NAME"+('X'*50),
                                                "DESName": "A_LOOONG_DES_Name"+('X'*50),
                                                "Message": "A_LOONG____CHAT_ENTRY"+('X'*255)
                                                })
        self.thread.start()


    def send_chat(self, message):
        """
        Sends a chat message to the chat table.

        Parameters:
            message (str): The message to send.

        Returns:
            result (str): The result of the operation.
        """
        user_id = self.current_user

        # Update chat display
        time_str = datetime.utcnow()
        time = time_str.strftime('%H:%M')
        self.chat_component.print(f"<{user_id} {time} UTC> {message}")
        self.chat_component.update()
        
        # Update database
        result = None 
        des_screen = self.current_des
        api_result = self.jsnDrop.store("tblChat", [{'Time PK': self.now_time_stamp(),
                                                    'UserName': user_id,
                                                    'DESName': f'{des_screen}',
                                                    'Message': message}])
        # Handle database api results
        if "ERROR" in api_result:
            result = self.jsnDrop.jsnStatus
        else:
            result = "Chat sent"
        return result


    def get_chat(self):
        """
        Gets the chat messages from the chat table.

        Returns:
            result (list): The chat messages.
        """
        result = None
        des_owner = self.current_des
        api_result = self.jsnDrop.select("tblChat",f"DESName = '{des_owner}'")
        # print("api_result:", api_result)
        if not ('Data error' in api_result):
            self.chat_list = self.jsnDrop.jsnResult
            # Delete messages older then 1 week
            for message in self.chat_list:
                if message['Time'] < (self.now_time_stamp() - 604800):
                    self.jsnDrop.delete("tblChat", f"Time = {message['Time']}")

            result = self.chat_list
        else:
            result = None
        return result
    

    def set_test_messages(self):
        """
        Sets test messages in the chat table.
        """
        self.send_chat("Hello")
        self.send_chat("How are you?")
        self.send_chat("I'm fine")
        self.send_chat("Goodbye")


    def thread_updater(self):
        """
        This function updates the chat component with new messages every second.
        """
        while self.run_thread:
            # Update chat
            self.get_chat()
            sleep(1)


    def stop(self):
        """
        Stops the thread.
        """
        self.run_thread = False
