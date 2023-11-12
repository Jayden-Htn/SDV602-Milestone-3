"""
Scans a csv file redirected or from the file object passed into the script
 "--header" indicates the first row is a header row
"""
import sys as sys
from typing import Dict

global file_path
file_path = './database/des_data/'

class Data_Manager():
    dict_list = []
    value_list = []
    def __init__(self) -> None:
        self.status: Dict = {}
        self.current_file = None


    def find_file(self, path_to_file):
        """
        Gets a file object for the path_to_file, handling any errors.

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


    def get_data(self, user):
        """
        Top-level function for des data retrieval. Find the user's matching csv file and scan the data on it.

        Parameters:
            user (str): The user's name.

        Returns:
            dict_list (list): A list of dictionaries representing the rows in the csv file.
            values_list (list): A list of lists representing the rows in the csv file.
        """
        # Get file object
        csv_file_obj = self.find_file(file_path+user+'.csv')
        # Handle error
        if 'File Error' in self.status:
            self.close_file(csv_file_obj)
            return None
        # If file object is valid, scan the file
        dict_list, values_list = self.scan(filter=None, has_header = True, csv_file = csv_file_obj)
        self.close_file(csv_file_obj)
        Data_Manager.dict_list = dict_list
        Data_Manager.value_list = values_list
        # If scan is valid, display the table
        # if not('File Error') in data_manager.status: data_manager.display_table(dict_lst)


    def get_chart_info(self, user):
        """
        Gets the chart title and description from the csv file.
        """
        csv_file_obj = self.find_file(file_path+'des.csv')
        # Handle error
        if 'File Error' in self.status:
            self.close_file(csv_file_obj)
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


if __name__ == "__main__":
    """
    Main function for testing.
    """
    pass




       


