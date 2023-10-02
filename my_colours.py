"""
This module contains functions for generating a rainbow colour palette
"""

# returns an array of html colour codes for n evenly spaced colours from red (#ff0000) to magenta (#ff00ff)
def find_rainbow_palette(n):
    """
    This function generates a rainbow colour palette containing n colours
    
    Args:
       n (int): the desired number of colours in the generated palette
    
    Returns:
       list: a list of colours in hex format
    """

    palette = []
    ind1d = 0
    di = 5/(n-1)

    for i in range(n):
        # red
        if ind1d == 0:
            ind3d = [1, 0, 0]
        # -> yellow
        elif ind1d <= 1:
            ind3d = [1, ind1d, 0]
        # -> green
        elif ind1d <= 2:
            ind3d = [2-ind1d, 1, 0]
        # -> cyan    	
        elif ind1d <= 3:
            ind3d = [0, 1, ind1d-2]
        # -> blue
        elif ind1d <= 4:
            ind3d = [0, 4-ind1d, 1]
        # -> magenta
        elif ind1d <= 5:
            ind3d = [ind1d-4, 0, 1]
        
        # convert from fractional to 0 to 255 format
        ind3d = [int(ind * 255) for ind in ind3d]
        
        # commented print statement, in case debugging is needed
        #print(i, ind1d, ind3d)
        
        # convert to hex format
        hex_colour = rgb_to_hex(ind3d)
        
        # add to our palette
        palette.append(hex_colour)
        
        ind1d += di

    return palette


def rgb_to_hex(rgb):
    """
    This function converts a colour from rgb format to hex format
    
    Args:
       rgb (list): the colour in rgb format (a list of size 3 with values from 0 to 255)
    
    Returns:
       str: the colour in hex format (a 7 character string)
    """
    
    # a list with the characters as integers
    hexi = [0] * 6
    # a list with the characters fully converted to hex format
    hexs = [0] * 6
    
    # convert the rgb values to integers
    hexi[0] = int(rgb[0]/16)
    hexi[1] = int(rgb[0]%16)
    hexi[2] = int(rgb[1]/16)
    hexi[3] = int(rgb[1]%16)
    hexi[4] = int(rgb[2]/16)
    hexi[5] = int(rgb[2]%16)
    
    # take care of the special characters
    for j in range(6):
        if (hexi[j]==10):
            hexs[j]='a'
        elif (hexi[j]==11):
            hexs[j]='b'
        elif (hexi[j]==12):
            hexs[j]='c'
        elif (hexi[j]==13):
            hexs[j]='d'
        elif (hexi[j]==14):
            hexs[j]='e'
        elif (hexi[j]==15):
             hexs[j]='f'
        else:
            hexs[j]=hexi[j]
        
        # convert the output to a string
        hex_string = '#'+str(hexs[0])+str(hexs[1])+str(hexs[2])+str(hexs[3])+str(hexs[4])+str(hexs[5])
    
    return hex_string
