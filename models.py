import pickle, json, random, time
from os import path


class Campaign:
    _id: int

    def __init__(self, title, sender, *recipients, message_subj=None, message_body=None):
        self._id = random.seed(time.time())
        self._title = title
        self._sender = sender
        self._recipients = recipients
        self._subject = message_subj
        self._body = message_body

    def __str__(self):
        return f'Campaign {self._title}'

    def save(self):
        with open(f'campaign_{self._id}.pickle', "wb") as camp_file:
            pickle.dump(self, camp_file)

    def getID(self):
        return self._id

    def getTitle(self):
        return self._title
