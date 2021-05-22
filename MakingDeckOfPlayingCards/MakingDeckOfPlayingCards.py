## Make a deck of playing cards

import random

card_faces=[]
suits=["Hearts","Diamonds","Clubs","Spades"]
royals=["King","Queen","Joker","Ace"]
deck=[]

#Append 2 to 10 number cards
for i in range(2,11):
    card_faces.append(str(i))

#Append face cards + Aces
for j in range(4):
    card_faces.append(royals[j])

# attach suits

for k in range(4):
    for l in range(13):
        card=(card_faces[l]+" of "+suits[k])
        deck.append(card)

# Shuffle the Deck
random.shuffle(deck)

# All 52 Cards

for m in range(52):
    print(deck[m])