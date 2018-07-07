# PARKING MANAGEMENT #

import datetime

# For insurance purposes, the management of an office building is required to
# maintain, at all time, an accurate list of all the vehicles in the dedicated
# parking. In addition, for billing the different companies, the office
# building management wants to record occupation of the parking at different
# times and automatically emit bills to each specific companies.

# You are tasked with completing the series of functions below that fill the
# need of the office building parking management. You are allowed (and
# encouraged) to create additional, intermediate functions.

# The main data structure that your suite of function handles is a record of
# entrances and exits. A sample is given below. It consist of a pair of lists
# of tuples. The first list gives the timestamps and license plate number of
# vehicles entering the parking, the second exiting.

# DO NOT MODIFY CONSTANTS
PARKING_DATA_SAMPLE = (
    [
        (datetime.datetime(2017, 12, 12, 7, 13, 44, 0), 'LR10GHT'),
        (datetime.datetime(2017, 12, 12, 7, 13, 48, 0), 'LC11FBF'),
        (datetime.datetime(2017, 12, 12, 7, 13, 59, 0), 'LR10ZPP'),
        (datetime.datetime(2017, 12, 12, 7, 15, 2, 0), 'LJ65OSN'),
        (datetime.datetime(2017, 12, 12, 7, 15, 22, 0), 'LA63EWH'),
        (datetime.datetime(2017, 12, 12, 13, 1, 42, 0), 'LC11FBF')
    ],
    [
        (datetime.datetime(2017, 12, 12, 12, 13, 1, 0), 'LC11FBF'),
        (datetime.datetime(2017, 12, 12, 16, 42, 10, 0), 'LR10ZPP'),
        (datetime.datetime(2017, 12, 12, 17, 2, 41, 0), 'LR10GHT'),
        (datetime.datetime(2017, 12, 12, 17, 2, 58, 0), 'LA63EWH'),
        (datetime.datetime(2017, 12, 12, 17, 4, 3, 0), 'LJ65OSN'),
        (datetime.datetime(2017, 12, 12, 17, 10, 21, 0), 'LC11FBF')
    ]
    )

# A secondary data structure includes billing information. It is a dictionary
# that maps company names to a list of registered license plates.

# DO NOT MODIFY CONSTANTS
COMPANY_REGISTRATIONS_SAMPLE = {
    'Shire Tobacco Inc.': ['LR10GHT', 'LA63EWH'],
    'Rohan Equestrian Equipments': [],
    'Moria Construction Hardware': ['LC11FBF', 'LS66XKE', 'LR10ZPP', 'LJ65OSN']
    }


def register_car(registration, company, plate):
    '''
    Registers a new car.

    NOTE: this function should not modify the registration dictionary that is
    given, instead it should create a new dictionary.
    NOTE: this function should not introduce duplicates in the registration
    system. Specifically, if a car is already registered with the given
    company it should return an identical registration information. If the car
    is registered with a different company it should remove the first
    registration.
    NOTE: if the company is not listed in the dictionary, it should not
    introduce it. Instead it should just return an identical registration.

    E.g., register_car({'Stark Industries': ['IRNMN']}, 'Stark Industries',
                       'JARVIS')
    is {'Stark Industries': ['IRNMN', 'JARVIS']}
    E.g., register_car({'Stark Industries': ['IRNMN']}, 'Wayne Enterprises',
                       'IMBTMN')
    is {'Stark Industries': ['IRNMN']}

    @param registration preexisting registration information
    @param company the company to register the car for
    @param plate the license plate of the car to register
    @return a new registration information dictionary with added registration
    '''
    raise NotImplementedError


def occupancy(parking_data, time=None):
    '''
    Computes the occupancy of the parking at a given time. If no time is
    provided, check the current occupancy.

    E.g.,
    data = ([(datetime.datetime(2017, 12, 12,  7, 13, 44, 0), 'LR10GHT')], [])
    occupancy(data, time=datetime.datetime(2017, 12, 12,  7, 13, 45, 0))
    is ['LR10GHT']
    E.g.,
    data = ([(datetime.datetime(2017, 12, 12,  7, 13, 44, 0), 'LR10GHT')], [])
    occupancy(data, time=datetime.datetime(2017, 12, 12,  7, 13, 43, 0))
    is []

    @param parking_data a tuple of list of timestamped arrival and departure
    information including license plate. See sample above.
    @param time the time (as a datetime.datetime object) at which to check for
    occupancy. If no time is provided, use now.
    @return the list of cars present in the parking at the given time.
    '''
    raise NotImplementedError


def company_bill(parking_data, company_registration, company, t_start, t_end):
    '''
    Computes the total, cumulated time in seconds, ignoring milliseconds, that
    cars registred with a given company stayed in the parking during the
    interval between t_start and t_end.

    E.g.,
    parking_data = (
        [(datetime.datetime(2017, 12, 12,  7, 13, 44, 0), 'LR10GHT')],
        [(datetime.datetime(2017, 12, 12,  7, 13, 45, 0), 'LR10GHT')]
    )
    company_registration = {'Shire Tobacco Inc.': ['LR10GHT']}
    company_bill(parking_data, company_registration,
                 'Shire Tobacco Inc.', …, …)
    is 1

    @param parking_data see sample above
    @param company_registration see sample above
    @param company the name of the company to compute billing for
    @param t_start the start of the billing interval
    @param t_end the end of the billing interval
    @return the cumulated number of seconds of car park occupancy
    '''
    raise NotImplementedError
