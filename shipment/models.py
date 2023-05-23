from django.db import models
import secrets


class Shipment(models.Model):
    sender_name = models.CharField(max_length=250)
    sender_nationality = models.CharField(max_length=100, null=True, blank=True)
    sender_location = models.CharField(max_length=100, null=True, blank=True)

    receiver_name = models.CharField(max_length=250, null=True, blank=True)
    receiver_address = models.CharField(max_length=300, null=True, blank=True)
    receiver_phone = models.CharField(max_length=20, null=True, blank=True)
    receiver_email =  models.EmailField(max_length=100, null=True, blank=True)

    tracking_number = models.CharField(max_length=80, null=True, blank=True)
    weight = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    shipment_location = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.tracking_number == None or self.tracking_number == '':
            tracking_number = secrets.token_urlsafe(8)
            object_with_similar_number = Shipment.objects.filter(tracking_number=tracking_number)
            if not object_with_similar_number:
                self.tracking_number=tracking_number
            else:
                self.tracking_number=f"{tracking_number} 'UED'"
        super(Shipment, self).save(*args, **kwargs)

    def __str__(self):
        return self.sender_name
    
