import unittest
from translator import en_to_fr
from translator import fr_to_en
#import e2f, f2e from translator
class Teste2f(unittest.TestCase): 


    def test_en_to_fr(self): 
        self.assertEqual(en_to_fr('Hello'), 'Bonjour')
        self.assertEqual(en_to_fr('Thank you'), 'Je vous remercie')
        self.assertEqual(en_to_fr(0), 0)
        self.assertEqual(en_to_fr('None'), '')
        
class Testf2e(unittest.TestCase):      
    def test_fr_to_en(self): 
        self.assertEqual(fr_to_en('Bonjour'), 'Hello')
        self.assertEqual(fr_to_en(0), 0)
        self.assertEqual(fr_to_en('None'), '')

if __name__=="__Main__":
    pass
unittest.main()

