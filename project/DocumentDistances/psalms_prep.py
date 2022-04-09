import os
# NOTE: this file does 

def prep_rsvce():
    in_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsRSVCE.txt"
    in_file = open(in_path)
    out_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsRSVCEprep.txt"
    out_file = open(out_path, 'w')
    for line in in_file:
        if "a psalm" in line.lower(): continue 
        if line == "\n": continue
        words = line.split(' ')
        out_line = ""
        for word in words:
            out_line += word + " "
        out_file.write(out_line)

        


def prep_kjv():
    in_path = os.getcwd() + "//project//Datasets//Psalms//kjvtemp.txt"
    in_file = open(in_path)
    out_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsKJVprep.txt"
    out_file = open(out_path, 'w')
    for line in in_file:
        if line == "\n": continue
        words = line.split(' ')
        if words[0][1].isnumeric(): words = words[1:]
        else: continue

        out_line = ""
        for word in words:
            out_line += word + " "
        out_file.write(out_line)


prep_rsvce()
# prep_kjv()