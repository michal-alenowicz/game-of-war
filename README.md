**The card game of war itself is NOT fun, unless you play with kids and cheat to lose ASAP ;)**
However, "war" proved quite interesting as my first excercise in OOP in Python. My code uses several classes such as Card, Deck, Player. Two instances of the Player class play out a game, using an instance of the Deck class. You don't need to do anything, it will play out itself, giving you the winner and the overall length of the game (the number of comparisons).

While it's seemingly simple, working on it allowed me to make an interesting observation (important info for "war" lovers out there!) - when a player picks up cards from the table to add them to the hand, the added cards have to get shuffled, otherwise, with certain hand patterns, an infinite game of war may be possible! I saw one play out in my own program. To avoid that, the cards being picked up are shuffled "between the table and the hand".

**I will add new features, such as the option to play out *N* games in a row and provide more stats (e.g. game length mean value and std over *N* games)!**
