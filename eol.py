#Ease of Life v0.1

from math import sqrt, gcd
import random

def slope(x1, x2, y1, y2):
    if x1==x2:
        return "Undefined."
    else:
        return (y2-y1)/(x2-x1)

def fquad(a, b, c):
    if a!=0:
        D = (b**2-4*a*c)
        if D>=0:
            return (-b + sqrt(D))/(2*a), (-b - sqrt(D))/(2*a)
        else:
            return "No real roots exist."
    else:
        if b==0 and c==0:
            return "Infinite solutions."
        elif b==0 and c!=0:
            return "No solutions."
        else:
            return -c/b

def fcube(a, b, c, d, start = -100, end = 100, step = 0.1, t = 1e-4):
    roots = list()

    x = start
    while x<=end:
        y = a*x**3+b*x**2+c*x+d

        if abs(y)<t:
            roots.append(x)
        else:
            pass
    x+=step

    return roots

def rev(x):
    if x.isalpha():
        return x[::-1]
    else:
        print("Type error: enter string as argument.")

def lcm(*nums):
    result = nums[0]

    for n in nums[1:]:
        result = abs(result*n)//gcd(result, n)
    return result

def add(*num):
    nums = 0

    for n in nums:
        sum = 0+n
    return sum

def numpull(string):
    s = ""
    nums = []
    current = ""

    for i in string:
        if i.isdigit():
            current+=i
        else:
            if current:
                nums.append(int(current))
                current=""
            s+=i
            
    if current:
        nums.append(int(current))
    return s, nums

def flatten(lst):
    l = list()

    for i in lst:
        for j in i:
            l.append(j)
    
    return l

def scramble(str):
    scr = list(str)
    random.shuffle(scr)
    wd = ""
    for i in scr:
        wd+=i
    return wd
        

def encrypt(x):
    wd = ""
    shift = 1
    for i in x:
        new=chr(ord(i)+shift)
        wd+=new
        shift+=1
    return wd

def decrypt(x):
    wd = ""
    for i, ch in enumerate(x):
        wd+=chr(ord(ch)-(i+1))
    return wd

def prank():
    error = ["compiler error: system gave up and f***ing died", "value error: value not found", "confidence error: brain cells lacking", "type error: cannot perform operation", "name error: variable not found", "code error: mood swings detected in runtime", "logic error: Python is ashamed"]
    random.choice(error)

def roast():
    roast = ["Confidence lacking", "Looking like a G-Wiz at 4:45 AM on a sunny Tuesday", "Automatic transmission detected", "be ashamed lol", "ARE YOU NOT ENTERTAINED?!", "A squirrel attempted to debug your Python and gave up on life choices."]
    random.shuffle(roast)
    return roast[random.randint(0, len(roast)-1)]

def slugify(txt):
    ln = len(txt)
    final = ""
    txt1 = list(txt)
    for i in range(0, ln):
        if txt1[i]==" ":
            txt1[i]="-"
            final+=txt1[i]
        else:
            final+=txt1[i]
    return final

def wcount(string):
    return len(string.split())

def morse(text):
    text = text.upper()
    x = ""
    morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
        }
    
    for i in text:
        if i.isalnum():
            x=x+morse[i]+" "
        elif i==" ":
            x+=" / "
    
    return x

def revmorse(text):
    text = text.upper()
    words = text.split(" / ")
    wd = "" 
    morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
        }
    reverse_morse = {v: k for k, v in morse.items()}

    for word in words:
        letters = word.split()
    for code in letters:
        result += reverse_morse[code]
        result += " "

    return result

def avg(*nums):
    average = 0
    for n in nums:
        average+=n
    average/=len(nums)

    return average