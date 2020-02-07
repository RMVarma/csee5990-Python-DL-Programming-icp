string = str(input("enter any string"))

def string_alternative(string):
    newstring= string[::2]
    print(newstring)
    return(newstring)
string_alternative(string)