# Random "language" generator
# Declare lists with the current alphabet
import random as r
# To be referenced later
VOWELS = ['a', 'e', 'i', 'o', 'u']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 
              'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

# To be altered later
# Make program expandable in future to consider vowel and consonant placement in
    # result
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 
              'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

print("\n\nLet's create a language!  Enter Ctrl + C to quit.")

# Remove letters from final result
print('\nLetter Omission Stage')
option = input("\tAre there any letters you wouldn't like to see in your " 
               "language? (y/n)  ")
# Make input case insensitive
option = option.lower()
# Only move forward until user provides valid input
while option != 'y' and option != 'n':
    # Error message, ask for input again
    option = input('\t\tInput error. Please enter "y" for yes or "n" for no.\n'
                   "\tAre there any letters you wouldn't like to see in your " 
                   "language? (y/n)  ")
    option = option.lower()
    if option == 'y' or option == 'n': break
# User declined, move onto next stage
if option == 'n': exit
# User accepted, collect following steps
elif option == 'y':
    print('\n\tEnter one letter to omit then press "Enter". '
          'Repeat until you are satisfied.\n'
          '\tEnter "2" to delete all letters and add them in manually.\n'
          '\tEnter "1" to see the list of remaining letters.\n'
          '\tEnter "0" to end\n')
    # Declare varible to be used later
    omit = ''
    # Automatic start
    while omit != '0':
        omit = input('Omit the letter:  ')
        # Target list housing inputed letter
        if omit in vowels:
            vowels.remove(omit)
        elif omit in consonants:
            consonants.remove(omit)
        # Wipe both lists/ all letters
        elif omit == '2':
            vowels.clear()
            consonants.clear()
            # Move onto next stage
            break
        # Display current letter bank
        elif omit == '1':
            print(f'\tThe vowels to be used are: {vowels}')
            print(f'\tThe consonants to be used are: {consonants}')
            print('\tContinue or Enter "0" to quit')
        # Exit loop, move onto next stage
        elif omit == '0': break
        # Error message for invalid input, collect input again
        else:
            print('\tInput error. Enter a letter to omit, '
                  '"1" to view current letter list, or "0" to exit.')

# Add letters to final result
print('\nLetter Addition Stage')
option = input("\tAre there any letters you'd like to see more often? (y/n)  ")
# Make input case insensitive
option = option.lower()
# Only move forward until user provides valid input
while option != 'y' and option != 'n':
    # Error message, ask for input again
    option = input('\t\tInput error. Please enter "y" for yes or "n" for no.\n'
                   "\tAre there any letters you'd like to see more often? "
                   "(y/n)  ")
    option = option.lower()
    if option == 'y' or option == 'n': break
# User declined, move onto next step
if option == 'n': exit
# User accepted, collect more input
elif option == 'y':
    print('\n\tEnter one letter to increase frequency then press "Enter". '
          'Repeat until you are satisfied.\n'
          '\t\tTip: add a few more vowels for a better result.\n'
          '\tEnter "1" to see the list of current letters.\n'
          '\tEnter "0" to end.\n')
    # Declare variable to be used later
    add = ''
    while add != '0':
        add = input('Add the letter:  ')
        # Identify which list to add letters to
        if add in VOWELS:
            vowels.append(add)
        elif add in CONSONANTS:
            consonants.append(add)
        # Display current letter bank
        elif add == '1':
            print(f'\tThe vowels to be used are: {sorted(vowels)}')
            print(f'\tThe consonants to be used are: {sorted(consonants)}')
            print('\tContinue or Enter "0" to quit')
        # Move onto next step
        elif add == '0': break
        # Error message. Restate options, wait until valid input provided
        else:
            print('\tInput error. Enter a letter to omit, '
                  '"1" to view current letter list, or "0" to exit.')
            
# Combine vowels and consonants into one list 
letter_bank = vowels + consonants

# Define the possible length of words
length_frequency = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8]

# Declare words as lists where letters are stored as list items
word0 = []
word1 = []
word2 = []
word3 = []
word4 = []
word5 = []
word6 = []
word7 = []

# Container for words
sentence = [word0, word1, word2, word3, word4, word5, word6, word7]
# Declare variable to store the given lengths of each word
word_lengths = []

# Populate word_lengths with random options from length_frequency
for words in sentence:
    word_lengths.append(r.choice(length_frequency))

# Assign each spot in each word a random letter
for x in range(word_lengths[0]):
    word0.append(r.choice(letter_bank))
for x in range(word_lengths[1]):
    word1.append(r.choice(letter_bank))
for x in range(word_lengths[2]):
    word2.append(r.choice(letter_bank))
for x in range(word_lengths[3]):
    word3.append(r.choice(letter_bank))
for x in range(word_lengths[4]):
    word4.append(r.choice(letter_bank))
for x in range(word_lengths[5]):
    word5.append(r.choice(letter_bank))
for x in range(word_lengths[6]):
    word6.append(r.choice(letter_bank))
for x in range(word_lengths[7]):
    word7.append(r.choice(letter_bank))

# Join word lists together for display
word0 = ''.join(word0)
word1 = ''.join(word1)
word2 = ''.join(word2)
word3 = ''.join(word3)
word4 = ''.join(word4)
word5 = ''.join(word5)
word6 = ''.join(word6)
word7 = ''.join(word7)

# Print result
print('\nSay hello to your new language!')
print(f'\t{word0.title()} {word1} {word2} {word3}, {word4} {word5} {word6} '
      f'{word7}.')