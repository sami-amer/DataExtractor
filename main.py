##https://stackoverflow.com/questions/1724693/find-a-file-in-python


import os.path, fnmatch,shutil,sys
from io import StringIO
from os import path
## This files path
##~/Library/Mobile\ Documents/com~apple~CloudDocs/Documents/School_files/Spring_2020/UROP/Data_Extractor
##HardDrive path
##/Volumes/My Passport/study_1
##/Volumes/ASUS/Wellness

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def move(L):
    '''
    The list is a list of paths
    '''
    for path in L:
        source = path
        name = os.path.basename(os.path.normpath(path))
        destination = r'C:\Users\Blender\iCloudDrive\Documents\School_Files\Spring_2020\UROP\Resources\Agreeability\Extracted' + name # edit this to move
        shutil.copyfile(source, destination)

if __name__ == "__main__":
    paths = (find('*.txt', r'C:\Users\Blender\iCloudDrive\Documents\School_Files\Spring_2020\UROP\Resources\Agreeability\Extracted\ExtractedIrene'))
    print(paths)
