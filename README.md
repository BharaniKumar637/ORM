# Ex02 Django ORM Web Application
## Date: 14/09/2025

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## ENTITY RELATIONSHIP DIAGRAM:
<img width="1048" height="733" alt="image" src="https://github.com/user-attachments/assets/ef57c820-1b33-4985-8546-f62964e858b0" />

## PROGRAM

MODELS.PY

```
from django.db import models
from django.contrib import admin
class Movies(models.Model):
    M_ID=models.IntegerField(primary_key=True)
    M_name=models.CharField(max_length=100)
    Release_date=models.DateField()
    Director=models.CharField(max_length=50)
    Actors=models.CharField(max_length=100)
 
class MoviesAdmin(admin.ModelAdmin):
    list_display=('M_ID','M_name','Release_date','Director','Actors')  


```
ADMIN.PY
```
from django.contrib import admin
from .models import Movies, MoviesAdmin
admin.site.register(Movies, MoviesAdmin)

```


## OUTPUT

![alt text](<Screenshot 2025-09-08 143503.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
