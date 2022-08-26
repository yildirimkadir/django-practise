from django.shortcuts import render, redirect
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'application/index.html')

def student_page(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        'form': form
    }

    return render(request, 'application/student.html', context)