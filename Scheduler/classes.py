class Patient:

	#initiliaze a patient by storing the variables given by the input
    def __init__(self, startI1, endI1, delay, lengthI2):
		#store it in lists, with first element always None to ease indexing
        self.startIs = [None, startI1, None]
        self.endIs = [None, endI1, None]
        self.delay = delay
        self.lengthI2 = lengthI2

        self.slots = [None, None, None]

        self.locations = [None, None, None]

class Hospitals:

    #initialize an empty list, since at the start there are no hospitals
    def __init__(self):
    	self.locations = []

    #open a new location, all with empty time slots (0)
    def newLocation(self):
    	self.locations.append(0)

    def printLocations(self):
        #find the furthest filled in timeslot
        formatLength = max(self.locations).bit_length() + 1
        #create the format accoridingly
        formatting = "0{}b".format(str(formatLength))
        print("=" * (formatLength + 2))
        for location in self.locations:
            #print the location, formatted into binary digits and reversed ([::-1]), replaceing 1s with Xs
            print("|" + format(location, formatting)[::-1].replace("1","X") + "|")
        print("=" * (formatLength + 2))
