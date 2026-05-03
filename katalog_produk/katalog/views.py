from django.shortcuts import render

# ─────────────────────────────────────────────────────
# SVG ICONS (inline, untuk thumbnail produk)
# ─────────────────────────────────────────────────────

SVG_LAPTOP = '''<svg width="60" height="60" fill="none" stroke="#334155" stroke-width="1.5"
     stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
  <rect x="2" y="3" width="20" height="14" rx="2"/>
  <path d="M1 20h22"/>
</svg>'''

SVG_PHONE = '''<svg width="60" height="60" fill="none" stroke="#334155" stroke-width="1.5"
     stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
  <rect x="5" y="2" width="14" height="20" rx="2" ry="2"/>
  <line x1="12" y1="18" x2="12.01" y2="18"/>
</svg>'''

SVG_BAG = '''<svg width="60" height="60" fill="none" stroke="#334155" stroke-width="1.5"
     stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
  <path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/>
  <line x1="3" y1="6" x2="21" y2="6"/>
  <path d="M16 10a4 4 0 01-8 0"/>
</svg>'''

SVG_HEADPHONE = '''<svg width="60" height="60" fill="none" stroke="#334155" stroke-width="1.5"
     stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
  <path d="M3 18v-6a9 9 0 0118 0v6"/>
  <path d="M21 19a2 2 0 01-2 2h-1a2 2 0 01-2-2v-3a2 2 0 012-2h3zM3 19a2 2 0 002 2h1a2 2 0 002-2v-3a2 2 0 00-2-2H3z"/>
</svg>'''

SVG_DESK = '''<svg width="60" height="60" fill="none" stroke="#334155" stroke-width="1.5"
     stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
  <rect x="2" y="7" width="20" height="3" rx="1"/>
  <line x1="7" y1="10" x2="7" y2="20"/>
  <line x1="17" y1="10" x2="17" y2="20"/>
  <line x1="5" y1="20" x2="9" y2="20"/>
  <line x1="15" y1="20" x2="19" y2="20"/>
</svg>'''

# ─────────────────────────────────────────────────────
# DATA PRODUK (hardcoded, tanpa database)
# ─────────────────────────────────────────────────────
DAFTAR_PRODUK = [
    {
        'id': 1,
        'nama': 'Laptop ASUS VivoBook 15',
        'kategori': 'Elektronik',
        'harga': 7500000,
        'stok': 12,
        'deskripsi': (
            'Laptop tipis dan ringan dengan prosesor Intel Core i5 generasi ke-12. '
            'Dilengkapi RAM 8GB dan SSD 512GB yang cepat. Layar 15.6 inci Full HD '
            'memberikan visual yang jernih dan nyaman di mata. Baterai tahan hingga '
            '8 jam pemakaian normal. Cocok untuk pelajar, mahasiswa, maupun pekerja kantoran.'
        ),
        'spesifikasi': {
            'Prosesor': 'Intel Core i5-1235U',
            'RAM': '8 GB DDR4',
            'Storage': '512 GB SSD',
            'Layar': '15.6 inci Full HD (1920x1080)',
            'Sistem Operasi': 'Windows 11 Home',
            'Baterai': '42 Wh, tahan hingga 8 jam',
        },
        'warna_badge': '#2563eb',
        'thumb_bg': '#e8f0fe',
        'thumb_svg': SVG_LAPTOP,
    },
    {
        'id': 2,
        'nama': 'Smartphone Samsung Galaxy A54',
        'kategori': 'Elektronik',
        'harga': 4200000,
        'stok': 25,
        'deskripsi': (
            'Smartphone Android dengan kamera utama 50MP yang memukau. '
            'Layar Super AMOLED 6.4 inci dengan refresh rate 120Hz memberikan '
            'pengalaman scrolling yang sangat mulus. Baterai 5000 mAh dengan fast '
            'charging 25W. Tersedia dalam pilihan warna Awesome Graphite dan Awesome Lime.'
        ),
        'spesifikasi': {
            'Prosesor': 'Exynos 1380 Octa-core',
            'RAM': '8 GB',
            'Storage': '256 GB',
            'Layar': '6.4 inci Super AMOLED 120Hz',
            'Kamera': '50MP + 12MP + 5MP',
            'Baterai': '5000 mAh, Fast Charge 25W',
        },
        'warna_badge': '#0891b2',
        'thumb_bg': '#e0f7fa',
        'thumb_svg': SVG_PHONE,
    },
    {
        'id': 3,
        'nama': 'Tas Ransel Laptop Eiger Elpine',
        'kategori': 'Tas & Aksesoris',
        'harga': 580000,
        'stok': 8,
        'deskripsi': (
            'Tas ransel premium dari Eiger dengan material canvas berkualitas tinggi '
            'dan tahan air. Kompartemen laptop khusus dengan pelindung empuk mendukung '
            'laptop hingga 15.6 inci. Desain ergonomis dengan tali bahu yang nyaman '
            'untuk pemakaian seharian. Kapasitas 25 liter ideal untuk kegiatan '
            'outdoor maupun perjalanan sehari-hari.'
        ),
        'spesifikasi': {
            'Material': 'Canvas premium + Cordura',
            'Kapasitas': '25 Liter',
            'Kompartemen Laptop': 'Maks. 15.6 inci',
            'Tahan Air': 'Ya (water resistant)',
            'Dimensi': '30 x 20 x 45 cm',
            'Berat': '0.85 kg',
        },
        'warna_badge': '#d97706',
        'thumb_bg': '#fef3c7',
        'thumb_svg': SVG_BAG,
    },
    {
        'id': 4,
        'nama': 'Headphone Sony WH-1000XM5',
        'kategori': 'Audio',
        'harga': 4800000,
        'stok': 5,
        'deskripsi': (
            'Headphone over-ear premium dengan teknologi Active Noise Cancelling (ANC) '
            'terdepan di kelasnya. Kualitas suara Hi-Res Audio dengan driver 30mm menghasilkan '
            'bass yang dalam dan treble jernih. Koneksi Bluetooth 5.2 dengan jangkauan '
            'hingga 10 meter. Daya tahan baterai mencapai 30 jam pemakaian.'
        ),
        'spesifikasi': {
            'Tipe': 'Over-ear, Closed-back',
            'Driver': '30 mm',
            'Bluetooth': 'Versi 5.2',
            'Active Noise Cancelling': 'Ya',
            'Baterai': '30 jam (ANC aktif)',
            'Berat': '250 gram',
        },
        'warna_badge': '#7c3aed',
        'thumb_bg': '#ede9fe',
        'thumb_svg': SVG_HEADPHONE,
    },
    {
        'id': 5,
        'nama': 'Meja Belajar Minimalis IKEA MICKE',
        'kategori': 'Furnitur',
        'harga': 1250000,
        'stok': 3,
        'deskripsi': (
            'Meja belajar minimalis dari IKEA dengan desain Scandinavian yang elegan. '
            'Dilengkapi laci penyimpanan dan rak kecil di sisi kanan. Permukaan meja '
            'luas 105 x 50 cm cukup menampung laptop, buku, dan perlengkapan belajar. '
            'Material particle board berkualitas dengan finishing melamin anti-gores.'
        ),
        'spesifikasi': {
            'Dimensi': '105 x 50 x 75 cm',
            'Material': 'Particle board, ABS plastik',
            'Finishing': 'Melamin anti-gores',
            'Laci': '1 laci besar',
            'Pilihan Warna': 'Putih / Hitam',
            'Maks. Beban': '50 kg',
        },
        'warna_badge': '#dc2626',
        'thumb_bg': '#fee2e2',
        'thumb_svg': SVG_DESK,
    },
]


# ─────────────────────────────────────────────────────
# HELPER
# ─────────────────────────────────────────────────────
def format_harga(harga):
    """Konversi angka menjadi format Rupiah."""
    return 'Rp {:,.0f}'.format(harga).replace(',', '.')


# ─────────────────────────────────────────────────────
# VIEWS
# ─────────────────────────────────────────────────────

def homepage(request):
    """Halaman utama: /"""
    context = {
        'judul_halaman': 'Beranda',
        'total_produk': len(DAFTAR_PRODUK),
    }
    return render(request, 'katalog/homepage.html', context)


def daftar_produk(request):
    """Halaman daftar produk: /produk/"""
    produk_list = []
    for p in DAFTAR_PRODUK:
        item = p.copy()
        item['harga_format'] = format_harga(p['harga'])
        produk_list.append(item)

    context = {
        'judul_halaman': 'Katalog Produk',
        'produk_list': produk_list,
    }
    return render(request, 'katalog/daftar_produk.html', context)


def detail_produk(request, id):
    """Halaman detail produk: /produk/<id>/"""
    produk = None
    for p in DAFTAR_PRODUK:
        if p['id'] == id:
            produk = p.copy()
            produk['harga_format'] = format_harga(p['harga'])
            break

    if produk is None:
        return render(request, 'katalog/produk_tidak_ditemukan.html', {
            'judul_halaman': 'Produk Tidak Ditemukan',
            'id': id,
        })

    context = {
        'judul_halaman': produk['nama'],
        'produk': produk,
    }
    return render(request, 'katalog/detail_produk.html', context)


def kontak(request):
    """Halaman kontak: /kontak/"""
    context = {
        'judul_halaman': 'Hubungi Kami',
    }
    return render(request, 'katalog/kontak.html', context)
