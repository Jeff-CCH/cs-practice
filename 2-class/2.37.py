"""
Write a simulator, as in the previous project, but add a Boolean gender field and a floating-point strength field to each animal, using an Animal class as a base class. If two animals of the same type try to collide, then they only create a new instance of that type of animal if they are of differ- ent genders. Otherwise, if two animals of the same type and gender try to collide, then only the one of larger strength survives
"""

import random

class Animal(object):
    def __init__(self, animal_type):
        self._type = animal_type
        self._gender = random.choice(["M", "F"])
        self._strength = random.randint(0,10)

    def collide(self, other):
        return self if self._strength > other._strength else other

    def get_type(self):
        return self._type

class Bear(Animal):
    def __init__(self):
        super(Bear, self).__init__("Bear")

    def collide(self, other):
        if self._type == other._type:
            if self._gender != other._gender:
                return Bear(), "newbirth"
            else:
                return super(Bear, self).collide(other), "collide"
        else: return self, "collide" # eats fish

class Fish(Animal):
    def __init__(self):
        super(Fish, self).__init__("Fish")

    def collide(self, other):
        if self._type == other._type:
            if self._gender != other._gender:
                return Fish(), "newbirth"
            else:
                return super(Fish, self).collide(other), "collide"
        else: return other, "collide" # eaten by bear

def migration(river, none_list):
    sp = random.choice(["Bear", "Fish"])
    loc_num = random.randint(0, len(river)-1)
    if sp == "Bear": # Bear
        if river[loc_num] != None:
            animal, state = Bear().collide(river[loc_num])
            if state == "newbirth":
                index = random.choice(none_list)
                river[index] = animal
                none_list.remove(index)
                print "born new bear at index %d" % index
            else:
                river[loc_num] = animal
                print "%s beats another at loc %d" % (animal.get_type(), loc_num)
        else:
            river[loc_num] = Bear()
            print "new bear moves in %d" % loc_num
    else: # fish
        if river[loc_num] != None:
            animal, state = Fish().collide(river[loc_num])
            if state == "newbirth":
                index = random.choice(none_list)
                river[index] = animal
                none_list.remove(index)
                print "born new fish at index %d" % index
            else:
                river[loc_num] = animal
                print "%s beats another at index %d" % (animal.get_type(), loc_num) # dead fish
        else:
            river[loc_num] = Fish()
            print "new fish moves in %d" % loc_num

def main():
    river_len = 10
    while True:
        river = [None] * river_len
        none_list = []
        for i in range(river_len):
            none_list.append(i)
        river[0] = Bear()
        none_list.remove(0)
        river[river_len-1] = Fish()
        none_list.remove(river_len-1)
        num = input("Please input the migration loop num: ")
        for i in range(num):
            r_status = ""
            migration(river, none_list)
            for animal in river:
                if animal != None:
                    r_status += animal.get_type() + " "
                else: r_status += "None" + " "
            print r_status # river status
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
