

class UserInterface: # an object of this class can be used to handle reading input from the user and showing output back to the user.



    def display(self, message):
        print(message)


    def read_command():
        name = input()
        return name

    def show_greeting():
        banner = '''
*******************************************************************************************
*  __          __  _                            _          __  __             _           *
*  \ \        / / | |                          | |        |  \/  |           | |          *
*   \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | \  / | ___  _ __ | |_ _   _   *
*    \ \/  \/ / _ \ |/ __/ _ \| '_ ' _ \ / _ \ | __/ _ \  | |\/| |/ _ \| '_ \| __| | | |  *
*     \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | | (_) | | | | |_| |_| |  *
*      \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  |_|\___/|_| |_|\__|\__, |  *
*                                                                                  __/ |  *
*                                                                                 |___/   *
*******************************************************************************************
    '''
        print(banner.strip(), '\n')
        print('LIST OF COMMANDS:\n')
        print(' exit     close the program \n \
list       list the items that you have added through todo and deadline commands \n \
chfile     change the file \n \
todo       Add a name of the task after "todo" into the list \n \
deadline   Add a name of a task after "deadline" into the list. Type in "by:" after the task name and set a deadline \n \
done       type done followed by an index number listed in the list to indicate that the item is done \n \
pending    type pending followed by an index number listed in the list to indicate that the item is pending \n \
delete     delete an item from the list by typing "delete" followed by an index number \n \
help       show commands')
        print('>>> What can I do for you?\n')  
