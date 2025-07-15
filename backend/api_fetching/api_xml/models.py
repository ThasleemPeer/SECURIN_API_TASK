from django.db import models

# Create your models here.
class xml_file(models.Model):
    cpe_title=models.CharField(max_length=2000)
    cpe_22_uri=models.TextField()
    cpe_23_uri=models.TextField()
    reference_links=models.TextField()
    cpe_22_deprecation_date=models.DateField()
    cpe_23_deprecation_date=models.DateField()