def make_greeting(language):

    def greet(name):
        if language.lower() == "hindi":
            print("Namaste,", name)
        else:
            print("Hello,", name)

    return greet

hindi_greet = make_greeting("hindi")
english_greet = make_greeting("english")

hindi_greet("Arsh")
english_greet("Rohit")