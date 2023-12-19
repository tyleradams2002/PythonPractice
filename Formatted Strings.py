# formatted Strings

name_cool = 'Tyler'
name_bitch = 'Joe'
age_cool = 21
age_bitch = 46

print('hi ' + name_cool)
print('bye ' + name_bitch)

print('hi ' + name_cool + '. You are ' + str(age_cool) + ' years old')
print('hi ' + name_bitch + '. You are ' + str(age_bitch) + ' years old \n FUCK OFF!!!')

print(f'hi {name_cool}. You are {age_cool}') #One way to format
print('hi {}. You are {} years old, and you are awesome'.format(name_cool, age_cool)) #Other way to format

print('hi {}. You are {} years old, U OLD FART!!!'.format(name_bitch, age_bitch))
print(f'hi {name_cool}. You are {age_cool}. You are awesome')
