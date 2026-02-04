"""
HW1


Usage of LLMs (ChatGPT):

- Help with input sanity checks in read_input()


"""

import builtins

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

TEST_DATA = {
    'Apple': [1, 2, 3, 4, 5, 6, 7],
    'Banana': [2, 2, 2, 2, 2, 2, 2],
    'Carrot': [3, 4, 5, 6, 7, 8, 9]
}

SEPARATOR = '-' * 25

# Task: Read and organize user input
# Solution: Read input with basic sanity checks, organize it in a form of a dict with client names as keys.  
def read_input():
    input_data = {}

    while True:
        try:
            total_clients = int(input('Enter the total number of clients: '))
        except ValueError:
            print("Effor: Please enter an integer")
        break

    for i in range(total_clients):
        client = input('Enter the client name: ')

        while True:
            raw = input(
                'Enter the number of messages for each day of the week (7 integers, space-separated): '
            ).split()
            # check count
            if len(raw) != 7:
                print("Error: Please enter exactly 7 numbers.")
                continue
            try:
                messages = list(map(int, raw))
            except ValueError:
                print("Error: All values must be integers.")
                continue
            # passed all checks
            break

        input_data[client] = messages

    return input_data


# Task: Aggregate the number of calls by client
# Solution: Create a dict with keys = client names and values = sum of values of input dict
def aggregate_by_client(data):
    totals = {}
    for client_name, message_counts in data.items():
        total = sum(message_counts)
        totals[client_name] = total
    return totals


# Task: Aggregate the number of calls by day of week
# Solution: Create a dict with keys = day of week, loop through clients to calc sum for each day
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
    

# Task: Visualise calls as a horizontal hystogram
# Solution: Both the client and the day of week visualization could be done in the same function.
#           Need to make sure the labels are padded, so their length is the same.
def draw_histogram(data):
    labels = data.keys()
    max_len = max(len(label) for label in labels)
    hist_string = ''
    for label in labels:
        hist_string += label + ' '*(max_len-len(label)+1) +':' + '*'*data[label] + '\n'
    return hist_string



#============================================================================================================
# UNIT TESTS 
#============================================================================================================

#------------------------------------------------------------------------------------------------------------
# read_input()
#------------------------------------------------------------------------------------------------------------


def test_read_input_common():
    # 1. Prepare fake inputs (exact order matters!)
    inputs = iter([
        "2",                    # total_clients
        "Alice",                # client 1 name
        "1 2 3 4 5 6 7",        # Alice messages
        "Bob",                  # client 2 name
        "0 0 1 1 2 2 3"         # Bob messages
    ])

    # 2. Save the real input function
    real_input = builtins.input

    try:
        # 3. Replace input() with our fake one
        builtins.input = lambda _: next(inputs)

        # 4. Call the function
        result = read_input()

        # 5. Assert expected output
        expected = {
            "Alice": [1, 2, 3, 4, 5, 6, 7],
            "Bob": [0, 0, 1, 1, 2, 2, 3]
        }

        assert result == expected, f"Expected {expected}, got {result}"

        print("✅ Test passed!")

    finally:
        # 6. Restore the real input()
        builtins.input = real_input


#------------------------------------------------------------------------------------------------------------
# aggregate_by_client()
#------------------------------------------------------------------------------------------------------------

def test_aggregate_by_client_common():
    data = {
        'A': [1,2,3,4,5,6,7],
        'B': [2,2,2,2,2,2,2]
    }
    result = aggregate_by_client(data)
    expected = {'A': 28, 'B': 14}
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test passed!")
    
def test_aggregate_by_client_edge():
    data = {
        'A': [1,1,1,1,1,1,1],
    }
    result = aggregate_by_client(data)
    expected = {'A': 7}
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test passed!")
    
def test_aggregate_by_client_special():
    data = {}
    result = aggregate_by_client(data)
    expected = {}
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test passed!")
    

#------------------------------------------------------------------------------------------------------------
# aggregate_by_day()
#------------------------------------------------------------------------------------------------------------

def test_aggregate_by_day_common():
    print("✅ Test passed!")

def test_aggregate_by_day_edge():
    print("✅ Test passed!")

def test_aggregate_by_day_special():    
    print("✅ Test passed!")    


#------------------------------------------------------------------------------------------------------------
# draw_histogram()
#------------------------------------------------------------------------------------------------------------

def test_draw_histogram_common():
    return

def test_draw_histogram_edge():
    return

def test_draw_histogram_special():    
    return    


#------------------------------------------------------------------------------------------------------------
# Unit test consolidator()
#------------------------------------------------------------------------------------------------------------

def test_all():
    tests = [
        test_read_input_common,
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


    
if __name__ == "__main__":

    if input("Enter 't' if you want to run the tests: ") == 't':
        test_all()
    
    else:
        input_data = read_input()
        data_by_client = aggregate_by_client(input_data)
        data_by_day = aggregate_by_day(input_data)

        print('\n' + SEPARATOR + '\n' + 'Number of Messages per Client\n' + SEPARATOR) 
        print(draw_histogram(aggregate_by_client(input_data)))
               
        print('\n' + SEPARATOR + '\n' + 'Number of Messages per Day\n' + SEPARATOR) 
        print(draw_histogram(aggregate_by_day(input_data)))
        

    