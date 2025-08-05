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

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages




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
#             return JsonResponse({'status': 'success'}, status=200)
#         except:
#             return JsonResponse({'status': 'error'}, status=500)

#     return JsonResponse({'error': 'Invalid request'}, status=400)




from django.http import JsonResponse
from django.http import JsonResponse

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['siddhidoiphode2022@gmail.com'],
            )
            return JsonResponse({'status': 'success', 'message': '✅ Email sent successfully!'})
            





            
        except:
            return JsonResponse({'status': 'error', 'message': '❌ Email sending failed!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

# from django.conf import settings
# print("ALLOWED_HOSTS at runtime =", settings.ALLOWED_HOSTS)
