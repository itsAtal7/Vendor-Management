Used mySql as database.
1. Install mysqlServer(if already not)
2. Create database vendor_management
3. Install required modules
install mysql client, run command pip install mysqlclient
install rest framework, run command pip install djangorestframework 
4. Run command 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

Now open web browser in address bar. Run project on localhost
/api/vendors for create vendors

retrieve single vendor
api/vendors/1

For purchase order
api/purchase_orders

if tryin to store data using form, you can try this sample data
{
    "po_number": "PO123456",
    "order_date": "2024-05-06T10:39:22.505860Z",
    "delivery_date": "2024-05-07T12:01:00Z",
    "items": [
        "Item1",
        "Item2",
        "Item3"
    ],
    "quantity": 1,
    "status": "Delivered",
    "quality_rating": 1.0,
    "issue_date": "2024-05-06T10:39:22.506865Z",
    "acknowledgment_date": "2024-05-11T12:11:00Z",
    "vendor": 1
}

retrieve single purchase order
api/purchase_orders/1

For vendor performance
api/vendors/1/performance


To run test case
    For vendors, run command 
    python manage.py test vendors.tests.test_vendors.VendorTestCase

    For purchase order
    python manage.py test vendors.tests.test_purchase_order.PurchaseOrderTestCase.test_purchase_order_creation

    For vendor performance
    python manage.py test vendors.tests.test.test_vendor_performance.VendorPerformanceTestCase.test_vendor_performance