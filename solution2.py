'''  Q2.You are given with a 1D array of height of towers of a 2D world, 
     consider all towers are adjacent to one another, 
     in the same order as specified the input array

     When it rains, water is collected on top of the towers, if the adjacent towers or their neighbouring towers are actually taller than itself
    Identify the total water which can be collected
'''

def Calculate_water(A):
    #initialization
    water = 0
    #left and right tower
    left = 1 
    right = len(A)-1
    #Capacity initialization
    W_left = A[0]           #lower
    W_right = A[len(A)-1]   #Upper

    while left <= right:
        if A[left] <= A[right]:
            W_left = max(A[left], W_left)
            water  = water + max(W_left - A[left], 0)
            left  = left + 1
        else:
            W_right = max(A[right], W_right)
            water  = water + max(W_right - A[right], 0)
            right  = right - 1
    print(water)

if __name__=="__main__":
    no_of_height = int(input("Enter No of Height:"))
    A = []
    for i in range(no_of_height):
        inp = int(input())
        A.append(inp)
    Calculate_water(A)
    
