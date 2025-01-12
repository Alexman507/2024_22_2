from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import ProductForm, VersionForm
from main.models import Product, Contact, Order, Version


class GetContextMixin:
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version'] = Version.objects.all()
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("main:product_list")


class ProductListView(GetContextMixin, ListView):
    model = Product


class ProductDetailView(GetContextMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:product_list')


class ContactListView(ListView):
    model = Contact


class OrderCreateView(CreateView):
    model = Order  # Модель
    fields = ('name', 'phone', 'message', 'created_at')  # Поля для заполнения при создании
    success_url = reverse_lazy('main:product_list')  # Адрес для перенаправления после успешного создания

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response


class VersionListView(ListView):
    model = Version


class VersionDetailView(DetailView):
    model = Version


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("main:versions")


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("main:versions")


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy("main:versions")
