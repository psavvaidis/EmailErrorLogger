import unittest, helpers
from logservice import LogService
from campaign import Campaign


class TestOperations(unittest.TestCase):
    _service = LogService()

    def test_init(self):
        self.assertIsInstance(self._service, LogService)

    def test_createAndSaveCampaign(self):
        sender = 'my@example.com'
        recipients = [
            'you@example.com',
            'him@example.com'
        ]
        subject = 'New Email'
        body = 'Hello user, \n\n\tThis is a dummy mail\n\nBest Regards'
        title = 'Dummy campaign'

        dummyCampaign = self._service.createCampaign(title, sender, recipients, subject, body)
        self.assertIsInstance(dummyCampaign, Campaign)
        self._service.save()


class TestReloadSession(unittest.TestCase):
    service = LogService()
    campaignObjects = []

    def test_printPreviousData(self):
        print(self.service.campaigns)
        for campaign in self.service.campaigns:
            print(helpers.loadCampaign(campaign['id']))


class TestRealData(unittest.TestCase):
    service = LogService()

    def testSend(self):
        aCampaign = self.service.createCampaign('Test', 'lokep20233@inmail92.com', 'yayan75511@exploraxb.com',
                                                'Test Email', 'Hello @name\n\nThis is the @number test email')
        self.service.log(aCampaign, 'Panos', 'first')
        self.service.log(aCampaign, 'Sav', 'second')
