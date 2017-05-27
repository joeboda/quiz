from easygui import *
import time
import requests
import wget
import json
import html



CHOICES = ["True", "False"]
TITLE = "These questions you answered incorrectly"
MESSAGE = "Click Ok to start over or Cancel to stop playing"
BUTTONS = ["Online","Offline"]
URL = "https://opentdb.com/api.php?amount=10&type=boolean"

reply = buttonbox("Online or Offline questions?", choices=BUTTONS)
if reply == "Online":
	reply = buttonbox("Request new token or use token from disk?", choices=["Yes", "No"])
	if reply == "Yes":
	
		r = requests.get('https://opentdb.com/api_token.php?command=request')
		with open('token.json', 'w') as f:
			json.dump(r.json(), f, ensure_ascii=False)

		
		if r.json()['response_code'] == 0:
			r = requests.get('https://opentdb.com/api.php?amount=10&type=boolean&token=' + str(r.json()['token']))
			
			if r.json()['response_code'] == 0:
				print("Retrieving data succesfully")
				data = json.loads(r.text)	
		else:
			print("Error retrieving data, aborting")
			quit()

	elif reply == "No":
		with open('token.json', 'r') as f:
			json_data = json.load(f)
			print(json_data['token'])
			r = requests.get('https://opentdb.com/api.php?amount=10&type=boolean&token=' + str(json_data['token']))
			data = json.loads(r.text)
			if data['response_code'] == 0:
				print("Retrieving data succesfully")
					
			else:
				print("Error retrieving data, aborting")
				quit()

#r = requests.get(URL)

#data = json.loads(r.text)
else:
	with open('data_small.json') as data_file:
		data = json.loads(data_file.read())

while True:
	correct_count = 0
	wrong_answers = []

	for q in data['results']:
		
		answer = buttonbox(html.unescape(q['question']),choices=CHOICES)
		

		if answer == q['correct_answer']:
			correct_count += 1
		else:
			wrong_answers.append(html.unescape(q['question']) + '\n')


	if len(wrong_answers) == 0:
		wrong_answers.append("Everything correct! Good job! ")

	wrong_answers.append('\n' + "***********************************************************")
	result_str = ""
	result_str = "You got " + str(correct_count) + " correct out of 10"
	wrong_answers.append('\n' + result_str)
	
	
	c1 = textbox("These questions you answered incorrectly", "List of files", wrong_answers)
	#c1 = choicebox(MESSAGE,TITLE, wrong_answers)
	print('{0} ends'.format("Quiz"))
	if c1 is not None:
		break