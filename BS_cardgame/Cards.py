# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:58:22 2019

@author: shivank agrawal
"""
import random
import time
print("Starting import random_measure")
#import random_measure
print("Ending import random_measure")

class card:
    def character(a,c, s, numb):
        a.Number=numb
        valid = False;
        while (valid == False):
            if numb>14 or numb<1:
                print("number too high")
                continue
            elif (numb <=10):
                face = str(numb)
            elif numb >10:
                if numb==11:
                    face="Jack"
                elif numb==12:
                    face="Queen"
                elif numb==13:
                    face="King"
                elif numb==14:
                    face="A"
        
            if c ==1: 
                color="red"
                if s==1:
                    suite = "diamond"
                    valid=True
                elif s==2:
                    suite = "hearts"
                    valid=True
            elif c==2:
                color = "black"
                if s==1:
                    suite = "clubs"
                    valid=True
                elif s==2:
                    suite = "spades"
                    valid=True
       
       
        a.Suite=suite;
        a.Color=color;
        a.Face=face;
    def prop (a):
       print(a.Color,a.Suite,a.Face)
        
class deck:
         
        
        def __init__ (d): #Constructor, have to use def _ ctrl/space
            d.pile=[];
            for x in range(1,3):
                for y in range(1,3):
                    for z in range(2,15):
                        a = card();
                        a.character(x,y,z)
                        d.pile.append(a)
        def breakshuffle (d,times):
           
            for x in range(times):  
                cardspulled=random.randint(10,26)
                where=random.randint(0,51-cardspulled)
                temp=[];
                for takeout in range(0,cardspulled):
                    temp.append(d.pile.pop(where))
                for putin in range(0,cardspulled):
                    d.pile.insert(putin,temp[putin])
                    
        def riffleshuffle (d,times):
           
            for x in range(times):  
                cardspulled=random.randint(20,31)
                where=random.randint(0,1)*(52-cardspulled)
                #print ("cards pulled = ",cardspulled, "location= ",where)
                #time.sleep(5)
                temp=[];
                for takeout in range(cardspulled):
                    temp.append(d.pile.pop(where))
# =============================================================================
#                 for takeout in range(cardspulled):
#                     temp[takeout].prop()
#                 time.sleep(5)
# =============================================================================
                numcards=0
                lastplace=0
                #for cardsleft in range(numcards,cardspulled):
                while numcards<cardspulled:
                    if cardspulled <5:
                        pulled=random.randint(0,(cardspulled-numcards))
                    else:
                        pulled=random.randint(0,5)
                    if pulled+lastplace > 51:
                        pulled=51-lastplace
                    #print(pulled,lastplace,numcards)
                   # time.sleep(2)
                    for numput in range(0,pulled):
                        d.pile.insert(lastplace,temp[numcards+numput])
                       # d.pile[lastplace].prop()
                        #time.sleep(5)
                        lastplace=lastplace+1
                        
                        #d.pile[lastplace].prop()
                    numcards=numcards+pulled
                    lastplace=lastplace+pulled+random.randint(0,5)
                    if lastplace>=51-cardspulled:
                        lastplace=51-(cardspulled-numcards)
                    #time.sleep(5)

# =============================================================================
#                 print("how many pulling: ", cardspulled)
#                 for takeout in range(0,cardspulled):
#                    temp[takeout].prop()
#                 time.sleep(8)
#                 print("where pulling: ",where)
#                 time.sleep(8)
#                 for x in range(0,52):                    
#                     d.pile[x].prop()
# =============================================================================
               # print (deck.pile[x].prop())
                   # print(pile[z-2].prop())
#print(pile[2].prop())
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
# =============================================================================
# first=deck();
# #first.reset() 
# second=deck();
# #second.reset  
# #a = random_measure.randomm(first)
# #for x in range(52):                    
# #    a.deck.pile[x].prop()   
# time.sleep(8)             
# for x in range(52):                    
#     first.pile[x].prop()
# print("Riffle shuffling")
# time.sleep(8)
# first.riffleshuffle()                   
# for x in range(0,52):                    
#    first.pile[x].prop()
# 
# print("Break shuffling")
# time.sleep(8)
# second.breakshuffle()                   
# for x in range(0,52):                    
#    second.pile[x].prop() # earlier when syntax was print(first.pile[x].prop()) first program was trying to print result then function
# 
# 
# =============================================================================
    