from django.shortcuts import render, get_object_or_404


def signUp(request):
    """
        이메일 입력 페이지
    """
    return render(request, 'cbums/signUp/certifyMail/certifyMail.html')
