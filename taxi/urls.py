from django.urls import path
from . import views

urlpatterns = [
    path("drivers/", views.DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/", views.DriverDetailView.as_view(), name="driver-detail"),
    path("drivers/create/", views.DriverCreateView.as_view(), name="driver-create"),
    path("drivers/<int:pk>/update-license/", views.DriverLicenseUpdateView.as_view(),
         name="driver-license-update"),
    path("drivers/<int:pk>/delete/", views.DriverDeleteView.as_view(),
         name="driver-delete"),

    path("cars/", views.CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", views.CarDetailView.as_view(), name="car-detail"),
    path("cars/create/", views.CarCreateView.as_view(), name="car-create"),

    path("manufacturers/", views.ManufacturerListView.as_view(),
         name="manufacturer-list"),
]
