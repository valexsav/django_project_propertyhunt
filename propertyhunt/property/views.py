from django.shortcuts import render, get_object_or_404,redirect

from .models import Property

from .forms import PropertyForm

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseNotAllowed


@login_required
def index_view(request):
    properties = Property.objects.all()
    return render(
        request,
        'index.html',
        context={'properties': properties}
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
        context={'form': form, 'property': property_data}
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
        form = PropertyForm(request.POST)
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
    