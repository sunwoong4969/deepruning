import numpy as np

class Loss_CategoricalCrossentropy:
    def __init__(self):
        pass

    def forward(self, predictions, targets):
        # Clip predictions to avoid log(0)
        predictions = np.clip(predictions, 1e-7, 1 - 1e-7)

        # Calculate correct confidences
        if targets.ndim == 1:
            correct_confidences = predictions[np.arange(len(predictions)), targets]
        else:
            correct_confidences = np.sum(predictions * targets, axis=1)

        # Calculate negative log likelihoods
        negative_log_likelihoods = -np.log(correct_confidences)

        # Return mean loss
        return np.mean(negative_log_likelihoods)

# Sample usage
if __name__ == "__main__":
    # Sample softmax outputs and targets
    softmax_outputs = np.array([
        [0.7, 0.1, 0.2],
        [0.1, 0.5, 0.4],
        [0.2, 0.2, 0.6],
    ])

    targets = np.array([0, 1, 2])  # Corresponding target classes

    # Create an instance of the loss class
    loss_function = Loss_CategoricalCrossentropy()

    # Compute the loss
    loss = loss_function.forward(softmax_outputs, targets)
    print("Categorical cross-entropy Loss:", loss)