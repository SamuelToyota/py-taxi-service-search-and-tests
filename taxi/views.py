from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Car, Manufacturer
from .forms import DriverLicenseUpdateForm, CarForm


User = get_user_model()


# -------------------- DRIVERS --------------------
class DriverListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "taxi/driver_list.html"
    context_object_name = "drivers"

    def get_queryset(self):
        queryset = User.objects.all()
        search_value = self.request.GET.get("search", "")
        if search_value:
            queryset = queryset.filter(username__icontains=search_value)
        return queryset


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "taxi/driver_detail.html"


class DriverCreateView(LoginRequiredMixin, generic.CreateView):
    model = User
    fields = ["username", "first_name", "last_name", "email", "license_number"]
    template_name = "taxi/driver_form.html"
    success_url = reverse_lazy("driver-list")


class DriverLicenseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = DriverLicenseUpdateForm
    template_name = "taxi/driver_license_form.html"
    success_url = reverse_lazy("driver-list")


class DriverDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = "taxi/driver_confirm_delete.html"
    success_url = reverse_lazy("driver-list")


# -------------------- CARS --------------------
class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "cars"

    def get_queryset(self):
        queryset = Car.objects.select_related("manufacturer").prefetch_related("drivers")
        search_value = self.request.GET.get("search", "")
        if search_value:
            queryset = queryset.filter(model__icontains=search_value)
        return queryset


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"

    def post(self, request, *args, **kwargs):
        car = self.get_object()
        if request.user in car.drivers.all():
            car.drivers.remove(request.user)
        else:
            car.drivers.add
