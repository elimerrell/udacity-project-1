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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def findCallsFromBangalore(calls):
  calls_from_bangalore = []
  for i in range(len(calls)):
    if calls[i][0].startswith('(080)'):
      calls_from_bangalore.append(calls[i])
  
  return calls_from_bangalore

def getAreaCodes(calls):
  # Use a set to avoid duplicates
  unique_codes = set([])
  for i in range(len(calls)):
    # Check for mobile numbers
    if calls[i][1].startswith('('):
      # Get the numbers within the ()
      unique_codes.add(calls[i][1][calls[i][1].find("(")+1:calls[i][1].find(")")])
    elif calls[i][1].startswith('140'):
      unique_codes.add('140')
    # Return first four digits for numbers that start with 7, 8 or 9
    elif calls[i][1].startswith('7') or calls[i][1].startswith('8') or calls[i][1].startswith('9'):
      unique_codes.add(calls[i][1][0 : 4])

  return unique_codes

def printCodes(calls):
  bangalore_calls = findCallsFromBangalore(calls)
  unique_calls = getAreaCodes(bangalore_calls)
  print("The numbers called by people in Bangalore have codes:")
  for elem in sorted(unique_calls):
        print(elem)

def callsWithinBangalore(calls):
  calls_within_bangalore = []
  for i in range(len(calls)):
    if calls[i][0].startswith('(080)') and calls[i][1].startswith('(080)'):
      calls_within_bangalore.append(calls[i])
  return calls_within_bangalore

def percentageOfCallsWithinBangalore(calls):
  numerator = float(len(callsWithinBangalore(calls)))
  denominator = float(len(findCallsFromBangalore(calls)))

  quotient = numerator / denominator
  percentage = quotient * 100

  print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format("{:.2f}".format(percentage)))

printCodes(calls)
percentageOfCallsWithinBangalore(calls)