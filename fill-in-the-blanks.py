# IPND Stage 2 Final Project

import random

quiz1 = ['''This submission is by __1__ (first name only). He is taking the __2__ course from __3__, and this project was submitted using __4__''',
    ['Jason', 'Intro to Programming', 'Udacity', 'GitHub'],
    ['__1__','__2__','__3__','__4__']
]

quiz2 = ['''__1__ is the language that we use to write web pages which stands for __2__.
These pages can be styled by using __3__ which is short for __4__, and interactions are commonly handled by __5__.''',
    ['HTML', 'Hypertext Markup Language', 'CSS', 'Cascading Style Sheets', 'JavaScript'],
    ['__1__','__2__','__3__','__4__','__5__']
]

quiz3 = ['''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.''',
    ['function', 'inputs', 'nothing', 'lists'],
    ['__1__','__2__','__3__','__4__']
]

def checkAnswer(input, answerList, idx):
    '''
    Did the player supply the correct answer?  Check the list, then respond
    accordingly
    '''

    correct = ['Hooray for you!', 'Yipee!', 'I guess that\'s right', 'Seems logical to me', 'YAAAAAAAY!!!11!!']
    fail    = ['Were you even paying attention?', 'How could you do this to me?', 'Don\'t quit your day job', 'FAILSAUCE', 'Somewhere a kitten is crying.']

    if input == answerList[idx]:
        return correct[random.randint(0,4)], 1
    return fail[random.randint(0,4)], 0


def initQuiz(selectedQuiz):
    '''
    Initialize the quiz: Start by showing the paragraph, then ask the user to
    fill in each blank.  Check each of the blanks using the checkAnswer function
    '''

    traverseQuiz(selectedQuiz)

        # Print the first element in the array, the text response to their input
        # either it was correct or a failure

    print('Think you\'re ready to move on? Or do you want to do something more meaningful?')
    print()

    nextStep = input('Type \'next\' to move on or \'exit\' to leave the quiz: ')

    if nextStep == 'next':

        # Go to the next quiz
        if selectedQuiz == quiz1:
            initQuiz(quiz2)
        elif selectedQuiz == quiz2:
            initQuiz(quiz3)
        else:
            print()
            print('Just kidding, you did the last quiz. Start over or exit?')
            print()

            nextStep = input('Type \'start over\' or \'exit\': ')

            if nextStep == 'start over':
                selectAQuiz()


def traverseQuiz(selectedQuiz):
    '''
    We will use this function for traversing the quiz questions
    '''

    # Assign variables from the selected quiz
    quiz = selectedQuiz[0]
    answers = selectedQuiz[1]
    blanks = selectedQuiz[2]

    # Start the indexing at 0
    blankIdx = 0

    print('===== Let\'s go! =====')
    print()
    print(quiz)
    print()

    while blankIdx < len(blanks):

        # Get the response from checkAnswer, comes back as an array
        response = checkAnswer(askAQuestion(blanks[blankIdx]), answers, blankIdx)
        print(response[0])
        print()

        # If this is a correct response, we can move on, otherwise it will fail
        # and loop back around
        if response[1] == 1:

            quiz = quiz.split()
            idx = 0

            while idx < len(quiz):

                # Fill in the blank with the proper answer
                if blanks[blankIdx] in quiz[idx]:
                    quiz[idx] = answers[blankIdx]

                idx += 1

            # Iterate the blankIdx value to go to the next option
            blankIdx += 1

            # Rejoin and prepare to print
            quiz = ' '.join(quiz)

            print(quiz)
            print()

        else:

            # Got it wrong, print an error and have them try again
            print('Try again')


def askAQuestion(blank):
    '''
    Ask the user to fill in the blank.  Perhaps this doesn't need to be a function
    '''

    response = input('What is the answer for ' + blank + '? ')
    return response

def selectAQuiz():
    intro = '''Welcome to the quiz!  Select a quiz from below:
        1 - This project's information
        2 - Basic web concepts
        3 - Python for dummies'''

    print()
    print(intro)
    selection = input('Type the number: ')

    if selection == '1':
        initQuiz(quiz1)
    elif selection == '2':
        initQuiz(quiz2)
    elif selection == '3':
        initQuiz(quiz3)
    else:
        print('That wasn\'t an option, try again, punk.')
        selectAQuiz()

selectAQuiz()