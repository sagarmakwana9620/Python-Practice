def sort(inp):
    return sorted(inp, key=end)

def end(last):
    return last[-1]  
 
inp=input("Enter list of tuples:")
res=sort(inp)

print("Sorted List of tuples:")

print(res)