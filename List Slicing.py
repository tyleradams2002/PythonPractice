# List Slicing

amazon_cart = ['notebooks',
               'sunglasses',
               'toys',
               'grapes'
               ]

string = 'helllooo'
string_slice = string[0:2:1]
print(string_slice)

print(amazon_cart[0::2])
print('====================')

# lists are mutable unlike strings

amazon_cart[0] = 'laptop'
print(amazon_cart)
print(amazon_cart[1:3])

new_cart = amazon_cart[0:3]
print(f'New Cart = {new_cart}')