import unittest
from logservice import LogService


class TestProperFunctionality(unittest.TestCase):


    def test_createCampaign(self):
        _service = LogService()
        sender = 'my@example.com'
        recipients = [
            'you@example.com'
            'him@example.com'
        ]
        subject = 'New Email'
        body = 'Hello user, \n\n\tThis is a dummy mail\n\nBest Regards'
        title = 'Dummy campaign'

        dummyCampaign = _service.createCampaign(title, sender, recipients, subject, body)
        print(dummyCampaign)
