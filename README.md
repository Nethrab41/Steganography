This project explains how LSB Steganography works.
What is LSB Steganography?
Any Digital File is composed of bytes. Like, an Image is made up of tiny squares called as pixels. 
Each pixel has color information representing the red, green and blue color values. Now, Least Significant Bit (LSB) is the last bit in the 8 bit representation.
Say if the value of the color is 100, then it's 8-bit representation would be 01100100. The LSB of this number is 0.
LSB Steganography works by taking a secret message and converting it into it's binary representation (0's and 1's). 
Then, it goes through the image's pixel data and replaces the LSB of the some of the color values with the bits of secret message. 
The small change in the value of the pixel's color is not visible to the human's eye.
This is how LSB's is replaced with the bits of secret message.
