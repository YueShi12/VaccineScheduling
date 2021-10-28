from random import choice
from helperfunctions import *

def newHospitalForEveryPatient(hospitals, patient, ps, gap):
    #open a new hospital
    hospitals.newLocation()

    location = len(hospitals.locations) - 1
    slot = patient.startIs[1]
    scheduleShot(hospitals, patient, location, slot, ps, 1)

    #determine the second interval now the first slot is given
    patient.startIs[2] = patient.slots[1] + ps[1] + gap + patient.delay
    patient.endIs[2] = patient.startIs[2] + patient.lengthI2 - 1

    location = len(hospitals.locations) - 1
    slot = patient.startIs[2]
    scheduleShot(hospitals, patient, location, slot, ps, 2)

def scheduleASAP(hospitals, patient, ps, gap):
    #find the first available free slot in any hospital within the interval
    freeSlots = findFirstFreeSlots(hospitals.locations, patient.startIs[1], patient.endIs[1], ps[1])

    #if there is no slot available, open a new hospital and adjust the location and slot accoridingly
    if freeSlots is None:
        hospitals.newLocation()
        location = len(hospitals.locations) - 1
        slot = patient.startIs[1]

    else:
        location, slot = freeSlots

    scheduleShot(hospitals, patient, location, slot, ps, 1)

    #determine the second interval now the first slot is given
    patient.startIs[2] = patient.slots[1] + ps[1] + gap + patient.delay
    patient.endIs[2] = patient.startIs[2] + patient.lengthI2 - 1

    freeSlots = findFirstFreeSlots(hospitals.locations, patient.startIs[2], patient.endIs[2], ps[2])

    if freeSlots is None:
        hospitals.newLocation()
        location = len(hospitals.locations) - 1
        slot = patient.startIs[2]

    else:
        location, slot = freeSlots

    scheduleShot(hospitals, patient, location, slot, ps, 2)

def scheduleRandom(hospitals, patient, ps, gap):
    #find the first available free slot in any hospital within the interval
    freeSlots = findFreeSlots(hospitals.locations, patient.startIs[1], patient.endIs[1], ps[1])

    #if there is no slot available, open a new hospital and adjust the location and slot accoridingly
    if len(freeSlots) == 0:
        hospitals.newLocation()
        location = len(hospitals.locations) - 1
        slot = patient.startIs[1]

    else:
        location, slot = choice(freeSlots)

    scheduleShot(hospitals, patient, location, slot, ps, 1)


    #determine the second interval now the first slot is given
    patient.startIs[2] = patient.slots[1] + ps[1] + gap + patient.delay
    patient.endIs[2] = patient.startIs[2] + patient.lengthI2 - 1

    freeSlots = findFreeSlots(hospitals.locations, patient.startIs[2], patient.endIs[2], ps[2])

    #if there is no slot available, open a new hospital and adjust the location and slot accoridingly
    if len(freeSlots) == 0:
        hospitals.newLocation()
        location = len(hospitals.locations) - 1
        slot = patient.startIs[2]

    else:
        location, slot = random.choice(freeSlots)

    scheduleShot(hospitals, patient, location, slot, ps, 2)

#this algorithms always schedules jobs leaving gaps accoriding to the uniform job length
def uniformJobs(hospitals, patient, ps, gap):
    #find the first available free slot in any hospital within the interval
    freeSlots = findFirstFreeSlots(hospitals.locations, patient.startIs[1], patient.endIs[1], ps[1])

    #if there is no slot available, open a new hospital and adjust the location and slot accoridingly
    if freeSlots is None:
        hospitals.newLocation()
        location = len(hospitals.locations) - 1
        slot = patient.startIs[1]

    else:
        location, slot = freeSlots

    scheduleShot(hospitals, patient, location, slot, ps, 1)

    #determine the second interval now the first slot is given
    patient.startIs[2] = patient.slots[1] + ps[1] + gap + patient.delay
    patient.endIs[2] = patient.startIs[2] + patient.lengthI2 - 1

    freeSlots = findFreeSlots(hospitals.locations, patient.startIs[2], patient.endIs[2], ps[2])

    if len(freeSlots) == 0:
        hospitals.newLocation()
        location = len(hospitals.locations) - 1
        slot = patient.startIs[2]

    else:
        #select the slots such that the gap between the first and second shot is a multiple of the processing time
        bestSlots = [(i,j) for (i,j) in freeSlots if (j - (patient.slots[1] + ps[1])) % ps[1] == 0]

        if len(bestSlots) == 0:
            location, slot = freeSlots[0]
        else:
            location, slot = bestSlots[0]

    scheduleShot(hospitals, patient, location, slot, ps, 2)

def scheduleALAP(hospitals, patient, ps, gap):
    #find the first available free slot in any hospital within the interval
    freeSlots = findLastFreeSlots(hospitals.locations, patient.startIs[1], patient.endIs[1], ps[1])

    #if there is no slot available, open a new hospital and adjust the location and slot accoridingly
    if freeSlots is None:
        hospitals.newLocation()
        location = len(hospitals.locations) - 1
        slot = patient.endIs[1] - ps[1]

    else:
        location, slot = freeSlots

    scheduleShot(hospitals, patient, location, slot, ps, 1)

    #determine the second interval now the first slot is given
    patient.startIs[2] = patient.slots[1] + ps[1] + gap + patient.delay
    patient.endIs[2] = patient.startIs[2] + patient.lengthI2 - 1

    freeSlots = findLastFreeSlots(hospitals.locations, patient.startIs[2], patient.endIs[2], ps[2])

    if freeSlots is None:
        hospitals.newLocation()
        location = len(hospitals.locations) - 1
        slot = patient.startIs[2] - ps[2]

    else:
        location, slot = freeSlots

    scheduleShot(hospitals, patient, location, slot, ps, 2)

def scheduleFirstASAPLastALAP(hospitals, patient, ps, gap):
    #find the first available free slot in any hospital within the interval
    freeSlots = findFirstFreeSlots(hospitals.locations, patient.startIs[1], patient.endIs[1], ps[1])

    #if there is no slot available, open a new hospital and adjust the location and slot accoridingly
    if freeSlots is None:
        hospitals.newLocation()
        location = len(hospitals.locations) - 1
        slot = patient.startIs[1]

    else:
        location, slot = freeSlots

    scheduleShot(hospitals, patient, location, slot, ps, 1)

    #determine the second interval now the first slot is given
    patient.startIs[2] = patient.slots[1] + ps[1] + gap + patient.delay
    patient.endIs[2] = patient.startIs[2] + patient.lengthI2 - 1

    freeSlots = findLastFreeSlots(hospitals.locations, patient.startIs[2], patient.endIs[2], ps[2])

    if freeSlots is None:
        hospitals.newLocation()
        location = len(hospitals.locations) - 1
        slot = patient.endIs[2] - ps[2]

    else:
        location, slot = freeSlots

    scheduleShot(hospitals, patient, location, slot, ps, 2)

#the idea is to schedule shots in such a way that we don't waste slots
#slots are wasted when it isn't possible to schedule a shot anymore because there is too little room
#we try and schedule the shots with enough space in between them for another shot
def scheduleWithGapCalculation(hospitals, patient, ps, gap):
    #calculate the least common multiple of the processing times, as this will be relevant when scheduling
    leastCommonMult = lcm(ps[1],ps[2])
    #find all the free slots in all hospitals where we can schedule a shot
    #for every free slot, we also store how many empty slots are between the slot and the last filled slot
    freeSlots = findFreeSlotsWithGap(hospitals.locations, patient.startIs[1], patient.endIs[1], ps[1])

    #if there are no free slots, create a new hospital try to find free slots again
    if len(freeSlots) == 0:
        hospitals.newLocation()
        freeSlots = findFreeSlotsWithGap(hospitals.locations, patient.startIs[1], patient.endIs[1], ps[1])

    #select the slots such that the gap between the last filled slot and this shot is ideal, i.e. a multiple of both processing times
    slots = [(i,j) for (i,j,g) in freeSlots if g % leastCommonMult == 0]

    #if there are no such slots, try and find slots that are a multiple of either of the two processing times, favoreing the larger one
    if len(slots) == 0:
        slots = [(i,j) for (i,j,g) in freeSlots if g % max(ps[1],ps[2]) == 0]
        if len(slots) == 0:
            slots = [(i,j) for (i,j,g) in freeSlots if g % min(ps[1],ps[2]) == 0]

    #pick the location and slot accoriding to our preference
    if len(slots) != 0:
        location, slot = slots[0]
    else:
        location, slot, _ = freeSlots[0]

    #schedule the shot
    scheduleShot(hospitals, patient, location, slot, ps, 1)

    #determine the second interval now the first slot is given
    patient.startIs[2] = patient.slots[1] + ps[1] + gap + patient.delay
    patient.endIs[2] = patient.startIs[2] + patient.lengthI2 - 1


    #do the same for the second shot
    freeSlots = findFreeSlotsWithGap(hospitals.locations, patient.startIs[2], patient.endIs[2], ps[2])

    if len(freeSlots) == 0:
        hospitals.newLocation()
        freeSlots = findFreeSlotsWithGap(hospitals.locations, patient.startIs[2], patient.endIs[2], ps[2])

    slots = [(i,j) for (i,j,g) in freeSlots if g % leastCommonMult == 0]

    if len(slots) == 0:
        slots = [(i,j) for (i,j,g) in freeSlots if g % max(ps[1],ps[2]) == 0]
        if len(slots) == 0:
            slots = [(i,j) for (i,j,g) in freeSlots if g % min(ps[1],ps[2]) == 0]

    if len(slots) != 0:
        location, slot = slots[0]
    else:
        location, slot, _ = freeSlots[0]

    scheduleShot(hospitals, patient, location, slot, ps, 2)
