# IPND Stage 2 Final Project

import random

data = {
    'quiz': {
        'easy': {
            'phrase': 'This submission is by __1__ (first name only). He is taking the __2__' + \
                'course from __3__, and this project was submitted using __4__',
            'answers': ['Jason', 'Intro to Programming', 'Udacity', 'GitHub'],
            'failures': 5
        },
        'medium': {
            'phrase': '__1__ is the language that we use to write web pages which stands' + \
                'for __2__.  These pages can be styled by using __3__ which is short for __4__,' + \
                'and interactions are commonly handled by __5__.',
            'answers': ['HTML', 'Hypertext Markup Language', 'CSS',
                'Cascading Style Sheets', 'JavaScript'],
            'failures': 4
        },
        'hard': {
            'phrase': 'A ___1___ is created with the def keyword. You specify the inputs a' + \
                '___1___ takes by adding ___2___ separated by commas between the parentheses.' + \
                '___1___s by default return ___3___ if you don\'t specify the value to return.' + \
                '___2___ can be standard data types such as string, number, dictionary, tuple,' + \
                'and ___4___ or can be more complicated such as objects and lambda functions.',
            'answers': ['function', 'inputs', 'nothing', 'lists'],
            'failures': 3
        },
    },
    'user': {
        'quiz': {},
        'score': 0,
        'blankIdx': 0,
        'attempts': 0
    }
}


def initQuiz(level):
    '''Initialize the quiz: Start by showing the paragraph, then ask the user to
    fill in each blank.  Check each of the blanks using the checkAnswer function'''
    data['user']['quiz'] = data['quiz'][level]
    data['user']['blankIdx'] = 0
    data['user']['score'] = 0

    print('\n\n===== Let\'s go! =====\n\n' + data['user']['quiz']['phrase'] + '\n\n')

    while data['user']['blankIdx'] < len(data['user']['quiz']['answers']):
        response = askAQuestion()
        checkAnswer(response)

    print('You got ' + str(data['user']['score']) + ' out of ' +
        str(len(data['user']['quiz']['answers'])) + ' correct!')

    endOfQuiz = 'Think you\'re ready to move on? Or do you want to do something more' + \
        ' meaningful? \n'

    print(endOfQuiz)
    nextSteps(level)

def askAQuestion():
    '''Ask the user to fill in the blank.  If they give the right answer, show
    them a happy message and return a point.  Otherwise, show them a fail note and
    return 0 points
    :return array: Returns a message and a point value'''
    correct = ['Hooray for you!', 'Yipee!', 'I guess that\'s right',
        'Seems logical to me', 'YAAAAAAAY!!!11!!']
    fail    = ['Were you even paying attention?', 'How could you do this to me?',
        'Don\'t quit your day job', 'FAILSAUCE', 'Somewhere a kitten is crying.']

    response = input('What is the answer for __' + str(data['user']['blankIdx'] + 1) + '__? ')

    # Updated to review the length of the arrays for the random limiter
    if response == data['user']['quiz']['answers'][data['user']['blankIdx']]:
        return correct[random.randint(0, len(correct) - 1)], 1 # Returns 1 point
    return fail[random.randint(0, len(fail) - 1)], 0 # Returns 0 points

def checkAnswer(response):
    '''
    Check the answer that was provided by the user to see if it is correct
    :param response: The resposne from the user
    '''
    quiz = data['user']['quiz']['phrase'].split()
    correct = 0

    print(response[0] + '\n')

    if response[1] == 1: # Correct response, move forward
        data['user']['attempts'] = 0 # Clear the attempts holder
        data['user']['quiz']['phrase'] = correctAnswerProvided(quiz)

    else: # Wrong answer
        check = checkAttempts()
        if check == True:
            print('Try again')
        else:
            print('Didn\'t get this one, moving on.')

def correctAnswerProvided(quiz):
    '''
    The correct answer has been provided.  This function will build the proper
    output for display to the user as well as increment counts for question number
    and score
    :param quiz: Not required to provide this as it is already stored, but this
    makes it faster
    :return quiz: Returns the new string with the proper answer in its place
    '''
    idx = 0

    while idx < len(quiz):
        # Fill in the blank with the proper answer
        if '__' + str(data['user']['blankIdx'] + 1) + '__' in quiz[idx]:
            quiz[idx] = data['user']['quiz']['answers'][data['user']['blankIdx']]
        idx += 1

    data['user']['blankIdx'] += 1 # Move to the next blank
    data['user']['score'] += 1 # Count the score for later
    quiz = ' '.join(quiz)

    print(quiz + '\n')
    return quiz

def checkAttempts():
    '''
    See how many attempts the user has made on this question, if they have
    attempts remaining, increment the counter and allow them to try again,
    otherwise increment the question counter, reset attempts to 0 and move to the
    next question
    :return boolean: Can we try again?
    '''
    if data['user']['attempts'] < data['user']['quiz']['failures']:

        data['user']['attempts'] += 1
        return True

    else:
        data['user']['blankIdx'] += 1
        data['user']['attempts'] = 0
        return False

def nextSteps(level):
    '''
    We have completed the quiz, now it's time for the student to figure out what
    they want to do next.  They can exit or select the next level.
    If they are at the end, they can choose to start over.
    '''
    nextStep = input('Go to next quiz or exit? (next / exit): ').lower()

    if nextStep == 'next':

        if level == 'easy':
            initQuiz('medium')
        elif level == 'medium':
            initQuiz('hard')
        else:
            print('\nJust kidding, you did the last quiz. Start over or exit?\n')
            nextStep = input('Type \'start over\' or \'exit\': ').lower()

            if nextStep == 'start over':
                selectAQuiz()

def selectAQuiz():
    '''The opening function of the application.  The user will select a level of
    difficulty by typing easy, medium or hard to start the quizzes'''
    intro = '''Welcome to the quiz!  Select a quiz from below:
        Easy - This project's information
        Medium - Basic web concepts
        Hard - Python for dummies'''

    print('\n' + intro + '\n')

    while True:
        level = input('Choose a difficulty: (easy / medium / hard)\n').lower()
        if level in data['quiz']:
            initQuiz(level) # Start the quiz at the level selected
            break
        print('Incorrect level! Try again!\n')

# Initialize the application
selectAQuiz()