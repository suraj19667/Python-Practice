numbs=(input("Enter the Number:"))
freq_map=dict()
for i in range(0,len(numbs)):
    if numbs[i] in freq_map:
        freq_map[numbs[i]]+=1
    else:
        freq_map[numbs[i]]=1
print(freq_map)