import unittest

from test_base import BaseTestCase

class AttractionTests(BaseTestCase):
	def test_can_get_all_attractions(self):
		with self.client:
			res = self.client.get('/attractions')
			self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
	unittest.main()		