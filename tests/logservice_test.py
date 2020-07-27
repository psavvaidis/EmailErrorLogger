import unittest
from logservice import LogService
from campaign import Campaign


class TestOperations(unittest.TestCase):
    _service = LogService()

    def test_init(self):
        self.assertIsInstance(self._service, LogService)

    def test_createAndSaveCampaign(self):
        sender = 'my@example.com'
        recipients = [
            'you@example.com'
            'him@example.com'
        ]
        subject = 'New Email'
        body = 'Hello user, \n\n\tThis is a dummy mail\n\nBest Regards'
        title = 'Dummy campaign'

        dummyCampaign = self._service.createCampaign(title, sender, recipients, subject, body)
        self.assertIsInstance(dummyCampaign, Campaign)
        print(self._service.campaigns)
        self._service.save()
