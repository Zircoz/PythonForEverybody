'''
WAP that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at https://pastebin.com/tTb5c2PK

Expected Output -->
Average spam confidence: 0.750718518519
'''

fname = input("Enter file name: ")
fh = open(fname)
total, count = 0, 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    numericValue = line[-7:len(line)].strip()
    count+=1
    total+=float(numericValue)
print("Average spam confidence: " + str(total/count))
