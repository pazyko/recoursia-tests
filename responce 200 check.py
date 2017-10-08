import requests
import unittest

class TestStringMethods(unittest.TestCase): 
	def test_check200Responce(self):
		r = requests.get('https://recoursia.by')
		self.assertEqual(r.status_code,200,'lolkek')
	def test_check200Responce(self):
		r = requests.get('https://recoursia.by/catalog/')
		self.assertEqual(r.status_code,200,'lolkek')
	def test_check200Responce(self):
		r = requests.get('https://recoursia.by/vendors/')
		self.assertEqual(r.status_code,200,'lolkek')
	def test_check200Responce(self):
		r = requests.get('https://recoursia.by/news/')
		self.assertEqual(r.status_code,200,'lolkek')
	def test_check200Responce(self):
		r = requests.get('https://recoursia.by/help/')
		self.assertEqual(r.status_code,200,'lolkek')
	def test_check200Responce(self):
		r = requests.get('https://recoursia.by/about/')
		self.assertEqual(r.status_code,400,'lolkek')

if __name__ == '__main__':
    unittest.main()
