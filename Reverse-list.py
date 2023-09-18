# using string slicing operator 
input_string = "Hello, World!"
reversed_string = input_string[::-1]
print(reversed_string)
#using for loop statement
input_string = "Hello, World!"
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
print(reversed_string)
#using recursive function recursiom
def reverse_string(input_string):
    if len(input_string) == 0:
        return input_string
    else:
        return reverse_string(input_string[1:]) + input_string[0]

input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(reversed_string)

