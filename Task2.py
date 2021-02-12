"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def longestCall(records):
    telephone_dict = {}

    for i in range(len(records)):
        #check outgoing number
        if records[i][0] not in telephone_dict:
            telephone_dict.update(
                {records[i][0]: int(records[i][3])}
                )
        else:
            #Add the call duration to the total for that number if it already exists
            telephone_dict[records[i][0]] += int(records[i][3])

        #checkout receiving number
        if records[i][1] not in telephone_dict:
            telephone_dict.update(
                {records[i][1]: int(records[i][3])}
                )
        else:
            #Add the call duration to the total for that number if it already exists
            telephone_dict[records[i][1]] += int(records[i][3])
    
    #Find the longest duration from the dictionary of numbers
    all_values = telephone_dict.values()
    max_value = max(all_values)
    max_key = max(telephone_dict, key=telephone_dict.get)

    return {
        'telephone_number': max_key,
        'total_time': max_value
    }

# print(longestCall(calls)['total_time'])

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longestCall(calls)['telephone_number'], longestCall(calls)['total_time']))