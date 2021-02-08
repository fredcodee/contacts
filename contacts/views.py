from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Contact


# Create your views here.
def index(request):
  context = {'contacts': Contact.objects.all()}
  return render(request, 'contacts/index.html', context)


#add contacts
def addpage(request):
  return render(request, 'contacts/add.html')

def add(request):
  first_name = request.POST['firstname']
  last_name = request.POST['lastname']
  relation = request.POST['relation']
  number = int(request.POST['number'])
  email = request.POST['email']
  address = request.POST['address']

  try:
    new_contact = Contact(first_name = first_name,last_name = last_name, relation = relation, number = number,email = email, address = address)
    new_contact.save()
  except:
    raise Http404("Flight does not exist")
  return HttpResponseRedirect(reverse('addpage'))

#view contact
def view(request, contact_id):
  try:
    contact = Contact.objects.get(pk = contact_id)
  except Contact.DoesNotExist:
    raise Http404('Contact does not exist')
  context = {
      'contact': contact
  }
  return render(request, 'contacts/view.html', context)

#delete contact
def delete(request,contact_id):
  try:
    contact =Contact.objects.get(pk= contact_id)
  except Contact.DoesNotExist:
    raise Http404('Contact does not exist')
  contact.delete()

  return HttpResponseRedirect(reverse('index'))

#edit contact
def edit(request, contact_id):
  try:
    contact =  Contact.objects.get(pk=contact_id)
  except:
    raise Http404("Flight does not exist")

  if request.method == 'POST':
    if request.POST['firstname'] :
      contact.first_name = request.POST['firstname']
    if request.POST['lastname']:
      contact.last_name = request.POST['lastname']
    if request.POST['relation']:
      contact.relation = request.POST['relation']
    if request.POST['number'] :
      contact.number = int(request.POST['number'])
    if request.POST['email']:
      contact.email = request.POST['email']
    if request.POST['address']:
      contact.address = request.POST['address']
    contact.save()
    
    return HttpResponseRedirect(reverse('index'))

  return render(request, 'contacts/edit.html', {'contact': contact})
