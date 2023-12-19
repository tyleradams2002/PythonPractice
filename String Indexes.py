# String Indexes

selfish = '12345678'
#          01234567

# accessing a string by its index

print(selfish[0])

# Python Array
#   [start] <-- [0]
#   [start:stop] <-- [0:3]
#   [start:stop:stepover]
# EX:::

print(selfish[0])
print(selfish[0:8])
print(selfish[0:8:2])

print(selfish[0:]) # Will start at 0 and go to the end
print(selfish[::2]) # Will go through entire index and do a stepover of 2
print(selfish[::-1]) # Will reverse the order of a string
print(selfish[::-2]) # Will do a reverse skip over.
