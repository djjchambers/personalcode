import unittest
import fibseq

class TestFibonacci(unittest.TestCase):
	def test_fibonacci(self):
		self.assertEqual(fibsequence(5), [2, 3, 5, 8])
	
if __name__ == '__main__':
	unittest.main()