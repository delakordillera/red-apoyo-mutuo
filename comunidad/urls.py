from django.urls import path
from django.contrib.auth import views as auth_views # Importante para el Login
from . import views

urlpatterns = [
    path('', views.muro_comunitario, name='muro'),
    path('ofrecer/', views.ofrecer_habilidad, name='ofrecer'),
    
    # Rutas de Autenticación
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='comunidad/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Gestión de Habilidades (CRUD)
    path('solicitar/<int:habilidad_id>/', views.solicitar_intercambio, name='solicitar_intercambio'),
    path('habilidad/editar/<int:habilidad_id>/', views.editar_habilidad, name='editar_habilidad'), # <--- NUEVA
    path('habilidad/eliminar/<int:habilidad_id>/', views.eliminar_habilidad, name='eliminar_habilidad'), # <--- NUEVA
    
    # Gestión de Vínculos y Perfil
    path('perfil/', views.mi_perfil, name='perfil'),
    path('completar/<int:intercambio_id>/', views.completar_intercambio, name='completar_intercambio'),
    path('agradecer/<int:intercambio_id>/', views.dejar_agradecimiento, name='dejar_agradecimiento'),
]