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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# Maintain sets of outgoing and received calls
outgoing_calls = set()
incoming_calls = set()

# Maintain sets of outgoing and received texts
outgoing_texts = set()
incoming_texts = set()

# Maintain set of possible telemarketers
possible_telemarketers = set()

def categorizeCalls(calls):
    for call in calls:
        outgoing_calls.add(call[0])
        incoming_calls.add(call[1])

def categorizeTexts(texts):
    for text in texts:
        outgoing_texts.add(text[0])
        incoming_texts.add(text[1])

#Call functions above to track calls and texts
categorizeCalls(calls)
categorizeTexts(texts)

def possibleTelemarketers():
    for call in outgoing_calls:
        # Add the call (phone number) to the list of posssible telemarketers if it didn't recieve calls,
        # send texts, or receive texts
        if call not in incoming_calls and call not in outgoing_texts and call not in incoming_texts:
            possible_telemarketers.add(call)

#Create list of possible telemarketers
possibleTelemarketers()

def printNumbers():
  print("These numbers could be telemarketers: ")
  for number in sorted(possible_telemarketers):
        print(number)

printNumbers()