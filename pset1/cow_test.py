import unittest
import ps1

class TestCowTransport(unittest.TestCase):

    """
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    """

    def test_get_largest_from_remaining(self):
        cows = ps1.load_cows("ps1_cow_data.txt")

        #self.assertEqual("Betsy", ps1.get_largest_from_remaining(cows, 10, [])[1])
        #self.assertEqual("Lola", ps1.get_largest_from_remaining(cows, 2, ["Milkshake", "Florence"])[1])

    def test_greedy_cow_transport(self):
        cows = ps1.load_cows("ps1_cow_data.txt")
        result = ps1.greedy_cow_transport(cows, 10)
        exp = [
            ["Betsy"],
            ["Henrietta"],
            ["Herman", "Maggie"],
            ["Oreo", "Moo Moo"],
            ["Millie", "Florence", "Lola"],
            ["Milkshake"]
        ]

        self.assertEqual(result, exp)

    """
    def test_validate_trip(self):
        cows = ps1.load_cows("ps1_cow_data.txt")

        self.assertTrue(ps1.validate_trip(cows, ["Moo Moo", "Milkshake", "Millie"], 10))
        self.assertFalse(ps1.validate_trip(cows, ["Herman", "Florence", "Lola"], 10))
        self.assertFalse(ps1.validate_trip(cows, ["Oreo", "Millie"], 10))
        self.assertTrue(ps1.validate_trip(cows, ["Oreo", "Maggie"], 10))

    """

    def test_brute_force_cow_transport(self):
        #cows = ps1.load_cows("ps1_cow_data.txt")

        cows = {
            "A": 5,
            "B": 3,
            "C": 4,
            "D": 1,
        }

        #for partition in ps1.get_partitions(cows):
        #    print (partition)
        self.assertEqual(ps1.brute_force_cow_transport(cows, 6), [
            "maggie"
        ])
    

if __name__ == '__main__':
    unittest.main()