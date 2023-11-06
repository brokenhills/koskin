from django.contrib import admin

from core.models import (
    Writings,
    News,
    Main,
    Contact,
    Gallery,
    Biography,
)

admin.site.register(
    (
        Writings,
        News,
        Main,
        Contact,
        Gallery,
        Biography,
    )
)
