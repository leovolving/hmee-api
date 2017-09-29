import unittest

from test_base import BaseTestCase

class LandTests(BaseTestCase):

	def test_can_get_all_lands(self):
		with self.client:
			res = self.client.get('/lands')
			self.assertEqual(res.status_code, 200)



if __name__ == '__main__':
	unittest.main()		