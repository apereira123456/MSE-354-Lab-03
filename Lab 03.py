import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

blue = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-354-Lab-03\Data - Blue.csv')
green = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-354-Lab-03\Data - Green.csv')
orange = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-354-Lab-03\Data - Orange.csv')
red = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-354-Lab-03\Data - Red.csv')
yellow = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-354-Lab-03\Data - Yellow.csv')


## Transmission
w = blue.iloc[:, 0]
blue_T = blue.iloc[:, 1]
green_T = green.iloc[:, 1]
orange_T = orange.iloc[:, 1]
red_T = red.iloc[:, 1]
yellow_T = yellow.iloc[:, 1]

fig_1 = plt.figure(dpi=300)
plt.plot(w, blue_T, 'blue', label = r'Blue Glass')
plt.plot(w, green_T, 'green', label = r'Green Glass')
plt.plot(w, orange_T, 'orange', label = r'Orange Glass')
plt.plot(w, red_T, 'red', label = r'Red Glass')
plt.plot(w, yellow_T, 'yellow', label = r'Yellow Glass')
    
plt.title('Transmission')
plt.xlabel(r'Wavelength (nm)')
plt.ylabel(r'Transmission (%)')
plt.legend(loc='lower right')

fig_1.savefig('transmission.png')


## Absorbance
blue_A = pd.Series(801)
green_A = pd.Series(801)
orange_A = pd.Series(801)
red_A = pd.Series(801)
yellow_A = pd.Series(801)

for i in range(0,801):
    if blue_T[i] == 0:
        blue_A[i] = 2 - np.log10(blue_T[i] + 10**(-5))
    else:
        blue_A[i] = 2 - np.log10(blue_T[i])
        
    if green_T[i] == 0:
        green_A[i] = 2 - np.log10(green_T[i] + 10**(-5))
    else:
        green_A[i] = 2 - np.log10(green_T[i])
        
    if orange_T[i] == 0:
        orange_A[i] = 2 - np.log10(orange_T[i] + 10**(-5))
    else:
        orange_A[i] = 2 - np.log10(orange_T[i])
        
    if red_T[i] == 0:
        red_A[i] = 2 - np.log10(red_T[i] + 10**(-5))
    else:
        red_A[i] = 2 - np.log10(red_T[i])
        
    if yellow_T[i] == 0:
        yellow_A[i] = 2 - np.log10(yellow_T[i] + 10**(-5))
    else:
        yellow_A[i] = 2 - np.log10(yellow_T[i])
        
fig_2 = plt.figure(dpi=300)
# plt.plot(w, blue_A, c='blue', label = r'Blue Glass')
# plt.plot(w, green_A, c='green', label = r'Green Glass')
# plt.plot(w, orange_A, c='orange', label = r'Orange Glass')
# plt.plot(w, red_A, c='red', label = r'Red Glass')
# plt.plot(w, yellow_A, c='yellow', label = r'Yellow Glass')

plt.scatter(w, blue_A, s=2, c='blue', label = r'Blue Glass')
plt.scatter(w, green_A, s=2, c='green', label = r'Green Glass')
plt.scatter(w, orange_A, s=2, c='orange', label = r'Orange Glass')
plt.scatter(w, red_A, s=2, c='red', label = r'Red Glass')
plt.scatter(w, yellow_A, s=2, c='yellow', label = r'Yellow Glass')
    
plt.title('Absorbance')
plt.xlabel(r'Wavelength (nm)')
plt.ylabel(r'Absorbance')
plt.legend(loc='upper right')

fig_2.savefig('absorbance.png')


## Absorption
blue_t = blue.iloc[:, 2]
green_t = green.iloc[:, 2]
orange_t = orange.iloc[:, 2]
red_t = red.iloc[:, 2]
yellow_t = yellow.iloc[:, 2]

blue_a = pd.Series(801)
green_a = pd.Series(801)
orange_a = pd.Series(801)
red_a = pd.Series(801)
yellow_a = pd.Series(801)

for i in range(0,801):
    blue_a[i] = np.log(10) / blue_t[0] * blue_A[i]
    green_a[i] = np.log(10) / green_t[0] * green_A[i]
    orange_a[i] = np.log(10) / orange_t[0] * orange_A[i]
    red_a[i] = np.log(10) / red_t[0] * red_A[i]
    yellow_a[i] = np.log(10) / yellow_t[0] * yellow_A[i]
        
fig_3 = plt.figure(dpi=300)
plt.scatter(w, blue_a, s=2, c='blue', label = r'Blue Glass')
plt.scatter(w, green_a, s=2, c='green', label = r'Green Glass')
plt.scatter(w, orange_a, s=2, c='orange', label = r'Orange Glass')
plt.scatter(w, red_a, s=2, c='red', label = r'Red Glass')
plt.scatter(w, yellow_a, s=2, c='yellow', label = r'Yellow Glass')
    
plt.title('Absorption')
plt.xlabel(r'Wavelength (nm)')
plt.ylabel(r'Absorption (cm$^{-1}$)')
plt.legend(loc='upper right')

fig_3.savefig('absorption.png')