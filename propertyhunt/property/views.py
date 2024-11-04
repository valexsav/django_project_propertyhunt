from django.shortcuts import render, get_object_or_404,redirect
from .models import Property
from .forms import PropertyForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from .forms import PropertySortForm, PropertyFilterForm


@login_required
def index_view(request):
    sort_form = PropertySortForm(request.GET or None)
    filter_form = PropertyFilterForm(request.GET or None)
    properties = Property.objects.all()

    if sort_form.is_valid() and sort_form.cleaned_data:
        sort_by = sort_form.cleaned_data.get('sort_by')
        if sort_by:
            properties = properties.order_by(sort_by)

    if filter_form.is_valid() and filter_form.cleaned_data:
        filters ={}

        min_price = filter_form.cleaned_data.get('min_price')
        if min_price:
            filters['price__gte'] = min_price

        max_price = filter_form.cleaned_data.get('max_price')
        if max_price:
            filters['price__lte'] = max_price

        min_area = filter_form.cleaned_data.get('min_area')
        if min_area:
            filters['area__gte'] = min_area

        max_area = filter_form.cleaned_data.get('max_area')
        if max_area:
            filters['area__lte'] = max_area

        properties = properties.filter(**filters)
    
    return render(
        request,
        'index.html',
        context={
            'properties': properties,
            'sort_form': sort_form,
        }
    ) 


def the_property_view(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(
        request,
        'the_property.html',
        context={'property': property}
    )


def my_properties_view(request):
    my_properties = Property.objects.filter(owner_id=request.user.id)
    return render(
        request,
        'my_properties.html',
        context={'my_properties': my_properties}
    )


def edit_property_view(request, property_id):
    property_data = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property_data)
        if form.is_valid():
            form.save()
            return redirect('my_properties')
    elif request.method == 'GET':
        form = PropertyForm(instance=property_data)
    return render(
        request,
        'edit_property.html',
        context={
            'form': form,
            'property': property_data
        }
    )


def delete_property(request, property_id):
    if request.method == 'POST':
        the_property = get_object_or_404(Property, id=property_id)
        the_property.delete()
        return redirect('my_properties')
    else:
        return HttpResponseNotAllowed(['POST'])
    

def create_property_view(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner_id = request.user.id
            property.save()
            return redirect('my_properties')
    elif request.method == 'GET':
        form = PropertyForm()
        return render(
            request,
            'create_property.html',
            context={'form': form}
        )
    