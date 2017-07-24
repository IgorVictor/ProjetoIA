import mnistloader
import network

trainingset = open("trainingset.txt", "r")
traininglines = trainingset.read().splitlines()
training_data = []
for line in traininglines:
    line = line.replace("[", "")
    line = line.replace("]", "")
    values = line.split("!")
    entries = values[0].split(",")
    values = values[1].split(",")
    entries = list(map(int, entries))
    values = list(map(int, values))
    training_tuple = (entries, values)
    training_data.append(training_tuple)

testingset = open("testingset.txt", "r")
testinglines = testingset.read().splitlines()
testing_data = []
for line in testinglines:
    line = line.replace("[", "")
    line = line.replace("]", "")
    values = line.split("!")
    entries = values[0].split(",")
    values = values[1].split(",")
    entries = list(map(int, entries))
    values = list(map(int, values))
    testing_tuple = (entries, values)
    testing_data.append(testing_tuple)

#training_data, validation_data, test_data = mnistloader.load_data_wrapper()
net = network.Network([16,30, 26])
net.SGD(training_data, 30, 10, 3.0, test_data=testing_data)
