#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

"""
_________                                                   ______              
__  ____/_____________________________________  ________ ______  /______________
_  /    __  ___/  __ \_  ___/_  ___/_  __ \  / / /_  __ `__ \_  __ \  _ \_  ___/
/ /___  _  /   / /_/ /(__  )_(__  )_  / / / /_/ /_  / / / / /  /_/ /  __/  /    
\____/  /_/    \____//____/ /____/ /_/ /_/\__,_/ /_/ /_/ /_//_.___/\___//_/     
                                                                                
A collection of functions which may be of use when solving crossnumber puzzles.
Author: Adam Vellender
dev@vellender.com
"""

"""
GENERATORS OF TUPLES OF INTEGERS WITH CERTAIN PROPERTIES
"""    

######## Primes ########
def primes(n):
    """Primes < n"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    s = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if s[i]:
            s[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return tuple([2] + [i for i in range(3,n,2) if s[i]])

def pol(n):
    """Primes of length n"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    return tuple(filter(lambda x: x>=10**(int(n)-1), primes(10**n)))

######## Powers ########   
def sol(n):
    """Squares of length n"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    import numpy as np
    return tuple([a**2 for a in range(int(np.ceil(np.sqrt(10**(n-1)))),int(np.ceil(np.sqrt(10**n))))])

def col(n):
    """Cubes of length n"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    import numpy as np
    return tuple([a**3 for a in range(int(np.ceil(np.cbrt(10**(n-1)))),int(np.ceil(np.cbrt(10**n))))])

######## Triangular numbers ########
def tol(n):
    """Triangular numbers of length n"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    import numpy as np
    return tuple([int(float(n*(n+1))/2) for n in range(int(np.ceil(.5*(-1+np.sqrt(1+8*10**(n-1))))),int(np.ceil(.5*(-1+np.sqrt(1+8*10**n)))))])

######## Integers ########
def iol(n):
    """All integers of length n"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    return tuple(range(10**(n-1),10**n))

######## Fibonacci numbers ########
def _fib(n):
    """Private function: returns (F(n), F(n+1)) (fast algorithm)"""
    if n==0:
        return (0,1)
    else:
        x,y=_fib(n//2)
        l=x*(2*y-x)
        m=x*x+y*y
        if n%2==0:
            return (l,m)
        else:
            return (m,l+m)
        
def _fibonacci_nth(n):
    """Private function: nth digit of Fibonacci sequence"""
    if n<0:
        raise ValueError("Argument cannot be negative")
    return _fib(n)[0]

def fibonacci(n):
    """Fibonacci numbers less than n"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    l=[]
    a=2
    while True:
        if _fibonacci_nth(a)<n:
            l.append(_fibonacci_nth(a))
            a+=1
        else:
            break
    return tuple(l)

def fol(n):
    """Fibonacci numbers of length n"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    l=[]
    a=2
    while True:
        if _fibonacci_nth(a)<10**n:
            if _fibonacci_nth(a)>=10**(n-1):
                l.append(_fibonacci_nth(a))
            a+=1
        else:
            break
    return tuple(l)

def friendlyol(n):
    """Friendly (divisible by its digit sum) numbers of length n"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    l=[]
    for a in range(10**(n-1),10**n):
        if isFriendly(a):
            l.append(a)
    return tuple(l)


"""
******* FUNCTIONS REGARDING DIGITS *******
(e.g. digit sum, product, anagram, length)
"""

def digitSum(n):
    """Digit sum"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    return sum([int(a) for a in str(n)])    
  
def digitProduct(n):
    """Digit product"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    a = 1
    for b in str(n):
        a = a * int(b)
    return a

def isAnagram(m,n):
    """Takes two numbers (or words) as inputs, returns True only if they're anagrams of each other"""
    if sorted(str(m))==sorted(str(n)):
        return True
    else:
        return False
    
def nthDigit(n,d):
    """d-th Digit of an integer n"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    return int(str(n)[d-1])

def match(n,a,m,b):
    if nthDigit(n,a)==nthDigit(m,b):
        return True
    else:
        return False

def isLength(n,l):
    """Returns True only if n is an integer of length l"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    if len(str(n))==l:
        return True
    else:
        return False
    
def isDistinct(l):
    """Returns True only if the list has no duplicates"""
    if len(l)==len(set(l)):
        return True
    else:
        return False
    
def rev(n):
    """Reverse an integer"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    return int(str(n)[::-1])    

def isCosy(n):
    """A cosy number's largest digit is the sum of the two smaller ones and allows the case where the largest digit is repeated (e.g. 990)"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    if sorted([int(a) for a in str(n)])[len(str(n))-1]==sum(sorted([int(a) for a in str(n)])[:-1]):#Allows any number of digits, not just 3.
        return True
    else:
        return False
    
def isFriendly(n):
    """A ‘friendly’ number is divisible by its digit sum"""
    if not (type(n)==int and n>0):
        raise ValueError('Argument must be a positive integer')
    if n%digitSum(n)==0:
        return True
    else:
        return False
    
def lcm(x,y):
   """Lowest common multiple"""
   if not (type(x)==int and x>0 and type(y)==int and y>0):
        raise ValueError('Arguments must be positive integers')
   if x>y:#choose the greater
       g=x
   else:
       g=y
   while(True):
       if g%x==0 and g%y==0:
           lcm=g
           break
       g+=1
   return lcm    

def gcf(x,y):
    if not (type(x)==int and x>0 and type(y)==int and y>0):
        raise ValueError('Arguments must be positive integers')
    """Greatest common factor"""
    while(y):
       x,y=y,x%y
    return x

"""
LETTER TO NUMBER TRANSLATION
"""
def singleNumToLetter(n):
    """Takes a single natural number less than 26 and returns correspondingly 
    positioned letter (e.g. numToLetter(5) returns E. Returns "?" if input>26"""
    if 1 <= n <= 26:
        return chr(64 + n) #'A' is ASCII 65
    else:
        return "?"
    
def numsToLetters(n,mod=26):
    """Takes a STRING of integers e.g. 092905, splits into 09 03 05 and returns
    correspondingly positioned letters modulo "mod" (default 26). 
    Needs a string of even length as input"""
    if len(str(n))%2==1:
        return ""
    else: 
        out=[]
        cursor=0
        for i in range(0, len(str(n)), 2):
            pair = int(str(n)[i:i+2])
            if pair%mod!=0:
                out.append(pair%mod)
            else:
                out.append(mod)#this means out is between 01 and mod (inclusive) rather than between 00 and mod-1
        return "".join([singleNumToLetter(a) for a in out])
    
def singleLetterToNum(s):
    """Takes a string s, outputs a STRING of their positions"""   
    # Convert the string to uppercase to handle both uppercase and lowercase letters.
    s = s.upper()
   
    # Initialize an empty list to store the results.
    result = []  
    # Iterate over each character in the string.
    for char in s:
        if 'A' <= char <= 'Z':
            # Calculate the position in the alphabet (1 to 26) and format it as a two-digit string.
            position = str(ord(char) - ord('A') + 1).zfill(2)
            result.append(position)
    
    # Join the list of positions into a single string and return it.
    return ''.join(result)

def lettersToNums(s,spaced=False):
    out=""
    for a in s:
        out+=singleLetterToNum(a)
        if spaced:
            out+=" "
    if spaced:
        return out[:-1]
    else:    
        return out

"""
FACTORISING
"""
from sympy.ntheory import factorint as primeFactorisation

def pf(n):
    """List of prime factors"""
    from sympy.ntheory import primefactors
    return tuple(primefactors(n))

def factors(n):
    from sympy import divisors
    return tuple(divisors(n))


"""
******* FUNCTIONS FOR NOTE-TAKING *******
"""    
def conclusion(m):
    from termcolor import colored
    print(colored('***CONCLUSION***: ', 'red'), colored(str(m), 'blue'))

def digits(m):
    from termcolor import colored
    print(colored('***DIGITS***: ', 'red'), colored(str(m), 'blue'))
    
def assumption(m):
    from termcolor import colored
    print(colored('***ASSUMPTION***: ', 'red'), colored(str(m), 'blue'))
    
def consider(m):
    from termcolor import colored
    print(colored('***CONSIDER***: ', 'green'), colored(str(m), 'green'))
    
def note(m):
    from termcolor import colored
    print(colored('***NOTE***: ', 'green'), colored(str(m), 'green'))    
    
def contradiction(m):
    from termcolor import colored
    print(colored('***CONTRADICTION***: ', 'red'), colored(str(m), 'blue'))        

def msg(kind,m):
    from termcolor import colored
    print(colored('***'+kind.upper()+'***: ', 'red'), colored(str(m), 'blue'))        