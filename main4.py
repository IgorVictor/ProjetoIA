import mnistloader
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

def compare_list(a, b):
        for x in range(len(a)):
                if a[x] != b[x]:
                        return False
        return True

def normalize_list(a):
       lista2 = []
       for b in a:
           if b < 0.6:
              lista2.append(0)
           else :
              lista2.append(1)
       return lista2

net = buildNetwork(16, 21, 26)

trainingset = open("trainingset.txt", "r")
traininglines = trainingset.read().splitlines()
DS = SupervisedDataSet( 16, 26 )
for line in traininglines:
    line = line.replace("[", "")
    line = line.replace("]", "")
    splitline = line.split("!")
    entries = splitline[0].split(",")
    desired =  splitline[1].split(",")
    entries = list(map(int, entries))
    desired = list(map(int, desired))
    
    DS.appendLinked( entries, desired )
trainer = BackpropTrainer(net, DS, 0.01, momentum=0.02)
for i in range(1, 40):
    print(trainer.train())

testingset = open("testingset.txt", "r")
testinglines = testingset.read().splitlines()
counter = 0
correctanswers = 0
for line in testinglines:
    line = line.replace("[", "")
    line = line.replace("]", "")
    values = line.split("!")
    entries = values[0].split(",")
    values = values[1].split(",")
    entries = list(map(int, entries))
    values = list(map(int, values))
    outputlist = normalize_list(net.activate(entries))
    counter = counter +1
    if compare_list(values, outputlist):
        correctanswers = correctanswers +1
print (correctanswers)
print (counter)
print (1.0 - (float(correctanswers)/float(counter))) 
#testingset = open("testingset.txt", "r")
#testinglines = testingset.read().splitlines()
#TDS = SupervisedDataSet( 16, 26 )
#for line in testinglines:
#    line = line.replace("[", "")
#    line = line.replace("]", "")
#    values = line.split("!")
#    entries = values[0].split(",")
#    values = values[1].split(",")
#    entries = list(map(int, entries))
#    output = net.activate(entries)
#    values = list(map(int, values))
#    print("Expected")
#    print(values)
#    print("got")
#    print(output)
