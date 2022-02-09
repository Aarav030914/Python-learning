# question_data = [
#     {"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The US emergency hotline is 911 because of the September 11th terrorist attacks.","correct_answer":"False","incorrect_answers":["True"]},
#     {"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Cucumbers are usually more than 90% water.","correct_answer":"True","incorrect_answers":["False"]},
#     {"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"You are allowed to sell your soul on eBay.","correct_answer":"False","incorrect_answers":["True"]},
#     {"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The average woman is 5 inches \/ 13 centimeters shorter than the average man.","correct_answer":"True","incorrect_answers":["False"]},
#     {"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Albert Einstein had trouble with mathematics when he was in school.","correct_answer":"False","incorrect_answers":["True"]},
#     {"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Fast food restaurant chains Carl&#039;s Jr. and Hardee&#039;s are owned by the same company.","correct_answer":"True","incorrect_answers":["False"]},
#     {"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The scientific name for the Southern Lights is Aurora Australis?","correct_answer":"True","incorrect_answers":["False"]},
#     {"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Popcorn was invented in 1871 by Frederick W. Rueckheim in the USA where he sold the snack on the streets of Chicago.","correct_answer":"False","incorrect_answers":["True"]},
#     {"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The commercial UK channel ITV stands for &quot;International Television&quot;.","correct_answer":"False","incorrect_answers":["True"]},
#     {"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"&quot;Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.&quot; is a grammatically correct sentence.","correct_answer":"True","incorrect_answers":["False"]}
# ]
import requests
questions = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
questions.raise_for_status()
question_data = questions.json()["results"]
