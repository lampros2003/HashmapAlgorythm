#hashmap_algos
from calendar import TUESDAY
from posixpath import split
import random
from typing_extensions import Self
from datetime import timedelta
random.seed(1092732)
import textwrap
import time



class Card:
    card_lst = []
    card_tup_lst = []
    n = 0
    total = 0
    charges = 0
    def __init__(self,textnum):
        self.textrepr = textnum
        self.number = [int(i)for i in textnum.split("-")]
    def gen_card_lst(n):
        templst = random.sample(range(1000000000000000, 9999999999999999),n)
        Card.card_lst = [Card(i) for i in [ "-".join(textwrap.wrap(str(i), 4)) for i in templst  ]]
        Card.n = n                                                
    def __repr__(self):
        return self.textrepr
    def __hash__(self):
        return hash(self.textrepr)
    



class HashTable:
    def __init__(self):
        self.size = 101
        self.table = [None] * self.size
        self.load_factor = 0
        self.occupied = 0
    primes = [101, 211, 431, 863, 1733, 3469, 6949, 13901, 27803, 55609, 111227, 222461, 444929, 889871, 1779737, 3559483, 7118971, 14238089, 28476181, 56952361, 113904529, 227809057, 455618273, 911236579, 1822473163, 3644946397]
    def hash_function(self, key):
        return hash(key) % self.size
    

    def resize(self):
            self.size = self.primes[self.primes.index(self.size)+1]
            old_table = self.table
            self.table = [None] * self.size
            for i in old_table:
                if i is not None:
                    self.insert(i[0], i[1])

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                if type(self.table[index][1]) == list:
                    self.table[index][1].append(value)
                else:
                    self.table[index] = (key, [self.table[index][1],value])
                return
            index = (index + 1) % self.size
            
            

        self.table[index] = (key, value)
        self.occupied +=1
        load_factor = self.occupied/self.size
        if load_factor > 0.7:
            self.resize()
        return
        
    def search(self, key):
        pass    

    def delete(self, key):
        pass
class Purchase:
    purchase_lst=[]
    n = 0 
    validdays = ["MON","TUE","WEN","THU","FRI", "SAT","SUN"]
    purchase_hash = HashTable()
    
    def __init__(self,card,value,date):
        self.card = card
        self.value = value
        self.date = date
    

    def generate_purchase_lst(n):
        for i in range(n):
            temp = Purchase(Card.card_lst[random.randint(0,Card.n-1)], random.randint(5,500),Purchase.validdays[random.randint(0,6)] )
            Purchase.purchase_lst.append(temp)
            Purchase.purchase_hash.insert(temp.card,temp)
        Purchase.n = n
    def __str__(self):
        return f"Purcheses of value: {self.value} at date: {self.date} with card number {self.card}"
    def __repr__(self):
        return f"Purcheses of value: {self.value} at date: {self.date} with card number {self.card}"
    def __lt__(self,other):
        return self.value < other.value
    def __eq__(self,other):
        return self.value == other.value
    def getvalue(self):
        return self.value
    def getdate(self):  
        return self.date
    def getcard(self):
        return self.card
    def __hash__(self) :
        return hash(self.card)
    



def lstsolver():
    for i in Purchase.purchase_lst:
        i.getcard().charges +=1
        i.getcard().total += i.getvalue()   
    maxcahrge = max(Card.card_lst,key = lambda x: x.charges)
    maxtotal = max(Card.card_lst,key = lambda x: x.total)
    mincharge = min(Card.card_lst,key = lambda x: x.charges)
    mintotal = min(Card.card_lst,key = lambda x: x.total)
    mostcommonday = max(Purchase.validdays,key = lambda x: sum([1 for i in Purchase.purchase_lst if i.getdate() == x]))
    print(f"Card with max charges: {maxcahrge} with {maxcahrge.charges} charges")
    print(f"Card with max total: {maxtotal} with {maxtotal.total} total")
    #print(f"Card with min charges: {mincharge} with {mincharge.charges} charges")
    print(f"Card with min total: {mintotal} with {mintotal.total} total")
    print(f"Most common day: {mostcommonday}")
def runer(n1,n2):
    Card.gen_card_lst(n1)
    Purchase.generate_purchase_lst(n2)
    
def hashsolver():
    daysdict = {"MON":0,"TUE":0,"WEN":0,"THU":0,"FRI":0, "SAT":0,"SUN":0}
    i = 0 
    while Purchase.purchase_hash.table[i] is  None:
        i +=1
    maxcahrge = Purchase.purchase_hash.table[i][0]
    maxtotal = Purchase.purchase_hash.table[i][0]   
    mintotal = Purchase.purchase_hash.table[i][0]
    print(maxcahrge,maxtotal,mintotal)
    for i in Purchase.purchase_hash.table:
        if i is not None:
          
            
            i[0].charges += len(i[1])
            if i[0].charges > maxcahrge.charges:
                maxcahrge = i[0]
            i[0].total += sum([j.getvalue() for j in i[1]])
            if i[0].total > maxtotal.total:
                maxtotal = i[0]
            if i[0].total < mintotal.total:
                
                mintotal = i[0]
            for j in i[1]:
                daysdict[j.getdate()] += 1
    print(f"Card with max charges: {maxcahrge} with {maxcahrge.charges} charges")
    print(f"Card with max total: {maxtotal} with {maxtotal.total} total")
    #print(f"Card with min charges: {mincharge} with {mincharge.charges} charges")
    print(f"Card with min total: {mintotal} with {mintotal.total} total")
    print(f"Most common day: {max(daysdict,key = daysdict.get)}")




#Card.gen_card_lst(20000)
#Purchase.generate_purchase_lst(1000000)   

#start = time.time()
#hashsolver()
#end  = time.time()
#print("hash solvertime = ",end-start)



#start = time.time()
#lstsolver()
#end  = time.time()
#print("lstsolvertime = ",end-start)