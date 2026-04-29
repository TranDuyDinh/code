import _array


if __name__ == "__main__":
    algs = _array.ArrayAlgorithms()
    array = [1, 2, 4, 5, 6, 6, 8, 9]
    target_number = 2
    sorted_array = sorted(array)


    print(algs.find_closest_number(sorted_array, target_number))
    print("\nGoodbye...\n")