from django.db import models

# Create your models here.


class BannerImages(models.Model):
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.image.url
    
    class Meta:
        verbose_name = "Banner Image"
        verbose_name_plural = "Banner Images"


class Clients(models.Model):
    image = models.ImageField(upload_to='clients/')
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
    

class Services(models.Model):
    image = models.ImageField(upload_to='services/')
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
    


class Courses(models.Model):
    image = models.ImageField(upload_to='courses/')
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
    
    

class Students(models.Model):
    image = models.ImageField(upload_to='students/')
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
    

    
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
    

