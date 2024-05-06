# tests/test_vendor.py

from django.test import TestCase
from vendors.models import Vendor

class VendorTestCase(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(name="Test Vendor", contact_details="test@example.com", address="123 Test St", vendor_code="VENDOR001")

    def test_vendor_creation(self):
        self.assertEqual(self.vendor.name, "Test Vendor")
        self.assertEqual(self.vendor.contact_details, "test@example.com")
        self.assertEqual(self.vendor.address, "123 Test St")
        self.assertEqual(self.vendor.vendor_code, "VENDOR001")

    def test_vendor_update(self):
        self.vendor.name = "Updated Vendor"
        self.vendor.save()
        self.assertEqual(self.vendor.name, "Updated Vendor")

    def test_vendor_deletion(self):
        vendor_count_before_deletion = Vendor.objects.count()
        self.vendor.delete()
        self.assertEqual(Vendor.objects.count(), vendor_count_before_deletion - 1)
