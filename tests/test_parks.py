import unittest

from test_base import BaseTestCase

class ParkTests(BaseTestCase):

	def test_can_get_parks(self):
		with self.client:
			res = self.client.get('/parks')
			self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
	unittest.main()			