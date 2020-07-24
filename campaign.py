import pickle, json, random, time, helpers
import gmail_api.connect as gmail
from os import path
from gmail_api.utils.messages import *
from gmail_api.utils.labels import *

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

    def updateSubject(self, subject):
        self._subject = subject

    def updateBody(self, body):
        self._body = body

    def log(self, *msg_params):
        client = self.connect()
        body_text = helpers.buildText(self._body, msg_params)
        try:
            message = CreateMessage(self._sender, self._recipients, self._subject, body_text)
            SendMessage(client, 'me', message)
        except:
            pass

        # TODO Finish the method

    def connect(self):
        return gmail.connect()
