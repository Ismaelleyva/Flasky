##challenges of a function that takes string and reverses it
#then takes string and returns it in all caps
#first one is flipit and the second one is called shout

def flipit(string):
    x = ""
    for character in string:
        x = character + x
        return x
print(flipit("word"))



def shout(string):
    return string.upper()
