import random

def reservoir_sampling(stream, k):
    reservoir = []

    # Fill the reservoir with the first k elements
    for i in range(k):
        reservoir.append(stream[i])

    # Iterate through the remaining elements in the stream
    for i in range(k, len(stream)):
        # Randomly choose an index from 0 to i (inclusive)
        j = random.randint(0, i)

        # If the chosen index is less than k, replace the element at that index in the reservoir
        if j < k:
            reservoir[j] = stream[i]

    return reservoir

# Example usage:
stream_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample_size = 3

result = reservoir_sampling(stream_data, sample_size)
print("Reservoir Sample:", result)