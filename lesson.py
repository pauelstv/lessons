__author__ = 'pauelstv'
# program check IF ELIF ELSE construction

import mymod

exit_phrase = ""
passtext = ""

while passtext != "exit":
    passtext = input("Please login:")
    if passtext == "huy":
        print("hello HUY")
    elif passtext == "kek":
        print("Hello KEK")
    else:
        print("User not found. Type exit")
print("Thats all", mymod.title)

