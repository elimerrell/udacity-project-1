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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def getFirstText(texts):
    # texts[0] gets the first text from the data
    incoming_number = texts[0][0]
    answering_number = texts[0][1]
    time = texts[0][2]
    print('First record of texts, {} texts {} at time {}'.format(incoming_number, answering_number, time))

def getLastCall(calls):
    # calls[-1] gets the last call from the data
    incoming_number = calls[-1][0]
    answering_number = calls[-1][1]
    time = calls[-1][2]
    duration = calls[-1][3]
    print('Last record of calls, {} calls {} at time {}, lasting {} seconds'
    .format(incoming_number, answering_number, time, duration))

getFirstText(texts)
getLastCall(calls)

