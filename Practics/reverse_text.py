input_file = "text.txt"
input_file2 = "reversed_text.txt"
output_file = "reversed_text.txt"
output_file2 = "text2.txt"
in_data = []
out_data = []


def read_data(file, data: list):
    data.clear()
    fread = open(file, 'r')
    for line in fread:
        data.append(line)
    fread.close()


def write_data(save_to, from_data: list):
    fwrite = open(save_to, 'w')
    for line in from_data:
        fwrite.write(line)
    fwrite.close()


def reverse_text(input_data: list, output_data: list):
    out_data.clear()
    for line in input_data:
        line = line[::-1]
        output_data.append(line)


def main():
    read_data(input_file, in_data)
    reverse_text(in_data, out_data)
    write_data(output_file, out_data)
    read_data(input_file2, in_data)
    reverse_text(in_data, out_data)
    write_data(output_file2, out_data)
    input("\nPress <ENTER> for quit")


if __name__ == "__main__":
    main()
