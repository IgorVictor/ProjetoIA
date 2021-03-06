import mnistloader
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

def compare_list(a, b):
        for x in range(a.len):
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

net = buildNetwork(16, 30, 26)

trainingset = open("trainingset.txt", "r")
traininglines = trainingset.read().splitlines()
DS = SupervisedDataSet( 16, 26 )
for line in traininglines:
    line = line.replace("[", "")
    line = line.replace("]", "")
    values = line.split("!")
    entries = values[0].split(",")
    values = values[1].split(",")
    entries = list(map(int, entries))
    values = list(map(int, values))
    
    DS.appendLinked( entries, values )
trainer = BackpropTrainer(net, DS)
print( trainer.train())
print( trainer.train())
print( trainer.train())
testingset = open("testingset.txt", "r")
testinglines = testingset.read().splitlines()
TDS = SupervisedDataSet( 16, 26 )
#for line in testinglines:
#    line = line.replace("[", "")
#    line = line.replace("]", "")
#   values = line.split("!")
#    entries = values[0].split(",")
#    values = values[1].split(",")
#    entries = list(map(int, entries))
#    output = net.activate(entries)
#    treated_output = normalize_list(output)
#    values = list(map(int, values))
#    print("Expected")
#    print(values)
#    print("got")
#    print(treated_output)
#    print("from")
#    print(output)
    


#testinglines = testingset.read().splitlines()
#testing_data = []
for line in testinglines:
    line = line.replace("[", "")
    line = line.replace("]", "")
    values = line.split("!")
    entries = values[0].split(",")
    values = values[1].split(",")
    entries = list(map(int, entries))
    values = list(map(int, values))
    TDS.appendLinked( entries, values )
print(trainer.activateOnDataSet(TDS))
#training_data, validation_data, test_data = mnistloader.load_data_wrapper()
#net = network.Network([16,30, 26])
#net.SGD(training_data, 30, 10, 3.0, test_data=testing_data)
