import numpy as np
import matplotlib.pyplot as plt
#from PIL import Image
import matplotlib.image as mpimg
#import sys
#import math


#Part 4



def keygenerator(key, rowcount, columncount): #generates the key array
    keycount = len(key) - key.count(" ")
    # keycount = len(key)
    key = []
    for row_index in range(rowcount):
        row = []
        for column_index in range(columncount):
            val = (row_index * column_index) % keycount
            val = val * ((2**8) // keycount)
            row.append(val)
        key.append(row)
    print("The key has been generated.")
    return key

def keygenerator2 (rowcount, columncount):
    randomnumber = np.random.randint(1000)#generates the key array
   
    keycount = randomnumber
    # keycount = len(key)
    key = []
    for row_index in range(rowcount):
        row = []
        for column_index in range(columncount):
            val = (row_index * column_index) % keycount
            val = val * ((2**8)//keycount)
            row.append(val)
        key.append(row)
    print("The key has been generated.")
    return key

def encryptor(image, key1): #decrypts the image
  
    image = np.array(image)
    key1 = np.array(key1)
    for i in range(len(image)):
        for j in range(len(image[i])):
            for k in range(len(image[i][j])):
                image[i][j][k] = image[i][j][k] ^ key1[i][j]
  
    return image

   
   
 

def Display_Histogram(image,names): #displays histograms of different color channels
   
   

    R,B,G = image[:,:,0],image[:,:,1],image[:,:,2]

    #seperating each of the color channels into arrays
    R_Array = np.array(R)
    R_Array = R_Array.flatten()

    B_Array = np.array(B)
    B_Array = B_Array.flatten()
   
    G_Array = np.array(G)
    G_Array = G_Array.flatten()

    #filling histograms with the arrays
    #then saves them

    plt.clf()
    plt.hist(R_Array)
    plt.title("Red Histogram "+names) #allowing to write the histograms with a general name
    plt.show()
    plt.savefig("Red_Histogram "+names)
   

    plt.clf()
    plt.hist(B_Array)
    plt.title("Blue Histogram "+names)
    plt.show()
    plt.savefig("Blue_Histogram "+names)
   
 
    plt.clf()
    plt.hist(G_Array)
    plt.title("Green Histogram "+names)
    plt.show()
    plt.savefig("Green_Histogram "+names)
   


def main():
   
    initialkey= input('Enter a new key: ')
    x=input('Enter name of file: ')
    image= plt.imread(f'{x}')
    Display_Histogram(image,x)  
    oldkey= keygenerator(initialkey,np.array(image).shape[0],np.array(image).shape[1]) #length and the width

    E_image=encryptor(image, oldkey)
   
    Display_Histogram(E_image, 'First Encryption Oldk')
   
    plt.imsave("First_Encryption_Oldk.tiff", E_image)
   
    newkey=keygenerator2(np.array(image).shape[0],np.array(image).shape[1])
    newimageE=encryptor(image, newkey)
    Display_Histogram(newimageE, "Encrypted Image Histogram")
    plt.imsave("Encrypted_Image.tiff", newimageE)
if __name__ == '__main__':
    main()
   
   
   
   