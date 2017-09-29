import unittest

from test_base import BaseTestCase

class LandTests(BaseTestCase):

	def test_can_get_all_lands(self):
		with self.client:
			res = self.client.get('/lands')
			self.assertEqual(res.status_code, 200)

	def test_can_get_lands_by_park_id(self):
		with self.client:
			res = self.client.get('/parks/%r/lands' % 1)
			self.assertEqual(res.status_code, 200)

	def test_can_get_land_by_id(self):
		with self.client:
			res = self.client.get('/lands/%r' % 1)
			self.assertEqual(res.status_code, 200)					



if __name__ == '__main__':
	unittest.main()		