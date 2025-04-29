import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Training data
X = np.array([[0.6, 0.1], [0.2, 0.3]])
Y = np.array([[1, 0], [0, 1]])

# Network architecture
input_neurons = 2
hidden_neurons = 3
output_neurons = 2

np.random.seed(42)
W1 = np.array([[0.1, -0.2, 0.1],
               [0.1, 0.2, -0.4]])
W2 = np.array([[0.2, -0.1],
               [0.1, 0.6],
               [-0.2, 0.6]])

eta = 0.1

def forward_propagation(x):
    hidden_input = np.dot(x, W1)
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output, W2)
    final_output = sigmoid(final_input)
    return hidden_output, final_output

def backpropagation(x, y):
    global W1, W2
    hidden_output, final_output = forward_propagation(x)

    # Output layer error and delta
    error_output = y - final_output
    delta_output = error_output * sigmoid_derivative(final_output)

    # Hidden layer error and delta
    error_hidden = delta_output.dot(W2.T)
    delta_hidden = error_hidden * sigmoid_derivative(hidden_output)

    # Update weights
    W2 += eta * hidden_output.T.dot(delta_output)
    W1 += eta * x.T.dot(delta_hidden)

for i in range(50):
    for x, y in zip(X, Y):
        backpropagation(x.reshape(1, -1), y.reshape(1, -1))
    
    if i + 1 in [1, 2, 50]:
        print(f"\nWeights after iteration {i + 1}:")
        print("W1:\n", W1)
        print("W2:\n", W2)
