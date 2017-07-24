
from numpy import exp, array, random, dot


class NeuralNetwork():
    def __init__(self):
        # Seed the random number generator, so it generates the same numbers
        # every time the program runs.

        # We model a single neuron, with 3 input connections and 1 output connection.
        # We assign random weights to a 3 x 1 matrix, with values in the range -1 to 1
        # and mean 0.
        self.synaptic_weights = 2 * random.random((16, 26)) - 1

    # The Sigmoid function, which describes an S shaped curve.
    # We pass the weighted sum of the inputs through this function to
    # normalise them between 0 and 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # Pass the training set through our neural network (a single neuron).
            output = self.think(training_set_inputs)

            # Calculate the error (The difference between the desired output
            # and the predicted output).
            error = training_set_outputs - output

            # Multiply the error by the input and again by the gradient of the Sigmoid curve.
            # This means less confident weights are adjusted more.
            # This means inputs, which are zero, do not cause changes to the weights.
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            # Adjust the weights.
            self.synaptic_weights += adjustment

    # The neural network thinks.
    def think(self, inputs):
        # Pass inputs through our neural network (our single neuron).
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == "__main__":

    #Intialise a single neuron neural network.
    neural_network = NeuralNetwork()

    print ("Random starting synaptic weights: ")
    print (neural_network.synaptic_weights)

    # The training set. We have 4 examples, each consisting of 3 input values
    # and 1 output value.
    input_data = []
    output_data = []
    trainingset = open("trainingset.txt", "r")
    traininglines = trainingset.read().splitlines()
    for line in traininglines:
        line = line.replace("[", "")
        line = line.replace("]", "")
        values = line.split("!")
        entries = values[0].split(",")
        values = values[1].split(",")
        entries = list(map(int, entries))
        values = list(map(int, values))
        input_data.append(entries)
        output_data.append(values)

    training_set_inputs = array(input_data)
    training_set_outputs = array(output_data).T

    # Train the neural network using a training set.
    # Do it 10,000 times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_outputs, 100)

    testingset = open("testingset.txt", "r")
    testinglines = testingset.read().splitlines()
    test_input = []
    test_output = []
    count = 0
    for line in testinglines:
        line = line.replace("[", "")
        line = line.replace("]", "")
        values = line.split("!")
        entries = values[0].split(",")
        values = values[1].split(",")
        entries = list(map(int, entries))
        values = list(map(int, values))
        result = neural_network.think(array(entries))
        if (max(result) == max(values)):
            count += 1
    print (count/4000.0);
	
    #print ("New synaptic weights after training: ")
    #print (neural_network.synaptic_weights)

    # Test the neural network with a new situation.
    #print ("Considering new situation [1, 0, 0] -> ?: ")
    #print (neural_network.think(array([1, 0, 1])))
