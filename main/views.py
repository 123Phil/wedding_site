from django.http import HttpResponseRedirect, Http404
from django.forms import modelformset_factory
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Person


def main_view(req):
	return render(req, "main.html")

def details_view(req):
	return render(req, "details.html")

def travel_view(req):
	return render(req, "travel.html")

def photo_view(req):
	return render(req, "photos.html")

def registry_view(req):
	return render(req, "registry.html")


## RSVP helpers
def not_required(field):
    return field.formfield(required=False)

def get_factory():
	return modelformset_factory(Person, fields='__all__', extra=6, formfield_callback=not_required)


## RSVP views
def rsvp_view(req):
	PersonFormSet = get_factory()
	return render(req, "rsvp.html", {'formset': PersonFormSet(queryset=Person.objects.none())})

def rsvp_success(req):
	PersonFormSet = get_factory()
	return render(req, "rsvp.html", {'formset': PersonFormSet(queryset=Person.objects.none()), 'post_success': True})

def rsvp_post(req):
	if req.method != 'POST':
		raise Http404('Invalid request.')
	PersonFormSet = get_factory()
	people = PersonFormSet(req.POST)
	if not people.is_valid():
		return render(req, "rsvp.html", {'formset': people})

	for person in people:
		if 'first_name' in person.cleaned_data and len(person.cleaned_data['first_name']) > 0:
			#print('saving: ' + person.cleaned_data['first_name'])
			entry = person.save(commit=False)
			entry.save()
	
	# subject = 'Wedding RSVP'
	# message = [str(person) ...]
	# sender = 'some_email@gmail.com'
	# recipients = ['phillipwstewart@gmail.com']
	# send_mail(subject, message, sender, recipients)

	return HttpResponseRedirect('/rsvp_thanks')

		
