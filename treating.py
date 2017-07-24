import copy
letterdict = { "a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9,
               "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18,
               "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25 }

zerolist = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
otherfile = open('procds.txt', 'a')
with open('LetterDataSet.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        values = line.split(',')
        position = letterdict[values[0].lower()]
        helpList = copy.copy(zerolist)
        helpList[position] = 1
        helpList2 = []
        for i in range(1, 17):
            helpList2.append(int(values[i]))
        otherfile.write(str(helpList2) + "!" + str(helpList)+"\n") 
