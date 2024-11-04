from django.shortcuts import render, redirect, get_object_or_404
from .forms import MessageForm
from django.contrib.auth.decorators import login_required

from .models import Interest
from property.models import Property


@login_required
def show_interest(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user_id = request.user.id
            message.property_id = property_id
            message.save()
            return redirect('the_property', property_id=property.id)
        
    elif request.method == 'GET':
        form = MessageForm()
    return render(
        request,
        'show_interest.html',
        context={
        'form': form,
        'property': property
        }
    )


def messages_owner(request):
    my_properties_ids = Property.objects.filter(owner_id=request.user.id).values_list('id', flat=True)
    income_messages = Interest.objects.filter(property_id__in=my_properties_ids).select_related('user', 'property')

    return render(
        request,
        'messages_owner.html',
        context={
            'income_messages': income_messages
        }
    )
