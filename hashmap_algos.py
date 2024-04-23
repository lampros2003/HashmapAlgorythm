#hashmap_algos
from calendar import TUESDAY
from posixpath import split
import random
from typing_extensions import Self
from datetime import timedelta
random.seed(1092732)
import textwrap



class Card:
    card_lst = []
    card_tup_lst = []
    n = 0
    def __init__(self,textnum):
        self.textrepr = textnum
        self.number = [int(i)for i in textnum.split("-")]
    def gen_card_lst(n):
        templst = random.sample(range(1000000000000000, 9999999999999999),n)
        Card.card_lst = [Card(i) for i in [ "-".join(textwrap.wrap(str(i), 4)) for i in templst  ]]
        Card.n = n                                                
    def __repr__(self):
        return self.textrepr
    
class Purchase:
    purchase_lst=[]
    n = 0 
    validdays = ["MON","TUE","WEN","THU","FRI", "SAT","SUN"]
    def generate_purchase_lst(self,n):
        self.purchase_lst = [ (i,x,y,z) for (i,x,y,z) in (random.sample(range(1000, 9999), n),random.sample(range(1000, 9999), n),random.sample(range(1000, 9999), n),random.sample(range(1000, 9999), n))]
        self.n = n
    def __init__(self,card,value,date):
        self.card = card
        self.value = value
        self.date = date
    def __str__(self):
        return f"Purches of value: {self.value} at date: {self.date} with card number {self.card}"

