from django.contrib import admin

from the_thing.models import (
    AThing,
)

@admin.register(AThing)
class AccessPlanAdmin(admin.ModelAdmin):
    """
    Admin class for the AccessPlan
    """
    readonly_fields = (
        'uuid',
    )
    list_display = (
        'uuid',
    )
    search_fields = (
        'uuid'
    )
    list_filter = ()
