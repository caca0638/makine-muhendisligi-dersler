"""
Diferansiyel Denklemler - Vize ve Final Soru Çözümleri (Bölüm 1)
Makine Mühendisliği Öğrencisi İçin Adım Adım Açıklamalı Python Betiği
"""

import os
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def soru_1_siniflandirma():
    """
    SORU 1: Mertebe, Derece ve Lineerlik Analizi
    """
    print("=" * 65)
    print("SORU 1: MERTEBE, DERECE VE LİNEERLİK ANALİZİ")
    print("=" * 65)
    
    x = sp.Symbol('x')
    y = sp.Function('y')(x)
    
    # (a) x^2 * y''' + (y')^4 - y = sin(x)
    ode_a = sp.Eq(x**2 * y.diff(x, 3) + (y.diff(x, 1))**4 - y, sp.sin(x))
    print("Denklem (a):")
    sp.pprint(ode_a)
    order_a = sp.ode_order(ode_a.lhs - ode_a.rhs, y)
    print(f"-> Mertebe (Order): {order_a}")
    print("-> Derece (Degree): 1")
    print("-> Lineerlik: (y')^4 terimi nedeniyle NON-LİNEER (Doğrusal Değil)\n")
    
    # (b) (y'')^2 - (y')^2 - 1 = 0
    ode_b = sp.Eq((y.diff(x, 2))**2 - (y.diff(x, 1))**2 - 1, 0)
    print("Denklem (b): (Köklü ifadeden kurtarılmış polinom hali)")
    sp.pprint(ode_b)
    order_b = sp.ode_order(ode_b.lhs, y)
    print(f"-> Mertebe (Order): {order_b}")
    print("-> Derece (Degree): 2  (En yüksek mertebeli türev olan y'' nin üssü 2)")
    print("-> Lineerlik: (y'')^2 ve (y')^2 terimleri nedeniyle NON-LİNEER\n")
    
    # (c) y'' + 4x*y' + cos(y) = 0
    ode_c = sp.Eq(y.diff(x, 2) + 4*x*y.diff(x) + sp.cos(y), 0)
    print("Denklem (c):")
    sp.pprint(ode_c)
    order_c = sp.ode_order(ode_c.lhs, y)
    print(f"-> Mertebe (Order): {order_c}")
    print("-> Derece (Degree): 1")
    print("-> Lineerlik: cos(y) terimi nedeniyle NON-LİNEER (y transandant fonksiyonda)\n")

def soru_2_ayrilabilir_ivp():
    """
    SORU 2: Değişkenlerine Ayrılabilir Denklem ve Başlangıç Değer Problemi
    dy/dx = [x*(y^2 + 1)] / [y*(x^2 + 1)], y(0) = 1
    """
    print("=" * 65)
    print("SORU 2: DEĞİŞKENLERİNE AYRILABİLİR DENKLEM (IVP: y(0) = 1)")
    print("=" * 65)
    
    x = sp.Symbol('x', real=True)
    y = sp.Function('y')(x)
    
    # Diferansiyel denklemi tanımlıyoruz:
    ode = sp.Eq(y.diff(x), (x * (y**2 + 1)) / (y * (x**2 + 1)))
    print("Diferansiyel Denklem:")
    sp.pprint(ode)
    
    # Genel Çözüm (C1 sabiti içeren form):
    gen_sol = sp.dsolve(ode, y)
    print("\nAdım 1 - Sembolik Genel Çözüm (SymPy):")
    sp.pprint(gen_sol)
    
    # Başlangıç Şartı ile Özel Çözüm: y(0) = 1
    part_sol = sp.dsolve(ode, y, ics={y.subs(x, 0): 1})
    print("\nAdım 2 - Başlangıç Şartı y(0)=1 Yerine Konmuş Özel Çözüm:")
    sp.pprint(part_sol)
    print("Analitik Kapalı Şekil: y(x) = sqrt(2*x^2 + 1)")
    
    return part_sol

def soru_3_lineer_ve_integral_carpani():
    """
    SORU 3: 1. Mertebe Lineer Denklem ve İntegral Çarpanı Metodu
    x*y' + 2y = 4*x^2
    """
    print("\n" + "=" * 65)
    print("SORU 3: İNTEGRAL ÇARPANI İLE LİNEER DENKLEM ÇÖZÜMÜ")
    print("=" * 65)
    
    x = sp.Symbol('x', positive=True)
    y = sp.Function('y')(x)
    
    # Denklem
    ode = sp.Eq(x * y.diff(x) + 2*y, 4 * x**2)
    print("Diferansiyel Denklem:")
    sp.pprint(ode)
    
    # Standart form: y' + (2/x)*y = 4*x
    P = 2 / x
    mu = sp.exp(sp.integrate(P, x))
    print(f"\nİntegral Çarpanı mu(x) = exp(integral(2/x dx)) = {mu}")
    
    # Genel Çözüm
    sol = sp.dsolve(ode, y)
    print("\nGenel Çözüm:")
    sp.pprint(sol)
    print("Analitik Açılım: y(x) = x^2 + C1 / x^2")
    
    return sol

def soru_4_bernoulli():
    """
    SORU 4: Bernoulli Diferansiyel Denklemi
    y' + (1/x)*y = x * y^2
    """
    print("\n" + "=" * 65)
    print("SORU 4: BERNOULLI DİFERANSİYEL DENKLEMİ")
    print("=" * 65)
    
    x = sp.Symbol('x', positive=True)
    y = sp.Function('y')(x)
    
    # Denklem: y' + (1/x)*y = x * y^2  (n = 2)
    ode = sp.Eq(y.diff(x) + (1/x)*y, x * y**2)
    print("Bernoulli Denklemi (n=2):")
    sp.pprint(ode)
    print("\nDönüşüm Kuralı: u = y^(1-n) = y^(1-2) = y^(-1) = 1/y")
    print("Lineerleşmiş Yeni Denklem: u' - (1/x)*u = -x")
    
    # SymPy doğrudan Bernoulli tanır ve çözer
    sol_bern = sp.dsolve(ode, y)
    print("\nGenel Çözüm:")
    sp.pprint(sol_bern)
    print("Analitik Açılım: y(x) = -1 / (x^2 + C1*x)")
    
    return sol_bern

def cizim_ve_gorsellestirme():
    """Mühendislik eğrilerini çizer ve kaydeder."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Grafik 1: Soru 2 Çözüm Ailesi y(x) = sqrt(C*(x^2+1) - 1)
    x_vals = np.linspace(-3, 3, 400)
    C_values = [1.5, 2.0, 3.0, 4.0]
    for C in C_values:
        # y = sqrt(C*(x^2 + 1) - 1)
        arg = C * (x_vals**2 + 1) - 1
        y_vals = np.sqrt(np.maximum(0, arg))
        lbl = f'$C={C}$ (Özel: $y(0)=1$)' if C == 2.0 else f'$C={C}$'
        lw = 2.5 if C == 2.0 else 1.2
        axes[0].plot(x_vals, y_vals, label=lbl, linewidth=lw)
        
    axes[0].plot(0, 1, 'ro', markersize=7, label='Başlangıç Noktası $(0, 1)$')
    axes[0].set_xlabel('Konum / Bağımsız Değişken $x$', fontsize=11)
    axes[0].set_ylabel('Yanıt $y(x)$', fontsize=11)
    axes[0].set_title('Soru 2: $y(x) = \\sqrt{C(x^2+1)-1}$ Çözüm Eğrileri', fontsize=12, fontweight='bold')
    axes[0].grid(True, linestyle=':', alpha=0.6)
    axes[0].legend(fontsize=9)
    
    # Grafik 2: Soru 3 Lineer Denklem Çözümleri y(x) = x^2 + C/x^2
    x_pos = np.linspace(0.4, 3.0, 300)
    C_linear = [-2.0, 0.0, 2.0, 5.0]
    for C in C_linear:
        y_lin = x_pos**2 + C / (x_pos**2)
        axes[1].plot(x_pos, y_lin, label=f'$C={C}$', linewidth=1.5)
        
    axes[1].plot(x_pos, x_pos**2, 'k--', label='Özel Zorlanmış Yanıt ($x^2$)', linewidth=1.8)
    axes[1].set_xlabel('Bağımsız Değişken $x$', fontsize=11)
    axes[1].set_ylabel('$y(x)$', fontsize=11)
    axes[1].set_ylim(-5, 15)
    axes[1].set_title('Soru 3: $y(x) = x^2 + C/x^2$ Lineer Sistem Tepkisi', fontsize=12, fontweight='bold')
    axes[1].grid(True, linestyle=':', alpha=0.6)
    axes[1].legend(fontsize=9)
    
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '03_Vize_Sorulari_Grafikleri.png')
    plt.savefig(output_path, dpi=300)
    print(f"\nGrafikler başarıyla kaydedildi: {output_path}")

if __name__ == '__main__':
    soru_1_siniflandirma()
    soru_2_ayrilabilir_ivp()
    soru_3_lineer_ve_integral_carpani()
    soru_4_bernoulli()
    cizim_ve_gorsellestirme()
