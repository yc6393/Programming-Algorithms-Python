"""
LLM Usage:
I used Claude to help plan out the steps for my code, which is why the order of functions is not "chronological", I worked on user input last,
making sure everything would work before that.


INPUTS:
    client names (at least 5)
    message counts for each client for 7 days (sunday - saturday)

OUTPUTS:
    histogram 1: total messages by client
    histogram 2: total messages by day of week

TESTS:
    3 unit tests per function (common, edge, special cases)
"""


def sum_by_client(data):
    """calculates total messages sent to each client"""
    # create empty totals dict
    totals = {}
    
    # loop through client and message_counts in data dict, sum message count and assign total and client to totals dict
    for client_name, message_counts in data.items():
        total = sum(message_counts)
        totals[client_name] = total
    return totals

# UNIT TESTS sum_by_client
def test_sum_by_client_common():
    # typical case with multiple clients
    data = {
        'A': [1,2,3,4,5,6,7],
        'B': [2,2,2,2,2,2,2]
    }
    result = sum_by_client(data)
    expected = {'A': 28, 'B': 14}
    assert result == expected, f"Expected {expected}, got {result}"
    print("test_sum_by_client_common PASSED")

def test_sum_by_client_edge():
    # edge case: only one client
    data = {
        'A': [1,1,1,1,1,1,1],
    }
    result = sum_by_client(data)
    expected = {'A': 7}
    assert result == expected, f"Expected {expected}, got {result}"
    print ("test_sum_by_client_edge PASSED")
    
def test_sum_by_client_special():
    # special case - empty data
    data = {}
    result = sum_by_client(data)
    expected = {}
    assert result == expected, f"Expected {expected}, got {result}"
    print ("test_sum_by_client_special PASSED")
    

# -----------------------------------------------------------------------

def sum_by_day(data, days):
    """calculate total messages per day across all clients"""
    
    # initialize dict with all days set to 0
    day_totals = {day: 0 for day in days}

    # loop through each clients message count
    for message_count in data.values():
        for i, count in enumerate(message_count):
            day_totals[days[i]] += count  # add count to appropriate day
            
    return day_totals


# UNIT TESTS sum_by_day    
def test_sum_by_day_common():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    data = {
        'A': [1, 2, 3, 4, 5, 6, 7],
        'B': [1, 1, 1, 1, 1, 1, 1]
    }
    result = sum_by_day(data,days)
    expected = {
        'Sunday': 2, 'Monday': 3, 'Tuesday': 4, 'Wednesday': 5,
        'Thursday': 6, 'Friday': 7, 'Saturday': 8
    }
    assert result == expected, f"Expected {expected}, got {result}"
    print("test_sum_by_day_common PASSED")

def test_sum_by_day_edge():
    # edge: some days have zero messages
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    data = {
        'A': [0, 2, 3, 4, 5, 6, 7],
        'B': [0, 1, 1, 1, 1, 1, 1]
    }
    result = sum_by_day(data, days)
    expected = {
        'Sunday': 0, 'Monday': 3, 'Tuesday': 4, 'Wednesday': 5,
        'Thursday': 6, 'Friday': 7, 'Saturday': 8
    }
    assert result == expected, f"Expected {expected}, got {result}"
    print("test_sum_by_day_edge PASSED")


def test_sum_by_day_special():
    # special: no clients
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    data = {}
    result = sum_by_day(data, days)
    expected = {
        'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0,
        'Thursday': 0, 'Friday': 0, 'Saturday': 0
    }
    assert result == expected, f"Expected {expected}, got {result}"
    print("test_sum_by_day_special PASSED")


# -----------------------------------------------------------------------

def create_histogram(label_data_dict, label_prefix=""):
    
    # handle empty input dict
    if not label_data_dict:
        return ""
    
    # build histogram lines
    histogram_lines = []
    for label, count in label_data_dict.items():
        full_label = label_prefix + label
        bar = "*" * count
        histogram_lines.append(f"{full_label}:{bar}")

    return '\n'.join(histogram_lines)


# UNIT TESTS create_histogram
def test_create_histogram_common():
    """test with multiple entries"""
    data = {'A': 10, 'B': 5}
    result = create_histogram(data, "client ")
    expected_lines = result.split('\n')

    assert len(expected_lines) == 2, f"Expected 2 lines, got {len(expected_lines)}"
    assert expected_lines[0].count('*') == 10, "A should have length 10"
    assert expected_lines[1].count('*') == 5, "B should have length 5"
    assert 'client' in result, "Should contain 'client' prefix"

    print("test_create_histogram_common PASSED")


def test_create_histogram_edge():
    """test with zero values"""
    data = {'A': 0}
    result = create_histogram(data)

    assert '*' not in result, "Should have no length for zero count"
    assert 'A' in result, "Should contain the label"
    assert ':' in result, "Should still have colon"

    print("test_create_histogram_edge PASSED")


def test_create_histogram_special():
    """test with empty dictionary"""
    data = {}
    result = create_histogram(data)
    expected = ""

    assert result == expected, f"Expected empty string, got '{result}'"
    print("test_create_histogram_special PASSED")


# -----------------------------------------------------------------------

def get_client_data():
    # ask user for client name, ensuring non-empty
    while True:
        client_name = input("Enter client name: ").strip()
        if client_name:
            break
        print("Name cannot be empty. Please enter a valid name.")

    # initialize days list, and message count list
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    message_counts = []

    # loop through each day, asking user for input for messages on that day
    for day in days:
        while True:
            try:
                count = int(input(f"  Messages on {day}: "))
                if count < 0: # ensure positive int
                    print("    Error: Please enter a non-negative number.")
                    continue
                message_counts.append(count)
                break
            except ValueError:
                print("    Error: Please enter a valid integer.")
    
    #return a tuple, (client name, list of message counts)
    return (client_name, message_counts)


# tests for get_client_data is harder, would have to run manually as such:
#
# - common: enter any client name with valid counts
# - edge: enter empty name or name with spaces
# - special: enter negative values for counts


# -----------------------------------------------------------------------

def main():
    """main function, put everything together"""

    print("Enter data for at least 5 clients.\n")

    # initialize empty dictionary
    data = {}
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # collect data for at least 5 clients
    num_clients = 0
    while num_clients < 5: # keeps running while < 5 clients entered
        print(f"\nClient #{num_clients + 1}:")
        client_name, message_counts = get_client_data()
        data[client_name] = message_counts
        num_clients += 1

    # ask if user wants to add more clients
    while True:
        add_more = input("\nAdd another client? (yes/no): ").strip().lower()
        if add_more in ['yes', 'y']:
            print(f"\nClient #{num_clients + 1}:")
            client_name, message_counts = get_client_data()
            data[client_name] = message_counts
            num_clients += 1
        elif add_more in ['no', 'n']:
            break
        else:
            print("Please enter 'yes' or 'no'.")

    # generate histograms
    client_totals = sum_by_client(data)
    day_totals = sum_by_day(data, days)

    histogram1 = create_histogram(client_totals, "client ")
    histogram2 = create_histogram(day_totals)

    # display results
    print("Total Messages by Client")
    print("=" * 50)
    print(histogram1)

    print("\n" + "=" * 50)
    print("Total Messages by Day")
    print("=" * 50)
    print(histogram2)
    print()


# ========================================================================
# PROGRAM ENTRY POINT
# ========================================================================

if __name__ == "__main__":
    import sys

    # run tests if --test flag is provided
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("\n=== Running Unit Tests ===\n")

        print("Testing sum_by_client:")
        test_sum_by_client_common()
        test_sum_by_client_edge()
        test_sum_by_client_special()

        print("\nTesting sum_by_day:")
        test_sum_by_day_common()
        test_sum_by_day_edge()
        test_sum_by_day_special()

        print("\nTesting create_histogram:")
        test_create_histogram_common()
        test_create_histogram_edge()
        test_create_histogram_special()

        print("\n=== All tests passed! ===\n")
    else:
        main()