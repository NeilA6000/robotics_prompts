#Today, i learned quite a lot. Mr Pancratz taught me how to use or operators effectively in Python in my code, which I believe won't just help me in console situations, but can help me in many more
#if I make a game or something.
interest = input("Are you interested in coding?")
if (interest == "yes" or interest == "Yes"):
    print("Great!")
    Python = input("Do you like Python?")
    if (Python == "yes" or Python == "Yes"):
        print("Great!")
        print("You should learn Python!")
        finalquestion = input("Is C# a good programming language?")
        if (finalquestion == "yes" or finalquestion == "Yes"):
            print("Great!")
            print("You like C#! You're definitely an superfan!")
        else:
                print("You're not an superfan!")
    else:
        print("You're not a coding superfan!")
else:
    print("Okay.")
