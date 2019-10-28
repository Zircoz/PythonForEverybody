'''
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.

Expected output: 0.8475
'''

text = "X-DSPAM-Confidence:    0.8475";
colon = text.find(":") #stores the position of colon in variable
slicedText = text[(colon+1):] #slices from whitespaces to the end
slicedTrimmedText = slicedText.strip() #removes ending and starting whitespaces
number = float(slicedTrimmedText)  #turns the string to float
print(number)
