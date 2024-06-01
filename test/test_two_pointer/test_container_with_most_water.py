
import unittest

from src.two_pointer import container_with_most_water

class Test_TestContainerWithMostWater(unittest.TestCase):

    def test_container_with_most_water(self):
        self.assertEqual(container_with_most_water.maxArea([1,1]), 1)

if __name__ == '__main__':
    unittest.main()