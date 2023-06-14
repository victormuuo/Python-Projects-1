# a dictionary that stores questions and answers
# have a variable that tracks the score of a player
# loop through the dictionary using key values pairs
# display each question to the user and allow them answer
# tell them if they are right or wrong
# show them final score when quiz is completed

quiz={
    "question1":{

        "question":"What is the capital city of USA?",
        "answer":"Washington DC"
    },
    "question2":{
        "question":"What is the capital city of England?",
        "answer":"London"
    },
    "question3":{
        "question":"What is the capital city of France?",
        "answer":"Paris"
    },
    "question4":{
        "question":"What is the capital city of Germany?",
        "answer":"Berlin"
    },
    "question5":{
        "question":"What is the capital city of China?",
        "answer":"Hong kong"
    },
    "question6":{
        "question":"What is the capital city of Switzerland?",
        "answer":"Bern"
    },
    "question7":{
        "question":"What is the capital city of Italy?",
        "answer":"Rome"
    },
    "question8":{
        "question":"What is the capital city of Spain?",
        "answer":"Madrid"
    },
    "question9":{
        "question":"What is the capital city of Portugal?",
        "answer":"Lisbon"
    },
    "question10":{
        "question":"What is the capital city of Austria?",
        "answer":"Vienna"
    },
}

score=0

for key, value in quiz.items():
    print(value['question'])
    answer=input("answer?: ")

    if answer.lower()==value['answer'].lower():
        print("Correct")
        score=score+1
        print("Score: "+ str(score))
        print("")
        print("")

    else:
        print("Incorrect")
        print("The correct answer is: "+ value['answer'])
        print("Score: "+ str(score))
        print("")
        print("")

print("Final score: " + str(score) + " out of 10 questions correctly ")
print("Percentage: " + str(int(score/10*100)) + "%")


