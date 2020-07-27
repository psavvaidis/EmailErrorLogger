from logservice import LogService
import helpers


def loadCampaign():
    camTitle = input('Enter Campaign Title')
    for campaign in service.campaigns:
        if camTitle == campaign['title']:
            return helpers.loadCampaign(campaign['id'])


def printMenu():
    return input(
        'Menu:\n'
        '1. List all Campaigns\n'
        '2. Load a Campaign by title\n'
        '3. Update a Campaign by title\n'
        '4. Delete a Campaign by title\n'
        '5. Send a custom message through a campaign\n'
        '6. Exit\n\n'
    )


# The User Interface
print("\n\tWelcome to Email Error Logger\n\n")
service = LogService()
while True:
    option = printMenu()
    if str(option) == '1':
        print(service.campaigns)
    elif str(option) == '2':
        loadCampaign()
    elif str(option) == '3':
        pass
    elif str(option) == '4':
        pass
    elif str(option) == '5':
        pass
    elif str(option) == '6':
        exit()
