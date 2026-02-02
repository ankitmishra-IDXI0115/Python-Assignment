#Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n 
# (where n is the number of lines in the file).

def number_lines(input_file, output_file):
    with open(input_file) as fin, open(output_file, "w") as fout:
        for i, line in enumerate(fin, start=1):
            fout.write(f"{i}: {line}")
