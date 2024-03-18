# Util file i wrote to easily process .csv (basically .txt so you can open in notepad)

import os

def trim(arr):
    result = []
    for string in arr:
        result.append(string.strip().replace("\n", ""))
    return result

class CSVFile():
    def __init__(self, filename):
        # All CSVFile files are in  ./playerdata
        self.directory = os.path.join(os.getcwd(), "playerdata")
        self.path = os.path.join(self.directory, filename + ".csv")
    
    # Util functions to shorthand on python's file methods

    def openFile(self, type):
        return open(self.path, type)
    
    def fileExists(self):
        return os.path.exists(self.path)

    def directoryExists(self):
        return os.path.exists(self.directory)

    # Return a read stream to the file,
    def openReadStream(self):
        return CSVReadStream(self.openFile("r"))
    
    # Return a write stream to the file, create a file if it doesent exist
    def openWriteStream(self):
        if (not self.fileExists()):
            if (not self.directoryExists()):
                os.makedirs(self.directory)
            file = self.openFile("x")
        else:
            file = self.openFile("w")
        return CSVWriteStream(file)


# Returned from a CSVFile, used to read data from   
class CSVReadStream():
    def __init__(self, file):
        self.file = file
        self.fields = []
        linesData = self.file.readlines()
        for line in linesData:
            line = line.strip()
            if (not (line.startswith("#") or line == "")):
                self.fields += trim(line.split(","))

        self.fieldIndex = 0
        self.fieldsLength = len(self.fields)

    def readField(self):
        self.fieldIndex += 1
        if (self.fieldIndex <= self.fieldsLength):
            return self.fields.pop(0)
        else:
            return ""

    def readFields(self, length):
        result = []
        for _ in range(length):
            field = self.readField()
            result.append(field)
        return result

    def hasEnded(self):
        return self.fieldIndex >= self.fieldsLength

    def close(self):
        self.file.close()

# Returned from a CSVFile, used to write data back into the file on the disk itself
class CSVWriteStream():
    def __init__(self, file):
        self.file = file

    def writeFieldsLine(self, fields):
        self.file.write(", ".join(fields) + "\n")

    def writeCommentLine(self, comment):
        self.file.write("# " + comment + "\n")

    def writeEmptyLine(self):
        self.file.write("\n")
    
    def close(self):
        self.file.close()