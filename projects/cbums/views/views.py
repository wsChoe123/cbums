from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
import hashlib
from cbums.models import TbMember
import bcrypt


# Create your views here.
def defaultPage(request):
    """
        기본 페이지
    """
    return render(request, 'cbums/default/default.html')

def signUp(request):
    """
        이메일 입력 페이지
    """
    return render(request, 'cbums/signUp/certifyMail/certifyMail.html')

@csrf_exempt
def inputCode(request):
    """
        인증 코드 입력 페이지
    """
    # session 값 초기화 코드
    # del request.session['code']
    # return render(request, 'cbums/signUp/inputCode/inputCode.html')

    code = request.session.get('code','none')
    if code == 'none':
        ip = get_client_ip(request)
        input_email = request.POST.get('email')
        # code = hashlib.sha256()
        # code.update((str)(input_email).encode('utf-8'))
        # request.session['code'] = (str)(code.hexdigest())
        # content = (str)(code.hexdigest())
        request.session['code'] = get_hash_value(input_email)
        content = get_hash_value(input_email)
        title = '씨부엉 회원가입 인증코드'
        email = EmailMessage(title, content, to=[input_email])
        email.send()
        print("ip : %s 이메일 전송 완료"%ip)
        return render(request, 'cbums/signUp/inputCode/inputCode.html')
    else:
        input_code = request.POST.get('code')
        ip = get_client_ip(request)
        if (input_code == (str)(request.session['code'])):
            del request.session['code']
            print("ip : %s 세션 값 삭제"%ip)
            return render(request, 'cbums/signUp/inputSignUpContent/inputSignUpContent.html')
        else :
            return render(request, 'cbums/signUp/inputCode/inputCode.html')


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


@csrf_exempt
def login(request):
    input_id = request.POST.get('user_id')
    input_pw = request.POST.get('user_pw')
    print(input_id)
    print(input_pw)

    return render(request, 'cbums/login/login.html')



# client ip function
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# hash function : key-streching & solting algorithm
# bycrypt 설치하면 끝남. 이거 없어도 됨.
def get_hash_value(value):
    data = hashlib.sha256()
    solt = "asiefak!@#!E@Q#4kjsdfiaekfaleif"
    data.update((str)(value).encode('utf-8'))
    data.update((str)(solt).encode('utf-8'))
    temp_value = (str)(data.hexdigest())
    for count in range(1000000):
        temp_hash = hashlib.sha256()
        temp_hash.update((temp_value).encode('utf-8'))
        temp_value = (str)(temp_hash.hexdigest())
    return temp_value