from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.http import FileResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import get_template
from django.conf import settings
from .models import PDFModel
from django.conf import settings
from django.core.mail import send_mail
from xhtml2pdf import pisa
from .forms import *
from io import BytesIO
import random
import uuid

# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponseRedirect('/login/')

class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(f'/dashboard/{request.user.id}')
        emp_register = Registration_Form()
        return render(request, 'UserLogin/register.html', {'register': emp_register})

    def post(self, request):
        emp_register = Registration_Form()
        register = Registration_Form(request.POST)
        if register.is_valid():
            messages.success(request, "Registration Completed Successfully!!")
            register.save()
            return HttpResponseRedirect('/login/')
        else:
            return render(request, 'UserLogin/register.html', {'register': register})


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(f'/dashboard/{request.user.id}')
        emp_login_form = Login_Form()
        return render(request, 'UserLogin/login.html', {'login': emp_login_form})

    def post(self, request):
        login_form = Login_Form(request, request.POST)
        if login_form.is_valid():
            uname = login_form.cleaned_data.get('username')
            upass = login_form.cleaned_data.get('password')
            user = authenticate(username=uname, password=upass)
            if user != None:
                login(request, user)
                return HttpResponseRedirect(f"/dashboard/{user.id}/")
            else:
                return render(request, 'UserLogin/login.html', {'login': login_form})
        else:
            return render(request, 'UserLogin/login.html', {'login': login_form})


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login/')


class Dashboard(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(f'/login/')
        return render(request, 'UserLogin/dashboard.html')


class OTP(View):
    def get(self, request, email):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(f'/login/')
        otp = random.randint(1000, 9999)
        subject = 'OTP Verification'
        message = f'The One Time Password (OTP) for http://127.0.0.1:8000 is {otp}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        return JsonResponse({'otp': otp})


def save_pdf(params):
    template = get_template('UserLogin/pdf_data.html')
    html = template.render(params)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), response)
    file_name = uuid.uuid4()
    try:
        with open(str(settings.BASE_DIR) + f'/media/pdfs/{file_name}.pdf', 'wb+') as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), output)
    except Exception as e:
        print(e)

    if pdf.err:
        return pdf.err, False

    else:
        return file_name, True


class First(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(f'/login/')
        return render(request, 'UserLogin/first.html')

    def post(self, request):
        pdf_model = PDFModel()
        title = request.POST.get('title')
        description = request.POST.get('description')

        if len(title.strip()) == 0 or len(description.strip()) == 0:
            messages.error(request, "All The Fields Are Compulsory!!!")
            return render(request, 'UserLogin/first.html')

        params = {
            'id': request.user.id,
            'title': title,
            'description': description,
        }

        file_name, status = save_pdf(params)
        if status:
            pdf_model.pdf = f'pdfs/{file_name}.pdf'
            pdf_model.save()
            pdf_model = PDFModel.objects.latest('id')
            messages.success(
                request, f'http://127.0.0.1:8000/pdf/{pdf_model.id}/')
            return render(request, 'UserLogin/first.html', {'success': True})
        else:
            messages.error(request, 'No PDF Available!!!')
            return render(request, 'UserLogin/first.html')


class Second(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(f'/login/')
        return render(request, 'UserLogin/second.html')

    def post(self, request):
        pdf_model = PDFModel()
        title = request.POST.get('title')
        description = request.POST.get('description')

        if len(title.strip()) == 0 or len(description.strip()) == 0:
            messages.error(request, "All The Fields Are Compulsory!!!")
            return render(request, 'UserLogin/second.html')

        params = {
            'id': request.user.id,
            'title': title,
            'description': description,
        }

        file_name, status = save_pdf(params)
        if status:
            pdf_model.pdf = f'pdfs/{file_name}.pdf'
            pdf_model.save()
            pdf_model = PDFModel.objects.latest('id')
            messages.success(
                request, f'http://127.0.0.1:8000/pdf/{pdf_model.id}/')
            return render(request, 'UserLogin/second.html', {'success': True})
        else:
            messages.error(request, 'No PDF Available!!!')
            return render(request, 'UserLogin/second.html')


class Third(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(f'/login/')
        return render(request, 'UserLogin/third.html')

    def post(self, request):
        pdf_model = PDFModel()
        title = request.POST.get('title')
        description = request.POST.get('description')

        if len(title.strip()) == 0 or len(description.strip()) == 0:
            messages.error(request, "All The Fields Are Compulsory!!!")
            return render(request, 'UserLogin/third.html')

        params = {
            'id': request.user.id,
            'title': title,
            'description': description,
        }

        file_name, status = save_pdf(params)
        if status:
            pdf_model.pdf = f'pdfs/{file_name}.pdf'
            pdf_model.save()
            pdf_model = PDFModel.objects.latest('id')
            messages.success(
                request, f'http://127.0.0.1:8000/pdf/{pdf_model.id}/')
            return render(request, 'UserLogin/third.html', {'success': True})
        else:
            messages.error(request, 'No PDF Available!!!')
            return render(request, 'UserLogin/third.html')


class Fourth(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(f'/login/')
        return render(request, 'UserLogin/fourth.html')

    def post(self, request):
        pdf_model = PDFModel()
        print(request.POST)
        title = request.POST.get('title')
        description = request.POST.get('description')

        if len(title.strip()) == 0 or len(description.strip()) == 0:
            messages.error(request, "All The Fields Are Compulsory!!!")
            return render(request, 'UserLogin/fourth.html')

        params = {
            'id': request.user.id,
            'title': title,
            'description': description,
        }

        file_name, status = save_pdf(params)
        if status:
            pdf_model.pdf = f'pdfs/{file_name}.pdf'
            pdf_model.save()
            pdf_model = PDFModel.objects.latest('id')
            messages.success(
                request, f'http://127.0.0.1:8000/pdf/{pdf_model.id}/')
            return render(request, 'UserLogin/fourth.html', {'success': True})
        else:
            messages.error(request, 'No PDF Available!!!')
            return render(request, 'UserLogin/fourth.html')


class PDF(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(f'/login/')
        try:
            pdf_model = PDFModel.objects.get(pk=id)
            if pdf_model.count < 5:
                pdf_model.count += 1
                pdf_model.save()
                return render(request, 'UserLogin/otp.html')
            else:
                return HttpResponse('<h1>Invalid Link!!!</h1>')
        except Exception as e:
            return HttpResponse(f"<h2>{e}</h2>")

    def post(self, request, id):
        post_data = request.POST
        otp = post_data.get('otp-hidden')
        input_1 = post_data.get('input-1')
        input_2 = post_data.get('input-2')
        input_3 = post_data.get('input-3')
        input_4 = post_data.get('input-4')
        user_otp = f"{input_1}{input_2}{input_3}{input_4}"
        if otp != "" and user_otp != "" and otp == user_otp:
            pdf_model = PDFModel.objects.get(pk=id)
            return FileResponse(open(f"media/{pdf_model.pdf.name}", "rb"), content_type="application/pdf")
        else:
            messages.error(request, "Invalid OTP!!!")
            return render(request, 'UserLogin/otp.html', {'error': True, 'send_otp' : otp})
