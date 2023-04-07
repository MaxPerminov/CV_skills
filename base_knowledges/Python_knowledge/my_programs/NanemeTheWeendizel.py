# This nick-creator is a program-joke, that creates up to 4 words length nick from inputted letters.


import random


def nick(x):
    if x == "Gs":
        return "Garmonicus"
    elif x == "q":
        return "Quantoparamucho"
    elif x == "w":
        return "Weendizel"
    elif x == "e":
        return "Endrew"
    elif x == "r":
        return "Romario"
    elif x == "t":
        return "2PAC"
    elif x == "y":
        return "Yussuf"
    elif x == "u":
        return "Unbelivable"
    elif x == "i":
        return "Igrek"
    elif x == "o":
        return "Optimus"
    elif x == "p":
        return "Tomas"
    elif x == "a":
        return "Aquaman"
    elif x == "s":
        return "Simpatico"
    elif x == "d":
        return "Devisious"
    elif x == "f":
        return "Fantom"
    elif x == "g":
        return "Gangster"
    elif x == "h":
        return "Hilarious"
    elif x == "j":
        return "DJ"
    elif x == "k":
        return "Kevin"
    elif x == "l":
        return "Lovemachine"
    elif x == "z":
        return "Z"
    elif x == "x":
        return "Xanavi"
    elif x == "c":
        return "CJ"
    elif x == "v":
        return "Ivan"
    elif x == "b":
        return "Barmen"
    elif x == "n":
        return "Ninja"
    elif x == "m":
        return "Mister"


def nick_con(y):
    if len(y) == 1:
        return y[0]
    else:
        return y[0] + nick_con(y[1:])


def first_let(z):
    if z > 0:
        return random.randint(0, 1)


a = input("Enter your name: ").lower()
b = []
for i in a:
    if i == "q":
        b.append("q")
    elif i == "w":
        b.append("w")
    elif i == "r":
        b.append("r")
    elif i == "t":
        b.append("t")
    elif i == "p":
        b.append("p")
    elif i == "s":
        b.append("s")
    elif i == "d":
        b.append("d")
    elif i == "f":
        b.append("f")
    elif i == "g":
        b.append("g")
    elif i == "h":
        b.append("h")
    elif i == "j":
        b.append("j")
    elif i == "k":
        b.append("k")
    elif i == "l":
        b.append("l")
    elif i == "z":
        b.append("z")
    elif i == "x":
        b.append("x")
    elif i == "c":
        b.append("c")
    elif i == "v":
        b.append("v")
    elif i == "b":
        b.append("b")
    elif i == "n":
        b.append("n")
    elif i == "m":
        b.append("m")
random.shuffle(b)
c = []
for i1 in a:
    if i1 == "e":
        c.append("e")
    elif i1 == "y":
        c.append("y")
    elif i1 == "u":
        c.append("u")
    elif i1 == "i":
        c.append("i")
    elif i1 == "o":
        c.append("o")
    elif i1 == "a":
        c.append("a")
random.shuffle(c)
d = []
if len(b) == len(c):
    d.append("Gs")
while len(b) != len(c):
    if len(b) > len(c):
        d.append(b.pop())
    elif len(b) < len(c):
        d.append(c.pop())
if first_let(1) == 0:
    e = "".join(nick_con(list((zip(b, c)))))
else:
    e = "".join(nick_con(list((zip(c, b)))))
nck = ["The"]
for i2 in d:
    nck.append(nick(i2))
    if nck.count("Quantoparamucho") == 2:
        nck.remove("Quantoparamucho")
        nck.append("Queen")
    if nck.count("Queen") == 2:
        nck.remove("Queen")
        nck.append("q7")
    if nck.count("Weendizel") == 2:
        nck.remove("Weendizel")
        nck.append("Waha")
    if nck.count("Waha") == 2:
        nck.remove("Waha")
        nck.append("Wahtang")
    if nck.count("Endrew") == 2:
        nck.remove("Endrew")
        nck.append("Endroid")
    if nck.count("Endroid") == 2:
        nck.remove("Endroid")
        nck.append("Evgen")
    if nck.count("Romario") == 2:
        nck.remove("Romario")
        nck.append("Respidont")
    if nck.count("Respidont") == 2:
        nck.remove("Respidont")
        nck.append("Reebok")
    if nck.count("2PAC") == 2:
        nck.remove("2PAC")
        nck.append("Tanya")
    if nck.count("Tanya") == 2:
        nck.remove("Tanya")
        nck.append("Terminator")
    if nck.count("Yussuf") == 2:
        nck.remove("Yussuf")
        nck.append("Yamaha")
    if nck.count("Yamaha") == 2:
        nck.remove("Yamaha")
        nck.append("Akula")
    if nck.count("Unbelivable") == 2:
        nck.remove("Unbelivable")
        nck.append("Unique")
    if nck.count("Unique") == 2:
        nck.remove("Unique")
        nck.append("Undelibavle")
    if nck.count("Igrek") == 2:
        nck.remove("Igrek")
        nck.append("Saddam")
    if nck.count("Saddam") == 2:
        nck.remove("Saddam")
        nck.append("Gusein")
    if nck.count("Optimus") == 2:
        nck.remove("Optimus")
        nck.append("Orlando")
    if nck.count("Orlando") == 2:
        nck.remove("Orlando")
        nck.append("O.B.")
    if nck.count("Tomas") == 2:
        nck.remove("Tomas")
        nck.append("Python")
    if nck.count("Python") == 2:
        nck.remove("Python")
        nck.append("PRIME")
    if nck.count("Aquaman") == 2:
        nck.remove("Aquaman")
        nck.append("Angelina")
    if nck.count("Angelina") == 2:
        nck.remove("Angelina")
        nck.append("Abracadabra")
    if nck.count("Simpatico") == 2:
        nck.remove("Simpatico")
        nck.append("Santiago")
    if nck.count("Santiago") == 2:
        nck.remove("Santiago")
        nck.append("SONY")
    if nck.count("Devisious") == 2:
        nck.remove("Devisious")
        nck.append("D'Artanian")
    if nck.count("D'Artanian") == 2:
        nck.remove("D'Artanian")
        nck.append("Dangerous")
    if nck.count("Fantom") == 2:
        nck.remove("Fantom")
        nck.append("50CENT")
    if nck.count("50CENT") == 2:
        nck.remove("50CENT")
        nck.append("F-16")
    if nck.count("Gangster") == 2:
        nck.remove("Gangster")
        nck.append("Gorgeous")
    if nck.count("Gorgeous") == 2:
        nck.remove("Gorgeous")
        nck.append("Givi")
    if nck.count("Hilarious") == 2:
        nck.remove("Hilarious")
        nck.append("Hilary Clinton")
    if nck.count("Hilary Clinton") == 2:
        nck.remove("Hilary Clinton")
        nck.append("Hector")
    if nck.count("DJ") == 2:
        nck.remove("DJ")
        nck.append("Tiesto")
    if nck.count("Tiesto") == 2:
        nck.remove("Tiesto")
        nck.append("MC")
    if nck.count("Kevin") == 2:
        nck.remove("Kevin")
        nck.append("Klein")
    if nck.count("Klein") == 2:
        nck.remove("Klein")
        nck.append("Killer")
    if nck.count("Lovemachine") == 2:
        nck.remove("Lovemachine")
        nck.append("Leonardo")
    if nck.count("Leonardo") == 2:
        nck.remove("Leonardo")
        nck.append("Lucky")
    if nck.count("Z") == 2:
        nck.remove("Z")
        nck.append("Fairlady")
    if nck.count("Fairlady") == 2:
        nck.remove("Fairlady")
        nck.append("Datsun")
    if nck.count("Xanavi") == 2:
        nck.remove("Xanavi")
        nck.append("Xerox")
    if nck.count("Xerox") == 2:
        nck.remove("Xerox")
        nck.append("Xena")
    if nck.count("CJ") == 2:
        nck.remove("CJ")
        nck.append("Celular")
    if nck.count("Celular") == 2:
        nck.remove("Celular")
        nck.append("Clarissa")
    if nck.count("Ivan") == 2:
        nck.remove("Ivan")
        nck.append("Vanessa")
    if nck.count("Vanessa") == 2:
        nck.remove("Vanessa")
        nck.append("Vito")
    if nck.count("Barmen") == 2:
        nck.remove("Barmen")
        nck.append("Boris")
    if nck.count("Boris") == 2:
        nck.remove("Boris")
        nck.append("Baskerville")
    if nck.count("Ninja") == 2:
        nck.remove("Ninja")
        nck.append("Nitro")
    if nck.count("Nitro") == 2:
        nck.remove("Nitro")
        nck.append("Nissan")
    if nck.count("Mister") == 2:
        nck.remove("Mister")
        nck.append("Misterious")
    if nck.count("Misterious") == 2:
        nck.remove("Misterious")
        nck.append("Master")
if len(nck) > 4:
    nck.insert(3, nck.pop(0))
print("your new name is", e.capitalize() + ",", " ".join(nck))
