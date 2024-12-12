from django.shortcuts import redirect
from .models import Property
from .forms import PropertyForm
from .forms import PropertySortAndFilterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.urls import reverse, reverse_lazy

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@method_decorator(cache_page(60*15), name='dispatch')
class PropertyListView(ListView, LoginRequiredMixin):
    model = Property
    template_name = 'index.html'
    context_object_name = 'properties'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.sort_and_filter_form = PropertySortAndFilterForm(self.request.GET or None)
        if self.sort_and_filter_form.is_valid():
            cleaned_data = self.sort_and_filter_form.cleaned_data
            filters = {}
            filter_fields = {
            'min_price': 'price__gte',
            'max_price': 'price__lte',
            'min_area': 'area__gte',
            'max_area': 'area__lte',
            }
            
            for field, query_param in filter_fields.items():
                value = cleaned_data.get(field)
                if value:
                    filters[query_param] = value
            queryset = queryset.filter(**filters)

            sort_by = cleaned_data.get('sort_by')
            if sort_by:
                queryset = queryset.order_by(sort_by)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_and_filter_form'] = self.sort_and_filter_form
        return context


class PropertyDetailView(DetailView, LoginRequiredMixin):
    model = Property
    template_name = 'the_property.html'
    context_object_name = 'the_property'


class MyPropertiesListView(ListView, LoginRequiredMixin):
    model = Property
    template_name = 'my_properties.html'
    context_object_name = 'owner_properties'

    def get_queryset(self):
        return Property.objects.filter(owner_id=self.request.user.id)


class PropertyUpdateView(UpdateView, LoginRequiredMixin):
    model = Property
    template_name = 'edit_property.html'
    form_class = PropertyForm

    # rewrite redirect logic if form is valid
    def get_success_url(self):
        return reverse('the_property', kwargs={'pk': self.object.pk})
    

class PropertyDeleteView(DeleteView, LoginRequiredMixin):
    model = Property
    success_url = reverse_lazy('owner_properties')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class PropertyCreateView(CreateView, LoginRequiredMixin):
    model = Property
    form_class = PropertyForm
    template_name = 'create_property.html'

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('the_property', kwargs={'pk': self.object.pk})
