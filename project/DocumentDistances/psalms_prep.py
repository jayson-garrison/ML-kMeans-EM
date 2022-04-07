import os
# NOTE: this file does 

def prep_rsvce():
    in_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsRSVCE.txt"
    in_file = open(in_path)
    out_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsRSVCEprep.txt"
    out_file = open(out_path, 'w')
    for line in in_file:
        if "psalm of" in line.lower() or "of david" in line.lower() or "Maskil" in line or "choirmaster" in line.lower() or "a prayer of" in line.lower() or "a psalm for" in line.lower(): continue
        words = line.split(' ')
        if words[0] == 'Psalm': continue
        if words[0] == '1*': words = words[1:]
        
        out_line = ""
        for word in words:
            if word[0].isnumeric():
                out_line+="\n"
                out_file.write(out_line)
            else:
                out_line += word+' '


def prep_kjv():
    in_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsKJV.txt"
    in_file = open(in_path)
    out_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsKJVprep.txt"
    out_file = open(out_path, 'w')
    for line in in_file:
        if line == "\n": continue
        words = line.split(' ')
        if words[0][0].isnumeric(): words = words[1:]

        out_line = ""
        for word in words:
            out_line += word + " "
        out_file.write(out_line)


# prep_rsvce()
# prep_kjv()