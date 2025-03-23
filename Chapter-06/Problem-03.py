# 3. A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams. 

spamMessage = ["Make a lot of money", "buy now", "subscribe this", "click this"]

text = input("Enter your messge : ")

if (spamMessage.lower() in text.lower()) :
    print("It's spam message!")
else : 
    print("It's safe")