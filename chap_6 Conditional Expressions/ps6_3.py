#A spam comment is defined as a text containing following keywords:
#'buy now','subscribe this', 'click here'.write a program to detect this.
spamwords = ['buy now', 'subscribe this', 'click here']
email = input("Enter your mail:").lower()
spam = False
if('buy now' in email):
    spam = True
if('subscribe this' in email):
    spam = True
if('click here' in email):
    spam = True

print("spam is:", spam)
