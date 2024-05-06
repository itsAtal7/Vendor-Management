from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from vendors.models import Vendor, PurchaseOrder

class VendorPerformanceTestCase(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(name="Test Vendor")
        # Create PurchaseOrder objects without specifying delivery_date
        self.purchase_order1 = PurchaseOrder.objects.create(vendor=self.vendor, status="completed", quality_rating=4)
        self.purchase_order2 = PurchaseOrder.objects.create(vendor=self.vendor, status="completed", quality_rating=5)
        self.purchase_order3 = PurchaseOrder.objects.create(vendor=self.vendor, status="completed", quality_rating=3)
        self.purchase_order4 = PurchaseOrder.objects.create(vendor=self.vendor, status="completed", quality_rating=2)
        self.purchase_order5 = PurchaseOrder.objects.create(vendor=self.vendor, status="completed", quality_rating=5)

    def test_vendor_performance(self):
        url = reverse('vendor-performance', kwargs={'vendor_id': self.vendor.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add assertions for performance metrics based on your logic

    def test_vendor_performance_vendor_not_found(self):
        url = reverse('vendor-performance', kwargs={'vendor_id': 999})  # Assuming 999 is not a valid vendor ID
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
