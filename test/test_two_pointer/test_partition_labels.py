
import unittest

from src.two_pointer.partition_labels import partitionLabels 

class Test_Partition_labels(unittest.TestCase):

    def test_partition_labels(self):
        s = "ababcbacadefegdehijhklij"
        size_labels = partitionLabels(s)
        print(size_labels)
        # assert(size_labels, [9,8,7])

if __name__ == "__main__":
    unittest.main()
