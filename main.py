#A0249396L -> 6 -> Digit 6, Choice 3: C-FlexibleDataSource
from UserInterface import UserInterface
from StorageManager import StorageManager
from TaskManager import TaskManager

items = []

def main1():

    ui = UserInterface
    ui.display('', '>>> Adding a new file')

    while True:
        try:
            add_new_file = input('>>> Do you want to name a new file?(y or n). Default file name: monty7.csv ')
            if add_new_file == 'y':
                DATA_FILE = input('>>> Name a new file(without .csv) within the current working directory and press enter: ') + '.csv'
                break
            elif add_new_file == 'n':
                DATA_FILE = 'monty7.csv'
                break
            else:
                raise ValueError('Invalid input: Please enter y or n')
        except ValueError as e:
            print(e)


    ui = UserInterface
    ui.show_greeting()

    Store_manager = StorageManager()
    Store_manager.create_file_if_missing(DATA_FILE)
    Store_manager.check_directory_for_csv_files(DATA_FILE)
    
    DATA_FILE = Store_manager.specify_which_csv_files()
    items = []
    Store_manager.load_data(DATA_FILE, items)
    
    next_questions = '>>> What can I do for you? \n'


    while True:
        try:
            command = ui.read_command()
            Task_manager = TaskManager
            Task_manager.execute_command(str(command), items, str(next_questions))
            Store_manager.save_data(DATA_FILE, items)
        except Exception as e:
            ui.display('SORRY, I could not perform that command. Problem: ' , str(e))


if __name__ == '__main__':
    main1()
