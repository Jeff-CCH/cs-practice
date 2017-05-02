"""
Write a Python program to simulate an ecosystem containing two types of creatures, bears and fish. The ecosystem consists of a river, which is modeled as a relatively large list. Each element of the list should be a Bear object, a Fish object, or None. In each time step, based on a random process, each animal either attempts to move into an adjacent list location or stay where it is. If two animals of the same type are about to collide in the same cell, then they stay where they are, but they create a new instance of that type of animal, which is placed in a random empty (i.e., previously None) location in the list. If a bear and a fish collide, however, then the fish dies (i.e., it disappears).
"""

import random

def migration(river, none_list):
    sp = random.choice(["Bear", "Fish"])
    loc_num = random.randint(0, len(river)-1)
    if sp == "Bear": # Bear
        if river[loc_num] != None:
            if river[loc_num] == "Bear":
                index = random.choice(none_list)
                river[index] = "Bear"
                none_list.remove(index)
                print "born new bear at index %d" % index
            else: 
                river[loc_num] = "Bear"
                print "bear eats the fish at loc %d" % loc_num
        else:
            river[loc_num] = "Bear"
            print "new bear moves in %d" % loc_num
    else: # fish
        if river[loc_num] != None:
            if river[loc_num] == "Fish":
                index = random.choice(none_list)
                river[index] = "Fish"
                none_list.remove(index)
                print "born new fish at index %d" % index
            else: print "fish is eaten by a bear at index %d" % loc_num # dead fish
        else:
            river[loc_num] = "Fish"
            print "new fish moves in %d" % loc_num

def main():
    river_len = 10
    while True:
        river = [None] * river_len
        none_list = []
        for i in range(river_len):
            none_list.append(i)
        river[0] = "Bear"
        none_list.remove(0)
        river[river_len-1] = "Fish"
        none_list.remove(river_len-1)
        num = input("Please input the migration loop num: ")
        for i in range(num):
            migration(river, none_list)
            print river
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
