from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from cbums.views.get_client_ip import get_client_ip
from cbums.views.get_hash_value import get_hash_value


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

