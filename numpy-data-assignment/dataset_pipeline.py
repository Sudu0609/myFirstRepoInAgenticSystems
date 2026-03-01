import numpy as np

np.random.seed(42)

data = np.random.rand(100, 5)

mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

normalized = (data - mean) / std

train = normalized[:80]
test = normalized[80:]

train[0, 0] = 999

print("Original data shape:", data.shape)
print("Normalized data shape:", normalized.shape)
print("Train shape:", train.shape)
print("Test shape:", test.shape)

print("\nMean per feature:", mean)
print("Standard deviation per feature:", std)

print("\nModified value in normalized array (should be 999):", normalized[0, 0])