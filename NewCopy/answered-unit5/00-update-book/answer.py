import random

def magic8ball():
    return getAnswer(random.randint(0,8))


def getAnswer(index):
    fortunes = [ 'It is certain', 
                 'It is decidedly so', 
                 'Yes', 
                 'Reply hazy try again', 
                 'Ask again later', 
                 'Concentrate and ask again', 
                 'My reply is no', 
                 'Outlook not so good', 
                 'Very doubtful'
               ]
    return fortunes[index]


keepgoing = True
while keepgoing:
    question = input("Enter a question or input 'quit' to quit. ")
    
    if question != 'quit':
        print(magic8ball())
    else:
        keepgoing = False
