selfish = '01234567'
        #  01234567
selfish[start:stop:stepover]

selfish[0] = '8'

print(selfish)

# Strings are immutable and cannot be changed within without completely resetting the value

# EX
selfish = '81234'
print(selfish)

# Only way to add to a string is as such :

selfish = selfish + '9'
print(selfish)