# CUSTOMER MANAGEMENT #

# DO NOT MODIFY CONSTANTS
CLIENT_SEGMENT_SAMPLE_1 = [
    {'first-name': 'Elsa', 'last-name': 'Frost', 'title': 'Princess',
     'address': '33 Castle Street, London', 'loyalty-program': 'Gold'},
    {'first-name': 'Anna', 'last-name': 'Frost', 'title': 'Princess',
     'address': '34 Castle Street, London', 'loyalty-program': 'Platinum'},
    {'first-name': 'Harry', 'middle-name': 'Harold', 'last-name': 'Hare',
     'title': 'Mr', 'email-address': 'harry.harold@hare.name',
     'loyalty-program': 'Silver'},
    {'first-name': 'Leonnie', 'last-name': 'Lion', 'title': 'Mrs',
     'loyalty-program': 'Silver'},
    ]


def preprocess_client_segment(segment):
    '''
    This function simplifies a segment of clients to prepare for a marketing
    campaign. For each client in the segment, if the client has a registered
    address, it makes a tuple that contains the following details:
        - full name with title (e.g., "Mr John Smith") omitting any part that
          are not provided,
        - the mailing address (not the email-address).
    If a client has no registered address, it should not be included in the
    returned list.

    E.g., preprocess_segment_for_marketing_campaign(CLIENT_SEGMENT_SAMPLE_1)
    inlcudes 'Princess Elsa Frost' but it should not include 'Mrs Leonnie
    Lion' because there are no associated addresses in the data.

    @param segment a list of client records. See sample above.
    @return a preprocessed list of full names and mailing address.
    '''
    raise NotImplementedError
