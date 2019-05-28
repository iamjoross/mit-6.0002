#!#/usr/bin/python3
# ##########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time, json

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    try:
        cows = {}
        with open(filename) as datafile:
            for row in datafile:
                read_data = row.split(',')
                cows[read_data[0]] = int(read_data[1].replace('\n', ''))
        datafile.close()
        return cows
    except Exception as err:
        raise err()

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowsCopy = cows.copy()
    result = []
    while True:
        trip = []
        total = 0
        for cow in list(cowsCopy):
            if (total + cowsCopy[cow] <= limit):
                total += cowsCopy[cow]
                trip.append(cow)
                cowsCopy.pop(cow)
        result.append(trip)

        if(len(cowsCopy) == 0):
            break
    return result

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    trips = []
    power_list = sorted(get_partitions(cows), key = len)
    possibilities = []
    for i in power_list:
        ship = []
        for j in i:
            print(j)
    # print(power_list)

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass

from ps1_partition import partitions, get_partitions

def main():
    cows = load_cows('./ps1/ps1_cow_data.txt')
    trips = greedy_cow_transport(cows)
    trips1 = brute_force_cow_transport(cows)
    # print(trips1)
if __name__=='__main__':
    main()

