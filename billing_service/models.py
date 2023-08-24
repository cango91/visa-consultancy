from django.db import models

# Create your models here.

class Payment(models.Model):
    job = models.ForeignKey('Job',on_delete=models.PROTECT)
    invoice = models.ForeignKey('Invoice',on_delete=models.PROTECT)
    PAYMENT_METHODS = (('cco','Online Credit/Debit Card'),
                       ('dep','Direct Deposit to Account'))
    method = models.CharField(max_length=25,choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=255)
    PAYMENT_STATUS = (('complete','Paid in Full'),
                      ('partial','Partially Paid'),
                      ('pending','Payment Pending'),
                      ('failed','Payment Failed'),
                      ('cancelled','Payment Cancelled'),
                      ('refunded','Payment Refunded'),
                      ('processing','Payment is Being Processed'))
    status = models.CharField(max_length=25)
    
class Invoice(models.Model):
    INVOICE_STATUS = (('draft', 'Draft'),
                      ('sent', 'Sent'),
                      ('partial', 'Partially Paid'),
                      ('paid', 'Paid in Full'),
                      ('overdue', 'Overdue'),
                      ('canceled', 'Canceled'))
    amount = models.DecimalField("Amount due", max_digits=10, decimal_places=2)
    status = models.CharField(max_length=25, choices=INVOICE_STATUS)