from app.io.input import *
from app.io.output import *
def main():
    s1,s2,s3=inputFromConsole(),readFromFile("s2.txt"),readWithPandas("s3.csv")
    outputToConsole(s1)
    writeToFile(s1,"o1.txt")
    outputToConsole(s2)
    writeToFile(s2, "o2.txt")
    outputToConsole(s3)
    writeToFile(s3, "o3.csv")
if __name__=="__main__":
    main()
