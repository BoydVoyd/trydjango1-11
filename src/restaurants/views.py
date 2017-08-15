from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
    
#     html_ = """
#     <!DOCTYPE html>
#     <html lang = en>
#         <head>
#         </head>
#         <body>
#             <h1>Hello World!</h1>
#             <p>Nathan is rad!</p>
#         </body>
#     </html>
#     """

#     return HttpResponse(html_)
#     #return render(request, "home.html",{})
def home(request):
    return render(request, "base.html", {})