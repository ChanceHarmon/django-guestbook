from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import VisitorEntry
# Create your views here.

def accept_req(request):
    req_message = request.GET.get('message', 'default')
    # return HttpResponse(f"You said: {req_message}")
    return JsonResponse({"message": req_message})

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
