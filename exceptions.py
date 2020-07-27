class WrongNumberOfArguments(TypeError):

    def __init__(self, error_message):
        self._message = error_message

    def __str__(self):
        return f'Wrong number of arguments was passed. {self._message}'
