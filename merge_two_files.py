# Merge two files into a third file

with open('file1.txt') as f1, open('file2.txt') as f2, open('merged_file.txt', 'w') as merged:
    merged.write(f1.read() + '\n')  # Add a newline between file1 and file2 contents
    merged.write(f2.read())
