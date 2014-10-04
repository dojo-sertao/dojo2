import unittest
from palavrasPrimas import is_primo,trans_palavra_em_num


class Test_PalavraPrima(unittest.TestCase):

	def test_palavraSeUmEhPrimo(self):
		self.assertEquals(is_primo(1),True)
	
	def test_palavraSeDoisEhPrimo(self):
	 	self.assertEquals(is_primo(2),True)
	
	def test_palavraSeTresEhPrimo(self):
		self.assertEquals(is_primo(3),True)
	
	def test_palavraSeQuatroEhPrimo(self):
		self.assertEquals(is_primo(4),False)

	def test_palavraSeCincoEhPrimo(self):
		self.assertEquals(is_primo(5),True)

	def test_palavraSeSeisEhPrimo(self):
		self.assertEquals(is_primo(6),False)

	def test_palavraSeSeteEhPrimo(self):
		self.assertEquals(is_primo(7),True)

	def test_palavraSeTrezeEhPrimo(self):
		self.assertEquals(is_primo(13),True)

	def test_palavraSe113EhPrimo(self):
		self.assertEquals(is_primo(113),True)

	def test_palavraFromNum(self):
		self.assertEquals(trans_palavra_em_num('ana'),[('ana', False)])

	def test_palavraFromNum(self):
		self.assertEquals(trans_palavra_em_num('A pizza chegou'),[('A', False), ('pizza',False), ('chegou',True)])

if __name__ == '__main__':
	unittest.main() 

