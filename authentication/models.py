from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ADMINISTRADOR = 'ADMIN'
    GESTOR = 'GESTOR'
    USUARIO = 'USUARIO'
    VISITANTE = 'VISITANTE'
    
    ROLES = [
        (ADMINISTRADOR, 'Administrador'),
        (GESTOR, 'Gestor'),
        (USUARIO, 'Usuario Registrado'),
        (VISITANTE, 'Visitante'),
    ]
    
    rol = models.CharField(max_length=20, choices=ROLES, default=VISITANTE)

    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"