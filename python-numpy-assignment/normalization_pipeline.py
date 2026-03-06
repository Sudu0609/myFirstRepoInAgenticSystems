import numpy as np

# Step 1: Create a NumPy array
data = np.array([10, 20, 30, 40, 50])

# Step 2: Calculate mean
mean = np.mean(data)

# Step 3: Calculate standard deviation
std = np.std(data)

# Step 4: Normalize the data
normalized = (data - mean) / std

# Step 5: Reshape into 2D array
reshaped = normalized.reshape(5, 1)

# Step 6: Print outputs
print("Original Array:", data)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Normalized Array:", normalized)
print("Reshaped Array:\n", reshaped)
print("Shape of Reshaped Array:", reshaped.shape)