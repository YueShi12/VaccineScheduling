import time
from algorithms import *
from classes import *
import os

def main():
    start_time = time.time()

    #set this to wherever you have saved the testinstances
    directory = "/home/lukas/Documents/UU/Algorithms for Decision Support/Vaccine/Instances/"

    #loop over all the testinstances
    for filename in os.listdir(directory):
        #create initial objects
        hospitals = Hospitals()
        patients = []

        #open instance
        path = directory + filename
        print(filename)
        instance = open(path)

        #read in global variables
        ps = [None]
        ps.append(int(instance.readline()))
        ps.append(int(instance.readline()))
        gap = int(instance.readline())

        #start patient loop
        while True:
            #read in patient
            patientInput = instance.readline()

            #if the input is x, break and print the amount of hospitals used, as well as the timetable
            #"x\n" is for reading from txt file.
            if patientInput == "x\n" or patientInput == "x":

                #for patient in patients:
                    #print the patients schedule
                    #print("{0}, {1}, {2}, {3}".format(patient.slots[1], patient.locations[1], patient.slots[2], patient.locations[2]))

                #print the amount of hospitals used
                print(len(hospitals.locations))
                #print the schedule of the hospitals, nicely formatted
                #hospitals.printLocations()
                break

            #if the input is a patient, add a patient to the hospitals
            startI1, endI1, delay, lengthI2 = map(int, patientInput.split(","))
            patient = Patient(startI1, endI1, delay, lengthI2)

            #run the algorithm of choice with the patient
            scheduleWithGapCalculation(hospitals, patient, ps, gap)
            #after all the operations ons the patient are done, add it to a list so we can print it later
            patients.append(patient)

    #print how long it took
    print("%s seconds" % (time.time() - start_time))

if __name__ == "__main__":
    main()
