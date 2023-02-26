from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'product',
        'created_at',
        'rating',
    )

    ordering = ('-created_at',)


admin.site.register(Review, ReviewAdmin)