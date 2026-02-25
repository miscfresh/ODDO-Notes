# im gonna play around with this question i had: how can i make a user input into a dynamic list that i can use?
# for example, what do i do if i want to print([2]) in a user input list, but the user input list is less than 2?

yup = input('Make a list, use commas!: ')

# since python treats user inputs as strings, using the method '.split()' allows you to split a string input based on whatever i put in ' '
list_yup = yup.split(',')
# now count number of items in list via the len() function; len ~ length (in my head at least)
count = len(list_yup)
print(list_yup)
print(count)

# now how can we tailor a program to the length of a list to prevent encountering errors?
# for example if i wanted to have student type out a list of their 5 favorite fruits, and than have my program print them out,
# how could i avoid an error if i wanted to print [4] if they only included 4 fruits?
import random

fruits = input('What are your favorite fruits?: ')
list_fruits = [item.strip() for item in fruits.split(',')]
num = len(list_fruits)

# .strip removes white space from the list; i.e. if i wrote "grapes, apples, ..." it'd turn into [grapes,apples,...]
# while loops can 

while num != 5:
    print(num)
    print('You didnt finish your list! Go again!')
    fruits = input('What are your favorite fruits?: ')
    list_fruits = [item.strip() for item in fruits.split(',')]
    num = len(list_fruits)
if num == 5:
    print(num)
    same = random.choice(list_fruits)
    print('I like ' + same + ' too!')

print('Thanks for participating!')


# this is depressingly unoptimized but whatever for now, i gotta work on my inorganic hw ngl
# some ideas to improve: is there a way to store list count without repeating the same commands (2 instances of num instead of 1)
# is there a way to only use var fruits once (same problem, two instances)?