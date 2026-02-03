"""
Message Tracker Program
Purpose: Help Jane visualize client message data through horizontal histograms
Author: Yuri
Date: 2026-02-02

INPUTS:
    client names (at least 5)
    message counts for each client for 7 days (sunday - saturday)

OUTPUTS:
    histogram 1: total messages by client
    histogram 2: total messages by day of week

CONSTRAINTS:
    3 unit tests per function (common, edge, special cases)
"""


def aggregate_by_client(data):
    """
    Purpose: Calculate total messages sent to each client
    Parameters: data (dict) - dictionary with client names as keys and
                lists of daily message counts as values
    Returns: dict - dictionary with client names as keys and total
             message counts as values
    Author: Yuri
    Date: 2026-02-02
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

def aggregate_by_day(data, days):
    """
    Purpose: Calculate total messages per day across all clients
    Parameters: data (dict) - dictionary with client names as keys and
                lists of daily message counts as values
                days (list) - list of day names in order
    Returns: dict - dictionary with day names as keys and total
             message counts as values
    Author: Yuri
    Date: 2026-02-02
    """
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


#===============================================================================

def create_histogram(label_data_dict, label_prefix=""):
    """
    Purpose: Generate formatted horizontal histogram string
    Parameters: label_data_dict (dict) - dictionary with labels as keys and
                counts as values
                label_prefix (str) - optional prefix for labels (e.g., "client ")
    Returns: str - formatted histogram with asterisks representing counts
    Author: Yuri
    Date: 2026-02-02
    """
    # Handle empty dictionary
    if not label_data_dict:
        return ""

    # Find the longest label for alignment
    max_label_length = max(len(label_prefix + label) for label in label_data_dict.keys())

    # Create histogram lines
    histogram_lines = []
    for label, count in label_data_dict.items():
        full_label = label_prefix + label
        # Pad label to align colons
        padded_label = full_label.ljust(max_label_length)
        # Create asterisk bar
        bar = '*' * count
        histogram_lines.append(f"{padded_label} :{bar}")

    return '\n'.join(histogram_lines)

#
# UNIT TESTS create_histogram
#
def test_create_histogram_common():
    """Test create_histogram with common case: multiple entries"""
    data = {'Apple': 10, 'Banana': 5}
    result = create_histogram(data, "client ")
    expected_lines = result.split('\n')

    # Check that we have 2 lines
    assert len(expected_lines) == 2, f"Expected 2 lines, got {len(expected_lines)}"

    # Check that asterisks match counts
    assert expected_lines[0].count('*') == 10, "Apple should have 10 asterisks"
    assert expected_lines[1].count('*') == 5, "Banana should have 5 asterisks"

    # Check that 'client' prefix appears
    assert 'client' in result, "Should contain 'client' prefix"

    print("test_create_histogram_common PASSED")


def test_create_histogram_edge():
    """Test create_histogram with edge case: zero values"""
    data = {'Apple': 0}
    result = create_histogram(data)

    assert '*' not in result, "Should have no asterisks for zero count"
    assert 'Apple' in result, "Should contain the label"
    assert ':' in result, "Should still have colon"

    print("test_create_histogram_edge PASSED")


def test_create_histogram_special():
    """Test create_histogram with special case: empty dictionary"""
    data = {}
    result = create_histogram(data)
    expected = ""

    assert result == expected, f"Expected empty string, got '{result}'"

    print("test_create_histogram_special PASSED")


#===============================================================================

def get_client_data():
    """
    Purpose: Input and validate data for one client
    Parameters: None (gets input from user via terminal)
    Returns: tuple - (client_name (str), message_counts (list of 7 ints))
    Author: Yuri
    Date: 2026-02-02
    """
    client_name = input("Enter client name: ").strip()

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    message_counts = []

    for day in days:
        while True:
            try:
                count = int(input(f"  Messages on {day}: "))
                if count < 0:
                    print("    Error: Please enter a non-negative number.")
                    continue
                message_counts.append(count)
                break
            except ValueError:
                print("    Error: Please enter a valid integer.")

    return (client_name, message_counts)


#===============================================================================

def main():
    """
    Purpose: Main program orchestration - collect data and display histograms
    Parameters: None
    Returns: None
    Author: Yuri
    Date: 2026-02-02
    """
    print("=== Message Tracker ===")
    print("Enter data for at least 5 clients.\n")

    data = {}
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # Collect data for at least 5 clients
    num_clients = 0
    while num_clients < 5:
        print(f"\nClient #{num_clients + 1}:")
        client_name, message_counts = get_client_data()
        data[client_name] = message_counts
        num_clients += 1

    # Ask if user wants to add more clients
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

    # Generate and display histograms
    client_totals = aggregate_by_client(data)
    day_totals = aggregate_by_day(data, days)

    histogram1 = create_histogram(client_totals, "client ")
    histogram2 = create_histogram(day_totals)

    # Display histograms
    print("\n" + "=" * 50)
    print("Total Messages by Client")
    print("=" * 50)
    print(histogram1)

    print("\n" + "=" * 50)
    print("Total Messages by Day")
    print("=" * 50)
    print(histogram2)
    print()


#===============================================================================
# PROGRAM ENTRY POINT
#===============================================================================

if __name__ == "__main__":
    import sys

    # Run tests if --test flag is provided
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("\n=== Running Unit Tests ===\n")

        print("Testing aggregate_by_client:")
        test_aggregate_by_client_common()
        test_aggregate_by_client_edge()
        test_aggregate_by_client_special()

        print("\nTesting aggregate_by_day:")
        test_aggregate_by_day_common()
        test_aggregate_by_day_edge()
        test_aggregate_by_day_special()

        print("\nTesting create_histogram:")
        test_create_histogram_common()
        test_create_histogram_edge()
        test_create_histogram_special()

        print("\n=== All tests passed! ===\n")
    else:
        main()
