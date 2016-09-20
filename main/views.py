from django.shortcuts import render

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

def rsvp_view(req):
	context = {}
	#context["name_form"] = NameForm()
	return render(req, "rsvp.html", context)

def rsvp_post(req):
	if req.method != 'POST':
		raise Http404('Invalid request.')
	f = NameForm(req.POST)
	if not f.is_valid():
		raise Http404('Invalid form.')

	first_name = task_form.cleaned_data["first_name"]
	last_name = task_form.cleaned_data["last_name"]
	title = task_form.cleaned_data["title"]
	attending = task_form.cleaned_data["attending"]
	meal = task_form.cleaned_data["meal"]

	Person.objects.create(first_name=first_name, last_name=last_name,
							title=title, attending=attending, meal=meal)

	context = {post_success:true}
	return render(req, "main.html", context)
