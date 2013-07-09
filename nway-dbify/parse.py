import sys

def parse_nway(file_path):
    """
    Reference, position, type, base (N), evidence (N), annotations (N)
    """
    with open(file_path) as fin:
        strains = get_strains(fin.readline())
        for line in fin:
            print len(line.split('\t'))

def get_strains(line):
    """
    Returns a list of strain IDs
    """
    number_of_strains = (len(line.split('\t')[4:])-1)/3
    return line.split('\t')[4:(4+number_of_strains)]
