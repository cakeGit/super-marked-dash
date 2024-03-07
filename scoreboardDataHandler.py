import csvStreamer
import constants

filename = "scoreboard"
scoreboardFile = csvStreamer.CSVFile(filename)

scores = []

# Sort the array and remove excess
def formatScores():
    global scores
    scores.sort(reverse=True, key=lambda o: o[1])
    print("Sorted scores: ", scores)
    if len(scores) > constants.SCORES_MAX_LENGTH:
        print("Removed excess score(s)")
        scores = scores[0:constants.SCORES_MAX_LENGTH]

# Write from scoreboard.csv -> See scvStreamer.py
def put(name, score):
    global scores

    if (name == ""):
        name = "Unknown"

    scores.append([name, score])
    formatScores()
    write()

# Write from scoreboard.csv -> See scvStreamer.py
def write():
    stream = scoreboardFile.openWriteStream()

    stream.writeCommentLine("Scoreboard data for Super Market Dash")
    stream.writeCommentLine("Format is: name, score")
    stream.writeEmptyLine()

    for entry in scores:
        stream.writeFieldsLine([ entry[0], str(entry[1]) ])
    
    stream.close()
    print("Saved scores to"+filename+".csv")

# Read from scoreboard.csv -> See scvStreamer.py
def read():
    global scores

    if not scoreboardFile.fileExists():
        print("Tried to read user data from "+filename+".csv but file doesent exist")
        return
    else:
        readScores = [] #Dont want to change the actual scores variable unless we are sure it was valid
        readStream = scoreboardFile.openReadStream()

        while not readStream.hasEnded():
            pair = readStream.readFields(2)

            if (pair[0] == "" or pair[1] == ""):
                print("Incorrect formatting in "+filename+".csv, missing / empty fields!")
                return
            
            try:
                score = int(pair[1])
            except ValueError:
                print("Incorrect formatting in "+filename+".csv, score is not an integer!")
                return

            readScores.append([pair[0], score])

        print("Read scores: ", readScores)
        scores = readScores
        formatScores()

# Return a string list to be displayed
def getStringEntries():
    entries = []
    index = 1
    for entry in scores:
        entries.append(str(index) +  "." + entry[0] + ": " + str(entry[1] /10) + "0",)
        index += 1
    return entries

read()