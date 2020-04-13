import random

adj = input("Insert an adjective ")
noun = input("Insert a noun ")
verb = input("Insert a verb ending with 'ing' ")
if verb.count('ing') == 0:
    verb = False

while verb == False:
    verb = input("Please insert a verb ending with 'ing' ")

sentences = [f"Our house has {adj} furniture and there is a {verb} {noun}",
             f"The school canteen has {adj} pizzas and a {verb} {noun}",
             f"The {adj} {noun} is {verb} ",
             f"He described the {noun} to be {adj} looking while he was {verb}"]
sentence = random.choice(sentences)
print(sentence)
