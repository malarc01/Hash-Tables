import random


def how_many_before_collision(loops, length_of_array):

    for i in range(loops):
        tries = 0
        tried = set()
        while True:
            random_key = random.random()
            hash_index = hash(random_key) % length_of_array
            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1
            else:
                break
        print(" we had {} buckets, and {} hashes before collision".format(
            length_of_array, tries))


how_many_before_collision(10, 10000)
