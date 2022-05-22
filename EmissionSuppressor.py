#! /usr/bin/env python3
# coding:utf-8

import copy
import math
import os
import sys
from shutil import ignore_patterns, rmtree
from PIL import Image as pimage
from wand.image import Image as wimage

#################### Set Parameters ####################

# Set input and output paths
inputDir = 'content'
outputDir = inputDir

# Max B value, beatween 0 and 255
maxB = 32

#################### Functions ####################

def listDdsFiles(path):
    fileList=[]
    for root,dirs,files in os.walk(path):
        for fileObj in files:
            if '_mg.dds' in fileObj:
                fileList.append(os.path.join(root,fileObj))
    return fileList

def saveSuppressedImage(inputFile, tempFile, outputFile):
    with pimage.open(inputFile) as inputImage:
        inputImage.load()
        for indx in range(inputImage.size[0]):
            for indy in range(inputImage.size[1]):
                coordinate = indx, indy
                currentColor = inputImage.getpixel(coordinate)
                if currentColor[2] > maxB:
                    modifiedColor = list(currentColor)
                    modifiedColor[2] = maxB
                    inputImage.putpixel(coordinate, tuple(modifiedColor))
        inputImage.save(tempFile)
        os.remove(inputFile)
    with wimage(filename = tempFile) as img:
        # img.options['dds:mipmaps'] = '0'
        img.compression = 'dxt5'
        img.save(filename = outputFile)
    os.remove(tempFile)

#################### Main program ####################

# Check folder existence
if not os.path.exists(inputDir):
    print('Incorrect input path')
    sys.exit() 

# Parse dds files
fileList = listDdsFiles(inputDir)
fileNum = 0
fileNumTotal = str(len(fileList))
for fileObj in fileList:
    fileNum = fileNum + 1
    rawPath = fileObj[len(inputDir):len(fileObj)]
    outputFile = outputDir + rawPath
    tempFile = outputDir + rawPath.replace('.dds', '.png')
    inputFile = copy.deepcopy(fileObj)
    print(str(fileNum) + '/' + fileNumTotal + ' Attempt to convert ' + rawPath)
    saveSuppressedImage(inputFile, tempFile, outputFile)
    print('Successfully converted ' + rawPath)
