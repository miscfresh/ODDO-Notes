# first little project to get back into code
# surface level review of if-else statements, variables, lists, methods, operators, etc.

#game data for keeping count via initialization:
correct_count = 0
wrong_count = 0

##################################################################

#introduction - use strings 'xxxxxx'
print('Welcome to the biochem quiz lil bro.')

#user input; if input = "no" then quits
#input(prompt): prompt is what appears to the user before they can begin typing.
#calling the variable "playing" will prompt the user response
#.lower().strip() just take the user input and makes it all lowercase (lower) and removes additional spaces (strip)
playing = input('Will you take the quiz? ').lower().strip()

#need to check for user response; use if statements!
# != is 'not equal to'
if playing != 'yes':
    quit()

print('Lets begin!')
##################################################################

#neg_charged is a list containing acceptable answer for the question
neg_charged = ['Glutamate', 'Glutamic Acid', 'Glu', 'E', 'Aspartate', 'Aspartic Acid', 'Asp', 'D']

answer = input('What amino acid residues are negatively charged at neutral pH? ')
#if answer 'in' basically says if the input is one of the strings in the list, it'll be correct (program will continue to run)
if answer in neg_charged:
    print('Correct!')
    correct_count += 1
#+= is an assignment operator; used to add to a variable. --> count += 1 is equal to  count = count + 1
else:
    print('Wrong!')
    wrong_count += 1

##################################################################

#another list lolz
serine = ['Serine', 'S', 'Ser']

answer = input('What residue acts as a nucleophile to form a covalent intermediate in the serine protease mechanism?: ')
if answer in serine:
    print('Correct!')
    correct_count += 1
else:
    print('Wrong!')
    wrong_count += 1

##################################################################

b_branch = ['Gly', 'Glycine', 'G', 'Valine', 'Val', 'V', 'Isoleucine', 'Isl', 'I']

answer = input('What is one residue that has beta-branches?: ')
if answer in b_branch:
    print('Correct!')
    correct_count += 1
else:
    print('Wrong!')
    wrong_count += 1

##################################################################

if wrong_count == 0:
    final_score = correct_count
else:
    final_score = correct_count/wrong_count

print('You got ' + str(final_score) + ' correct!')
percent = ((final_score / 3) * 100)
print('You got a ' + str(round(percent, 2)) + "%")
if final_score == 3:
    print('Youre goated!')
else:
    print('Start studying idiot.')
    quit()
print('Thanks for playing!')
quit()