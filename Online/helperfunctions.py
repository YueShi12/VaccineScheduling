from math import gcd

#returns the least common multiple of x and y
def lcm(x,y):
    return x * y // gcd(x,y)

#function that sets all digits between start up to and including end to 1 in a binary number
def fillSlots(location, start, end):
    for i in range(start, end + 1):
        location = location | (1 << i)
    return location

#function that returns True if all slots are free between start up to and including end
def checkFreeSlots(location, start, end):
    #assume all slots are free
    slotsFree = True
    #start checking if all slots are free
    for i in range(start, end + 1):
        #if a slot is not free, slotsFree will be set to false
        slotsFree &= not(bool(location & (1 << i)))
    return slotsFree

#function that returns the location and starting index of the first stretch of free slots it finds
def findFirstFreeSlots(locations, startI, endI, p):
    for i in range(len(locations)):
        #start at the beginning of the interval, only checking options that do not exceed the interval
        for j in range(startI, (endI - (p-1)) + 1):
            if checkFreeSlots(locations[i], j, j + (p-1)):
                return (i,j)

def findLastFreeSlots(locations, startI, endI, p):
    for i in range(len(locations)):
        #start at the end of the interval, only checking options that do not exceed the interval
        for j in range((endI - (p-1)), startI - 1, -1):
            if checkFreeSlots(locations[i], j, j + (p-1)):
                return (i,j)

#returns a list of tuples (i,j) where i is the index of the location and j is the start of the free interval of length p
def findFreeSlots(locations, startI, endI, p):
    slots = []
    for i in range(len(locations)):
        #start at the beginning of the interval, only checking options that do not exceed the interval
        for j in range(startI, (endI - (p-1)) + 1):
            if checkFreeSlots(locations[i], j, j + (p-1)):
                slots.append((i,j))
    return slots

#returns a list of tuples (i,j,g) where i is the index of the location and j is the start of the free interval of length p, g is the gap between j and the last free slot
def findFreeSlotsWithGap(locations, startI, endI, p):
    slots = []
    for i in range(len(locations)):
        #create a variable to keep track of the last filled slot
        #scan from the start of the interval backwards to find the initial lastFilledSlot, default to -1
        lastFilledSlot = -1
        for n in range(startI, -1, -1):
            if not(checkFreeSlots(locations[i], n, n)):
                lastFilledSlot = n
                break

        #create a variable to check if the previous slot is free, set it accordingly
        previousSlotsFree = (lastFilledSlot != startI - 1)
        #start at the beginning of the interval, only checking options that do not exceed the interval
        for j in range(startI, (endI - (p-1)) + 1):
            currentSlotsFree = checkFreeSlots(locations[i], j, j + (p-1))
            #if the previous slot was not free, but the current slot is, update the lastFilledSlot
            if not(previousSlotsFree) and currentSlotsFree:
                lastFilledSlot = j - 1
            if currentSlotsFree:
                slots.append((i,j, j - lastFilledSlot - 1 ))
            previousSlotsFree = currentSlotsFree
    return slots

#schedule a patients ith slot at location with duriation ps[i]
def scheduleShot(hospitals, patient, location, slot, ps, i):
    patient.locations[i] = location
    patient.slots[i] = slot
    #fill the slots in the hospital
    hospitals.locations[location] = fillSlots(hospitals.locations[location], slot, slot + ps[i] - 1)
