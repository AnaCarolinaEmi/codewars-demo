#Given a random non-negative number
#You have to return the digits of this number within an array in reverse order.

def digitize(n):
    new_array = []
    
    for i in str(n):
        new_array.append(int(i))
    
   
    inversao = new_array[::-1]
        
    
    return inversao