import random

HANGMAN_PICKS = ['''
    +---+
        |
        |
        |
       ===''','''
    +---+
    0   |
        |
        |
       ===''','''     
    +---+
    0   |
    |   |
        |
       ===''','''    
    +---+
    0   |
   /|   |
        |
       ===''','''
    +---+
    0   |
   /|\  |
        |
       ===''','''
    +---+
    0   |
   /|\  |
   /    |
       ===''','''    
    +---+
    0   |
   /|\  |
   / \  |
       ===''','''
    +---+
   [0   |
   /|\  |
   / \  |
       ===''','''
    +---+
   [0]  |
   /|\  |
   / \  |
       ===''']

words = {'Colors': 'red orange yellow green blue indigo violet white black brown'.split(), 
         'Shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruits':'apple orange lemon lime pear watermellon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
         'Animals':'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return (wordDict[wordKey][wordIndex], wordKey)

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICKS[len(missedLetters)])
    print()
    
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end= ' ')
    print()
    
    blanks = '-' * len(secretWord[0])
    
    for i in range(len(secretWord[0])):
        if secretWord[0][i] in correctLetters:
            blanks = blanks[:i] + secretWord[0][i] + blanks[i+1:]
    
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')

difficulty = 'X'
while difficulty not in 'EMH':
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICKS[8]
    del HANGMAN_PICKS[7]
if difficulty == 'H':
    del HANGMAN_PICKS[8]
    del HANGMAN_PICKS[7]
    del HANGMAN_PICKS[5]
    del HANGMAN_PICKS[3]
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while not gameIsDone:
    print('The secret word is in the set:', secretWord[1])
    displayBoard(missedLetters, correctLetters, secretWord)
    
    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord[0]:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord[0])):
            if secretWord[0][i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord[0] + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMAN_PICKS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) +  ' correct guesses, the word was "' + secretWord[0] + '"')
            gameIsDone = True
    
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            gameIsDone = False
        else:
            break

