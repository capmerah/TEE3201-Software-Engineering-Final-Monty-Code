import ToDo as ToDo

class Deadline(ToDo.ToDo):

    TYPE_KEY = 'D'

    def __init__(self, description, status, expiry):
        super().__init__(description, status)
        self.expire = expiry

    def as_csv(self):
        """ Return the details of deadline object as a list,
        suitable to be stored in a csv file.
        """
        return [Deadline.TYPE_KEY, self.description, 'done' if self.is_done else 'pending' , self.expire]
    