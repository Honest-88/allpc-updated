from django.db import models
from tinymce.models import HTMLField

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)
    feedback = models.TextField()

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us' 


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
        

class DMCA(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    about = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Digital Millennium Copyright Act'
        verbose_name_plural = 'Digital Millennium Copyright Act'

    def __str__(self):
        return self.subject


class PrivacyPolicy(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    about = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Our Privacy Policy'
        verbose_name_plural = 'Our Privacy Policy'

    def __str__(self):
        return self.subject


class TermsOfUse(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    about = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Terms Of Use'
        verbose_name_plural = 'Terms Of Use'

    def __str__(self):
        return self.subject

class AboutUs(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    about = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


    def __str__(self):
        return self.subject



