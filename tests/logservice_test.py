import unittest
from logservice import LogService
from gmail_api imp


class TestProperFunctionality(unittest.TestCase):
    _service = LogService()

    def test_createCampaign(self):
        sender = 'my@example.com'
        recipients = [
            'you@example.com'
            'him@example.com'
        ]
        subject = 'New Email'
        body = 'Hello user, \n\n\tThis is a dummy mail\n\nBest Regards'
        title = 'Dummy campaign'

        dummyCampaign = self._service.createCampaign(title, sender, recipients, subject, body)
        print(dummyCampaign)
