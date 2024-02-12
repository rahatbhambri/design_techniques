class cons_hash():
    def __init__(self, rsize):
        self.ring = [-1 for i in range(rsize)]
        self.hashv = rsize 
    
    def addServer(self, pos):
        pos = pos%self.hashv
        if self.ring[pos] == -1:
            self.ring[pos] = 1
            print(f"Server added at {pos}")
        else:
            print("Server already placed here")
    
    def removeServer(self, pos):
        if self.ring[pos] == 1:
            self.ring[pos] = 0 
            print(f"Server removed from {pos}")
        else:
            print("No Server was found")
        
    def serveRequest(self, val):
        init_pos = val%self.hashv
        if self.ring[init_pos] == 1:
            print(f"request {val} served at {init_pos} server")
        else:
            pos = init_pos
            while self.ring[pos%self.hashv] != 1 :
                pos += 1
            print(f"request {val} served at {pos%self.hashv} server")
    
    

consh = cons_hash(16)

consh.addServer(4)
consh.addServer(8)
consh.addServer(12)

for req in range(25, 50):
    consh.serveRequest(req)
print("all done")

consh.removeServer(8)
for req in range(25, 50):
    consh.serveRequest(req)
print("all done")


consh.addServer(150)
for req in range(25, 50):
    consh.serveRequest(req)
print("all done")

