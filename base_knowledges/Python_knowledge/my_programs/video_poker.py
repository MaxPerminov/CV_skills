# This video-poker counts deals, while reaching 1000000 dollars.
# The result goes to the leaderboard.

import datetime
import random


def win(w, b):
    if ("2" in w and "3" in w and "4" in w and "5" in w and "6" in w) or \
            ("3" in w and "4" in w and "5" in w and "6" in w and "7" in w) or \
            ("4" in w and "5" in w and "6" in w and "7" in w and "8" in w) or \
            ("5" in w and "6" in w and "7" in w and "8" in w and "9" in w) or \
            ("6" in w and "7" in w and "8" in w and "9" in w and "10" in w) or \
            ("7" in w and "8" in w and "9" in w and "10" in w and "J" in w) or \
            ("8" in w and "9" in w and "10" in w and "J" in w and "Q" in w) or \
            ("9" in w and "10" in w and "J" in w and "Q" in w and "K" in w):
        if w.count("\u2660") == 5 or w.count("\u2661") == 5 or w.count("\u2662") == 5 or w.count("\u2663") == 5:
            return "Street Flash", b * 26
        return "Street", b * 6
    elif "10" in w and "J" in w and "Q" in w and "K" in w and "A" in w:
        if w.count("\u2660") == 5 or w.count("\u2661") == 5 or w.count("\u2662") == 5 or w.count("\u2663") == 5:
            return "Royal Flash", b * 51
        return "Street", b * 6
    elif w.count("\u2660") == 5 or w.count("\u2661") == 5 or w.count("\u2662") == 5 or w.count("\u2663") == 5:
        return "Flash", b * 6
    elif w.count("2") == 4 or w.count("3") == 4 or w.count("4") == 4 or w.count("5") == 4 or \
            w.count("6") == 4 or w.count("7") == 4 or w.count("8") == 4 or w.count("9") == 4 or \
            w.count("10") == 4 or w.count("J") == 4 or w.count("Q") == 4 or w.count("K") == 4 or w.count("A") == 4:
        return "Poker", b * 13
    elif w.count("2") == 3 or w.count("3") == 3 or w.count("4") == 3 or w.count("5") == 3 or w.count("6") == 3 or \
            w.count("7") == 3 or w.count("8") == 3 or w.count("9") == 3 or w.count("10") == 3 or w.count("J") == 3 or \
            w.count("Q") == 3 or w.count("K") == 3 or w.count("A") == 3:
        if w.count("2") == 2 or w.count("3") == 2 or w.count("4") == 2 or w.count("5") == 2 or w.count("6") == 2 or \
                w.count("7") == 2 or w.count("8") == 2 or w.count("9") == 2 or w.count("10") == 2 or \
                w.count("J") == 2 or w.count("Q") == 2 or w.count("K") == 2 or w.count("A") == 2:
            return "Full House", b * 5
        return "Three of Kind", b * 4
    elif w.count("2") == 2:
        if w.count("3") == 2 or w.count("4") == 2 or w.count("5") == 2 or w.count("6") == 2 or \
                w.count("7") == 2 or w.count("8") == 2 or w.count("9") == 2 or w.count("10") == 2 or \
                w.count("J") == 2 or w.count("Q") == 2 or w.count("K") == 2 or w.count("A") == 2:
            return "Two Pairs", b * 3
        return "Pair", b
    elif w.count("3") == 2:
        if w.count("4") == 2 or w.count("5") == 2 or w.count("6") == 2 or w.count("7") == 2 or \
                w.count("8") == 2 or w.count("9") == 2 or w.count("10") == 2 or w.count("J") == 2 or \
                w.count("Q") == 2 or w.count("K") == 2 or w.count("A") == 2:
            return "Two Pairs", b * 3
        return "Pair", b
    elif w.count("4") == 2:
        if w.count("5") == 2 or w.count("6") == 2 or w.count("7") == 2 or w.count("8") == 2 or \
                w.count("9") == 2 or w.count("10") == 2 or w.count("J") == 2 or \
                w.count("Q") == 2 or w.count("K") == 2 or w.count("A") == 2:
            return "Two Pairs", b * 3
        return "Pair", b
    elif w.count("5") == 2:
        if w.count("6") == 2 or w.count("7") == 2 or w.count("8") == 2 or w.count("9") == 2 or w.count("10") == 2 or \
                w.count("J") == 2 or w.count("Q") == 2 or w.count("K") == 2 or w.count("A") == 2:
            return "Two Pairs", b * 3
        return "Pair", b
    elif w.count("6") == 2:
        if w.count("7") == 2 or w.count("8") == 2 or w.count("9") == 2 or w.count("10") == 2 or w.count("J") == 2 or \
                w.count("Q") == 2 or w.count("K") == 2 or w.count("A") == 2:
            return "Two Pairs", b * 3
        return "Pair", b
    elif w.count("7") == 2:
        if w.count("8") == 2 or w.count("9") == 2 or w.count("10") == 2 or w.count("J") == 2 or \
                w.count("Q") == 2 or w.count("K") == 2 or w.count("A") == 2:
            return "Two Pairs", b * 3
        return "Pair", b
    elif w.count("8") == 2:
        if w.count("9") == 2 or w.count("10") == 2 or w.count("J") == 2 or \
                w.count("Q") == 2 or w.count("K") == 2 or w.count("A") == 2:
            return "Two Pairs", b * 3
        return "Pair", b
    elif w.count("9") == 2:
        if w.count("10") == 2 or w.count("J") == 2 or w.count("Q") == 2 or w.count("K") == 2 or w.count("A") == 2:
            return "Two Pairs", b * 3
        return "Pair", b
    elif w.count("10") == 2:
        if w.count("J") == 2 or w.count("Q") == 2 or w.count("K") == 2 or w.count("A") == 2:
            return "Two Pairs", b * 3
        return "Pair", b
    elif w.count("J") == 2:
        if w.count("Q") == 2 or w.count("K") == 2 or w.count("A") == 2:
            return "Two Pairs", b * 3
        return "High Pair", b * 2
    elif w.count("Q") == 2:
        if w.count("K") == 2 or w.count("A") == 2:
            return "Two Pairs", b * 3
        return "High Pair", b * 2
    elif w.count("K") == 2:
        if w.count("A") == 2:
            return "Two Pairs", b * 3
        return "High Pair", b * 2
    elif w.count("A") == 2:
        return "High Pair", b * 2
    else:
        return "Sorry", 0


def extra_cards(e):
    if "2" in e:
        return 1
    elif "3" in e:
        return 2
    elif "4" in e:
        return 3
    elif "5" in e:
        return 4
    elif "6" in e:
        return 5
    elif "7" in e:
        return 6
    elif "8" in e:
        return 7
    elif "9" in e:
        return 8
    elif "10" in e:
        return 9
    elif "J" in e:
        return 10
    elif "Q" in e:
        return 11
    elif "K" in e:
        return 12
    else:
        return 13


def double(card1, card2, cred):
    if card1 > card2:
        cred *= 2
        return cred
    elif card1 == card2:
        return cred
    else:
        cred *= 0
        return cred


def deck():
    ranks = "2", "3", "4", "5",  "6", "7", "8", "9", "10", "J", "Q", "K", "A"
    suits = "\u2660", "\u2661", "\u2662", "\u2663"
    cards_deck = []
    for suit in suits:
        for rank in ranks:
            cards_deck.append(rank + suit)
    random.shuffle(cards_deck)
    return cards_deck


score = 0
dollars = 2000
print("\n You have 2000$")
while 0 < dollars < 1000000:
    score += 1
    bet = int(input(f"\nThe {score} deal. Your bet: "))
    if dollars > bet != 0:
        dollars -= bet
    else:
        bet = dollars
        dollars = 0
    cards = deck()
    deal = []
    for i in range(5):
        deal.append(cards.pop())
    print("\n" + " ".join(deal))
    game = input("Throw all away - 0\nDiscard some - 3\nHold - Enter\nYour choice: ")
    if game == "3":
        for i in range(5):
            if input(deal[i] + "  Hold - Enter, Throw away - 3  ") == "3":
                deal.pop(i)
                deal.insert(i, cards.pop())
    elif game == "0":
        deal.clear()
        for i in range(5):
            deal.append(cards.pop())
    hand, credit = win(" ".join(deal), bet)
    print(" ".join(deal), "----", hand, "%d$ won" % credit)
    if credit > 0:
        if input("Extra game - 3, new deal - Enter  ") == "3":
            cards = deck()
            c1 = []
            c2 = []
            c1.append(cards.pop())
            print(c1[-1], "vs. ?")
            while input("Double - 3, take money - Enter  ") == "3":
                c2.append(cards.pop())
                credit = double(extra_cards(c1[-1]), extra_cards(c2[-1]), credit)
                print(c1[-1], "vs.", c2[-1], "---- %d$" % credit)
                if credit > 0:
                    cards = deck()
                    c1.append(cards.pop())
                    print(c1[-1], "vs. ?")
                else:
                    break
    dollars += credit
    print("\n You have %d$" % dollars)
else:
    if dollars == 0:
        print("\n\n            GAME OVER")
    else:
        print(f"Congratulations! You have reached one million on the {score} deal.")
        name = input("Enter your name: ")
        while not name.isalnum() or len(name) > 6:
            name = input("Name can contain letters or numbers and must be less than 7 characters.\nEnter your name: ")
        leaders_list = [f". {name} --- score {score} --- dollars {dollars}$ --- "
                        f"{datetime.datetime.now().replace(microsecond=0)}\n"]
        try:
            leaderboard_file = open("leaderboard.txt", "r")
        except FileNotFoundError:
            leaderboard_file = open("leaderboard.txt", "w+")
        with leaderboard_file:
            digits = 1
            leader_line = leaderboard_file.readline()[len(str(digits)):]
            while leader_line:
                digits += 1
                leaders_list.append(leader_line)
                leader_line = leaderboard_file.readline()[len(str(digits)):]
        leaders_dict1 = []
        for i in leaders_list:
            leaders_dict1.append(i.replace('. ', '{".": "'))
        leaders_dict2 = []
        for i in leaders_dict1:
            leaders_dict2.append(i.replace(" --- score", '", "score":'))
        leaders_dict3 = []
        for i in leaders_dict2:
            leaders_dict3.append(i.replace(" --- dollars", ', "dollars":'))
        leaders_dict4 = []
        for i in leaders_dict3:
            leaders_dict4.append(i.replace("$ --- ", ', "-": "'))
        leaders_dict5 = []
        for i in leaders_dict4:
            leaders_dict5.append(i.replace("\n", '"}'))
        leaders_dict = []
        for i in leaders_dict5:
            leaders_dict.append(eval(i))
        leaders_dict.sort(key=lambda x: x["-"])
        leaders_dict.sort(key=lambda x: x["dollars"], reverse=True)
        leaders_dict.sort(key=lambda x: x["score"])
        leaders_str1 = []
        for i in leaders_dict:
            leaders_str1.append(str(i).replace("'}", "\n"))
        leaders_str2 = []
        for i in leaders_str1:
            leaders_str2.append(i.replace("{'.': '", ". "))
        leaders_str3 = []
        for i in leaders_str2:
            leaders_str3.append(i.replace("', 'score': ", " --- score "))
        leaders_str4 = []
        for i in leaders_str3:
            leaders_str4.append(i.replace(", 'dollars': ", " --- dollars "))
        leaders_str5 = []
        for i in leaders_str4:
            leaders_str5.append(i.replace(", '-': '", "$ --- "))
        leaders_numbered = []
        for i, j in enumerate(leaders_str5, 1):
            leaders_numbered.append(str(i) + j)
        leaderboard_actual = []
        for i in leaders_numbered:
            leaderboard_actual.append("".join(i))
        print("\n         LEADERBOARD\n\n" + "".join(leaderboard_actual))
        leaderboard_file = open("leaderboard.txt", "w")
        with leaderboard_file:
            leaderboard_file.writelines(leaderboard_actual)
