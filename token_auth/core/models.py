from django.db import models

# Create your models here.


# ------------------ registered user table --------------------------------------
class register(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=200, blank=False, default='')
    last_name = models.CharField(max_length=200, blank=False, default='')
    mobile = models.CharField(max_length=100, blank=False, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=False, default='')
    district = models.CharField(max_length=100, blank=False, default='')
    village = models.CharField(max_length=100, blank=False, default='')
    block = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.first_name

    class Meta:
        # The default ordering for the object, for use when obtaining lists of objects
        ordering = ['created']
