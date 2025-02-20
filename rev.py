import csv

# 입력 파일과 출력 파일 지정
input_file = "data.csv"  # 원본 파일
output_file = "filtered_data.csv"  # 수정된 파일

def filter_data(input_file, output_file):
    with open(input_file, "r", newline="") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            # 마지막 열이 "780.33"이면 빈 문자열로 대체
            row = ["" if cell == "780.33" else cell for cell in row]
            writer.writerow(row)

# 실행
filter_data(input_file, output_file)
print(f"Filtered data saved to {output_file}")
