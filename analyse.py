import numpy as np
from matplotlib import pyplot as plt

with open("datafile.csv") as file_name:
    dataarray = np.loadtxt(file_name, delimiter=", ", skiprows=1)

    
mlist = []

for line in dataarray:
    # Calculate the invariant mass (in GeV) of the first two light jets:
    m12 = np.sqrt((line[13]+line[17])**2 - (line[14]+line[18])**2 - (line[15]+line[19])**2 - (line[16]+line[20])**2)/1000
    # Example for a code that selects pairs of jets which fulfill a condition and appends them to a list
    if abs(m12)<150:
            mlist.append(m12)

mean = np.mean(mlist)
print('Mean: ', mean)
          
plt.hist(mlist, bins=20, range=(40,120), label="m(j1j2) [GeV]") 
plt.xlabel("m(j1j2) [GeV]")
plt.savefig('Mj1j2.png')
plt.show()
                
     
