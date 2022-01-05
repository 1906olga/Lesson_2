import builtins

def open(path):
    f = builtins.open(path, 'r')
    return UpperCaser(f)
