import math
def originCord():
    x_init, y_init = map(int,input("Enter a x and y origin cordinates:").split())
    n = int(input("how many cordinates do you want:"))
    new_cords = []
    for i in range(n):
        xcord, ycord = map(int,input().split())
        new_cords.append([xcord,ycord])
    #print(new_cords[0][0])
    #here i will use plane distance formula
    #pow(x_init-x_cord, 2) + pow(y_init - y_cord, 2)
    #here i assigen Distance 1D array or list
    distance  = []
    for i in range(len(new_cords)):
        j = 0
        val = math.sqrt(pow(x_init - new_cords[i][j], 2) + pow(y_init - new_cords[i][j+1], 2))
        distance.append(val)
    #what the minimum value in distance list
    print(min(distance))
    #when i am getting minimum distance then i am finding index number
    row_number = distance.index(min(distance))
    print(row_number)
    #when i got index number or row_number then i am printing which cordinates it's nearby origin-cords(like --> x_init and y_init)
    print(new_cords[row_number])

if __name__=="__main__":
    originCord()

