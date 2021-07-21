from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from cbums.models import TbMember
from cbums.views.get_client_ip import get_client_ip

@csrf_exempt
def inputInfo(request):
    """
        사용자 정보 입력 페이지
    """
    if(request.POST.get('name') != '' and request.POST.get('nickname') != '' and request.POST.get('school_number') != ''
    and request.POST.get('password') != ''):
        name = request.POST.get('name')
        school_number = request.POST.get('school_number')
        nickname = request.POST.get('nickname')
        input_password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if(input_password != re_password):
            return render(request, 'cbums/signUp/inputSignUpContent/inputSignUpContent.html')
        data = TbMember(m_name=name, class_no=school_number, password=input_password,department="computer",sysop_status=1)
        data.save()
        ip = get_client_ip(request)
        print("ip : %s signUp is succeed"%ip)
        return render(request, 'cbums/default/default.html')
    else:
        return render(request, 'cbums/signUp/inputSignUpContent/inputSignUpContent.html')