import subprocess
import csv

D = input(str("Enter Domain name:"))
v = input(str("Do you want to save outputs in csv ? type Y or N :"))
print ("Enumerating subdomains for",D)

command = f"sublist3r -d {D} | tail -n +26"
A = subprocess.run(command, capture_output=True, text=True, shell=True)
B = subprocess.run(["subfinder","-d",D], capture_output=True, text=True)
C = subprocess.run(["assetfinder","-subs-only",D],capture_output=True, text=True)

def arrange_output(output):
    lines = output.strip().split("\n")
    rows = [Line.split(",") for Line in lines]
    return rows

output1 = arrange_output(A.stdout)
output2 = arrange_output(B.stdout)
output3 = arrange_output(C.stdout)

all_rows = output1 + output2 + output3

if v == "Y":
    output_file = "subdomains.csv"
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(all_rows)
    print(f"Combined CSV file has been created: {output_file}")
elif v == "N":
    for row in all_rows:
        print(",".join(row))

associate = subprocess.run("")
