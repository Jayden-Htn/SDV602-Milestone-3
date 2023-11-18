"""
Scans a csv file redirected or from the file object passed into the script
 "--header" indicates the first row is a header row
"""
import sys as sys
from typing import Dict
import csv

from model.network.jsn_drop_service import jsnDrop

global file_path
file_path = './database/des_data/'


class Data_Manager():
    """
    This class handles the data for the DES.
    """
    jsn_tok = "14419e82-082e-4ae7-a128-ef0118e9d483"

    def __init__(self) -> None:
        self.status: Dict = {}
        self.current_file = None
        self.dict_list = []
        self.jsnDrop = jsnDrop(self.jsn_tok,"https://newsimland.com/~todd/JSON")
        # Schema for tables, will not wipe existing data
        # self.jsnDrop.drop('tblData') # Optional clear tables
        result = self.jsnDrop.create("tblData", {"ID PK auto": 'xxxxxxxxxx',
                                                "DESName": "A_LOOONG_DES_Name"+('X'*50),
                                                "ColumnName": "A_LOOONG_Col_Name"+('X'*50),
                                                "DataValue": "A_LOONG_Data_Value"+('X'*255),
                                                })


    def find_file(self, path_to_file, mode='r'):
        """
        Gets a file object for the path_to_file, handling any errors.

        Args:
            path_to_file (str): The path to the file.

        Returns:
            file object: The file object or None if an error occurred.
        """
        try:
            self.current_file = open(path_to_file, mode)
            return self.current_file
        except FileNotFoundError:
            file_not_found = ("File not found error", path_to_file)
            self.status['File Error'] = [file_not_found] if not ('File Error' in self.status) else self.status['File Error'] + [file_not_found]
            return None
        except FileExistsError   :
            file_exists_error = ("File exists error", path_to_file)
            self.status['File Error'] =  [file_exists_error] if not ('File Error' in self.status) else self.status['File Error'] + [file_exists_error]
            return None 
        except:
            print("Unexpected error:", sys.exc_info()[0]) 
            return None
                
        
    def close_file(self, file_object):
        file_object.close()


    def scan(self, has_header=False, csv_file=sys.stdin):
        """
        Scans a csv and returns the row values in dictionary and list structures.

        Args:
            filter (function, optional): A function that filters the rows in the csv file. Defaults to None.
            has_header (bool, optional): Indicates if the csv file has a header row. Defaults to False.
            csv_file (file object, optional): The file object to scan. Defaults to sys.stdin.

        Returns:
            dict, list: The row values in dictionary and list structures (e.g. {'header1': ['value1', 'value2'], 'header2': ['value1', 'value2']})
        """
        values_dict = {}
        try:
            # Set up dict with headers as keys
            this_line = csv_file.readline().split(',')
            for i in range(len(this_line)):
                values_dict[this_line[i].strip()] = []
            
            # Read each line of the csv file and append to each column
            for aline in csv_file:
                this_line = aline.strip().split(',')
                for col, header in zip(this_line, list(values_dict.keys())):
                    values_dict[header].append(col)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return None
        return values_dict
    

    def clear_data(self, user):
        """
        Clears the data for a user.

        Parameters:
            user (str): The user's name.
        """
        # Clear remote data
        api_result = self.jsnDrop.delete("tblData", f"DESName = '{user}'")
        # Clear local data
        csv_file_obj = self.find_file(file_path+user+'.csv', 'w')
        csv_file_obj.write('')
        self.close_file(csv_file_obj)
        # Clear info data
        try:
            with open(f'{file_path}des.csv', 'r') as csv_file_obj:
                csv_file_obj = self.find_file(file_path+'des.csv', 'r+')
                lines = csv_file_obj.readlines()
            for i in range(len(lines)):
                this_line = lines[i].strip().split(',')
                print(this_line)
                # If the user's name is found, delete row
                if this_line[0] == user:
                    del lines[i]
                    break
            # Write the updated lines to the csv file
            with open(f'{file_path}des.csv', 'w') as csv_file_obj:
                csv_file_obj.seek(0)
                csv_file_obj.writelines(lines)
        except:
            print("Unexpected error:", sys.exc_info()[0])
        # Update remote info
        # self.update_des_info(user, '', '')
    

    def write_csv(self, values_dict):
        """
        Writes a csv file from a dictionary. Will overwrite any existing file.

        Args:
            values_dict (dict): The values to write to the csv file.

        Returns:
            str: The csv file as a string.
        """
        csv_str = ''
        # Write the header row
        for header in list(values_dict.keys()):
            csv_str += header + ','
        csv_str += '\n'
        # Write each row
        for i in range(len(values_dict[list(values_dict.keys())[0]])):
            for header in list(values_dict.keys()):
                csv_str += values_dict[header][i] + ','
            csv_str += '\n'
        return csv_str
    

    def update_remote_data(self, user, column, data):
        """
        Updates the remote data for a des.

        Parameters:
            user (str): The user's name.
            column (str): The column name.
            data (str): The data to update.
        """
        data_list = []
        for item in data:
            data_list.append({"DESName": user, "ColumnName": column, "DataValue": item})
        api_result = self.jsnDrop.store("tblData", data_list)


    def merge_data(self, new_file, user_name):
        # Note: The use of reading and writing could definitely be optimised more, 
        # # but this is a quick solution for now due to time constraints

        # Get new data
        with open(f'{new_file}', 'r') as csv_file:
            new_data = self.scan(has_header=True, csv_file=csv_file)
            # Know file must exists as found in browser

        # Get existing user file
        existing_file_obj = self.find_file(file_path+user_name+'.csv', 'r') # a+ doesn't work, must be r to get data first
        # See if file exists
        if 'File Error' in self.status and self.status['File Error'][0][0] == 'File not found error':
            # If file dosn't exist, create new file in local storage
            with open(f'{file_path}{user_name}.csv', 'w') as new_csv:
                new_csv.write(self.write_csv(new_data))
        else:          
            # Get data from existing file
            existing_data = self.scan(has_header=True, csv_file=existing_file_obj)
            self.close_file(existing_file_obj)

            # If no data in existing file, just write as can't match headers
            if existing_data == {'': []} or existing_data == None:
                with open(f'{file_path}{user_name}.csv', 'w') as csv_file:
                    csv_file.write(self.write_csv(new_data))
            else:
                # Make set of current headers
                existing_headers = set(list(existing_data.keys()))

                # Match data to current headers, delete any not matching
                for header in list(new_data.keys()):
                    if header not in existing_headers:
                        del new_data[header]

                # Add new rows to existing file, row by row
                for col in list(existing_data.keys()):
                    if col in list(new_data.keys()):
                        existing_data[col] += new_data[col]
                    else:
                        existing_data[col] += [''] * len(new_data[list(new_data.keys())[0]])

                # Write the updated lines to the csv file
                existing_file_obj = self.find_file(file_path+user_name+'.csv', 'w') # reopen in mode w now
                existing_file_obj.write(self.write_csv(existing_data))
                self.close_file(existing_file_obj)
            
    

    def update_des_file(self, user):
        """
        Updates the local csv file from the remote server.

        Parameters:
            user (str): The user's name.
        """
        # Get file object
        csv_file_obj = self.find_file(file_path+user+'.csv')
        # Handle error
        if 'File Error' in self.status:
            return False
        # Get file from jsndrop
        api_result = self.jsnDrop.select("tblData", f"DESName = '{user}'")
        # Handle error
        if "ERROR" in api_result:
            result = self.jsnDrop.jsnStatus
        else:
            result = api_result
            # Write the file to local storage
            try:
                self.current_file.write(self.write_csv(result))
            except:
                print("Unexpected error:", sys.exc_info()[0])
                return False
            self.close_file(csv_file_obj)
        return True


    def get_data(self, user):
        """
        Top-level function for des data retrieval. Updates local files from remote server. 
        Find the user's matching csv file and scan the data on it, storing the results in the Data_Manager class.

        Parameters:
            user (str): The user's name.

        Returns:
            bool: True if the data was retrieved successfully, False otherwise.
        """
        # Update local file from remote server
        self.update_des_file(user)
        # Get file object
        csv_file_obj = self.find_file(file_path+user+'.csv')
        # Handle error
        if 'File Error' in self.status:
            return False
        # If file object is valid, scan the file
        self.dict_list = self.scan(has_header=True, csv_file=csv_file_obj)
        self.close_file(csv_file_obj)
        return True


    def get_chart_info(self, user):
        """
        Gets the chart title and description from the csv file.
        """
        csv_file_obj = self.find_file(file_path+'des.csv')
        # Handle error
        if 'File Error' in self.status:
            return None
        # Read each line of the csv file
        try:
            for aline in csv_file_obj:
                this_line = aline.strip().split(',')
                # If the user's name is found, return the chart info
                if this_line[0] == user:
                    self.close_file(csv_file_obj)
                    return {'title': this_line[1], 'description': this_line[2]}
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return None
        self.close_file(csv_file_obj)
        return None
    

    def update_des_info(self, user, title, description):
        """
        Updates the chart title and description in the csv file.

        Parameters:
            user (str): The user's name.
            title (str): The chart title.
            description (str): The chart description.
        """
        found = False
        csv_file_obj = self.find_file(file_path+'des.csv', 'r+')
        # Handle error
        if 'File Error' in self.status:
            return False
        # Read each line of the csv file
        try:
            lines = csv_file_obj.readlines()
            self.close_file(csv_file_obj)
            for i in range(len(lines)):
                this_line = lines[i].strip().split(',')
                # If the user's name is found, update the chart info
                if this_line[0] == user:
                    del lines[i]
            # Write new info to csv file
            with open(f'{file_path}des.csv', 'w') as csv_file_obj:
                csv_file_obj.seek(0)
                csv_file_obj.writelines(lines)
                csv_file_obj.write(user + ',' + title + ',' + description + '\n')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return False
        self.close_file(csv_file_obj)
        return True


if __name__ == "__main__":
    """
    Main function for testing.
    """
    pass




       


