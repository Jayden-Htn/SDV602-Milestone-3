"""
This module provides a wrapper for the JsnDrop API.
"""


# Imports
import requests 
import json 


class jsnDrop(object):
    """
    This class provides a wrapper for the JsnDrop API

    Functions:
        _jsnDropApi(command): This function sends a command to the JsnDrop API.
        create(table_name, example): This function creates a table.
        store(table_name, value_list): This function stores values in a table.
        all(table_name): This function gets all the values in a table.
        select(table_name, where): This function gets values from a table where a condition is met.
        delete(table_name, where): This function deletes values from a table where a condition is met.
        drop(table_name): This function drops (deletes) a table.
    """
    def __init__(self, tok = None, url = None) -> None:
        self.tok = tok
        self.url = url
        self.jsnStatus = ""
        self.jsnResult = {}

        # Setting up data structures for storing JsnDrop Commands
        self.decode = json.JSONDecoder().decode
        self.encode = json.JSONEncoder().encode

        self.jsnDropRecord = self.decode('{"tok":"","cmd":{}}')
        self.jsnDropCreate = self.decode('{"CREATE":"aTableName","EXAMPLE":{}}')
        self.jsnDropStore  = self.decode('{"STORE":"aTableName","VALUE":[]}')
        self.jsnDropAll    = self.decode('{"ALL":"aTableName"}')
        self.jsnDropSelect = self.decode('{"SELECT":"aTableName","WHERE":"aField = b"}')
        self.jsnDropDelete = self.decode('{"DELETE":"aTableName","WHERE":"aField = b"}')
        self.jsnDropDrop   = self.decode('{"DROP":"aTableName"}')


    def _jsnDropApi(self, command):
        """
        This function sends a command to the JsnDrop API. 

        Parameters:
            command (dict): The command to send.

        Returns:
            dict: The result of the command.
        """
        # Set up the payload
        api_call  = self.jsnDropRecord
        api_call["tok"] = self.tok
        api_call["cmd"] = command
        payload = {'tok': self.encode(api_call)}
        
        # Send the request
        r = requests.get(self.url, payload)

        # Update the status and result
        jsnResponse = r.json()
        self.jsnStatus = jsnResponse["JsnMsg"]
        self.jsnResult = jsnResponse["Msg"]

        # Feedback to check it works
        # print(f"Status = {self.jsnStatus} , Result = {self.jsnResult}")
        return self.jsnResult 

    
    def create(self, table_name, example):
        """
        This function creates a table.
        """
        command = self.jsnDropCreate
        command["CREATE"] = table_name
        command["EXAMPLE"] = example
        return self._jsnDropApi(command)
        

    def store(self, table_name, value_list):
        """
        This function stores values in a table.
        """
        command = self.jsnDropStore
        command["STORE"] = table_name
        command["VALUE"] = value_list
        return self._jsnDropApi(command)


    def all(self, table_name):
        """
        This function gets all the values in a table.
        """
        command = self.jsnDropAll
        command["ALL"] = table_name
        return self._jsnDropApi(command)


    def select(self, table_name, where):
        """
        This function gets values from a table where a condition is met.
        """
        command = self.jsnDropSelect
        command["SELECT"] = table_name
        command["WHERE"] = where
        return self._jsnDropApi(command)


    def delete(self, table_name, where):
        """
        This function deletes values from a table where a condition is met.
        """
        command = self.jsnDropDelete
        command["DELETE"] = table_name
        command["WHERE"] = where
        return self._jsnDropApi(command)


    def drop(self, table_name):
        """
        This function drops (deletes) a table.
        """
        command = self.jsnDropDrop
        command["DROP"] = table_name
        return self._jsnDropApi(command)
