import pandas as pd
import os
import shutil
from collections import Counter

vgMidiCSVTrain = pd.read_csv("vgmidi_train.csv")

vgMidiCSVTest = pd.read_csv("vgmidi_test.csv")

filePaths = os.listdir("../vgMidiDataset")

filePaths.remove("Angry")
filePaths.remove("Happy")
filePaths.remove("Sad")
filePaths.remove("Calm")

# for x in filePaths:
#     print(x)

valenceValues = vgMidiCSVTrain["valence"].to_list()
arousalValues = vgMidiCSVTrain["arousal"].to_list()
trackNames = vgMidiCSVTrain["filepath"].to_list()

trackNames = [x[16:] for x in trackNames]

valenceValuesTest = vgMidiCSVTest["valence"].to_list()
arousalValuesTest = vgMidiCSVTest["arousal"].to_list()
trackNamesTest = vgMidiCSVTest["filepath"].to_list()

trackNamesTest = [x[16:] for x in trackNamesTest]

# print(trackNames[0], valenceValues[0], arousalValues[0])

# print(trackNamesTest[0], valenceValuesTest[0], arousalValuesTest[0])


######## Checking for duplicates #############

# trackCounts = Counter(trackNames)
# testTrackCounts = Counter(trackNamesTest)

# for x in trackCounts:
#     if (trackCounts[x]) > 1:
#         print("alert1")

# for x in testTrackCounts:
#     if(testTrackCounts[x]) > 1:
#         print("alert2")


for i in range(len(valenceValues)):

    if valenceValues[i] == 1:

        if arousalValues[i] == 1:
            # quadrantNumbers.append(1)
            shutil.move("../vgMidiDataset/"+trackNames[i], "../vgMidiDataset/Happy/"+trackNames[i])
        else:
            # quadrantNumbers.append(4)
            shutil.move("../vgMidiDataset/"+trackNames[i], "../vgMidiDataset/Calm/"+trackNames[i])

    else:

        if arousalValues[i] == 1:
            # quadrantNumbers.append(2)
            shutil.move("../vgMidiDataset/"+trackNames[i], "../vgMidiDataset/Angry/"+trackNames[i])
        else:
            # quadrantNumbers.append(3)
            shutil.move("../vgMidiDataset/"+trackNames[i], "../vgMidiDataset/Sad/"+trackNames[i])


for i in range(len(valenceValuesTest)):

    if valenceValuesTest[i] == 1:

        if arousalValuesTest[i] == 1:
            # quadrantNumbers.append(1)
            shutil.move("../vgMidiDataset/"+trackNamesTest[i], "../vgMidiDataset/Happy/"+trackNamesTest[i])
        else:
            # quadrantNumbers.append(4)
            shutil.move("../vgMidiDataset/"+trackNamesTest[i], "../vgMidiDataset/Calm/"+trackNamesTest[i])

    else:

        if arousalValuesTest[i] == 1:
            # quadrantNumbers.append(2)
            shutil.move("../vgMidiDataset/"+trackNamesTest[i], "../vgMidiDataset/Angry/"+trackNamesTest[i])
        else:
            # quadrantNumbers.append(3)
            shutil.move("../vgMidiDataset/"+trackNamesTest[i], "../vgMidiDataset/Sad/"+trackNamesTest[i])