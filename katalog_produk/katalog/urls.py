from django.urls import path
from katalog import views

# Nama aplikasi untuk namespace URL
app_name = 'katalog'

urlpatterns = [
    # Halaman Utama: /
    path('', views.homepage, name='homepage'),

    # Halaman Daftar Produk: /produk/
    path('produk/', views.daftar_produk, name='daftar_produk'),

    # Halaman Detail Produk: /produk/<id>/
    path('produk/<int:id>/', views.detail_produk, name='detail_produk'),

    # Halaman Kontak: /kontak/
    path('kontak/', views.kontak, name='kontak'),
]
