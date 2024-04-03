def outputToConsole(s):
    """
    Outputs the given text to console

    Input:
    s - any object which can be printed
    """
    print(s)
    return

def writeToFile(s,path):
    """
    Outputs the given text to file

    Input:
    s - any object which can be printed
    """
    open(path,'a').write(s)
    return