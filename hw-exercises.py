from curses.ascii import isspace


# #1. Filter out all of the empty strings from the list below
places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']


new_places = list(filter(lambda x: x and not x.isspace(), places))

print(new_places)
  

# 2. Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"
authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]

authors.sort(key=lambda name: name.split(" ") [-1].lower())
print(authors)


# #3. Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]
f_places = list(map(lambda t: (t[0], t[1]*1.8 +32), places))
print(f_places)




# DID NOT COMPLETE THIS ONE
# 4. Write a recursive function that returns the fibonacci sequence up to the number passed in.
# def fib(num):
#     print(f"fib({num})")
#     if num <= 0:
#         print("elif==")
#         # print(0)
#         return 0
#     elif num == 1:
#         print("eifnum==1")
#         # print(1)
#         return [1]
#     elif num == 2:
#         print("elifnum==2")
#         # print(1)
#         return [1]
#     else:
#         print(f"else {num}")
        
#         f1 = fib(num-1)
#         print(f"tester {num}")
#         f2 = fib(num-2)
#         f = f1 + f2
#         print(f"else2 {num}")
#         print(f)
#         return f

# fib(5)

