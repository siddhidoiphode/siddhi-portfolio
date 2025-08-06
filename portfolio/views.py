from django.http import HttpResponse,HttpRequest
from django.http import FileResponse, Http404
import os
from django.conf import settings
from django.shortcuts import redirect, render

def home(request):
    return render(request,"index.html")


def view_resume(request):
    file_path = os.path.join(settings.STATICFILES_DIRS[0], 'docs', 'resume.pdf')
    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404("Resume not found")



def emenuPresentation(request):
    file_path = os.path.join(settings.STATICFILES_DIRS[0], 'docs', 'emenuPresentation.pdf')
    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404("Presenation not found")  


def emenuReport(request):
    file_path = os.path.join(settings.STATICFILES_DIRS[0], 'docs', 'emenuReport.pdf')
    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404("Report not found")  
      

def ecommerceSalesReport(request):
    file_path = os.path.join(settings.STATICFILES_DIRS[0], 'docs', 'ecommerceSalesReport.pdf')
    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404("Report not found")  
      
def webEmenu(request):
    return render(request, 'webEmenu.html')

def webCarnival(request):
    return render(request , 'webCarnival.html')

def webEcommerceSalesDashboard(request):
    return render(request, 'webEcommerceSalesDashboard.html')


def SupermarketSalesDashboard(request):
    return render(request, 'SupermarketSalesDashboard.html')

# from django.core.mail import send_mail
# from django.conf import settings
# from django.shortcuts import render
# from django.contrib import messages
# from django.http import JsonResponse

# def contact_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         full_message = f"Message from {name} ({email}):\n\n{message}"

#         try:
#             send_mail(
#                 subject,
#                 full_message,
#                 settings.DEFAULT_FROM_EMAIL,
#                 ['siddhidoiphode2022@gmail.com'],
#             )
#             return JsonResponse({'status': 'success', 'message': '✅ Email sent successfully!'})
  
#         except:
#             return JsonResponse({'status': 'error', 'message': '❌ Email sending failed!'})

#     return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


# from django.conf import settings
# import requests



# def verify_email(request):
#     email = request.GET.get('email')
#     if not email:
#         return JsonResponse({'error': 'Email required'}, status=400)

#     url = "http://apilayer.net/api/check"
#     params = {
#         'access_key': settings.MAILBOXLAYER_API_KEY,
#         'email': email,
#         'smtp': 1,
#         'format': 1
#     }

#     try:
#         response = requests.get(url, params=params)
#         data = response.json()

#         if data.get('format_valid') and data.get('smtp_check'):
#             return JsonResponse({'valid': True, 'message': '✅ Valid email'})
#         else:
#             return JsonResponse({'valid': False, 'message': '❌ Invalid or fake email'})

#     except Exception as e:
#         return JsonResponse({'error': 'Failed to verify email', 'details': str(e)}, status=500)





from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
import requests

def contact_view(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not (name and email and subject and message):
            return JsonResponse({'status': 'error', 'message': '❌ All fields are required'})

        # Optional server-side email re-validation (secure fallback)
        if not email.endswith('@gmail.com'):
            return JsonResponse({'status': 'error', 'message': '❌ Only Gmail addresses are accepted'})

        try:
            full_message = f"From: {name} <{email}>\n\n{message}"
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['siddhidoiphode2022@gmail.com']
            )
            return JsonResponse({'status': 'success', 'message': '✅ Email sent successfully!'})
        except Exception:
            return JsonResponse({'status': 'error', 'message': '❌ Email sending failed!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def verify_email(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'valid': False, 'message': '❌ Email required'}, status=400)

    url = "http://apilayer.net/api/check"
    params = {
        'access_key': settings.MAILBOXLAYER_API_KEY,
        'email': email,
        'smtp': 1,
        'format': 1
    }

    try:
        res = requests.get(url, params=params)
        data = res.json()

        if data.get('format_valid') and data.get('smtp_check'):
            return JsonResponse({'valid': True, 'message': '✅ Valid email'})
        else:
            return JsonResponse({'valid': False, 'message': '❌ Invalid or disposable email'})
    except Exception as e:
        return JsonResponse({'valid': False, 'message': '⚠ Verification failed'}, status=500)
