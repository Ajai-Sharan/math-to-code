
import numpy as np

def check(vector):

    vector = vector if isinstance(vector, np.ndarray) else np.array(vector)
    dist = np.linalg.norm(vector)
    print("It is unit vector") if np.isclose(dist, 1.0) else  print(f"It is not unit vector. distance == {dist}")





