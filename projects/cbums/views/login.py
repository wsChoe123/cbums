from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    input_id = request.POST.get('user_id')
    input_pw = request.POST.get('user_pw')
    print(input_id)
    print(input_pw)

    return render(request, 'cbums/login/login.html')
