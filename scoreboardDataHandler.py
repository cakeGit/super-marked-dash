import csvStreamer
import constants

# the start of the level filenames, scoreboard-1.csv
filenameRoot = "scoreboard"

class ScoreboardDataHandler():
    def __init__(self, levelNumber):
        self.level = levelNumber
        self.filename = filenameRoot + "-" + levelNumber
        self.scoreboardFile = csvStreamer.CSVFile(self.filename)
        self.scores = []
        self.read()

    # Sort the array and remove excess
    def formatScores(self):
        # Sort
        self.scores.sort(reverse=False, key=lambda o: o[1])
        print("Sorted scores: ", self.scores)

        # If there is more than the max, limit the list and put a note in the log
        if len(self.scores) > constants.SCORES_MAX_LENGTH:
            print("Removed excess score(s)")
            self.scores = self.scores[0:constants.SCORES_MAX_LENGTH]

    # Add in a new entry to the scoreboard, sort the rankings, and save the file
    def put(self, name, score):
        if (name == ""):
            name = "Unknown"

        self.scores.append([name, score])
        self.formatScores()
        self.write()

    # Write from scoreboard.csv -> See scvStreamer.py
    def write(self):
        stream = self.scoreboardFile.openWriteStream()

        stream.writeCommentLine("Scoreboard data for Super Market Dash")
        stream.writeCommentLine("Format is: name, score")
        stream.writeEmptyLine()

        for entry in self.scores:
            stream.writeFieldsLine([ entry[0], str(entry[1]) ])
        
        stream.close()
        print("Saved scores to"+self.filename+".csv")

    # Read from scoreboard.csv -> See scvStreamer.py
    def read(self):

        if not self.scoreboardFile.fileExists():
            print("Tried to read user data from "+self.filename+".csv but file doesent exist")
            return
        else:
            readScores = [] #Dont want to change the actual scores variable unless we are sure it was valid
            readStream = self.scoreboardFile.openReadStream() #Open the stream

            while not readStream.hasEnded():
                pair = readStream.readFields(2) #Read 2 fields at a time

                #Check that the fields are not empty
                if (pair[0] == "" or pair[1] == ""):
                    print("Incorrect formatting in "+self.filename+".csv, missing / empty fields!")
                    return #Cancel reading
                
                #The second field should be a number, so check
                try:
                    score = int(pair[1])
                except ValueError:
                    print("Incorrect formatting in "+self.filename+".csv, score is not an integer (of time in 1/100 seconds)!")
                    return #Cancel reading

                readScores.append([pair[0], score])

            print("Read scores: ", readScores)
            self.scores = readScores
            self.formatScores()

    # Return a string list to be displayed
    def getStringEntries(self):
        entries = [] #Create a list to be returned
        index = 1 #Track the current ranking of the entry

        for entry in self.scores:
            #Add in an entry formatted as Ranking. Name: Time
            entries.append(str(index) +  ". " + entry[0] + ": " + str(entry[1] /100),)
            index += 1

        return entries