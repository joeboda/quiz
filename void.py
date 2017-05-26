from easygui import *
import time
import requests
import wget
import json
import html
from pprint import pprint


#token = wget.download('https://opentdb.com/api_token.php?command=request')

#json_Data = open('data.json','r').read()

CHOICES = ["True", "False"]


with open('data_small.json') as data_file:    
    data = json.load(data_file)
#pprint(data)

#questions = json.JSONDecoder(data)

result = 0

for q in data['results']:
	question = buttonbox(q['question'],choices=CHOICES)
#	print(html.unescape(q['question']))
#	inp = input('True / False ?')
	if(inp == 't'):
		answer = 'True'

	elif(inp == 'f'):
		answer = 'False'

	if(answer == q['correct_answer']):
		result += 1

print("Out of ten questions, you answered ", result , "correctly")