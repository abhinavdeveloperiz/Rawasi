from django.db import models

# Create your models here.


class BannerImages(models.Model):
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return f"Banner Image {self.id}"
    
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


class Projects(models.Model):
    image = models.ImageField(upload_to='projects/')
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"



    
    


    

    

    

