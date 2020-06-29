import os.path, fnmatch,shutil,sys
from io import StringIO
from os import path


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
