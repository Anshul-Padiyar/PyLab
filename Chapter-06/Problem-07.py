# 7. Write a program to find out whether a given post is talking about “Deadpool” or not.

post = input("Enter your post : ")

superHero = "Deadpool"

if (superHero.lower() in post.lower()):
    print(f"This post is talk about {superHero}")
else:
    print(f"This post is not talk about {superHero}")