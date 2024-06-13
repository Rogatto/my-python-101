# find a value within the array and simply return true or false

array = [43434,54,235,8787,323235,11]

def find_value_array(value):
    exists = False
    for i in array:
        print('The value in the array is: ', i)
        if i == value:
            exists = True
    
    return exists


print(find_value_array(1235))

print('================================================================')
# Now return how many times that value was found within the array

array2 = [43434,54,235,8787,434345,11]

def find_value_array_counting(value):
    c = 0
    for i in array2:
        if i == value:
            c+=1
    return c

print(find_value_array_counting(43434))