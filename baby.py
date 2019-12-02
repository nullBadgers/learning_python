from random import choice

questions = ["What time is it?: ","What year is it?: ", 
            "What food is it?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just":
    answer = input("Why?: ").strip().lower()

print("ok")

