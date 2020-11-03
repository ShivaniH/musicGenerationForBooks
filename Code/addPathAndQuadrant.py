import pandas as pd
import matplotlib.pyplot as plt

pianoMidiCSV = pd.read_csv("pianoMidiVA_Init.csv")

# print(pianoMidiCSV.head())

quadrantNumbers = []

filePaths = []

valenceValues = pianoMidiCSV["Valence"].to_list()
arousalValues = pianoMidiCSV["Arousal"].to_list()

for i in range(len(valenceValues)):

    if valenceValues[i] >= 0.5:

        if arousalValues[i] >= 0.5:
            quadrantNumbers.append(1)
        else:
            quadrantNumbers.append(4)

    else:

        if arousalValues[i] >= 0.5:
            quadrantNumbers.append(2)
        else:
            quadrantNumbers.append(3)


######## trying to shift the X-axis lower ############

# arousalInc = [x+0.35 for x in arousalValues]

# modQuadrantNumbers = []

# for i in range(len(valenceValues)):

#     if valenceValues[i] >= 0.5:

#         if arousalInc[i] >= 0.5:
#             modQuadrantNumbers.append(1)
#         else:
#             modQuadrantNumbers.append(4)

#     else:

#         if arousalInc[i] >= 0.5:
#             modQuadrantNumbers.append(2)
#         else:
#             modQuadrantNumbers.append(3)

# quad1 = 0
# quad2 = 0
# quad3 = 0
# quad4 = 0

# for i in range(len(modQuadrantNumbers)):
#     if modQuadrantNumbers[i] == 1:
#         quad1 += 1
#     elif modQuadrantNumbers[i] == 2:
#         quad2 += 1
#     elif modQuadrantNumbers[i] == 3:
#         quad3 += 1
#     else:
#         quad4 += 1

# print("quad1 = ", quad1)
# print("quad2 = ", quad2)
# print("quad3 = ", quad3)
# print("quad4 = ", quad4)

#################################################



# quad1 = 0
# quad2 = 0
# quad3 = 0
# quad4 = 0

# for i in range(len(quadrantNumbers)):
#     if quadrantNumbers[i] == 1:
#         quad1 += 1
#     elif quadrantNumbers[i] == 2:
#         quad2 += 1
#     elif quadrantNumbers[i] == 3:
#         quad3 += 1
#     else:
#         quad4 += 1

# print("quad1 = ", quad1)
# print("quad2 = ", quad2)
# print("quad3 = ", quad3)
# print("quad4 = ", quad4)




# plt.scatter(valenceValues, arousalValues)
# plt.title('VA pianoMidi')
# plt.xlabel('Valence')
# plt.ylabel('Arousal')
# plt.show()




# pianoMidiCSV["Quadrant"] = quadrantNumbers

# pianoMidiCSV.to_csv("pianoMidiVA_2.csv", index=False)