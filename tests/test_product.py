# tests/test_product.py


import unittest

from project import db
from base import BaseTestCase
from project.models import Purchase


class TestProductBlueprint(BaseTestCase):

    def test_purchase(self):
        # Ensure purchase returns correct info.
        purchase = Purchase(email="foo@bar.com")
        db.session.add(purchase)
        db.session.commit()
        get_purchase = Purchase.query.filter_by(email='foo@bar.com').first()
        self.assertEqual(get_purchase.id, 1)
        self.assertEqual(get_purchase.email, 'foo@bar.com')
        self.assertEqual(get_purchase.downloads_left, 5)

    def test_product_download(self):
        # Ensure end user can download file after purchase.
        purchase = Purchase(email="foo@bar.com")
        db.session.add(purchase)
        db.session.commit()
        response = self.client.get('/1', follow_redirects=True)
        self.assertTrue(response.status_code == 200)
        self.assertEqual(response.data, 'foo')

    def test_product_download_abort(self):
        # Ensure there is a 404 error if user tries to download but
        # there isn't an associated purchase in the database.
        response = self.client.get('/1', follow_redirects=True)
        self.assertTrue(response.status_code == 404)

    def test_product_no_download(self):
        # Ensure end user cannot download file if there are no downloads left.
        purchase = Purchase(email="foo@bar.com")
        db.session.add(purchase)
        db.session.commit()
        get_user = Purchase.query.filter_by(email='foo@bar.com').first()
        get_user.downloads_left = 0
        db.session.commit()
        response = self.client.get('/1', follow_redirects=True)
        self.assertTrue(response.status_code == 200)
        self.assertIn('No downloads left!', response.data)


if __name__ == '__main__':
    unittest.main()
