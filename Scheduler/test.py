from helperfunctions import *

locations = [0]

formatLength = max(locations).bit_length() + 1
formatting = "0{}b".format(str(formatLength))

locations[0] = fillSlots(locations[0], 0, 3)

print("|" + format(locations[0], formatting)[::-1].replace("1","X") + "|")

print(findFreeSlotsWithGap(locations, 5, 14, 2))
