"""""
--Hadeed Pall
--Cs 1026
--Assignment 2
--Octoer 21,2020
"""""

import volumes
#creating variables for calculations
length_cube= 0
base_pyramid = 0
height_pyramid = 0
radius_P= 0
radius_T= 0
radius_TH=0
output_list=[]
# Function that makes sure users input is valid even if its upper or lower case
def formatInput(textline) :
    textLine = textline.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return  textLine
invalid_choice = False
# list with all the available options for the user
shapes=["c","cube","pyramid", "p", "ellipsoid","e","q","quit"]
# while Loop to check whether the choice of shape  is in the selection/process code if it is
while not invalid_choice:
    user_choice= formatInput(input("Please enter a shape(quit/q, cube/c, pyramid/p, ellipsoid/e):"))
    if user_choice == "q" or user_choice== "quit":
        break
    if user_choice not in shapes:
        while user_choice not in shapes:
            print("Sorry you can not select this shape, please try again")
            break
        continue
        user_choice= formatInput(input("Please enter a shape(quit/q, cube/c, pyramid/p, ellipsoid/e):"))
        if user_choice == "q" or user_choice=="quit":
            break
        continue
 #  statement for if the user chooses the cube shape
    if user_choice== "cube" or user_choice== "c":
            user_choice= "cube"
            length_cube= (input("Enter length of side of the cube:"))
            length_cube= float(length_cube)
            volume = volumes.volume_cube(length_cube)
            print("The volume of a cube with length",length_cube, "is",volume)
            print("%.2f"%volume)
            output_list.append((user_choice, volume))

 #  statement for if the user chooses the pyramid shape
    elif user_choice== "pyramid" or user_choice=="p":
            user_choice= "pyramid"
            pyramid_base= (input("Enter the base of the pyramid:"))
            pyramid_base= float(pyramid_base)
            pyramid_height =(input("Enter the height of the pyramid:"))
            pyramid_height= float(pyramid_height)
            volume = volumes.volume_pyramid(pyramid_base,pyramid_height)
            print("The volume of a pyramid with base",pyramid_base,"and height:",pyramid_height,"is",volume)
            print("%.2f"%volume)
            output_list.append((user_choice, volume))
#  statement for if the user chooses the ellipsoid shape
    elif user_choice=="ellipsoid" or user_choice=="e":
            user_choice= "ellipsoid"
            radius_P=(input("Enter first radius:"))
            radius_P= float(radius_P)
            radius_T=(input("Enter second radius:"))
            radius_T= float(radius_T)
            radius_TH=(input("Enter third radius:"))
            radius_TH= float(radius_TH)
            volume= volumes.volume_elliposoid(radius_P, radius_T, radius_TH)
            print("The volume of a elliposoid with radii",radius_P,"and",radius_T,"and", radius_TH,"is:",volume)
            print("%.2f"%volume)
            output_list.append((user_choice,volume))




output_list.sort(key=lambda output_list:output_list[1]) # sorts list using the volume value
print()
print("Output: Volume of shapes entered in sorted order: ")
for i in range(len(output_list)):
    shape,volume = (output_list[i]) # the shape and volume values are gathered from the list here
    print("%s %.2f"%(shape,volume))











