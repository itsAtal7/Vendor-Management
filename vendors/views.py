from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer
from .utils import *
from rest_framework.views import APIView
from django.db import models

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformance(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            purchase_orders = PurchaseOrder.objects.filter(vendor=vendor)

            total_orders = purchase_orders.count()
            if total_orders == 0:
                return Response({'error': 'No purchase orders found for this vendor'}, status=400)

            # Calculate on-time delivery rate
            on_time_deliveries = purchase_orders.filter(status='completed', delivery_date__lte=models.F('acknowledgment_date')).count()
            on_time_delivery_rate = (on_time_deliveries / total_orders) * 100

            # Calculate quality rating average
            quality_rating_avg = purchase_orders.aggregate(avg_quality=models.Avg('quality_rating'))['avg_quality']

            # Calculate average response time
            response_times = purchase_orders.exclude(acknowledgment_date=None).annotate(response_time=models.F('acknowledgment_date') - models.F('issue_date')).aggregate(avg_response=models.Avg('response_time'))
            average_response_time = response_times['avg_response'].total_seconds() / 3600  # Convert to hours

            # Calculate fulfillment rate
            fulfilled_orders = purchase_orders.filter(status='completed').count()
            fulfillment_rate = (fulfilled_orders / total_orders) * 100

            performance_metrics = {
                'on_time_delivery_rate': on_time_delivery_rate,
                'quality_rating_avg': quality_rating_avg,
                'average_response_time': average_response_time,
                'fulfillment_rate': fulfillment_rate,
            }
            return Response(performance_metrics)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=404)