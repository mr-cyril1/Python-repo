
# Ask the user to input a sentence

msg = 'Wtite a sentence: '
sentence = input(msg)
print_first_ten = sentence[:11]

# print ('You wrote: ' + print_first_ten)

# reserse the sliced string

reverse_slice = print_first_ten[::-1]

# Convert the reversed sliced string to a Capital letter

capital_slice_output = reverse_slice.upper()

# Ouput: display the trasformed sting to the user

print ('Your ouput is: ' + capital_slice_output)
