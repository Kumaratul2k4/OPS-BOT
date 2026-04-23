import os
from datetime import datetime

# input file name
inputfile = "server.log"

# output file name
curr_date = datetime.now().strftime("%Y-%m-%d")
outputfile = f"security_alert_{curr_date}.txt"

# keywords that we have to filter out
keywords = ["ERROR", "CRITICAL", "FAILED LOGIN"]

# Dictionary for counting keywords
Count  = {
    "ERROR": 0,
    "CRITICAL": 0,
    "FAILED LOGIN": 0
}

# List to store all filtered lines
filtered_line = []

# Step 1 : Read and parse the file
# Step 2 : Filter the keywords
# Step 3 : Write the filtered lines to the output file
with open(inputfile,'r') as file:
    for line in file:
        line = line.strip()

        for key in keywords:
            if key in line:
                filtered_line.append(line)
                Count[key]+=1
            
with open(outputfile,'w') as output:
    output.write("---Security Alert Report---\n")
    output.write("\n")

    for line in filtered_line:
        output.write(line+'\n')
    output.write("\n")
    output.write("---Summary---\n")
    for key in Count:
        output.write(f"{key}:{Count[key]}\n")

# Step 4: Automation Check
if os.path.exists(outputfile):
    print("File created successfully")
    print("File size:", os.path.getsize(outputfile), "bytes")
else:
    print("File not created.")

