calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    tuple_ = len(string), string.upper(), string.lower()
    return tuple_

def is_contains(string, list_to_search):
    count_calls()
    list_to_search_1 = []
    for i in list_to_search:
        list_to_search_1.append(i.lower())
    if string.lower() in list_to_search_1:
        return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)