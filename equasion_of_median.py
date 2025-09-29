import math
def readfile():
    # sets all the coordinate points in the file, can be initiated instead of 1 to be n number of times depending on how many sets of coordinates you wish to put in the text file
    x1 = [None] * 1
    y1 = [None] * 1
    x2 = [None] * 1
    y2 = [None] * 1
    # counter +1 on line 21 iterates if we need another set of coordinates to calculate
    counter = 0

    # opens the file and reads into the coordinates text file
    with open("coordanates.txt", "r") as readfile:
        line = readfile.readline().rstrip("\n")
        while line:
            items = line.split(",")
            x1[counter] = int(items[0])
            y1[counter] = int(items[1])
            x2[counter] = int(items[2])
            y2[counter] = int(items[3])

            line = readfile.readline().rstrip("\n")
            counter +=1


    return x1, y1, x2, y2

def find_midpoint(x1, y1, x2, y2):

    #finds the midpoint by looping through x1, by adding x1 and y1 and dividing by 2 and displays the midpoint
    for i in range(len(x1)):
        mid_x = (x1[i] + x2[i]) / 2
        mid_y = (y1[i] + y2[i]) / 2
        print(f"Midpoint {i + 1}: ({int(mid_x)}, {int(mid_y)})")

    return mid_x, mid_y

def find_gradient(y2, y1, x2, x1):

    #finds the gradient by looping through x1 and using the equasion y2-y1 all divided x2-x1
    for i in range(len(x1)):
        gradient = (y2[i] - y1[i]) / (x2[i] - x1[i])

    print(int(gradient))

    # perpendicular gradient can be used if we are calculating the perpendicular bisector
    perpendicular_gradient = -1/gradient


    return gradient, perpendicular_gradient

def the_equasion(mid_x, mid_y, gradient):

    #displays the final equasion in the form y-b = m(x-a)
    print("Equasion: ", "y -",int(mid_y), "=", int(gradient), "( x -", int(mid_x),")")


#calls all the functions
def main():
    x1, y1, x2, y2 = readfile()
    mid_x, mid_y = find_midpoint(x1, y1, x2, y2)
    gradient, perpendicular_gradient = find_gradient(y2, y1, x2, x1)
    the_equasion(mid_x, mid_y, gradient)

main()
