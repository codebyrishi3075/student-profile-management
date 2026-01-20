from django.http import JsonResponse, HttpRequest, HttpResponse
from .models import Student
from django.shortcuts import render, get_object_or_404
from django.db.models import QuerySet
from django.contrib import messages


def add_student(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        try:
            name = request.POST.get('student_name', '').strip()
            email = request.POST.get('email', '').strip()
            age = request.POST.get('age', '').strip()
            profile_image = request.FILES.get('profile_image')

            # Validation
            if not name:
                return JsonResponse({
                    'success': False,
                    'message': 'Student name is required.'
                }, status=400)
            
            if not email:
                return JsonResponse({
                    'success': False,
                    'message': 'Email is required.'
                }, status=400)
            
            if not age:
                return JsonResponse({
                    'success': False,
                    'message': 'Age is required.'
                }, status=400)

            # Check if email already exists
            if Student.objects.filter(email=email).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'Email already exists.'
                }, status=400)

            # Create student
            Student.objects.create(
                name=name,
                email=email,
                age=age,
                profile_image=profile_image
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Student added successfully!',
                'redirect_url': '/student/list/'  # URL to redirect after success
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error: {str(e)}'
            }, status=400)
    
    # GET request
    return render(request, 'student/add_student.html')


def student_list(request: HttpRequest) -> HttpResponse:
    students: QuerySet = Student.objects.all().order_by('-created_at')
    print(f'\nViews Hit Successfully. Database Data: {students}')
    return render(request, 'student/student_list.html', {'students': students})


def student_detail(request: HttpRequest, id: int) -> HttpResponse:
    student = get_object_or_404(Student, id=id)
    return render(request, 'student/details.html', {'student': student})