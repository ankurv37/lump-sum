import hashlib

sampleData = "The miner(s) of this block earned a total reward of 12.50000000 BTC ($454,443.88). " \
             "The Block rewards, also known as the Coinbase reward, were sent to this address."

Bits = 0x1d00ffff;

###
# HEX 0x1d DEC 29
# HEX 00ffff DEC 29

p1 = 30
p2 = 0x148edf

# TARGET: t = 00ffff * 2^(8*(0x1d -3))
# Bits = 0x171484df
# target = 0x148edf * 2^(B(0x17-3))

num1 = p1 - 3
num2 = num1 * 8
num3 = 2**num2
target = p2 * num3
targetHex = format(target, "016x").zfill(64)

nonce = 0

while 1:
    testHash = hashlib.sha256(sampleData.encode() + str(nonce).encode()).hexdigest()
    if testHash < targetHex :
        print(str(nonce) + " " + testHash + " " + targetHex + " FOUND!!!\n")
        break
    else:
        print(str(nonce) + " " + testHash + " " + targetHex + "\n")
        nonce+=1


