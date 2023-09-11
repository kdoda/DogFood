#!/usr/bin/env python
import unittest

def calculate_food_required(small_dogs, medium_dogs, large_dogs, leftover):
    food_required = ((small_dogs * 10) + (medium_dogs * 20) + (large_dogs * 30) - leftover) * 1.2
    return 0 if food_required < 0 else food_required


class DogFoodRequiredTests(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(calculate_food_required(3, 1, 4, 15), 186)

    def test_medium_dogs_zero(self):
        self.assertEqual(calculate_food_required(3, 0, 4, 50), 120)

    def test_small_dogs_zero(self):
        self.assertEqual(calculate_food_required(0, 11, 9, 60), 516)
    
    def test_large_dogs_zero(self):
        self.assertEqual(calculate_food_required(6, 7, 0, 10), 228)

    def test_all_dogs_zero(self):
        self.assertEqual(calculate_food_required(0, 0, 0, 0), 0)
    
    def test_all_values_zero(self):
        self.assertEqual(calculate_food_required(0, 0, 0, 0), 0)

    def test_leftover_more_than_food_required(self):
        self.assertEqual(calculate_food_required(3, 1, 4, 200), 0)

    def test_leftover_equal_to_food_required(self):
        self.assertEqual(calculate_food_required(7, 2, 5, 260), 0)


if __name__ == '__main__':
    unittest.main()
