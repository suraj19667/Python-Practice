def sort_array():
    li = [0,0,1,1,1,2,2,3,3,4]
    li = set(li)        
    li = list(li)       
    li.sort()          
    return len(li)      

print(sort_array())