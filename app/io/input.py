import pandas as pd
def inputFromConsole():
    """
    Returns input from console
    """
    return input()

def readFromFile(path):
    """
    Reads the file

    Input:
    path to the file - string

    Output:
    Content from the file - string
    """
    return open(path,'r').read()

def readWithPandas(path):
    """
        Reads the file using Pandas

        Input:
        path to the file - string

        Output:
        Content from the file - string
        """
    return pd.read_csv(path).to_string()