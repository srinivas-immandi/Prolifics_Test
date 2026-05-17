with open(r"C:\Users\ABC\Downloads\library_records.txt","r") as f:
    all_lines = f.readlines()
    line_line = f.readline()
    Total_no_of_lines = len(all_lines)
print('All_lines:',all_lines)
print('Line_line:',line_line)
print("Total_no_of_lines:",Total_no_of_lines)


