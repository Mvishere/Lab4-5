import numpy as np

data_set = np.array([[1, 0, 0, 1, 1],
                     [1, 0, 0, 0, 1],
                     [0, 0, 1, 1, 0],
                     [0, 1, 0, 0, 0],
                     [1, 1, 0, 0, 1],
                     [0, 0, 1, 1, 1],
                     [0, 0, 0, 1, 0],
                     [0, 0, 1, 0, 0],
                    ])

class Perceptron:
    def __init__(self, data_set, iterations=5000, learning_rate=0.1, bias=0): #bias and learning has default values 0 and 0.1 respectiverly
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.bias = bias
        self.weights = np.random.rand(len(data_set[0])-1)
        self.input_data = [x[:-1] for x in data_set]
        self.output_data = [x[-1] for x in data_set]

    def activation(self, x):
        return 1 if x >= 0 else 0 # actvation will decide the output based on the net value calculated in predict function
    
    def train(self):
        for _ in range(self.iterations):
            for i, x in enumerate(self.input_data):
                net_input = np.dot(x, self.weights) + self.bias
                prediction = self.activation(net_input)

                error = self.output_data[i] - prediction
                self.weights += self.learning_rate * error * x
                self.bias += self.learning_rate * error

    def predict(self, input_data):
        net_input = np.dot(self.weights, input_data) + self.bias
        return self.activation(net_input)

p = Perceptron(data_set)
p.train()

test_inputs = np.array([
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 1, 0],
])

for i, x in enumerate(test_inputs):
    print(f"prediction for test_input {i+1} is {p.predict(x)}")