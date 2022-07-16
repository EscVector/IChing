#!/usr/bin/env python3

# Heads is True - Value of three to any coins that are heads 
# Tails is False - Value of two to any coins that are tails. 

import random

def flipCoin():
    random.seed
    coin = random.choice([True,False])
    # print(coin)
    if coin==True:
        return 3
    else:
        return 2

def toss():
    line = ""
    coin1 = flipCoin()
    coin2 = flipCoin()
    coin3 = flipCoin()

    result = coin1+coin2+coin3
    if result in (6,8):
       line = "-------"
    else: 
        line = "--- ---"
    return line

for i in range (0,6):
    hex1Line1 = toss()
    hex1Line2 = toss()
    hex1Line3 = toss()
    hex1Line4 = toss()
    hex1Line5 = toss()
    hex1Line6 = toss()

    hex2Line1 = toss()
    hex2Line2 = toss()
    hex2Line3 = toss()
    hex2Line4 = toss()
    hex2Line5 = toss()
    hex2Line6 = toss()

print ('Your I Ching Hexagram Results' + '\n\n' +       
       hex1Line6 + ' | ' + hex2Line6 +'\n' +
       hex1Line5 + ' | ' + hex2Line5 +'\n' +
       hex1Line4 + ' | ' + hex2Line4 +'\n' +
       hex1Line3 + ' | ' + hex2Line3 +'\n' + 
       hex1Line2 + ' | ' + hex2Line2 +'\n' +
       hex1Line1 + ' | ' + hex2Line1 +'\n')
