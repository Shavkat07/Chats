from django.shortcuts import render, get_object_or_404, redirect
from .models import Vacancy
from django.http import HttpResponse

# Create your views here.

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy_list.html', {'vacancies': vacancies})

def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    return render(request, 'vacancy_detail.html', {'vacancy': vacancy})

def create_vacancy(request):
    if 'POST' == request.method:
        title = request.POST['title']
        owner = request.user
        description = request.POST['description']
        pay = request.POST['pay']
        tags = request.POST.getlist('tags')
        required_level = request.POST['required_level']
        project_length = request.POST['project_length']
        
        vacancy = Vacancy(title=title, owner=owner, description=description, pay=pay, required_level=required_level, project_length=project_length)
        vacancy.save()
        vacancy.tags.set(tags)
        return redirect('vacancy_detail', vacancy_id=vacancy.id)
    
    elif 'GET' == request.method:
        if not request.user.is_authenticated:
            return HttpResponse('registration required.')
        return render(request, 'create_vacancy.html')
    
    elif 'DELETE' == request.mehtod:
        vacancy_id = request.GET.get('vacancy_id')
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)

        if vacancy.owner != request.user:
            return HttpResponse('Unauthorized')
        
        vacancy.delete()
        return HttpResponse('Vacancy deleted successfully.')