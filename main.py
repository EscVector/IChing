#!/usr/bin/env python3

# Heads is True - Value of three to any coins that are heads 
# Tails is False - Value of two to any coins that are tails. 

# https://aleadeum.com/2013/07/12/the-i-ching-random-numbers-and-why-you-are-doing-it-wrong/


import random
import sqlite3
from unittest import registerResult

connection = sqlite3.connect("IChing.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS answers (hexagram INTERGER,binary INTERGER, line6 INTERGER,line5 INTERGER,line4 INTERGER,line3 INTERGER, line2 INTERGER, line1 INTERGER, iching TEXT)")
cursor.execute("INSERT INTO answers VALUES (1,111111,1,1,1,1,1,1,'The Creative')")
cursor.execute("INSERT INTO answers VALUES (2,222222,2,2,2,2,2,2,'The Receptive')")
cursor.execute("INSERT INTO answers VALUES (3,212221,2,1,2,2,2,1,'Difficulty at the Beginning')")
cursor.execute("INSERT INTO answers VALUES (4,122212,1,2,2,2,1,2,'Youthful Folly')")
cursor.execute("INSERT INTO answers VALUES (5,212111,2,1,2,1,1,1,'Waiting (Nourishment)')")
cursor.execute("INSERT INTO answers VALUES (6,111212,1,1,1,2,1,2,'Conflict')")
cursor.execute("INSERT INTO answers VALUES (7,222212,2,2,2,2,1,2,'The Army')")
cursor.execute("INSERT INTO answers VALUES (8,212222,2,1,2,2,2,2,'Holding Together (Union)')")
cursor.execute("INSERT INTO answers VALUES (9,112111,1,1,2,1,1,1,'The Taming Power of the Small')")
cursor.execute("INSERT INTO answers VALUES (10,111211,1,1,1,2,1,1,'Treading (Conduct)')")
cursor.execute("INSERT INTO answers VALUES (11,222111,2,2,2,1,1,1,'Peace')")
cursor.execute("INSERT INTO answers VALUES (12,111222,1,1,1,2,2,2,'Standstill (Stagnation)')")
cursor.execute("INSERT INTO answers VALUES (13,111121,1,1,1,1,2,1,'Fellowship with Others')")
cursor.execute("INSERT INTO answers VALUES (14,121111,1,2,1,1,1,1,'Possession in Great Measure')")
cursor.execute("INSERT INTO answers VALUES (15,222122,2,2,2,1,2,2,'Modesty')")
cursor.execute("INSERT INTO answers VALUES (16,221222,2,2,1,2,2,2,'Enthusiasm')")
cursor.execute("INSERT INTO answers VALUES (17,211221,2,1,1,2,2,1,'Following')")
cursor.execute("INSERT INTO answers VALUES (18,122112,1,2,2,1,1,2,'Work on What has been Spoiled (Decay)')")
cursor.execute("INSERT INTO answers VALUES (19,222211,2,2,2,2,1,1,'Approach')")
cursor.execute("INSERT INTO answers VALUES (20,112222,1,1,2,2,2,2,'Contemplation')")
cursor.execute("INSERT INTO answers VALUES (21,121221,1,2,1,2,2,1,'Biting Through')")
cursor.execute("INSERT INTO answers VALUES (22,122121,1,2,2,1,2,1,'Grace')")
cursor.execute("INSERT INTO answers VALUES (23,122222,1,2,2,2,2,2,'Splitting Appart')")
cursor.execute("INSERT INTO answers VALUES (24,222221,2,2,2,2,2,1,'Return')")
cursor.execute("INSERT INTO answers VALUES (25,111221,1,1,1,2,2,1,'Innocense (The Unexpected)')")
cursor.execute("INSERT INTO answers VALUES (26,122111,1,2,2,1,1,1,'The Taming Power of the Great')")
cursor.execute("INSERT INTO answers VALUES (27,122221,1,2,2,2,2,1,'The Corners of the Mouth (Providing Nourishment)')")
cursor.execute("INSERT INTO answers VALUES (28,211112,2,1,1,1,1,2,'Preponderance of the Great')")
cursor.execute("INSERT INTO answers VALUES (29,212212,2,1,2,2,1,2,'The Abysmal (Water)')")
cursor.execute("INSERT INTO answers VALUES (30,121121,1,2,1,1,2,1,'The Clinging Fire')")
cursor.execute("INSERT INTO answers VALUES (31,211122,2,1,1,1,2,2,'Influence (Wooing)')")
cursor.execute("INSERT INTO answers VALUES (32,221112,2,2,1,1,1,2,'Duration')")
cursor.execute("INSERT INTO answers VALUES (33,111122,1,1,1,1,2,2,'Retreat')")
cursor.execute("INSERT INTO answers VALUES (34,221111,2,2,1,1,1,1,'The Power of the Great')")
cursor.execute("INSERT INTO answers VALUES (35,121222,1,2,1,2,2,2,'Progress')")
cursor.execute("INSERT INTO answers VALUES (36,222121,2,2,2,1,2,1,'Darkening of the Light')")
cursor.execute("INSERT INTO answers VALUES (37,112121,1,1,2,1,2,1,'The Family (The Clan)')")
cursor.execute("INSERT INTO answers VALUES (38,121211,1,2,1,2,1,1,'Opposition')")
cursor.execute("INSERT INTO answers VALUES (39,212122,2,1,2,1,2,2,'Obstruction')")
cursor.execute("INSERT INTO answers VALUES (40,221212,2,2,1,2,1,2,'Deliverance')")
cursor.execute("INSERT INTO answers VALUES (41,122211,1,2,2,2,1,1,'Decrease')")
cursor.execute("INSERT INTO answers VALUES (42,112221,1,1,2,2,2,1,'Increase')")
cursor.execute("INSERT INTO answers VALUES (43,211111,2,1,1,1,1,1,'Breakthrough (Resolutness)')")
cursor.execute("INSERT INTO answers VALUES (44,111112,1,1,1,1,1,2,'Coming to Meet')")
cursor.execute("INSERT INTO answers VALUES (45,211222,2,1,1,2,2,2,'Gather Together')")
cursor.execute("INSERT INTO answers VALUES (46,222112,2,2,2,1,1,2,'Pushing Upward')")
cursor.execute("INSERT INTO answers VALUES (47,211212,2,1,1,2,1,2,'Oppression (Exhaustion)')")
cursor.execute("INSERT INTO answers VALUES (48,212112,2,1,2,1,1,2,'The Well')")
cursor.execute("INSERT INTO answers VALUES (49,211121,2,1,1,1,2,1,'Revolution')")
cursor.execute("INSERT INTO answers VALUES (50,121112,1,2,1,1,1,2,'The Caldron')")
cursor.execute("INSERT INTO answers VALUES (51,221221,2,2,1,2,2,1,'The Arousing (Shock)')")
cursor.execute("INSERT INTO answers VALUES (52,122122,1,2,2,1,2,2,'Keeping Still, Mountain')")
cursor.execute("INSERT INTO answers VALUES (53,112122,1,1,2,1,2,2,'Development (Gradual Process)')")
cursor.execute("INSERT INTO answers VALUES (54,221211,2,2,1,2,1,1,'The Marrying Maiden')")
cursor.execute("INSERT INTO answers VALUES (55,221121,2,2,1,1,2,1,'Abundance (Fullness)')")
cursor.execute("INSERT INTO answers VALUES (56,121122,1,2,1,1,2,2,'The Wanderer')")
cursor.execute("INSERT INTO answers VALUES (57,112112,1,1,2,1,1,2,'The Gentle (The Penetrating, Wind)')")
cursor.execute("INSERT INTO answers VALUES (58,211211,2,1,1,2,1,1,'The Joyous, Lake')")
cursor.execute("INSERT INTO answers VALUES (59,112212,1,1,2,2,1,2,'Dispersion (Dissolutin)')")
cursor.execute("INSERT INTO answers VALUES (60,212211,2,1,2,2,1,1,'Limitation')")
cursor.execute("INSERT INTO answers VALUES (61,112211,1,1,2,2,1,1,'Inner Truth')")
cursor.execute("INSERT INTO answers VALUES (62,221122,2,2,1,1,2,2,'Preponderance of the Small')")
cursor.execute("INSERT INTO answers VALUES (63,212121,2,1,2,1,2,1,'After Completion')")
cursor.execute("INSERT INTO answers VALUES (64,121212,1,2,1,2,1,2,'Before Completion')")

rows = cursor.execute("SELECT * FROM answers").fetchall()
# print(rows)
# print(connection.total_changes)

def flipCoin():
    random.seed
    coin = random.choice([True,False])
    # print(coin)
    if coin==True:
        return 3
    else:
        return 2

def toss():
    theresult={"l":"","b":"0","f":"0"}
    result = flipCoin()+flipCoin()+flipCoin()
    print(result)
    if result ==6:
       theresult['l'] = "---x---"
       theresult['b'] = "2"
       theresult['f'] = "1"
    if result ==7: 
       theresult['l'] = "-------"
       theresult['b'] = "1"
       theresult['f'] = "1"
    if result ==8:
       theresult['l'] = "--- ---"
       theresult['b'] = "2"
       theresult['f'] = "2"
    if result ==9: 
        theresult['l'] = "---0---"
        theresult['b'] = "1"
        theresult['f'] = "2"
    
    return theresult


def future(convert):
    thefuture=""
    thefuture = convert.replace('x','-').replace('0',' ')
    return thefuture

# for i in range (0,6):
    # print(i)
tossA1 = toss()
tossA2 = toss()
tossA3 = toss()
tossA4 = toss()
tossA5 = toss()
tossA6 = toss()

print ('Your I Ching Hexagram Results' + '\n\n' +       
       tossA6['l'] + ' | ' + future(tossA6['l']) +'\n' +
       tossA5['l'] + ' | ' + future(tossA5['l']) +'\n' +
       tossA4['l'] + ' | ' + future(tossA4['l']) +'\n' +
       tossA3['l'] + ' | ' + future(tossA3['l']) +'\n' + 
       tossA2['l'] + ' | ' + future(tossA2['l']) +'\n' +
       tossA1['l'] + ' | ' + future(tossA1['l']) +'\n')

sql = "SELECT hexagram,iching FROM answers WHERE binary =?"

p = (tossA6['b']+tossA5['b']+tossA4['b']+tossA3['b']+tossA2['b']+tossA1['b'])
answer1 = cursor.execute(sql,(p,)).fetchall()

p = (tossA6['f']+tossA5['f']+tossA4['f']+tossA3['f']+tossA2['f']+tossA1['f'])
answer2 = cursor.execute(sql,(p,)).fetchall()

print(answer1[0]+ answer2[0])
#



