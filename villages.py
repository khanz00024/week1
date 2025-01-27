def smallest_neighborhood():
    # Input the number of villages
    n = int(input())
    # Input the positions of the villages
    villages = sorted([int(input()) for _ in range(n)])

    # Initialize a list to store neighborhood sizes
    neighborhood_sizes = []

    # Calculate midpoints and neighborhood sizes
    for i in range(1, n - 1):  # Skip the leftmost and rightmost villages
        left_mid = (villages[i - 1] + villages[i]) / 2
        right_mid = (villages[i] + villages[i + 1]) / 2
        neighborhood_size = right_mid - left_mid
        neighborhood_sizes.append(neighborhood_size)

    # Find the smallest neighborhood size
    smallest_size = min(neighborhood_sizes)

    # Output the result with one decimal place
    print(f"{smallest_size:}")

smallest_neighborhood()
