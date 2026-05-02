class ArrayAlgorithms:
    def __init__(self) -> None:
        pass

    def optimal_tasks(self, tasks: list[int]) -> list[tuple(int, int)]:
        """
        Greedy Algorithms: Optimal Task Assignment
        Input: tasks = [6, 3, 2, 7, 1, 5, 8]
        Output: [(1, 8), (2, 7), (3, 6), (5, 0)]
        T(A) = O(nlogn) + O(n) + O(1)
        Big-O = O(nlogn)
        """
        pairs = []
        sorted_tasks = sorted(tasks)    # Timsort: O(nlogn)
        for i in range(len(sorted_tasks) // 2): # O(n/2)
            pairs.append((sorted_tasks[i], sorted_tasks[-i - 1]))
        if len(tasks) % 2 == 1: # O(1)
            pairs.append((sorted_tasks[len(sorted_tasks) // 2], 0))
        return pairs

    def intersection(self, array_1: list[int], array_2: list[int]) -> list[int]:
        """
        Sorting Algorithms: Intersection of Two Unsorted Arrays
        Big-O = O(nlogn + mlogm) + O(n) + O(m) = O(nlogn + mlogm)
        """
        # Old solution: duplicate values
        # for i in array_1:
        #     for j in array_2: # O(n^2)
        #         if i == j:
        #             intersections.append(i)
        i = 0
        j = 0
        intersections = []
        sorted_array_1 = sorted(array_1)  # Timsort: O(nlogn)
        sorted_array_2 = sorted(array_2)  # Timsort: O(mlogm)
        while i < len(sorted_array_1) and j < len(sorted_array_2):
            if sorted_array_1[i] == sorted_array_2[j]:
                if i == 0 or sorted_array_1[i] != sorted_array_1[i-1]:
                    intersections.append(sorted_array_1[i])
                i = i + 1
                j = j + 1
            elif sorted_array_1[i] < sorted_array_2[j]:
                i = i + 1
            else:
                j = j + 1
        return intersections

    def _find_closest_number(self, array: list[int], target: int) -> int | None:
        """
        Linear Search: Find the Closest Number in a Sorted Array
        Big-O = O(n)
        """
        if not array:
            return None
        if len(array) == 1:
            return array[0]
        min_value = -1
        for i in range(len(array)): # O(n)
            distance = (target - array[i])**2
            if min_value == -1 or distance < min_value:
                closest_number = array[i]
                min_value = distance
        return closest_number

    def find_closest_number(self, array: list[int], target: int) -> int | None:
        """
        Binary Search: Find the Closest Number in a Sorted Array
        Big-O = O(logn)
        """
        if not array:
            return None
        if len(array) == 1:
            return array[0]
        left, right = 0, len(array) - 1
        while left < right:
            mid = (left + right) // 2   # n = 2^x <=> x = log2(n) ~ log(n) = Big-O
            if array[mid] == target:
                return array[mid]
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if abs(array[left] - target) < abs(array[right] - target):
            closest_number = array[left]
        else:
            closest_number = array[right]
        return closest_number

    def find_fixed_point(self, sorted_array : list[int]) -> int | None:
        """
        Binary Search: Find Fixed Point in a Sorted Array
        """
        if not sorted_array and len(sorted_array) == 1:
            return None
        left, right = 0, len(sorted_array) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid == sorted_array[mid]:
                return mid
            elif mid < sorted_array[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return None

    def find_bitonic_peak(self, array: list[int]) -> int:
        """
        Binary Search: Find Bitonic Peak
        """
        if not array:
            return None
        left, right = 0, len(array) - 1
        while left < right:
            mid = (left + right) // 2
            if array[mid] > array[mid + 1]:
                right = mid
                peak = array[mid]
            else:
                left = mid + 1
                peak = array[mid + 1]
        return peak

    def find_first_entry(self, array: list[int], key: int) -> int | None:
        """
        Binary Search: Find First Entry in List with Duplicates
        """
        if not array:
            return None
        left, right = 0, len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] < key:
                left = mid + 1
            elif array[mid] == key:
                if mid - 1 < 0 or array[mid - 1] != key:
                    return mid
                if array[mid - 1] == key:
                    right = mid - 1
            else:
                right = mid - 1
        return None

    def plus_one(self, array: list[int]) -> list[int]:
        """
        Array: Plus One
        """
        flag = True
        index = 0
        while flag:
            array[-(1 + index)] = array[-(1 + index)] + 1
            if array[-(1 + index)] < 10:
                flag = False
            else:
                array[-(1 + index)] = 0
                if index < len(array) - 1:
                    index = index + 1
                else:
                    array.insert(0, 1)
                    flag = False
        return array