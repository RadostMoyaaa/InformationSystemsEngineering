import unittest, io
from Chess import Pawn, Elephant
import unittest.mock

class testTemplateMethod(unittest.TestCase):

	@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
	def test_move(self, mock_stdout):
		pawn  = Pawn("Pawn", "White")
		pawn.move()
		self.assertEqual(mock_stdout.getvalue(), 'Pawn is moving + 1\n')
		
	@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
	def test_death(self, mock_stdout):
		pawn  = Pawn("Pawn", "White")
		pawn.death()
		self.assertEqual(mock_stdout.getvalue(), 'The Pawn is eaten\n')

		
if __name__ == '__main__':
	unittest.main()
