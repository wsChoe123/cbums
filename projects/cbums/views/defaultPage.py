from django.shortcuts import render, get_object_or_404


def defaultPage(request):
    """
        기본 페이지
    """
    return render(request, 'cbums/default/default.html')