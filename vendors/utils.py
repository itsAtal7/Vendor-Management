from .models import Vendor, PurchaseOrder

def calculate_vendor_performance(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    
    # Calculate On-Time Delivery Rate
    total_completed_orders = completed_orders.count()
    on_time_deliveries = completed_orders.filter(delivery_date__lte=models.F('issue_date')).count()
    on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * 100 if total_completed_orders > 0 else 0
    
    # Calculate Quality Rating Average
    quality_ratings = completed_orders.exclude(quality_rating=None).aggregate(avg_quality=models.Avg('quality_rating'))
    quality_rating_avg = quality_ratings['avg_quality'] if quality_ratings['avg_quality'] else 0
    
    # Calculate Response Time
    acknowledged_orders = completed_orders.exclude(acknowledgment_date=None)
    response_time = acknowledged_orders.aggregate(avg_response=models.Avg(models.F('acknowledgment_date') - models.F('issue_date')))
    average_response_time = response_time['avg_response'].total_seconds() / acknowledged_orders.count() if acknowledged_orders.count() > 0 else 0
    
    # Calculate Fulfilment Rate
    fulfilled_orders = completed_orders.filter(issue_date=models.F('acknowledgment_date'))
    fulfilment_rate = (fulfilled_orders.count() / total_completed_orders) * 100 if total_completed_orders > 0 else 0
    
    # Update Vendor model with performance metrics
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.quality_rating_avg = quality_rating_avg
    vendor.average_response_time = average_response_time
    vendor.fulfillment_rate = fulfilment_rate
    vendor.save()
