#hashmap_algos
from calendar import TUESDAY
from posixpath import split
import random
from datetime import timedelta
random.seed(1092732)
import textwrap
import time


#Create the Card class
class Card:
    
    #Create all necessary class vars
    #A list of all cards an the number of cards

    card_lst = []
    card_tup_lst = []
    n = 0
    

    #Def the innitialisation func

    def __init__(self,textnum):
        self.total = 0
        self.charges = 0
        self.textrepr = textnum
        self.number = [int(i)for i in textnum.split("-")]
    #Generate a lst of cards 
    def clear ():
        for i in Card.card_lst:
            i.total = 0
            i.charges = 0   
        
        
    def gen_card_lst(n):
        #Use sample to ensure every card number is completely unique
        templst = random.sample(range(1000000000000000, 9999999999999999),n)
        #Format the card number according to specs for repr and for hashing
        Card.card_lst = [Card(i) for i in [ "-".join(textwrap.wrap(str(i), 4)) for i in templst  ]]
        Card.n = n       

    #def repr                                         
    def __repr__(self):
        return self.textrepr
    
    #Hash according to specs
    def __hash__(self):
        return hash(self.textrepr)
    


#define a hash table datatype
#Hash table key:value => Card : list of purchases with said card
class HashTable:
    #Hash init values
    def __init__(self):
        self.size = 101
        self.table = [None] * self.size
        self.load_factor = 0
        self.occupied = 0
    #A list of possible hash size values
    primes = [101, 211, 431, 863, 1733, 3469, 6949, 13901, 27803, 55609, 111227, 222461, 444929, 889871, 1779737, 3559483, 7118971, 14238089, 28476181, 56952361, 113904529, 227809057, 455618273, 911236579, 1822473163, 3644946397]
    #Def the way the keys are hashed
    def hash_function(self, key):
        return hash(key) % self.size
    
    #hash table hash resizing capability with this func
    def resize(self):
            self.size = self.primes[self.primes.index(self.size)+1]
            old_table = self.table
            self.table = [None] * self.size
            for i in old_table:
                if i is not None:
                    self.insert(i[0], i[1])
    #Def insert function
    def insert(self, key, value):
        index = self.hash_function(key)

        #Linear probing
        #If index full continue unitl you find an empty
        while self.table[index] is not None:
            #if the purchase contains an already stored card num then add the purchase to lst
            if self.table[index][0] == key:
                if type(self.table[index][1]) == list:
                    self.table[index][1].append(value)
                
                else:
                    self.table[index] = (key, [self.table[index][1],value])
                return
            #If index full continue unitl you find an empty

            index = (index + 1) % self.size
            
            
        #If index full continue unitl you find an empty
        self.table[index] = (key, value)
        #Calc load factor, resize if >0.7
        self.occupied +=1
        load_factor = self.occupied/self.size
        if load_factor > 0.7:
            self.resize()
        return
        
    #del not necessary
    def search(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None
    #del not necessary
    def delete(self, key):
        pass
#Create purchase class Purcahse : (Card:Card,Value:Int,Date:str)
class Purchase:
    # create class vars
    #An lst and hash table to store purchases
    #And a list of all valide days
    purchase_lst=[]
    n = 0 
    validdays = ["MON","TUE","WEN","THU","FRI", "SAT","SUN"]
    purchase_hash = HashTable()
    
    def __init__(self,card,value,date):
        self.card = card
        self.value = value
        self.date = date
    
    #Generate the list and hash table for n purchases
    def generate_purchase_lst(n):
        for i in range(n):
            temp = Purchase(Card.card_lst[random.randint(0,Card.n-1)], random.randint(5,500),Purchase.validdays[random.randint(0,6)] )
            Purchase.purchase_lst.append(temp)
            Purchase.purchase_hash.insert(temp.card,temp)
        Purchase.n = n

    #Expand the list and hash table for n purchases
    def expandlst(n):
        for i in range(n):
            temp = Purchase(Card.card_lst[random.randint(0,Card.n-1)], random.randint(5,500),Purchase.validdays[random.randint(0,6)] )
            Purchase.purchase_lst.append(temp)
            Purchase.purchase_hash.insert(temp.card,temp)
        Purchase.n += n

    #str func
    def __str__(self):
        return f"Purcheses of value: {self.value} at date: {self.date} with card number {self.card}"
    def __repr__(self):
        return f"Purcheses of value: {self.value} at date: {self.date} with card number {self.card}"
    #Copmpare functions 
    def __lt__(self,other):
        return self.value < other.value
    def __eq__(self,other):
        return self.value == other.value
    #getters
    def getvalue(self):
        return self.value
    def getdate(self):  
        return self.date
    def getcard(self):
        return self.card
    #Hash function
    #HaSH according to card num 
    def __hash__(self) :
        return hash(self.card)
    


#Function to find the requested values using lst datatype
def lstsolver():
    maxcahrge = Purchase.purchase_lst[0].getcard()
    maxtotal = Purchase.purchase_lst[0].getcard()
    mintotal = Purchase.purchase_lst[0].getcard()
    daysdict = {"MON":0,"TUE":0,"WEN":0,"THU":0,"FRI":0, "SAT":0,"SUN":0}

    for i in Purchase.purchase_lst:
        temp = i.getcard()
        temp.charges +=1
        temp.total += i.getvalue()   
        if temp.total > maxtotal.total:
            maxtotal = temp
        if temp.total < mintotal.total:
            mintotal = temp
        if temp.charges > maxcahrge.charges:
            maxcahrge = temp
        daysdict[i.getdate()] += 1
    mostcommonday = max(daysdict,key = daysdict.get)
        
    
    print(f"Card with max charges: {maxcahrge} with {maxcahrge.charges} charges")
    print(f"Card with max total: {maxtotal} with {maxtotal.total} total")
    #print(f"Card with min charges: {mincharge} with {mincharge.charges} charges")
    print(f"Card with min total: {mintotal} with {mintotal.total} total")
    print(f"Most common day: {mostcommonday}")

#Function to find the requested values using hash table datatype
def hashsolver():
    daysdict = {"MON":0,"TUE":0,"WEN":0,"THU":0,"FRI":0, "SAT":0,"SUN":0}
    i = 0 
    dUMMY = Card.card_lst[0]
    maxcahrge = dUMMY
    maxtotal = dUMMY
    mintotal = dUMMY
    print(maxcahrge,maxtotal,mintotal)
    for i in Purchase.purchase_hash.table:
        if i is not None:
            for t in i[1]:   
                i[0].charges +=1
                i[0].total += t.getvalue()
                daysdict[t.getdate()] += 1
            if i[0].total > maxtotal.total:
                maxtotal = i[0]
            if i[0].total < mintotal.total:
                mintotal = i[0]
            if i[0].charges > maxcahrge.charges:
                maxcahrge = i[0]
    print(f"Card with max charges: {maxcahrge} with {maxcahrge.charges} charges")
    print(f"Card with max total: {maxtotal} with {maxtotal.total} total")
    #print(f"Card with min charges: {mincharge} with {mincharge.charges} charges")
    print(f"Card with min total: {mintotal} with {mintotal.total} total")
    print(f"Most common day: {max(daysdict,key = daysdict.get)}")
#Function to gen card and purchase lst
def runer(n1,n2):
    Card.gen_card_lst(n1)
    Purchase.generate_purchase_lst(n2)



runer(20000,1000000)
#file to store results
f =open('output.txt', 'a')
# time the funcs for various n vals
Card.clear()
start = time.time()
hashsolver()
end  = time.time()
print("hash solvertime = ",end-start,f"for n = {Purchase.n},",file = f)
Card.clear()    
start = time.time()
lstsolver()
end  = time.time()
print("lstsolvertime = ",end-start,f"for n = {Purchase.n}\n\n",file = f)

Purchase.expandlst(1000000)
Card.clear()
start = time.time()
hashsolver()
end  = time.time()
print("hash solvertime = ",end-start,f"for n = {Purchase.n}",file = f)
Card.clear()
start = time.time()
lstsolver()
end  = time.time()
print("lstsolvertime = ",end-start,f"for n = {Purchase.n}\n\n",file = f)

Purchase.expandlst(3000000)
Card.clear()
start = time.time()
hashsolver()
end  = time.time()
print("hash solvertime = ",end-start,f"for n = {Purchase.n}",file = f)
Card.clear()
start = time.time()
lstsolver()
end  = time.time()
print("lstsolvertime = ",end-start,f"for n = {Purchase.n}\n",file = f)
 
f.close()
