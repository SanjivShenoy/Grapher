
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 10:01:41 2018

@author: sanjivshenoy
"""

# Project --> Grapher 2.0

"""
1. The user will first be asked how many curves he/she wants to
plot in the graph.

2. If the number of Curves is more than 1, program will ask whether user
wants a single plot or subplots ans in (single/sub)

If user wants sub plots, the user will be asked to enter number of rows and columns.

Then for each subplot - The remaining with some subtle modifications.  


3. The program will then ask you the Title, x axis - label, y axis label if any.(else default will be used)

4. It will then ask you the label for each curve in the legend.

5. It will then ask you whether you want to change x and y start values(kink)
   If yes it will ask you to enter the values.

6. The program will ask you to input (x,y) co-ordinates
each on a new line:
Eg  Curve1:
       2 3
       5 6
       7 8

    Curve2:
       6 7
       8 9
       7 0

7. The output will be a graph in which the curve(s) are plotted.

"""
import pylab as plot
# 1
NoOfCurves = int(input("Please enter the number of curves you would like to plot : "))
print("")
plot.figure('New Figure')
plot.clf
# 2
RC = 'single'
if(NoOfCurves!=1):
    m = input("Do you want subplots(y/n):")
    if(m == 'y'):
        RC = input("Please enter whether row wise or column wise subplot(row/column):")

Title = input("Please enter a title : ")
#plot.suptitle(Title)

#if(RC == 'row'):
#    labelx = input("Please enter x-axis label : ")
#    plot.text(0.5, 0.04, labelx, ha='center')
#
#    
#if(RC == 'column'):
#    labely = input("Please enter y-axis label : ")
#    plot.text(0.04, 0.5, labely, va='center', rotation='vertical')
#    #plot.ylabel(labely)

if(RC == 'single'):
    labelx = input("Please enter x-axis label : ")
    plot.xlabel(labelx)
    labely = input("Please enter y-axis label : ")
    plot.ylabel(labely)

for p in range(NoOfCurves):
    if(RC == "row"):
        plot.subplot(NoOfCurves, 1, p+1)
        labelx = input("Please enter x-axis label : ")
        plot.xlabel(labelx)
        labely = input("Please enter y-axis label : ")
        plot.ylabel(labely)
        
    elif(RC == "column"):
        plot.subplot(1, NoOfCurves, p+1)
        labelx = input("Please enter x-axis label : ")
        plot.xlabel(labelx)
        labely = input("Please enter y-axis label : ")
        plot.ylabel(labely)
    
    elif(RC == 'single'):
        reply = input("Enter whether you want to change x and y limits in (y/n):")
        if(reply == 'y'):
            xlim = [int(i) for i in input("Please enter x limits separated by space: ").strip().split()]
            ylim = [int(i) for i in input("Please enter y limits separated by space: ").strip().split()]

            plot.ylim(ylim[0], ylim[1])
            plot.xlim(xlim[0], xlim[1])
            
        RC = 'done'


# 3
    labelkey = input("Please enter label for curve "+str(p+1)+": ")
    


# 4
    if(RC != 'done'):
        reply = input("Enter whether you want to change x and y limits in (y/n):")
    
        if(reply == 'y'):
            xlim = [int(i) for i in input("Please enter x limits separated by space: ").strip().split()]
            ylim = [int(i) for i in input("Please enter y limits separated by space: ").strip().split()]

            plot.ylim(ylim[0], ylim[1])
            plot.xlim(xlim[0], xlim[1])

# 5

    LAllCurvesX = []
    LAllCurvesY = []

    m = int(input("Please enter the number of points for the curve " + str(p+1)+":"))
    print("Enter points in pairs separated by space and each pair on a new line:")
    print('')
    for i in range(m):
        Pair = [int(k) for k in input().strip().split()]
        LAllCurvesX.append(Pair[0])
        LAllCurvesY.append(Pair[1])

# 7

    plot.plot(LAllCurvesX, LAllCurvesY, label=labelkey)

    plot.legend()
    
plot.tight_layout()
plot.suptitle(Title, y = 1.08)
