"""Write a python program to find the wordcount in a file (input.txt) for each line and then print the output.
 o Finally store the output in output.txt file."""


"reading input file"
infile=open("/Users/venkatavarunnelakuditi/Desktop/input.txt",'r')
"saving lines in a varible"
lines=infile.readlines()
"declaring a dictionary"
d=dict()
"converting lines into list of line"
for line in lines:
    "strip the space before and after the string"
    line=line.strip()
    "converting line into list of word"
    words=line.split()
    "checking word in dictionary and updating the count"
    for word in words:
        if word in d:
            d[word]=d[word]+1
        else:
            d[word]=1
outfile=open("/Users/venkatavarunnelakuditi/Desktop/output.txt",'w')
text=""
"writing into the string and coping to file"
for key in list(d.keys()):
    text=text+str(key) +" : " +str(d[key])+"\n"
outfile.write("output: \n"+ text)
