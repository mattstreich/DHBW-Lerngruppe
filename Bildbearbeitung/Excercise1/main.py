import cv2
import ImageManipulation as IM
import Utilities


#Group F: Daniel Arnaudo, Daniel Christen, Jan Geppert & Matthias Streich

# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Course')

    # Your code here
    image_path="./Baum.jpg"
    pic = cv2.imread(image_path,1)
    #Manipulation of the Image
    IM.myFirstImageManipulation(pic) 
    #Print Details for BGR
    IM.printImageDetails(pic)
    #Print Details for BW
    picBW = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
    IM.printImageDetails(picBW)
    