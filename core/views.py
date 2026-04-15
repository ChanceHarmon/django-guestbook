from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import VisitorEntry
from .forms import VisitorEntryForm
# Create your views here.


# Basic first test
def accept_req(request):
    req_message = request.GET.get('message', 'default')
    # return HttpResponse(f"You said: {req_message}")
    return JsonResponse({"message": req_message})

# Render Homepage
def render_homepage(request):
    if request.method == "POST":
        form = VisitorEntryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Entry added to the guestbook!")
            return redirect("/guestbook/")

    else:
        form = VisitorEntryForm()

    entries = VisitorEntry.objects.order_by("-created_at")

    return render(request, "core/guestbook.html", {
        "form": form,
        "entries": entries,
    })



# Get and Post visitors
def list_visitors(request):
    if request.method == "POST":
        name = request.POST.get("name", "test name")
        message = request.POST.get("message", "test message")
        created_visitor = VisitorEntry.objects.create(name=name, message=message)
        return JsonResponse({"name": created_visitor.name, "message": created_visitor.message})

    else:    
        entries = VisitorEntry.objects.all()
        entry_info = [{"name": entry.name, "message": entry.message} for entry in entries]
        return JsonResponse(entry_info, safe=False)


# Delete entry
def delete_entry(request, entry_id):
    if request.method == "POST":
        entry = VisitorEntry.objects.get(id=entry_id)
        entry.delete()
    return redirect("/guestbook/")