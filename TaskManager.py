import sys


from ToDo import ToDo
from Deadline import Deadline
from UserInterface import UserInterface
from StorageManager import StorageManager

ui = UserInterface()



class TaskManager: # an object of this class will hold the list of Task/Deadline objects and will execute commands.
    

    def add_item(user_input, items):
        command_parts = user_input.strip().split(' ', 1) # split the command into two: first word and the remainder
        first_action = command_parts[0]
        second_action = command_parts[1]
        keyword = "by: "
        value_of_by = user_input.split(keyword)[-1]
        value_of_discription = user_input.split(keyword)[0].strip().split(' ', 1)

        if first_action == 'todo':
            ToDo_instance = ToDo(second_action, False)
            ToDo_instance.mark_as_pending()
            items.append(ToDo_instance.as_csv())

        elif first_action == 'deadline':
            Deadline_instance = Deadline(value_of_discription[1], False , value_of_by)
            Deadline_instance.mark_as_pending()
            items.append(Deadline_instance.as_csv())


    def get_items_as_table(items):
        if len(items) == 0:
            print('>>> Nothing to list')
        else:
            print('>>> Here is the list of tasks:')
            print('============================================================')
            print('STATUS | INDEX | DESCRIPTION                 | DEADLINE     ')
            print('------------------------------------------------------------')
            i=0
            for i in range(len(items)):  #for i, item in enumerate(items):
                index_number = str(i+1)
                description = str(items[i][1])
                deadline = items[i][-1] if 'D' in items[i][0] else '-'

                aligned_index_number = index_number.center(5," ")
                aligned_description = description.ljust(27," ")                        
                aligned_deadline = deadline.ljust(1," ")

                status = '  -   ' if items[i][2] == 'pending' else '  X   '

                print(status, '|' ,aligned_index_number, '|', aligned_description, '|', aligned_deadline)

        print('------------------------------------------------------------')

    def execute_command(command, items, message):
        if command == '':
            return
        elif command == 'exit':
            TaskManager.terminate()
        elif command == 'list':
            TaskManager.get_items_as_table(items)
        elif command == 'chfile':
            import main
            main.main1()
        elif command == 'help':
            UserInterface.show_greeting()
        elif command.startswith('todo ') or command.startswith('deadline '):
            TaskManager.add_item(command, items)
        elif command.startswith('done '):
            TaskManager.mark_item_as_done(command, items)
        elif command.startswith('pending '):
            TaskManager.mark_item_as_pending(command, items)
        elif command.startswith('delete '):
            TaskManager.delete_item(command, items)
            print('>>> Task deleted from the list\n')
        
        else:
            raise Exception('Command not recognized \n>>> What can I do for you?\n')
        
        ui.display(message)
        

    def terminate(): 
        if TaskManager.is_exit_confirmed():
            print('>>> Bye!')
            sys.exit()
        else:
            print('>>> What can I do for you?\n')

    def is_exit_confirmed():
        print('>>> Are you sure? y/n')
        response = input()
        return response == 'y'


    def get_item_for_index(index_as_string, items):
        try:
            index = int(index_as_string.strip())
        except Exception:
            raise ValueError(index_as_string + ' is not a number \n>>> What can I do for you?\n')

        if index < 1:
            raise ValueError('Index must be greater than 0 \n>>> What can I do for you?\n')

        try:
            return items[index - 1]
        except IndexError:
            raise ValueError('No item at index ' + index_as_string + '\n>>> What can I do for you?\n')
        

    def delete_item(user_input, items):
        index_as_string = user_input[7:]
        index = TaskManager.get_item_for_index(index_as_string, items)
        items.remove(index)


    def mark_item_as_done(user_input, items):
        index_as_string = user_input[5:]
        TaskManager.get_item_for_index(index_as_string, items)[2] = 'done'

 
    
    def mark_item_as_pending(user_input, items):
        index_as_string = user_input[8:]
        TaskManager.get_item_for_index(index_as_string, items)[2] = 'pending'
