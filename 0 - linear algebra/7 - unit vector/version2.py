
import math

vector = [0, 0]

magnitude = math.sqrt(sum(x**2 for x in vector))

if magnitude == 0:
    unit_vector = vector # Or raise an error
else:
    unit_vector = [x / magnitude for x in vector]