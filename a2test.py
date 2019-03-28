#Riya Singh
#2017309

import unittest
from a2 import *

class testpoint(unittest.TestCase):

	def test_updateMove(self):
		case0()
		updateMove(2)
		from a2 import tile2
		self.assertTrue(tile2==1,msg=None)
		self.assertFalse(tile7==1,msg=None)

	def test_winningMove(self):
		case1()
		self.assertEqual(winningMove(),3)
		case2()
		self.assertFalse(winningMove())
		case3()
		self.assertEqual(winningMove(),3)

	def test_blockingMove(self):
		case4()
		self.assertEqual(blockingMove(),3)
		case2()
		self.assertFalse(blockingMove())
		case5()
		self.assertEqual(blockingMove(),3)
	
	def test_validMove(self):
		case2()
		self.assertTrue(validMove(2),msg=None)
		case3()
		self.assertFalse(validMove(8),msg=None)
		self.assertFalse(validMove(4),msg=None)

	def test_win(self):
		case6()
		self.assertTrue(win(),msg=None)
		case2()
		self.assertFalse(win(),msg=None)
	
	def test_validBoard(self):
		case7()
		self.assertFalse(validBoard(),msg=None)
		case1()
		self.assertTrue(validBoard(),msg=None)

	def test_takeNaiveMove(self):
		case2()	
		self.assertAlmostEqual(takeNaiveMove(),5,delta=5)

	def test_takeStrategicMove(self):
		case2()
		self.assertEqual(takeStrategicMove(),1)
		case8()
		self.assertEqual(takeStrategicMove(),5)
		case1()
		self.assertEqual(takeStrategicMove(),3)
		case5()
		self.assertEqual(takeStrategicMove(),3)
		case9()
		self.assertAlmostEqual(takeStrategicMove(),5,delta=5)
	
	def test_game(self):
		self.assertAlmostEqual(game(),1,delta=1)

	def test_game1(self):
		self.assertAlmostEqual(game1(1000),0.58,delta=0.05)

	def test_game2(self):
		self.assertAlmostEqual(game2(1000),0.045,delta=0.05)

	def test_game3(self):
		self.assertAlmostEqual(game3(1000),0.12,delta=0.05)

if __name__=='__main__':
	unittest.main()


