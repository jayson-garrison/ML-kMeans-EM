import os

if __name__ == "__main__":
    email_in_path = os.getcwd() + "//project//Datasets//Email//emails.csv"
    email_out_path = os.getcwd() + "//project//Datasets//Email//email_for_wmd.txt"
    in_file = open(email_in_path)
    out_file = open(email_out_path, 'w')
    vocab = in_file.readline()[6:].split(',')
    for in_line in in_file:
        cts = in_line[6:].split(',')
        cts = list(map(int, cts))
        out_line = ""
        for idx in range(len(vocab)):
            for ct in range(cts[idx]):
                out_line += vocab[idx] + " "
        out_line += "\n"
        out_file.write(out_line)
        






