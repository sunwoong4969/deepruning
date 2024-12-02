import numpy as np

input = [[1.0, 2.0, 3.0, 2.5],
         [3.0, 5.0, -0.1, 2.0],
         [-.15, 2.7, 3.3, -0.8]]

weights = [[0.2, 0.8, -0.5, 1.0],
         [0.5, -0.91, 0.26, -0.5],
         [-0.26, -0.27, 0.17, 0.87]]

biases = [2.0, 3.0, 0.5]


layers_outputs = np.dot(input, np.array(weights).T)+biases
print(layers_outputs)



import numpy as np

input = [[1.0, 2.0, 3.0, 2.5],
         [2.0, 5.0, -0.1, 2.0],
         [0.7, -0.91, 0.26, -0.5],
         [0.5, -0.91, 0.46, -0.5],
         [-.15, 2.7, 3.3, -0.8]]

weights = [[0.2, 0.8, -0.5, 1.0],
         [0.5, -0.91, 0.26, -0.5],
         [-0.26, -0.27, 0.17, 0.87]]

biases = [2.0, 3.0, 0.5]


layers_outputs = np.dot(input, np.array(weights).T)+biases
print(layers_outputs)


import numpy as np

input = [[1.0, 2.0, 3.0, 2.5],
         [2.0, 5.0, -0.1, 2.0],
         [-.15, 2.7, 3.3, -0.8]]
weights = [[0.2, 0.8, -0.5, 1.0],
         [0.5, -0.91, 0.26, -0.5],
         [-0.26, -0.27, 0.17, 0.87]]

biases = [2.0, 3.0, 0.5]

biases_2 = [5.0, 8.0, 2.5]

layers_outputs = np.dot(input, np.array(weights).T)+biases
print(layers_outputs)

layers_outputs = np.dot(output, np.array(weights).T)+biases_2
print(layers_outputs)