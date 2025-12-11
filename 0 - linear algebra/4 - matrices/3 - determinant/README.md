# Determinant

## Pure Python

### version 1 --> A. Recursive Expansion (Laplace Method)

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mi>det</mi><mo>⁡</mo><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo><mo>=</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mo stretchy="false">(</mo><mo>−</mo><mn>1</mn><msup><mo stretchy="false">)</mo><mrow><mi>i</mi><mo>+</mo><mi>j</mi></mrow></msup><mtext> </mtext><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mtext> </mtext><mi>det</mi><mo>⁡</mo><mo stretchy="false">(</mo><msub><mi>M</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">\det(A) = \sum_{i=1}^{n} (-1)^{i+j} \, a_{ij} \, \det(M_{ij})</annotation></semantics></math>
where i = 0 
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><msub><mi>C</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><mo stretchy="false">(</mo><mo>−</mo><mn>1</mn><msup><mo stretchy="false">)</mo><mrow><mi>i</mi><mo>+</mo><mi>j</mi></mrow></msup><mi>det</mi><mo>⁡</mo><mo stretchy="false">(</mo><msub><mi>M</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">C_{ij} = (-1)^{i+j} \det(M_{ij})</annotation></semantics></math>

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mi>det</mi><mo>⁡</mo><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo><mo>=</mo><msub><mi>a</mi><mrow><mi>i</mi><mn>1</mn></mrow></msub><msub><mi>C</mi><mrow><mi>i</mi><mn>1</mn></mrow></msub><mo>+</mo><msub><mi>a</mi><mrow><mi>i</mi><mn>2</mn></mrow></msub><msub><mi>C</mi><mrow><mi>i</mi><mn>2</mn></mrow></msub><mo>+</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mo>+</mo><msub><mi>a</mi><mrow><mi>i</mi><mi>n</mi></mrow></msub><msub><mi>C</mi><mrow><mi>i</mi><mi>n</mi></mrow></msub></mrow><annotation encoding="application/x-tex">\det(A) = a_{i1}C_{i1}+a_{i2}C_{i2}+...+a_{in}C_{in}</annotation></semantics></math>

## NumPy

### version 2 --> A. Standard Calculation

### version 3 --> B. Log Determinant

Used for very large matrices or probabilistic models to prevent floating point overflow/underflow. It returns (sign, log_determinant).

## Deep Learning Libraries

### version 4 --> A. PyTorch

### version 5 --> B. TensorFlow