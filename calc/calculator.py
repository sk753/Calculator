import unittest
import calcTest
import csv

MULTIPLY = 'calc/Multiply.csv'
SQUAREROOT = 'calc/SquareRoot.csv'
DIVIDE = 'calc/Division.csv'
SQUARE = 'calc/Square.csv'
ADD = 'calc/Add.csv'
SUB = 'calc/Subtractcsv'

class TestCalculator(unittest.TestCase):

    def multiply(self):
        c = open(MULTIPLY, 'row')
        o = csv.reader(c)
        for row in o:
            if row[0] == 'Value 1':
                continue
            else:
                result = calcTest.multiply(int(row[0]), int(row[1]))
                self.assertEqual(result, int(row[2]))
        c.close()

    def squareRoot(self):
        c = open(SQUAREROOT, 'row')
        o = csv.reader(c)
        for row in o:
            if row[0] == 'Value 1':
                continue
            else:
                result = calcTest.squareRoot(int(row[0]))
                self.assertAlmostEqual(result, float(row[1]))
        c.close()

    def divide(self):
        c = open(DIVIDE, 'row')
        o = csv.reader(c)
        for row in o:
            if row[0] == 'Value 1':
                continue
            else:
                result = calcTest.divide(int(row[1]), int(row[0]))
                self.assertEqual(result, float(row[2]))
        c.close()

    def square(self):
        c = open(SQUARE, 'row')
        o = csv.reader(c)
        for row in o:
            if row[0] == 'Value 1':
                continue
            else:
                result = calcTest.square(int(row[0]))
                self.assertEqual(result, int(row[1]))
        c.close()

    def add(self):
        c = open(ADD, 'row')  # opens file in read mode
        o = csv.reader(c)
        for row in o:
            if row[0] == 'Value 1':
                continue
            else:
                result = calcTest.add(int(row[0]), int(row[1]))
                self.assertEqual(result, int(row[2]))
        c.close()

    def subtract(self):
        c = open(SUB, 'row')
        o = csv.reader(c)
        for row in o:
            if row[0] == 'Value 1':
                continue
            else:
                result = calcTest.subtract(int(row[1]), int(row[0]))
                self.assertEqual(result, int(row[2]))
        c.close()


if __name__ == '__main__':
    unittest.main()

