"""
Usage of LLMs (ChatGPT, Claude):
    - Help with finalized formatting and structure
    - To build checks for read_input using builtins
    - To create README.md
"""


import builtins

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

# TEST_DATA = {
#     'Apple': [1, 2, 3, 4, 5, 6, 7],
#     'Banana': [2, 2, 2, 2, 2, 2, 2],
#     'Carrot': [3, 4, 5, 6, 7, 8, 9]
# }

SEPARATOR = '-' * 25


#------------------------------------------------------------------------------------------------------------
# Function: read_input
# Task: Read and organize user input for client messaging data
# Solution: Read input with basic sanity checks (minimum 5 clients, exactly 7 non-negative integers),
#           organize it in a form of a dict with client names as keys and lists of daily counts as values.
#------------------------------------------------------------------------------------------------------------
def read_input():
    input_data = {}

    while True:
        try:
            total_clients = int(input('Enter the total number of clients: '))
            if total_clients < 5:
                print("Error: Must enter at least 5 clients")
                continue
            break
        except ValueError:
            print("Error: Please enter an integer")

    for i in range(total_clients):
        client = input(f'Enter the name for client {i+1}: ')

        while True:
            raw = input(
                'Enter message counts for Sunday through Saturday (7 integers, space-separated): '
            ).split()
            # check count
            if len(raw) != 7:
                print("Error: Please enter exactly 7 numbers.")
                continue
            try:
                messages = list(map(int, raw))
            # check if int
            except ValueError:
                print("Error: All values must be integers.")
                continue

            # check for negative values
            if any(msg < 0 for msg in messages):
                print("Error: Message counts cannot be negative.")
                continue
            
            # passed all checks
            break

        input_data[client] = messages

    return input_data


#------------------------------------------------------------------------------------------------------------
# Function: aggregate_by_client
# Task: Aggregate the total number of messages by client
# Solution: Create a dict with keys = client names and values = sum of daily message counts
#------------------------------------------------------------------------------------------------------------
def aggregate_by_client(data):
    # create empty dict
    totals = {}
    # loop through clients and message counts
    # sum message counts per client
    # add client as key, summed count as value to dict
    for client_name, message_counts in data.items():
        total = sum(message_counts)
        totals[client_name] = total
    return totals


#------------------------------------------------------------------------------------------------------------
# Function: aggregate_by_day
# Task: Aggregate the total number of messages by day of week
# Solution: Create a dict with keys = day of week, loop through all clients to calculate sum for each day
#------------------------------------------------------------------------------------------------------------
def aggregate_by_day(data):
    # initialize dict with all days set to 0
    day_totals = {day: 0 for day in DAYS}   
    # loop through each clients message count
    for message_counts in data.values():
        # loop through each days count with index
        for i, count in enumerate(message_counts):
            # add count to appropriate day
            day_totals[DAYS[i]] += count
    return day_totals
    

#------------------------------------------------------------------------------------------------------------
# Function: draw_histogram
# Task: Visualize data as a horizontal histogram
# Solution: Build a string with padded labels (so columns align) followed by asterisks representing counts.
#           Works for both client and day-of-week data since labels are variable length.
#------------------------------------------------------------------------------------------------------------
def draw_histogram(data):
    # for empty input data
    if not data:
        return ''
    
    labels = data.keys()
    # find max label length for padding
    max_len = max(len(label) for label in labels)
    hist_string = ''
    # label, then padding based on max label length, then histogram
    for label in labels:
        hist_string += label + ' '*(max_len-len(label)+1) + ':' + '*'*data[label] + '\n'
    return hist_string


#============================================================================================================
# UNIT TESTS 
#============================================================================================================

#------------------------------------------------------------------------------------------------------------
# read_input() tests
#------------------------------------------------------------------------------------------------------------

# Test: Common case - typical valid input of 5 clients with normal message counts
def test_read_input_common():
    inputs = iter([
        "5",                    # total_clients
        "Alice",                # client 1 name
        "1 2 3 4 5 6 7",        # Alice messages
        "Bob",                  # client 2 name
        "0 0 1 1 2 2 3",        # Bob messages
        "Charlie",              # client 3 name
        "1 1 1 1 1 1 1",        # Charlie messages
        "Dave",                 # client 4 name
        "2 2 2 2 2 2 2",        # Dave messages
        "Eve",                  # client 5 name
        "3 3 3 3 3 3 3"         # Eve messages
    ])
    
    real_input = builtins.input
    try:
        builtins.input = lambda _: next(inputs)
        result = read_input()
        expected = {
            "Alice": [1, 2, 3, 4, 5, 6, 7],
            "Bob": [0, 0, 1, 1, 2, 2, 3],
            "Charlie": [1, 1, 1, 1, 1, 1, 1],
            "Dave": [2, 2, 2, 2, 2, 2, 2],
            "Eve": [3, 3, 3, 3, 3, 3, 3]
        }
        assert result == expected, f"Expected {expected}, got {result}"
    finally:
        builtins.input = real_input


# Test: Edge case - exactly 5 clients with all zero values for first client
def test_read_input_edge():
    inputs = iter([
        "5",
        "A", "0 0 0 0 0 0 0",
        "B", "1 1 1 1 1 1 1",
        "C", "2 2 2 2 2 2 2",
        "D", "3 3 3 3 3 3 3",
        "E", "4 4 4 4 4 4 4"
    ])
    
    real_input = builtins.input
    try:
        builtins.input = lambda _: next(inputs)
        result = read_input()
        assert len(result) == 5, f"Expected 5 clients, got {len(result)}"
        assert result["A"] == [0, 0, 0, 0, 0, 0, 0]
    finally:
        builtins.input = real_input


# Test: Special case - large message count values
def test_read_input_special():
    inputs = iter([
        "5",
        "A", "100 200 300 400 500 600 700",
        "B", "1000 1000 1000 1000 1000 1000 1000",
        "C", "1 2 3 4 5 6 7",
        "D", "10 20 30 40 50 60 70",
        "E", "5 5 5 5 5 5 5"
    ])
    
    real_input = builtins.input
    try:
        builtins.input = lambda _: next(inputs)
        result = read_input()
        assert result["A"] == [100, 200, 300, 400, 500, 600, 700]
        assert result["B"] == [1000, 1000, 1000, 1000, 1000, 1000, 1000]
    finally:
        builtins.input = real_input  
  

#------------------------------------------------------------------------------------------------------------
# aggregate_by_client() tests
#------------------------------------------------------------------------------------------------------------

# Test: Common case - typical multi-client data
def test_aggregate_by_client_common():
    data = {
        'A': [1, 2, 3, 4, 5, 6, 7],
        'B': [2, 2, 2, 2, 2, 2, 2]
    }
    result = aggregate_by_client(data)
    expected = {'A': 28, 'B': 14}
    assert result == expected, f"Expected {expected}, got {result}"

    
# Test: Edge case - single client only
def test_aggregate_by_client_edge():
    data = {
        'A': [1, 1, 1, 1, 1, 1, 1],
    }
    result = aggregate_by_client(data)
    expected = {'A': 7}
    assert result == expected, f"Expected {expected}, got {result}"

    
# Test: Special case - empty input dictionary
def test_aggregate_by_client_special():
    data = {}
    result = aggregate_by_client(data)
    expected = {}
    assert result == expected, f"Expected {expected}, got {result}"
    

#------------------------------------------------------------------------------------------------------------
# aggregate_by_day() tests
#------------------------------------------------------------------------------------------------------------

# Test: Common case - typical multi-client data
def test_aggregate_by_day_common():
    data = {
        'A': [1, 2, 3, 4, 5, 6, 7],
        'B': [1, 1, 1, 1, 1, 1, 1]
    }
    result = aggregate_by_day(data)
    expected = {
        'Sunday': 2, 'Monday': 3, 'Tuesday': 4, 'Wednesday': 5,
        'Thursday': 6, 'Friday': 7, 'Saturday': 8
    }
    assert result == expected, f"Expected {expected}, got {result}"


# Test: Edge case - some days have zero messages
def test_aggregate_by_day_edge():
    data = {'A': [0, 2, 3, 4, 5, 6, 7]}
    result = aggregate_by_day(data)
    expected = {
        'Sunday': 0, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4,
        'Thursday': 5, 'Friday': 6, 'Saturday': 7
    }
    assert result == expected, f"Expected {expected}, got {result}"


# Test: Special case - no clients (empty dictionary)
def test_aggregate_by_day_special():
    data = {}
    result = aggregate_by_day(data)
    expected = {
        'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0,
        'Thursday': 0, 'Friday': 0, 'Saturday': 0
    }
    assert result == expected, f"Expected {expected}, got {result}"


#------------------------------------------------------------------------------------------------------------
# draw_histogram() tests
#------------------------------------------------------------------------------------------------------------

# Test: Common case - typical multi-item data
def test_draw_histogram_common():
    data = {'Apple': 5, 'Banana': 3}
    result = draw_histogram(data)
    # check it has the right labels
    assert 'Apple' in result
    assert 'Banana' in result
    # check total asterisks
    assert result.count('*') == 8  # 5 + 3


# Test: Edge case - zero value produces no asterisks
def test_draw_histogram_edge():
    data = {'Apple': 0}
    result = draw_histogram(data)
    assert 'Apple' in result
    assert '*' not in result  # no asterisks for zero


# Test: Special case - empty dictionary returns empty string
def test_draw_histogram_special():
    data = {}
    result = draw_histogram(data)
    assert result == ''  # should return empty string


#------------------------------------------------------------------------------------------------------------
# Unit test consolidator
#------------------------------------------------------------------------------------------------------------
def test_all():
    tests = [
        test_read_input_common,
        test_read_input_edge,
        test_read_input_special,
        test_aggregate_by_client_common,
        test_aggregate_by_client_edge,
        test_aggregate_by_client_special,
        test_aggregate_by_day_common,
        test_aggregate_by_day_edge,
        test_aggregate_by_day_special,
        test_draw_histogram_common,
        test_draw_histogram_edge,
        test_draw_histogram_special,
    ]
    for test in tests:
        test()
    print(f'OK: Total {len(tests)} tests passed')


#============================================================================================================
# MAIN PROGRAM
#============================================================================================================

    
if __name__ == "__main__":

    if input("Enter 't' if you want to run the tests: ") == 't':
        test_all()
    
    else:
        input_data = read_input()
        data_by_client = aggregate_by_client(input_data)
        data_by_day = aggregate_by_day(input_data)

        print('\n' + SEPARATOR + '\n' + 'Number of Messages per Client\n' + SEPARATOR) 
        print(draw_histogram(data_by_client))
               
        print('\n' + SEPARATOR + '\n' + 'Number of Messages per Day\n' + SEPARATOR) 
        print(draw_histogram(data_by_day))