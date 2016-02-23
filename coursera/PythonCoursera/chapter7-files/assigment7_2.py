'''
Created on 23/02/2016

@author: Carlos
'''

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"
fh = open(fname)
value = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    pos = line.find(".")
    value = value + float(line[pos:].strip()) 
    count = count + 1
print "Average spam confidence: " + str(value/count)
