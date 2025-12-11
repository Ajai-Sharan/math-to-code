# Matrix Inverse

## Pure Python

### version 1 --> A. 2x2 Shortcut Formula (my version)

$$A^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

### version 1 --> A1. 2x2 Shortcut Formula (gemini version)

### version 2 --> B. Gauss-Jordan Elimination (General N x N)

$$
[A \mid I] \; \longrightarrow \; [I \mid A^{-1}]
$$


## NumPy

### version 3 --> A. numpy.linalg.inv

### version 4 --> B. numpy.linalg.pinv (Pseudo-Inverse)
In real-world Machine Learning, we often use the Moore-Penrose Pseudo-Inverse. It calculates the inverse if it exists, but if the matrix is singular (or not square), it gives the "best fit" approximation instead of crashing.

## Deep Learning Libraries

### version 5 --> A. PyTorch

### version 6 --> B. TensorFlow