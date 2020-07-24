import pickle
from functools import reduce
from os import path
import re

from exceptions import WrongNumberOfArguments


def loadCampaign(self, campaignID):
    if path.exists(f'/resources/campaign_{campaignID}.pickle'):
        with open(f'/resources/campaign_{campaignID}.pickle', "rb") as camp_file:
            campaign = pickle.load(camp_file)


def buildMessage(message, *msg_args, param_prefix='@'):
    params = []

    # Extracting and striping white spaces from params
    for param, arg in re.findall(r'((^| )' + param_prefix + '\w+)', message):
        param = re.sub(" ", "", param)
        params.append(param)

    if not len(params) == len(msg_args):
        raise WrongNumberOfArguments

    for index, arg in enumerate(msg_args):
        message = message.replace(params[index], arg)

    return message
