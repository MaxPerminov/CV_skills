# This program converts Latin letters to Ukrainian.
# To get Ukrainian letters from Latin, it's necessarily to make input
# and press Enter. Ukrainian letters appear as an output and become available
# in the Clipboard.

# а = a
# б = b
# в = v
# г = g
# д = d
# е = e
# є = ye
# ж = zh
# з = z
# и = y
# і = i
# ї = yi
# й = j
# к = k
# л = l
# м = m
# н = n
# о = o
# п = o
# р = r
# с = s
# т = t
# у = u
# ф = f
# х = h
# ц = ts
# ч = ch
# ш = w
# щ = q
# ь = /
# ю = yu
# я = ya
# ) = x
# ( = c
# ы = [

# to write capital letters, enter ` before the letter.
# also, such symbols are provided:  " ", "'", ".",  ",", ":", "?", "`", "-"


import pyperclip
# to Install on Windows, in terminal use command:
# pip install pyperclip (to get a result available in the Clipboard).


def ts(content):
    text = ""
    if "ts" in content:
        a_ts = content.split("ts")
        b = "ц".join(a_ts)
        text += b
    else:
        return content
    return text


def yi(content):
    text = ""
    if "yi" in content:
        a_yi = content.split("yi")
        b = "ї".join(a_yi)
        text += b
    else:
        return content
    return text


def zh(content):
    text = ""
    if "zh" in content:
        a_zh = content.split("zh")
        b = "ж".join(a_zh)
        text += b
    else:
        return content
    return text


def ye(content):
    text = ""
    if "ye" in content:
        a_ye = content.split("ye")
        b = "є".join(a_ye)
        text += b
    else:
        return content
    return text


def ya(content):
    text = ""
    if "ya" in content:
        a_ya = content.split("ya")
        b = "я".join(a_ya)
        text += b
    else:
        return content
    return text


def ch(content):
    text = ""
    if "ch" in content:
        a_ch = content.split("ch")
        b = "ч".join(a_ch)
        text += b
    else:
        return content
    return text


def yu(content):
    text = ""
    if "yu" in content:
        a_yu = content.split("yu")
        b = "ю".join(a_yu)
        text += b
    else:
        return content
    return text


def transliteration(content):
    simple = ""
    for x in content:
        if x == "j":
            simple += "й"
        elif x == "ц":
            simple += "ц"
        elif x == "u":
            simple += "у"
        elif x == "k":
            simple += "к"
        elif x == "e":
            simple += "е"
        elif x == "n":
            simple += "н"
        elif x == "g":
            simple += "г"
        elif x == "w":
            simple += "ш"
        elif x == "q":
            simple += "щ"
        elif x == "z":
            simple += "з"
        elif x == "h":
            simple += "х"
        elif x == "ї":
            simple += "ї"
        elif x == "f":
            simple += "ф"
        elif x == "i":
            simple += "і"
        elif x == "v":
            simple += "в"
        elif x == "a":
            simple += "а"
        elif x == "p":
            simple += "п"
        elif x == "r":
            simple += "р"
        elif x == "o":
            simple += "о"
        elif x == "l":
            simple += "л"
        elif x == "d":
            simple += "д"
        elif x == "ж":
            simple += "ж"
        elif x == "є":
            simple += "є"
        elif x == "я":
            simple += "я"
        elif x == "ч":
            simple += "ч"
        elif x == "s":
            simple += "с"
        elif x == "m":
            simple += "м"
        elif x == "y":
            simple += "и"
        elif x == "t":
            simple += "т"
        elif x == "/":
            simple += "ь"
        elif x == "b":
            simple += "б"
        elif x == "ю":
            simple += "ю"
        elif x == " ":
            simple += " "
        elif x == "'":
            simple += "'"
        elif x == ".":
            simple += "."
        elif x == ",":
            simple += ","
        elif x == ":":
            simple += ":"
        elif x == "x":
            simple += ")"
        elif x == "c":
            simple += "("
        elif x == "?":
            simple += "?"
        elif x == "`":
            simple += "`"
        elif x == "-":
            simple += "-"
        elif x == "[":
            simple += "ы"
    return simple


def big(content):
    text = ""
    if "`" in content:
        a_big = content.split("`")
        text += a_big[0]
        for i in a_big[1:]:
            text += " "
            text += i.capitalize()
    else:
        return content
    return text


while True:
    a = big(transliteration(yu(ch(ya(ye(zh(yi(ts(input("    "))))))))))
    if a == "е)іт":
        print("    Bye!")
        break
    else:
        pyperclip.copy(a)
        print(f"    {a}")
