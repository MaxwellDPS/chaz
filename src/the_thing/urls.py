from django.urls import path
from the_thing.views import (
    a_thing,
)

urlpatterns = [
    path('athing/', a_thing.List.as_view()),
    path('athing/<uuid:request_uuid>/', a_thing.View.as_view()),
]
