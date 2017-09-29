from flask_testing import TestCase
from project import app, db
from project.models import Parks, Lands, Attractions, Mickeys
import unittest

class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app   

    def setUp(self):
        db.create_all()
        db.session.add(Parks("foo"))
        db.session.add(Parks("bar"))
        db.session.add(Lands(1, "bizz"))
        db.session.add(Lands(2, "bang"))
        db.session.add(Attractions(1, 8, "Buzz"))
        db.session.add(Attractions(2, 3, "Fizz"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()