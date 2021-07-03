from django.contrib import admin
from django.urls import path

from tours.views import main_view
from tours.views import departure_view
from tours.views import tour_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('departure/<str:departure_id>', departure_view),
    path('tour/<int:tour_id>', tour_view)
]
