import unittest
import json

from test_base import BaseTestCase

class MickeyTests(BaseTestCase):

	def test_can_get_all_mickeys(self):
		with self.client:
			res = self.client.get('/mickeys')
			self.assertEqual(res.status_code, 200)

	def test_can_get_mickey_by_id(self):
		with self.client:
			res = self.client.get('/mickeys/1')
			self.assertEqual(res.status_code, 200)

	def test_can_post_new_mickey(self):
		with self.client:
			u = dict(
				park_id=1,
				land_id=15,
				attraction_id=73,
				photo_url='test_post.url',
				description='test post',
				hint='test post hint'
			)
			res = self.client.post('/mickeys', data=json.dumps(u),
				content_type='application/json')
			self.assertEqual(res.status_code, 201)

	def test_can_edit_mickey(self):
		with self.client:
			u = dict(
				photo_url='test_put.url',
				description='test put',
				hint='test put hint'
			)
			res = self.client.put('/mickeys/1', data=json.dumps(u),
				content_type='application/json')
			self.assertEqual(res.status_code, 204)					

	def test_can_delete_mickey(self):
		with self.client:
			res = self.client.delete('/mickeys/1')
			self.assertEqual(res.status_code, 204)						


if __name__ == '__main__':
	unittest.main()	