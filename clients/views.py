from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib import messages
from .models import Client
from .forms import ClientForm
# Create your views here.

def get_all_clients(request):
    clients = Client.objects.order_by("-joined_date")
    print(clients)
    return render(request, 'clients/clients.html', {'clients': clients})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            try:    
                form.save()
                return redirect('clients') 
            except IntegrityError:
                form.add_error('email', 'Email already associated to another client.')
    else:
        form = ClientForm()

    return render(request, 'clients/client.html', {'form': form})

def update_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            if form.has_changed():
                try:
                    form.save()
                    return redirect('clients')
                except IntegrityError as e:
                    form.add_error('email', 'Email already associated to another client.')
            else:
                messages.info(request, "No change was detected.")
    else:
        form = ClientForm(instance=client)
    
    return render(request, 'clients/client.html', {'form': form})

def toggle_client_status(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    try:
        client.is_active = not client.is_active
        client.save()
    except Exception as e:
        messages.warning(request, str(e))
    return redirect('clients')

