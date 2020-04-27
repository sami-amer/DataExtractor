from main import find
import csv


Emily = find('*.txt',r'C:\Users\Blender\iCloudDrive\Documents\School_Files\Spring_2020\UROP\Resources\Agreeability\Extracted\ExtractedEmily')
Irene = find('*.txt',r'C:\Users\Blender\iCloudDrive\Documents\School_Files\Spring_2020\UROP\Resources\Agreeability\Extracted\ExtractedIrene')

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
                    subjectNumber = (path[126:129])
                    sessionNumber =(path[130:133])
                    annotator = (path[134:])
                    annotator = annotator.split('.')
                    annotator = annotator[0]
                    text = line[4]
                    time = line[1]

                    toAdd = [time,duration, annotator,sessionNumber,subjectNumber,text]
                    output.append(toAdd)
    return output
                

def writeToCSV(inp):
    with open("output.csv",'w',newline="") as f:
        writer = csv.writer(f)
        writer.writerows(inp)

if __name__ == "__main__":
    Emily.extend(Irene)
    L = get_defaults(Emily)
    writeToCSV(L)
