from datetime import datetime
FIXED_CALL_COST = 0.36
COST_PER_MINUTE = 0.09

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
        'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
        'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
        'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
        'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
        'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
        'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
        'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
        'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
        'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
        'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564627800, 'start': 1564626000}
]


def classify_by_phone_number(records):
    """
    Computes and organizes the telephone costs.
    :param records: dictionary array
    Dictionary array with every call
    """
    billing = {}

    # If this is the first call with the source, just put the cost there
    # If not, just add both costs
    for call in records:
        if (call['source'] in billing.keys()):
            billing[call['source']] = round(compute_cost(call) +
                                            billing[call['source']], 2)
        else:
            billing[call['source']] = round(compute_cost(call), 2)

    # Sorting the billing by its cost
    order_billing = sorted(billing.items(), key=lambda x: x[1], reverse=True)

    # Formating the output
    final_billing = []
    for bill in order_billing:
        final_billing.append({'source': bill[0], 'total': bill[1]})

    return final_billing


def compute_cost(call):
    """
    Computes call costs.
    :param call: dictionary
    Dictionary call with source, destination, end, start
    """

    # Pick the datetime for the start and end for this call
    start = datetime.fromtimestamp(call['start'])
    end = datetime.fromtimestamp(call['end'])

    # Making two UNIX timestamps to help calculate the seconds
    unix_day_6h = unix_constant(call['start'], 6)
    unix_day_22h = unix_constant(call['start'], 22)

    if (start.hour >= 6 and start.hour < 22):  # Daytime call
        if (end.hour >= 22):  # Stops billing at 22h
            billed_minutes = (unix_day_22h - call['start']) // 60
        else:  # Calculates exact value
            billed_minutes = (call['end'] - call['start']) // 60
    else:  # Nighttime call
        if (end.hour >= 6 and start.hour < 22):  # Starts billing after 6
            billed_minutes = (call['final'] - unix_day_6h) // 60
        else:  # Does not needs to bill
            billed_minutes = 0

    return FIXED_CALL_COST + (COST_PER_MINUTE * billed_minutes)


def unix_constant(day, hour):
    """
    Make a UNIX timestamp.
    :param day: UNIX timestamp
    :param hour: int
    """
    return datetime(
        datetime.fromtimestamp(day).year, datetime.fromtimestamp(day).month,
        datetime.fromtimestamp(day).day, hour)


if __name__ == "__main__":
    classify_by_phone_number(records)
