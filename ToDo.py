class ToDo:

    TYPE_KEY = 'T'

    def __init__(self, description, status):
        self.description = description
        self.is_done = status
    def mark_as_done(self):
        self.is_done = True
    def mark_as_pending(self):
        self.is_done = False

    def __status_as_icon(self):
        return 'X' if self.is_done else '-'
    def __str__(self):
        return '(' + self.__status_as_icon() + ') ' + self.description

    def as_string(self):
        """ Return the details of todo object as a string"""
        status = 'X' if self.is_done else '-'
        return status.center(6) + ' |' + '   -'.ljust(13) + self.description
    def as_csv(self):
        """ Return the details of todo object as a list,
        suitable to be stored in a csv file.
        """
        return [ToDo.TYPE_KEY, self.description, 'done' if self.is_done else 'pending']
    