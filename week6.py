#python learning 2
#week 6 - OOP

#Notes from lectures
#Object is a collection of rules or properties that can be called upon or manipulates
#This segregation of code makes objects interchangable, and programmes incredibly flexible with minimum effort
#it is also a very different style of thinking and feels like a whole other language
#E.g. when making black jack:
    #Physical things that I need to represent [card, hand, cards]
    #card = number, suit, image
    #hand = collection of cards & hit, score total
    #deck = collection of cards & shuffle, deal a card
#the types or classes you define above are a mix of types and values of data and their behaviour, so hand and deck are kinda different
#primary objective of OODesign is to make code as reusable as possible
#e.g. cards don't have value inherently, e.g. an Ace in poker is different to an ace in 21
#In the videos they talk about putting the calcs in the hand class, but shouldn't they be abstracted from that into a game class so you can put the rules of the game in the game class and separate the concept of a hand of cards.
#abstraction is key, it is the process of separating how a class behaves from how you interact with it
