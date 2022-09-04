from typing import List

import random 
class Question:
   def __init__(self, icorrects, corrects, question):
        self.icorrects = icorrects
        self.corrects = corrects
        self.question = question


questions = [
        Question(corrects = "Genesis",
            icorrects=["Exodus","Leviticus","Numbercorrectss"],
            question= "What is the first book of the Old Testament?"),
        
        Question(corrects = "Adios",
            icorrects=[" Hola","Au Revoir","Salir"],
            question= "How would one say goodbye in Spanish?"),
        
        Question(corrects = "Quebec",
            icorrects=["Ontario","Nova Scotia","Alberta"],
            question= "Montreal is in which Canadian province?"),
        
        Question(corrects = "1926",
            icorrects=["1923","1929","1930"],
            question= "What year was Queen Elizabeth II born?"),
        
        Question(corrects = "True",
            icorrects=["False",],
            question= "Kissing someone for one minute burns about 2 calories."),
        
        Question(corrects = "Lily of the Valley",
            icorrects=["Hydrangea","Harebell","Yarrow"],
            question= "In the Animal Crossing series, which flower is erroneously called the Jacobs"),
        
        Question(corrects = "John F. Kennedy",
            icorrects=["Exodus","Leviticus","Numbercorrectss"],
            question= "Which of the following presidents is not on Mount Rushmore?"),
        
        Question(corrects = "Bergamot oil",
            icorrects=["Theodore Roosevelt" ,"Abraham Lincoln","Thomas Jefferson"],
            question= "What is the first book of the Old Testament?"),
        
        Question(corrects = "Genesis",
            icorrects=["Lavender","Vanilla","Honey"],
            question= "Earl Grey tea is black tea flavoured with what?"),
        
        Question(corrects = "True",
            icorrects=["False"],
            question= "Popcorn was invented in 1871 by Frederick W. Rueckheim in the USA where he sold the snack on the streets of Chicago."),
    ]


def answer_question(question:Question):
    print(question.question)
    print("")
    answers = question.icorrects
    answers.append(question.corrects)
    random.shuffle(answers)
    for i in range(len(answers)):
        print(i+1,"-",answers[i])
    
    answer = input("Enter your answer: ")
    if(answer.lower() == question.corrects.lower()):
        print("Your answer was correct")
        return 1
    else: 
        print("Your answer was incorrect")
        print("The correct answer was",question.corrects)
        return 0


def trivia(questions:List[Question]):
    result = 0
    for i in range(len(questions)):
        result += answer_question(questions[i])
    print("Your result is ",result,"\n of",len(questions))
    
    
trivia(questions=questions)




