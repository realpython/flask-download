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


if __name__ == '__main__':
    unittest.main()
