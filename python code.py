class BinaryIndexedTree:
    def __init__(self, size):
        # Initialize Binary Indexed Tree with given size
        self.size = size
        self.tree = [0] * (size + 1)

    @staticmethod
    def lowbit(index):
        # Get the lowest bit that is 1 in the binary representation of index
        return index & -index

    def update(self, index, delta):
        # Increase the value at a specific index by delta and update the tree
        while index <= self.size:
            self.tree[index] += delta
            index += BinaryIndexedTree.lowbit(index)

    def query(self, index):
        # Compute and return the prefix sum up to a given index
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= BinaryIndexedTree.lowbit(index)
        return sum


class Solution:
    def countSmaller(self, nums):
        # Counts the smaller elements to the right for each element in nums

        # Deduplicate and sort the list of numbers
        unique_nums = sorted(set(nums))
        # Create a mapping from number to its index in sorted unique numbers
        num_to_index = {value: idx for idx, value in enumerate(unique_nums, 1)}
      
        # Initialize Binary Indexed Tree with size equal to the number of unique elements
        tree = BinaryIndexedTree(len(num_to_index))
        counts = []  # List to store counts of smaller elements
      
        # Iterate through the numbers in reverse order
        for value in reversed(nums):
            # Get the index of the current value in the sorted unique list
            index = num_to_index[value]
          
            # Update the Binary Indexed Tree with the index
            tree.update(index, 1)
          
            # Compute the count of smaller elements by querying the tree
            # Query for index - 1 because it needs to return count for numbers less than current value
            counts.append(tree.query(index - 1))
      
        # Since we iterated in reverse order, reverse the counts to match the original order
        return counts[::-1]
