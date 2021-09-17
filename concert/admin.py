from django.contrib import admin
from .models import Concert


@admin.register(Concert)
class AdminForConcert(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    # prepopulated_fields = {
    #     "slug": ("title",),
    # }


# admin.site.register(AnotherModel)
