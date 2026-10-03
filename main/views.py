from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Student

def welcome(request):
    return render(request, 'main/welcome.html')

def home(request):
    student_list = Student.objects.all()
    paginator = Paginator(student_list, 10)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    return render(request, 'main/home.html', {
        'students': students
    })