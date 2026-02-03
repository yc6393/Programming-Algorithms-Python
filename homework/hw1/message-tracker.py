"""
INPUTS:
    client names (at least 5)
    message counts for each client for 7 days (sunday - saturday)

OUTPUTS:
    histogram 1: total messages by client
    histogram 2: total messages by day of week

CONSTRAINTS:
    3 unit tests per function (common, edge, special cases)
"""


t_data = {
    'Apple': [1, 2, 3, 4, 5, 6, 7],
    'Banana': [2, 2, 2, 2, 2, 2, 2],
    'Carrot': [3, 4, 5, 6, 7, 8, 9]
}


def aggregate_by_client(data):
    """Calculate total messages sent to each client

    Args:
        data (dictionary): client_names as keys, lists of daily message counts as values

    Returns:
        dictionary: client name as key, total message count as value
    """
    totals = {}
    for client_name, message_counts in data.items():
        total = sum(message_counts)
        totals[client_name] = total
    return totals
#
# UNIT TESTS aggregate_by_client
#
def test_aggregate_by_client_common():
    data = {
        'A': [1,2,3,4,5,6,7],
        'B': [2,2,2,2,2,2,2]
    }
    result = aggregate_by_client(data)
    expected = {'A': 28, 'B': 14}
    assert result == expected, f"Expected {expected}, got {result}"
    print("test_aggregate_by_client_common PASSED")

def test_aggregate_by_client_edge():
    data = {
        'A': [1,1,1,1,1,1,1],
    }
    result = aggregate_by_client(data)
    expected = {'A': 7}
    assert result == expected, f"Expected {expected}, got {result}"
    print ("test_aggregate_by_client_edge PASSED")
    
def test_aggregate_by_client_special():
    data = {}
    result = aggregate_by_client(data)
    expected = {}
    assert result == expected, f"Expected {expected}, got {result}"
    print ("test_aggregate_by_client_special PASSED")
    
   



#===============================================================================

# input as dict, list
# returns dict, keys are day names, values are total messages for that day
def aggregate_by_day(data, days):
    # initialize dict with all days set to 0
    day_totals = {day: 0 for day in days}
    
    # loop through each clients message count
    for message_count in data.values():
        # loop through each days count with index
        for i, count in enumerate(message_count):
            # add count to appropriate day
            day_totals[days[i]] += count
    return day_totals
    
def test_aggregate_by_day_common():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    data = {
        'A': [1, 2, 3, 4, 5, 6, 7],
        'B': [1, 1, 1, 1, 1, 1, 1]
    }
    result = aggregate_by_day(data,days)
    expected = {
        'Sunday': 2, 'Monday': 3, 'Tuesday': 4, 'Wednesday': 5,
        'Thursday': 6, 'Friday': 7, 'Saturday': 8
    }
    assert result == expected, f"Expected {expected}, got {result}"
    print("test_aggregate_by_day_common PASSED")

def test_aggregate_by_day_edge():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    data = {
        'A': [0, 2, 3, 4, 5, 6, 7],
        'B': [0, 1, 1, 1, 1, 1, 1]
    }
    result = aggregate_by_day(data, days)
    expected = {
        'Sunday': 0, 'Monday': 3, 'Tuesday': 4, 'Wednesday': 5,
        'Thursday': 6, 'Friday': 7, 'Saturday': 8
    }
    assert result == expected, f"Expected {expected}, got {result}"
    print("test_aggregate_by_day_edge PASSED")


def test_aggregate_by_day_special():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    data = {}
    result = aggregate_by_day(data, days)
    expected = {
        'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0,
        'Thursday': 0, 'Friday': 0, 'Saturday': 0
    }
    assert result == expected, f"Expected {expected}, got {result}"
    print("test_aggregate_by_day_special PASSED")

    
    
    
if __name__ == "__main__":
    test_aggregate_by_client_common()
    test_aggregate_by_client_edge()
    test_aggregate_by_client_special()
    
    test_aggregate_by_day_common()
    test_aggregate_by_day_edge()
    test_aggregate_by_day_special()
