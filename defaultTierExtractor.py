from main import find
import csv
import pandas as pd


def get_defaults(paths):
    #tag, start, stop, duration, notes
    output = []
    for path in paths:
        with open(path,'r') as f:
            for line in f:
                line = line.split("\t")
                del line[1]
                line[-1] = line[-1].strip("\n")
                if line[0] == 'default':
                    duration = line[3]
                    subjectNumber = (path[44:47])
                    sessionNumber =(path[48:51])
                    annotator = (path[38:43])
                    text = line[4]
                    time = line[1]

                    toAdd = [time,duration, annotator,sessionNumber,subjectNumber,text]
                    output.append(toAdd)
    return output
                

def import_paths_from_txt(txt):  ## **DONE**
    """
    borrowed from data counter, imports lines as elements of a list.

    allows us to store paths in persistent .txt file, and just pull from that

    arguments:
        txt (str): path to text file with paths

    returns:
        out (list): list where elements are paths
    """

    out = pd.read_csv(txt, header=None).values.flatten().tolist()
    return out

def writeToCSV(inp):
    with open("output.csv",'w',newline="") as f:
        writer = csv.writer(f)
        writer.writerows(inp)

if __name__ == "__main__":
    paths = import_paths_from_txt('pathsTotal.txt')
    L = get_defaults(paths)
    writeToCSV(L)
    # path = "/home/sami/Work/resources/inter-rater/Emily/P01/S02/P01_S02_wellness_Emily.txt"
    # print(path[48:51])