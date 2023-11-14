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


    def scan(self, has_header=False, csv_file= sys.stdin):
        """
        Scans a csv and returns the row values in dictionary and list structures.

        Args:
            filter (function, optional): A function that filters the rows in the csv file. Defaults to None.
            has_header (bool, optional): Indicates if the csv file has a header row. Defaults to False.
            csv_file (file object, optional): The file object to scan. Defaults to sys.stdin.

        Returns:
            dict, list: The row values in dictionary and list structures.
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
        # print("values_dict:", values_dict)
        return values_dict


    def get_data(self, user):
        """
        Top-level function for des data retrieval. Find the user's matching csv file and scan the data on it, storing the results in the Data_Manager class.

        Parameters:
            user (str): The user's name.

        Returns:
            bool: True if the data was retrieved successfully, False otherwise.
        """
        # Get file object
        csv_file_obj = self.find_file(file_path+user+'.csv')
        # Handle error
        if 'File Error' in self.status:
            self.close_file(csv_file_obj)
            return False
        # If file object is valid, scan the file
        dict_list = self.scan(has_header = True, csv_file = csv_file_obj)
        self.close_file(csv_file_obj)
        Data_Manager.dict_list = dict_list
        return True


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




       


