"""Create and add label to user's account.
"""

from apiclient import errors


def CreateLabel(service, user_id, label_object):
    """Creates a new label within user's mailbox, also prints Label ID.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      label_object: label to be added.

    Returns:
      Created Label.
    """
    try:
        label = service.users().labels().create(userId=user_id,
                                                body=label_object).execute()
        print(label['id'])
        return label
    except errors.HttpError as error:
        print('An error occurred: %s' % error)


def MakeLabel(label_name, mlv='show', llv='labelShow'):
    """Create Label object.

    Args:
      label_name: The name of the Label.
      mlv: Message list visibility, show/hide.
      llv: Label list visibility, labelShow/labelHide.

    Returns:
      Created Label.
    """
    label = {'messageListVisibility': mlv,
             'name': label_name,
             'labelListVisibility': llv}
    return label


def CreateMsgLabels(*labels):
    """Create object to update labels.

    Returns:
      A label update object.
    """

    labelsArray = []
    for label in labels:
        labelsArray.append(label)

    return {'removeLabelIds': [], 'addLabelIds': labelsArray}


def RemoveMsgLabels(*labels):
    """Create object to update labels.

    Returns:
      A label update object.
    """

    labelsArray = []
    for label in labels:
        labelsArray.append(label)

    return {'removeLabelIds': labelsArray, 'addLabelIds': []}
