# function called count_vowels(text)
# counts how many vowels (a, e, i, o, u) are in a piece of text.

def count_vowels(text="None"):
    a = text.count("a")
    e = text.count("e")
    i = text.count("i")
    o = text.count("o")
    u = text.count("u")
    print(f"a = {a}")
    print(f"e = {e}")
    print(f"i = {i}")
    print(f"o = {o}")
    print(f"u = {u}")
    return a,e,i,o,u

count_vowels("Hello, my name is Leah.")
