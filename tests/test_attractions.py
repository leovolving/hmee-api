import unittest

from test_base import BaseTestCase

class AttractionTests(BaseTestCase):
	def test_can_get_all_attractions(self):
		with self.client:
			res = self.client.get('/attractions')
			self.assertEqual(res.status_code, 200)

	def test_can_get_attractions_by_park_id(self):
		with self.client:
			res = self.client.get('/parks/%r/attractions' % 1)
			self.assertEqual(res.status_code, 200)

	def test_can_get_attractions_by_land_id(self):
		with self.client:
			res = self.client.get('/lands/%r/attractions' % 1)
			self.assertEqual(res.status_code, 200)
			
	def test_can_get_attraction_by_id(self):
		with self.client:
			res = self.client.get('/attractions/%r' % 1)
			self.assertEqual(res.status_code, 200)									


if __name__ == '__main__':
	unittest.main()		