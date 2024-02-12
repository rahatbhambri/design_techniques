import hashlib

class cons_hash():
    def __init__(self, rsize):
        self.ring = [-1 for i in range(rsize)]
        self.hashv = rsize 
        self.server = {}

    def getHashedPos(self, name):
        hsh = hashlib.sha256()
        hsh.update(bytes(name.encode('utf-8')))

        pos = int(hsh.hexdigest(), 16)%self.hashv
        return pos
    
    def addServer(self, name):
        pos = self.getHashedPos(name)
        if self.ring[pos] == -1:
            self.ring[pos] = 1
            self.server[pos] = name
            print(f"Server {name} added at {pos}")
        else:
            print("Server already placed here")
    
    def removeServer(self, name):
        pos = self.getHashedPos(name)
        if self.ring[pos] == 1:
            self.ring[pos] = 0 
            self.server.pop(pos)
            print(f"Server {name} removed from {pos}")
        else:
            print("No Server was found")
        
    def serveRequest(self, val):
        init_pos = val%self.hashv
        if self.ring[init_pos] == 1:
            print(f"request {val} served at {self.server[init_pos]} server")
        else:
            pos = init_pos
            while self.ring[pos%self.hashv] != 1 :
                pos += 1
            print(f"request {val} served at {self.server[pos%self.hashv] } server")

def simulate(consh):
    for req in range(25, 50):
        consh.serveRequest(req)
    
    print("all done")

    

consh = cons_hash(16)

consh.addServer("Satyam")
consh.addServer("Shivama")
consh.addServer("Sundarama")

consh.removeServer("Shivama")
simulate(consh)

consh.addServer("Shyama")
simulate(consh)

