
filter_len = hashv = 256
bloom = [False for i in range(filter_len)]


vals = [1023, 3596, 6249, 8274, 2948, 293, 511]

for v in vals:
    bloom[v%hashv] = True 


def isPresent(num):
    if bloom[num%hashv]:
        print("Val may or may not be present")
    else: 
        print("Val not present")


isPresent(511)
