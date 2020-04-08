# rules for all hash functions
#  'apple' => HASH => af10
# RULE 1. Output must be deterministic
# RULE 2. Defined output range
# RULE 3. Predictable Speed
# RULE 4. Non-invertable

# Secure hash => wants to limit collision and be non-invertable

# SHA 256
# MD5

import time

input_string = b"apple"
n = 100000

print(f"Hashing {n}x")
start_time = time.time()

for i in range(n):
    output_hash = hash(input_string)

end_time = time.time()

print(f"Python hash runtime:{end_time-start_time} seconds")


def djb2(key):
    '''
    DJB2 hash
    '''
    # start from an arbitrary large prime
    hash_value = 5381
    # bit-shift and sum value for each character
    for char in key:
        hash_value = ((hash_value << 5)+hash_value) + char
    return hash_value


start_time = time.time()
for item in range(n):
    djb2(input_string)
end_time = time.time()
print(djb2(input_string))
print(f"DJB2 hash runtime: {end_time - start_time} seconds")


# ------------------
# hash tables
# 1. Hash the key and get a number in some range
# 2. store/retrieve value at the hashed number
