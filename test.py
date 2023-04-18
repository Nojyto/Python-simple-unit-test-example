import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls): 
        '''Run once before all test cases'''
        pass
  
    @classmethod
    def tearDownClass(cls): 
        '''Run once after all test cases'''
        pass
  
    def setUp(self): 
        '''Run before each test case'''
        self.calc = Calculator()  # Create an instance of the Calculator class
        pass
  
    def tearDown(self): 
        '''Run after each test case'''
        pass
  
    def test_add(self):
        '''Test case function for addition'''
        result = self.calc.add(4, 7)
        expected = 11
        self.assertEqual(result, expected)

    def test_sub(self):
        '''Test case function for subtraction'''
        result = self.calc.sub(10, 5)
        expected = 5
        self.assertEqual(result, expected)

    @unittest.skip('Some reason')
    def test_mul(self):
        '''Test case function for multiplication'''
        result = self.calc.mul(3, 7)
        expected = 21
        self.assertEqual(result, expected)

    def test_div(self):
        '''Test case function for division'''
        result = self.calc.div(10, 2)
        expected = 5
        self.assertEqual(result, expected)
        
        # Test case for division by zero
        with self.assertRaises(ValueError):
            self.calc.div(10, 0)
            

# Run the tests
if __name__ == '__main__':
    unittest.main()