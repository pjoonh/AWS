import csv

input= "원본파일명.csv" 
output = "수정후파일명.csv"

def rev_file(input, output):
    with open(input, "r", newline="") as infile, open(output, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            row = ["" if cell == "780.33" else cell for cell in row]
            writer.writerow(row)


rev_file(input, output)
print("rev done")
