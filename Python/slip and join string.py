def split_and_join(line):
    s_line = line.split(" ")
    return "-".join(s_line)

if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)