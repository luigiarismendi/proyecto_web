from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home_publico(request):
    return render(request, 'home_publica.html')

@login_required
def dashboard(request):
    rol = getattr(request.user, 'rol', 'VISITANTE')
    
    if rol == 'ADMIN':
        return render(request, 'dashboard_admin.html')
    elif rol == 'GESTOR':
        return render(request, 'dashboard_gestor.html')
    elif rol == 'USUARIO':
        return render(request, 'dashboard_usuario.html')
    else:
        return render(request, 'home_publica.html')