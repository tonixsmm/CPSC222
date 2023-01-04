import requests
import json
import html

url = "https://opentdb.com/api.php?amount=5&category=9&difficulty=easy"

# make a request for data
response = requests.get(url=url)
print(response.text)

json_obj = json.loads(response.text)
print(type(json_obj))
# task: print out each questions
result_list = json_obj["results"]
for result_obj in result_list:
    question = result_obj["question"]
    question = html.unescape(question)
    print(question)
    answer = input()
    if answer == result_obj["correct_answer"]:
        print("yay")
    else:
        print("nay")
        print(result_obj["correct_answer"])