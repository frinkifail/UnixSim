#!catecoin lib #source_code
#@import libs
import random
import time
#@variables
priceLow = random.uniform(0.01,1984.91)
priceHigh = random.uniform(priceLow, 2984.91)
#@functions

def checkPrice():
    global priceLow
    global priceHigh
    print(random.uniform(priceLow,priceHigh))

while True:
    checkPrice()
    time.sleep(0.85)
