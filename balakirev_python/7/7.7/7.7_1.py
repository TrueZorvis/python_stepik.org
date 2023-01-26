F = {
    'C:': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    }
}


def get_files(path, depth=0):
    for f in path:
        print(" " * depth, f)
        if type(path[f]) is dict:
            get_files(path[f], depth + 2)
        else:
            print(" " * (depth + 2), " ".join(path[f]))


get_files(F)
