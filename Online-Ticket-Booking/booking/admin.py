from django.contrib import admin
from .models import Book, customer, ticket

# Register your models here.

admin.site.register(customer)
admin.site.register(ticket)
admin.site.register(Book)
