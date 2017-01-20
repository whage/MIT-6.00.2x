import unittest
import p5

class TestQuiz(unittest.TestCase):

	def test_enumerate_subsequances(self):
		a = [1, 2, 3, 4, 5]
		expected = [
			[1],
			[2],
			[3],
			[4],
			[5],
			[1, 2],
			[2, 3],
			[3, 4],
			[4, 5],
			[1, 2, 3],
			[2, 3, 4],
			[3, 4, 5],
			[1, 2, 3, 4],
			[2, 3, 4, 5],
			[1, 2, 3, 4, 5],
		]

		self.assertEqual(expected, p5.enumerate_subsequences(a))

	def test_max_contig_sum(self):
		l1 = [3, 4, -1, 5, -4]
		l2 = [3, 4, -8, 15, -1, 2]
		l3 = [3, -5, 2, -3, 6, 4, -5, 3, 2]

		self.assertEqual(p5.max_contig_sum(l1), 11)
		self.assertEqual(p5.max_contig_sum(l2), 16)
		self.assertEqual(p5.max_contig_sum(l3), 10)


if __name__ == '__main__':
	unittest.main()