import os
import csv

import ToDo as ToDo
import Deadline as Deadline

class StorageManager: # an object of this class can be used to read data from the data file and write data back to the data file.


    def save_data(self, filename, items_to_save):
        output_file = open(str(filename), 'w', newline='')
        output_writer = csv.writer(output_file)
        for item in items_to_save:
            output_writer.writerow(item) #.as_csv()
        output_file.close()


    def create_file_if_missing(self, filename):
        if not os.path.exists(filename):
            open(filename, 'a').close()


    def load_data(self, filename, items):
        with open(str(filename), 'r') as data_file:
            deliveries_reader = csv.reader(data_file)
            for row in deliveries_reader:
                if row[0] == 'T':
                    ToDo_instance = ToDo.ToDo(row[1], True if row[2] == 'done' else False)
                    items.append(ToDo_instance.as_csv())
                elif row[0] == 'D':
                    Deadline_instance = Deadline.Deadline(row[1], True if row[2] == 'done' else False, row[3])
                    items.append(Deadline_instance.as_csv())
            data_file.close()

    def check_directory_for_csv_files(self, filename):
        csv_files = []
        cwd = os.getcwd()
        for filename in os.listdir(cwd):
            if filename.endswith(".csv"):
                csv_files.append(filename)

        if len(csv_files) > 0:
            print(f">>> The directory contains {len(csv_files)} CSV file(s):")
            for file in csv_files:
                print(file)
        else:
            print("No CSV files found in the directory.")


    def specify_which_csv_files(self):

        while True:
            try:
                filename = input(">>> Please enter the filename of the CSV file above(without .csv): " ) + '.csv'

                print('\nThe file you have chosen is: ' + filename , '\n')
                print('>>> What can I do for you? \n')
                return str(filename)
            except FileNotFoundError as e:
                print(f"Error: File {e.filename} not found. Please enter a valid filename.")

