#define custom song function.
def custom_song(name, verb1, noun1, adjective, verb2, noun2, noun3, noun4,):
    print("\n\n")
    print(f"{name} {verb1} on a {noun1},")
    print (f"{name} had a {adjective} {verb2}")
    print (f"All the {noun2}'s {noun3} and all the {noun2}'s {noun4}")
    print (f"Couldn't put {name} together again.")

#ask for user input
name = input ("Give me a name: ")
verb1 = input ("Give me a verb: ")
noun1 = input ("Give me a noun: ")
adjective = input ("Give me an adjective: ")
verb2 = input ("Give me another verb: ")
noun2 = input ("Give me another noun: ")
noun3 = input ("Give me another noun: ")
noun4 = input ("Give me another noun: ")

#call function
custom_song(name, verb1, noun1, adjective, verb2, noun2, noun3, noun4,)

    