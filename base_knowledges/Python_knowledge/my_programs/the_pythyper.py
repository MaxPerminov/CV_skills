# This game trains to type fast. It is counting time and errors, while user is executing letter patterns
# (nums patterns aren't counted - they are warming up the player)
# Result appears as an output and becomes available in the Clipboard.
# To type fast:
# - you must not look at keyboard;
# - you must type from the starting position:
#       left pinkie = a;
#       left ring finger = s;
#       left middle finger = d;
#       left index finger = f;
#       right pinkie = ;;
#       right ring finger = l;
#       right middle finger = k;
#       right index finger = j.
# - you must type with 10 fingers:
#       left pinkie = `,1,q,a,z,Shift,Tab,CapsLock;
#       left ring finger = 2,w,s,x;
#       left middle finger = 3,4,e,d,c;
#       left index finger = 5,6,r,t,f,g,v,b;
#       right pinkie = Backspace,Enter,Shift,=,],\,/,-,[,',p,;;
#       right ring finger = 0,o,l,.;
#       right middle finger = 9,i,k,,;
#       right index finger = 7,8,y,u,h,j,b,n,m;
#       thumbs = space key.


import time
import pyperclip
# to Install on Windows, in terminal use command:
# pip install pyperclip (to get a result available in the Clipboard).
import random


def typer(pats, efforts, errors=0):
    for pattern in pats:
        n = 0
        while n != efforts:
            question = input(f"  {efforts - n} '{pattern}' to do: ")
            if question == pattern:
                print("+1".rjust(20))
                n += 1
            else:
                n = 0
                errors += 1
                print("oops\n".rjust(24))
        else:
            print("done".rjust(23, "_"))
    return errors


def main():
    patterns = [
                "we", "wr", "wa", "ws",
                "po", "pi", "pu", "py", "p:", "pl", "ph", "p/", "p.", "p,",

                "eq", "er", "et", "ea", "es", "ed", "ef", "eg", "ex", "ec", "ev", "eb",
                "op", "ou", "o:", "ol", "ok", "o/", "o.", "o,", "om", "on", "o'",

                "re", "rt", "ra", "rs", "rd", "rg", "rc", "rv", "rb",
                "ip", "io", "im", "il", "ik", "in",

                "tw", "te", "tr", "ta", "ts",
                "up", "uy", "u:", "ul", "uk", "uj", "uh", "u/", "u.", "u,", "um", "un",

                "aq", "aw", "ae", "ar", "at", "as", "ad", "af", "ag", "az", "ax", "ac", "av", "ab", "a2", "a1",
                "yp", "yo", "yi", "yu", "y:", "yj", "y.", "y,", "y/",

                "sq", "sw", "se", "sr", "st", "sa", "sd", "sc", "sv", "sb",
                "lp", "lo", "li", "lu", "l:", "l/", "l.", "l,", "ln", "l9", "l0", "l-", "l=",

                "dw", "de", "dr", "da", "ds", "dv", "d3", "d4",
                "ko", "ki", "ku", "k:", "kl", "k/", "k.", "k,",

                "fe", "fr", "ft", "fa", "fs", "f6", "f5",
                "jh", "j7", "j8", "jo", "ji", "jy",

                "ge", "gr", "gt", "ga", "gs", "gv",
                "ho", "hi", "hu",

                "ze", "za", "xe", "xr", "xt", "xc", "ce", "cr", "ct", "ca", "cd",
                "mp", "mo", "mi", "mu", "my", "m:", "ml", "m/", "m.", "m,", "mn",

                "ve", "va", "vs", "vr", "be", "br", "ba", "bs",
                "np", "no", "ni",  "nu", "n:", "n/", "n.", "n,"
    ]
    patterns_nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] * 3
    random.shuffle(patterns)
    random.shuffle(patterns_nums)
    typer(patterns_nums, 1)
    start = time.time()
    res = typer(patterns, 3)
    timer = round(time.time() - start)
    finish = f"    mistakes: {res} time:{timer // 60} min {timer % 60} sec!"
    pyperclip.copy(finish)
    print(finish)
    time.sleep(3)
    return


main()
