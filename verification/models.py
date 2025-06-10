from django.db import models

class VerificationRequest(models.Model):
    aadhaar_image = models.ImageField(upload_to='aadhaar/')
    selfie_image = models.ImageField(upload_to='selfie/')
    dob_extracted = models.CharField(max_length=20, blank=True)
    face_match = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)