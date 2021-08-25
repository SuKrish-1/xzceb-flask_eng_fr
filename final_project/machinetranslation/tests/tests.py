import unittest

from translator import englishToFrench, frenchToEnglish

class F2E(unittest.TestCase):
    def test_is_not_null(self):
        self.assertNotEqual(frenchToEnglish("Bonjour"),"")
    def test_translation(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

class E2F(unittest.TestCase):
    def test_is_not_null(self):
        self.assertNotEqual(englishToFrench("Hello"), "")
    def test_translation(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

unittest.main()