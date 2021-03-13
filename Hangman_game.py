import random

def hangman():
    # print("welcoe to hell young man")
    list_of_words = ['Prasanna', 'shubham', 'mohit','mrunal']
    word=random.choice(list_of_words)
    # print(word)
    attempts = 10
    guessed_name = ''
    correct_entries = set('abcdefghijklmnopqrstuvwxyz')


    while len(word)>0:
        main_word = ""
        missed=0


        for letter in word :
            if letter in guessed_name :
                main_word = main_word+letter
            else :
                main_word = main_word + "_ "

        
        if main_word == word :
            print(main_word)
            print("you guessed the correct name ..congtatulation you saved him...")
            break


        print("Guess the word", main_word)
        guess = input()

        if guess in correct_entries :
            guessed_name = guessed_name + guess
        else :
            print("enter correct values")
            guess = input()

        
        if guess not in word :
            attempts = attempts - 1
            

            if attempts == 9 :
                print("\n You have 9 chances left to save the victim")
                print("================")
                print(" ")
            if attempts == 8 :
                print("\n You have 8 chances left to save the victim")
                print("=================")
                print("        O        ")
                print(" ")
            if attempts == 7 :
                print("\n You have 7 chances left to save the victim")
                print("=================")
                print("        O        ")
                print("        |        ")
                print(" ")
            if attempts == 6 :
                print("\n You have 6 chances left to save the victim")
                print("=================")
                print("        O        ")
                print("       /|        ")
                print(" ")
            if attempts == 5 :
                print("\n You have 5 chances left to save the victim")
                print("=================")
                print("        O        ")
                print("       /|\       ")
                print(" ")
            if attempts == 4 :
                print("\n You have 4 chances left to save the victim")
                print("=================")
                print("        O        ")
                print("       /|\       ")
                print("       /         ")
                print(" ")
            if attempts == 3 :
                print("\n You have 3 chances left to save the victim")
                print("=================")
                print("        O        ")
                print("       /|\       ")
                print("       / \       ")
                print(" ")
            if attempts == 2 :
                print("\n You have 2 chances left to save the victim")
                print("=================")
                print("        O     |  ")
                print("       /|\       ")
                print("       / \       ")
                print(" ")
            if attempts == 1 :
                print("\n You have only 1 chance!!!! bhai bacha le yaar plzzz")
                print("=================")
                print("        O    __|  ")
                print("       /|\       ")
                print("       / \       ")
                print(" ")
            if attempts == 0:
                print("\n Marwa diya na bhai ko bancho.")
                print("=================")
                print("        O_____|  ")
                print("       /|\       ")
                print("       / \       ")
                print(" ")
                break

                


name =  input("Hello protagonist pleae tell your name : ")
print("Welcome {} ! i was waiting for you from a long time! Glad you are here ..  please save my friend !".format(name))
print("------------------------------------------------------------------------------------------------------------------")
print("To save him you have to guess his name in  10 attempts ...")
mera_man = 'y'
while(mera_man=='y'):
    hangman()
    mera_man= input("fir se try karoge????? \n Agar khelna hai to 'y' dabao otherwise press anything")

