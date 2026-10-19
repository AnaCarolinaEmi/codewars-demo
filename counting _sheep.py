#Consider an array/list of sheep where some sheep may be missing from their place. 
#We need a function that counts the number of sheep present in the array (true means present).



def count_sheeps(sheep):
    result = 0 
    
    for i in sheep:
        if i == True:
            result += 1
    return result 