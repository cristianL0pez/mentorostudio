from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def code_server(request):
    return render(request, "code_server.html")

# Create your views here.
