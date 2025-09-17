# function called count_vowels(text)
# counts how many vowels (a, e, i, o, u) are in a piece of text.

def count_vowels(text="None"):
    return print("a =", text.count("a")), print("e =", text.count("e")), print("i =", text.count("i")), print("o =", text.count("o")), print("u =", text.count("u"))

count_vowels("Hello, my name is Leah.")
