"""
Scans a csv file redirected or from the file object passed into the script
 "--header" indicates the first row is a header row
"""
import sys as sys
from os import path
import argparse
from typing import Dict

class Data_Manager():
    dict_list = []
    value_list = []
    def __init__(self) -> None:
        self.status:Dict = {}
        self.current_files:Dict = {}
        self.current_file = None


    def find_file(self, path_to_file):
        """
        Gets a file object for the path_to_file

        Args:
            path_to_file (str): The path to the file.
        """
        try:
            self.current_file = open(path_to_file)
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
                
        
    def close_file(self,file_object):
        file_object.close()


    def scan(self,filter= None, has_header=False, csv_file= sys.stdin):
        """
        Scans a csv and returns the row values in dictionary and list structures.

        Args:
            filter (function, optional): A function that filters the rows in the csv file. Defaults to None.
            has_header (bool, optional): Indicates if the csv file has a header row. Defaults to False.
            csv_file (file object, optional): The file object to scan. Defaults to sys.stdin.

        Returns:
            result (list): A list of dictionaries representing the rows in the csv file.
            values (list): A list of lists representing the rows in the csv file.
        """
        result = []
        values = []
        do_header = has_header
        header_names = {}
        try:
            lines = [aline for aline in csv_file if filter(aline)] if filter != None else csv_file
            for aline in lines:
                    this_line = aline.strip().split(',')
                    if do_header:
                        header_names = this_line
                        # print(f" header names {header_names}")
                        do_header = False
                    else:
                        a_dict = {}
                        i = 0
                        max_header_index = len(header_names) -1 
                        for column in this_line:
                            if has_header :
                                if i > max_header_index :
                                    break
                                
                                a_dict[header_names[i]] = column
                            else:
                                a_dict[i]= column
                            i = i + 1 
                        
                        result += [a_dict]
                        values += [this_line]
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return None, None

        Data_Manager.dict_list = result
        Data_Manager.value_list = values 
        return result, values


    def display_table(self,a_list_of_dictionary):
        """
        Prints a table with a header - if there is no header the header becomes the column number.

        Args
                a_list_of_dictionary - each item in the list is a Dictionary representing a Row in the table.
        """
        if a_list_of_dictionary != [] :
            lines = ""
            # Get a header line
            a_dictionary = a_list_of_dictionary[0]
            header_line = ""
            for key in a_dictionary:
                header_line += f'{key}\t'
            header_line = header_line.strip()

            # Make up the table
            lines += header_line 

            for a_dictionary in a_list_of_dictionary:
                a_line = ''
                for key,value in a_dictionary.items():
                    a_line += f'{value}\t'
                a_line = a_line.strip()
                lines += f'\n{a_line}'
            print(lines)
        else:
            print("No items to tabulate")


    def line_col(x,num):
        """
        Gets num place value from each column.
        """
        c =  (x.strip().split(',')[num]).strip()
        return c


    def get_data(user):
        """
        Find the right file for the user's des.

        Parameters:
            user (str): The user's name.
        """
        file_path = './database/des_data/'
        data_manager = Data_Manager()
        # Get file object
        csv_file_obj = data_manager.find_file(file_path+user+'.csv')
        # Handle error
        if 'File Error' in data_manager.status:
            return None
        # If file object is valid, scan the file
        dict_list, values_list = data_manager.scan(filter=None, has_header = False, csv_file = csv_file_obj)
        data_manager.close_file(csv_file_obj)
        Data_Manager.dict_list = dict_list
        Data_Manager.value_list = values_list
        print(f" STATUS [{data_manager.status}]")
        print("values:", values_list[:5])
        # If scan is valid, display the table
        # if not('File Error') in data_manager.status: data_manager.display_table(dict_lst)


if __name__ == "__main__":
    """
    """
    # csv_file_name = "data.csv"
    # data_manager = Data_Manager()
    # csv_file_obj = data_manager.get_file(csv_file_name)
    # print(f" STATUS [{data_manager.status}]")
    # if not('File Error') in data_manager.status:
    #     dict_lst,values_lst = data_manager.scan(filter=lambda line: '5' in [line_col(line,4)], has_header = False, csv_file = csv_file_obj)
    #     data_manager.close_file(csv_file_obj)
    #     if not('File Error') in data_manager.status: data_manager.display_table(dict_lst)

       


