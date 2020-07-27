class WrongNumberOfArguments(TypeError):

    def __init__(self, error_message):
        self._message = error_message

    def __str__(self):
        return f'Wrong number of arguments was passed. {self._message}'


class APICredentialsNotFound(FileNotFoundError):

    def __str__(self):
        return 'File credentials.json not found. Visit Gmail API website to ask for credentials.json file.\n\n' \
               '!IMPORTANT: As project name use "EshopErrorLogger"'
