import os
from random import randint
import random
def create(name):
    if os.path.exists(name):
        print("file already exists")
    else:
        open(name,'x') 
        print("file created") 

def generate_random_bits(limit,type):
    if(type==1):
        return ''.join(["{}".format(randint(0, 9)) for num in range(0, limit)])
    else:
        return  res = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N))    
def string_generator()
try:     
    n = int(input("How many Random Tescases to be genrated? : "))
    m = int(input("Size of testcases: "))
    print(
        "1)Integer type\n"
        "2)String type\n"
    )
    ch = int(input("Choice: "))
    if(ch==1):

    create("results.txt")
    for i in range(n):
        print(generate_random_bits(m))
        f = open("results.txt","a")
        f.write(generate_random_bits(m))
        f.write("\n")
    f.close()
except ValueError:
    print("Your input is wrong!")
