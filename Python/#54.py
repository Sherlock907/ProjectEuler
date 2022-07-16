"""

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
	 	2C 3S 8S 8D TD
Pair of Eights
	 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
	 	2C 5C 7D 8S QH
Highest card Queen
	 	Player 1
3	 	2D 9C AS AH AC
Three Aces
	 	3D 6D 7D TD QD
Flush with Diamonds
	 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
	 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
	 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
	 	3C 3D 3S 9S 9D
Full House
with Three Threes
	 	Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
import time
start = time.time()

def pokerwin(n,m):
    """Hearts,Tiles,Clovers,Pikes"""
    nres = 0
    mres = 0
    """ 8C TS KC 9H 4S    7D 2S 5D 3S AC
        5C AD 5D AC 9C    7C 5H 8D TD KS
        3H 7H 6S KC JS    QH TD JC 2D 8S"""

    flush = ["CCCCC", "HHHHH", "DDDDD", "SSSSS"]
    straight = ["23456", "34567", "45678", "56789", "6789T", "789JT", "89JQT", "9JKQT", "AJKQT"]
    allcards = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    fullhouse = ([''.join(sorted(str(i) + str(i) + str(i) + x)) for i in range(2, 10) for x in
                  ["TT", "JJ", "QQ", "KK", "AA"]] +
                 [''.join(sorted(str(i) + str(i) + str(i) + str(x) + str(x))) for i in range(2, 10) for x in
                  range(2, 10)] +
                 [''.join(sorted(a + str(i2) + str(i2))) for a in ["TTT", "JJJ", "QQQ", "KKK", "AAA"] for i2 in
                  range(2, 10)] +
                 [''.join(sorted(a + str(c))) for a in ["TTT", "JJJ", "QQQ", "KKK", "AAA"] for c in
                  ["TT", "JJ", "QQ", "KK", "AA"] if c[0] != a[0]])


    # check for royal
    if ''.join(sorted(n[0::2])) == "AJKQT" and n[1::2] in flush:
        nres += 1
    if ''.join(sorted(m[0::2])) == "AJKQT" and m[1::2] in flush:
        mres += 1
    if nres > mres: return "1"
    if mres > nres: return "2"
    if nres == mres and nres != 0: return "Draw"


    # check for straight flush
    if n[1::2] in flush and ''.join(sorted(n[0::2])) in straight:
        nres += 1
    if m[1::2] in flush and ''.join(sorted(m[0::2])) in straight:
        mres += 1
    if nres > mres: return "1"
    if mres > nres: return "2"
    if nres == mres == 1:
        if int(''.join(sorted(n[0::2]))[0]) > int(''.join(sorted(m[0::2]))[0]): return "1"
        if int(''.join(sorted(n[0::2]))[0]) < int(''.join(sorted(m[0::2]))[0]): return "2"
        if int(''.join(sorted(n[0::2]))[0]) == int(''.join(sorted(m[0::2]))[0]): return "Draw"

    # four of a kind
    tempn, tempm = "", ""

    for card in allcards:
        if n[0::2].count(card) == 4:
            nres += 1
            tempn += card
        if m[0::2].count(card) == 4:
            mres += 1
            tempm += card

    if nres > mres: return "1"
    if mres > nres: return "2"
    if nres == mres == 1:
        if tempn == tempm:
            for cards in reversed(allcards):
                if cards in n[0::2].replace(tempn,""): return "1"
                if cards in m[0::2].replace(tempm, ""): return "2"
        if tempn != tempm:
            for cards in reversed(allcards):
                if cards in tempn: return "1"
                if cards in tempm: return "2"


    # Full House
    if ''.join(sorted(n[0::2])) in fullhouse: nres += 1
    if ''.join(sorted(m[0::2])) in fullhouse: mres += 1
    if ''.join(sorted(n[0::2])) == ''.join(sorted(m[0::2])): return "Draw"
    if nres > mres: return "1"
    if nres < mres: return "2"
    if nres == mres and nres != 0:
        for card in reversed(allcards):
            if n[0::2].count(card) == 3: return "1"
            if m[0::2].count(card) == 3: return "2"
        for card in reversed(allcards):
            if n[0::2].count(card) == 2: return "1"
            if m[0::2].count(card) == 2: return "2"

    # Flush
    if n[1::2] in flush: nres += 1
    if m[1::2] in flush: mres += 1
    if n[1::2] == m[1::2]: "Draw"
    if nres > mres: return "1"
    if nres < mres: return "2"
    if nres == mres and nres != 0:
        for card in reversed(allcards):
            if card in n[0::2]: return "1"
            if card in m[0::2]: return "2"


    # Straight
    if ''.join(sorted(n[0::2])) in straight: nres += 1
    if ''.join(sorted(m[0::2])) in straight: mres += 1
    if ''.join(sorted(n[0::2])) == ''.join(sorted(m[0::2])): return "Draw"
    if nres > mres: return "1"
    if nres < mres: return "2"
    if nres == mres == 1:
        if ''.join(sorted(n[0::2]))[0] == "A": return "1"
        if ''.join(sorted(m[0::2]))[0] == "A": return "2"
        if int(''.join(sorted(n[0::2]))[0]) > int(''.join(sorted(m[0::2]))[0]): return "1"
        if int(''.join(sorted(n[0::2]))[0]) < int(''.join(sorted(m[0::2]))[0]): return "2"

    # Three of a Kind
    tempn, tempm = "", ""
    for card in reversed(allcards):
        if n[0::2].count(card) == 3:
            nres += 1
            tempn = card
        if m[0::2].count(card) == 3:
            mres += 1
            tempm = card
    if ''.join(sorted(n[0::2])) == ''.join(sorted(m[0::2])): return "Draw"
    if mres < nres: return "1"
    if mres > nres: return "2"
    if nres == mres == 1 and tempn != tempm:
        for card in reversed(allcards):
            if n[0::2].count(card) == 3: return "1"
            if m[0::2].count(card) == 3: return "2"
    if nres == mres == 1 and tempn == tempm:
        #n remaining cards
        nrc = ''.join(sorted(n[0::2])).replace(tempn, "")
        # m remaining cards
        mrc = ''.join(sorted(m[0::2])).replace(tempm, "")
        for card in reversed(allcards):
            if card in nrc and card not in mrc: return "1"
            if card in mrc and card not in mrc: return "2"
            if card in mrc and card in nrc:
                for card2 in reversed(allcards):
                    if card2 in nrc.replace(card, ""): return "1"
                    if card2 in mrc.replace(card, ""): return "2"

    # Two Pair + One Pair
    tempn, tempm = [],[]
    for card in reversed(allcards):
        if n[0::2].count(card) == 2:
            nres += 1
            tempn.append(card)
        if m[0::2].count(card) == 2:
            mres += 1
            tempm.append(card)

    if nres > mres: return "1"
    if nres < mres: return "2"
    if ''.join(sorted(n[0::2])) == ''.join(sorted(m[0::2])): return "Draw"
    if nres == mres == 2:
        for card in reversed(allcards):
            if (tc:=card) in tempn and card in tempm:
                for card2 in reversed(allcards):
                    if tc == card2: continue
                    if card2 in tempn and card2 in tempm:
                        nrc = ''.join(sorted(n[0::2])).replace(tempn[0], "").replace(tempn[1], "")
                        mrc = ''.join(sorted(m[0::2])).replace(tempm[0], "").replace(tempm[1], "")
                        for card3 in reversed(allcards):
                            if card3 in nrc: return "1"
                            if card3 in mrc: return "2"
                    if card2 in tempn: return "1"
                    if card2 in tempm: return "2"
            if card in tempn: return "1"
            if card in tempm: return "2"

    if nres == mres == 1:
        nrc = ''.join(sorted(n[0::2])).replace(tempn[0], "")
        mrc = ''.join(sorted(m[0::2])).replace(tempm[0], "")
        for card in reversed(allcards):
            if card in tempn[0] and card in tempm[0]:
                for nextcard in reversed(allcards):
                    if nextcard in nrc and card in mrc:
                        nrc = nrc.replace(nextcard, "")
                        mrc = mrc.replace(nextcard, "")
                        for card2 in reversed(allcards):
                            if card2 in nrc and card in mrc:
                                nrc = nrc.replace(card2, "")
                                mrc = mrc.replace(card2, "")
                                for card3 in reversed(allcards):
                                    if card3 in nrc: return "1"
                                    if card3 in mrc: return "2"
                    if nextcard in nrc: return "1"
                    if nextcard in mrc : return "2"
            if card in tempn[0]: return "1"
            if card in tempm[0]: return "2"

    # High Card
    nrc = n[0::2]
    mrc = m[0::2]
    for card in reversed(allcards):
        if card in nrc and card in mrc:
            nrc = nrc.replace(card, "")
            mrc = mrc.replace(card, "")
            for card2 in reversed(allcards):
                if card2 in nrc and card in mrc:
                    nrc = nrc.replace(card2, "")
                    mrc = mrc.replace(card2, "")
                    for card3 in reversed(allcards):
                        if card3 in nrc and card in mrc:
                            nrc = nrc.replace(card3, "")
                            mrc = mrc.replace(card3, "")
                            for card4 in reversed(allcards):
                                if card4 in nrc: return "1"
                                if card4 in mrc: return "2"
                        if card3 in nrc: return "1"
                        if card3 in mrc: return "2"
                if card2 in nrc: return "1"
                if card2 in mrc: return "2"
        if card in nrc: return "1"
        if card in mrc: return "2"



f = open("#54", "r")
player1 = 0
player2 = 0
draws = 0
myresults = []
for line in f:
    pokerhands = line.replace("\n","").replace(" ","")
    handresult = pokerwin(pokerhands[:10],pokerhands[10:])
    if handresult == "1":
        player1 += 1
        myresults.append(1)
    if handresult == "2":
        player2 += 1
        myresults.append(2)
    if handresult == "Draw": draws += 1
f.close()

print(player1,player2, draws)
print(time.time()-start)