import unittest

from test_base import BaseTestCase

class MickeyTests(BaseTestCase):

	def test_can_get_all_mickeys(self):
		with self.client:
			res = self.client.get('/mickeys')
			self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
	unittest.main()	