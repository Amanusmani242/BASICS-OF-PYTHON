#program to create a dictionary of hindi words with values as their english translation provide user with an option to look it up
oxford = {
    "taufa": "gift",
    "pagaar": "salary",
    "khoon" : "blood"

}
key = input("enter the key:")
print("the corresponding key is:",oxford.get(key))