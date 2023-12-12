import random
words = ["apple", "oracle", "microsoft", "dog", "piano","orange", "cartoon", "teacher", "machine", "anxiety", "morning", "congrats"]
con = 'y'
print("THE GAME BEGINS")
while con in ['y','Y', 'yes', 'Yes', 'YES'] or len(words) == 0:
    guess = random.choice(words)
    words.remove(guess)
    jumble = ''.join(random.sample(guess, len(guess)))
    print("Guess the word: {}".format(jumble))
    answer = input('Type your answer here: ')
    if answer == guess:
        print("Congrats for the correct guess")
        print("Do you want to continue?")
        while True:
            print("Press 'y' -> 'Yes'\n'n' -> 'No'")
            con = input()
            if con in ['y','Y', 'yes', 'Yes', 'YES']:
                break
            elif con in ['n','N', 'no', 'No', 'NO']:
                break
            else:
                continue
    else:
        print("Next time, the correct answer : {}".format(guess))
        print("Do you want to continue?")
        while True:
            print("Press 'y' -> 'Yes'\n'n' -> 'No'")
            con = input()
            if con in ['y','Y', 'yes', 'Yes', 'YES']:
                break
            elif con in ['n','N', 'no', 'No', 'NO']:
                break
            else:
                continue
print("Thank you for playing.\nHave a nice day 🙂")