# -*- coding: utf-8 -*-
"""
Title-->            Angular Spectrym Example
Author-->           Ana Doblas, Carlos Trujillo, Raul Castaneda,
Date-->             03/03/2019
Last modified-->    16/07/2020
                    University of Memphis
                    Optical Imaging Research lab (OIRL)
                    EAFIT University
                    Applied Optics Group
Abstract -->        Sample code to use the angular spectrum method to observe different Fresnel Zones
Links-->          - https://unal-optodigital.github.io/JDiffraction/
"""

import numpy as np

import numericalPropagation
from utilities.display import show
import utilities

#pyDiffraction welcome message
utilities.salutation()

#Load an image and automatically converts it into a gray-scale image
hologram = utilities.imread('data/HoloMedal_3.tif')

#Display an gray value image with the given title
show (hologram, 'Hologram')

#This function calculates the propagated complex field of an input transmitance 
#(in this case this function is used to numerically reconstruct an hologram)
complexfield = numericalPropagation.fresnel( (hologram - np.average(hologram)), 532e-9, 3.480, 4.5e-6, 4.5e-6)

#This function calculates the amplitude representatin of a given complex field
#(The second parameter allows to determine if a log operation is performed)
out = utilities.display.amplitude(complexfield, True)

#Display an gray value image with the given title
show (out, 'Amplitude recontruction - log display')

