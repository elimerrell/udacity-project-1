"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def countUniqueNumbers(texts, calls):
    # Add unique numbers to set if they don't already exist 
    num_set = set()

    for i in texts:
        num_set.add(i[0])
        num_set.add(i[1])
    for i in calls:
        num_set.add(i[0])
        num_set.add(i[1])

    return len(num_set)

print('There are {} different telephone numbers in the records.'.format(countUniqueNumbers(texts, calls)))