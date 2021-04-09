import os
def create(name):
    if os.path.exists(name):
        print("file already exists")
    else:
        open(name,'x') 
        print("file created")       

create("game.txt")

def read(name):
    return open(name,"r")
    
f = read("game.txt")
print(f.read())

def delete(name):
    if os.path.exists(name):
        os.remove(name)
        print("file deleted")
    else:
        print("The file does not exist")

delete("game.txt")
