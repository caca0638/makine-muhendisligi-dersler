"""
Diferansiyel Denklemler - Tam Denklemler, İntegral Çarpanı ve Homojen Dönüşümler
Hesaplamalı Doğrulama ve Grafik Çizim Betiği
"""

import os
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def test_tam_ve_homojen():
    print("=" * 65)
    print("TAM DİFERANSİYEL DENKLEMLER VE HOMOJEN DÖNÜŞÜMLER ÇÖZÜM DOĞRULAMASI")
    print("=" * 65)
    
    x = sp.Symbol('x', real=True)
    y = sp.Function('y')(x)
    
    # PROBLEM 1: Tam Denklem: (2xy + 3) + (x^2 - 1)*y' = 0, y(2) = 1
    ode1 = sp.Eq((2*x*y + 3) + (x**2 - 1)*y.diff(x), 0)
    sol1 = sp.dsolve(ode1, y, ics={y.subs(x, 2): 1})
    print("\n1. Problem 1 (Tam Denklem, y(2)=1 Özel Çözümü):")
    sp.pprint(sol1)
    
    # PROBLEM 2: İntegrasyon Çarpanı: (3xy + y^2) + (x^2 + xy)*y' = 0
    ode2 = sp.Eq((3*x*y + y**2) + (x**2 + x*y)*y.diff(x), 0)
    sol2 = sp.dsolve(ode2, y)
    print("\n2. Problem 2 (İntegral Çarpanlı Denklem Genel Çözümü):")
    sp.pprint(sol2)
    
    # PROBLEM 3: Homojen Denklem: (x^2 + y^2) - 2xy*y' = 0
    ode3 = sp.Eq((x**2 + y**2) - 2*x*y*y.diff(x), 0)
    sol3 = sp.dsolve(ode3, y)
    print("\n3. Problem 3 (Homojen Denklem Genel Çözümü):")
    sp.pprint(sol3)
    
    # Grafik Çizimi: Problem 1 Çözümü y(x) = (9 - 3x) / (x^2 - 1)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Problem 1 Grafiği (x=1 ve x=-1 asimptotları)
    x1_left = np.linspace(-3, -1.05, 200)
    x1_mid = np.linspace(-0.95, 0.95, 200)
    x1_right = np.linspace(1.05, 4, 300)
    
    for x_part in [x1_left, x1_mid, x1_right]:
        y_part = (9.0 - 3.0*x_part) / (x_part**2 - 1.0)
        axes[0].plot(x_part, y_part, 'b-', linewidth=2)
        
    axes[0].plot(2.0, 1.0, 'ro', markersize=8, label=r'Başlangıç Şartı $(2, 1)$')
    axes[0].axvline(1.0, color='gray', linestyle='--', alpha=0.7, label=r'Tekil Noktalar ($x = \pm 1$)')
    axes[0].axvline(-1.0, color='gray', linestyle='--', alpha=0.7)
    axes[0].set_ylim(-15, 15)
    axes[0].set_xlabel('x', fontsize=11)
    axes[0].set_ylabel('y(x)', fontsize=11)
    axes[0].set_title(r'Problem 1: $y(x) = \frac{9 - 3x}{x^2 - 1}$ Çözüm Eğrisi', fontsize=12, fontweight='bold')
    axes[0].grid(True, linestyle=':', alpha=0.6)
    axes[0].legend(fontsize=9)
    
    # Problem 3 Grafiği: x^2 - y^2 = C*x Hiperboller Ailesi
    y_grid = np.linspace(-3, 3, 300)
    x_grid = np.linspace(-3, 3, 300)
    X, Y = np.meshgrid(x_grid, y_grid)
    
    C_values = [-3.0, -1.5, 0.0, 1.5, 3.0]
    for C in C_values:
        F = X**2 - Y**2 - C*X
        axes[1].contour(X, Y, F, levels=[0], linewidths=1.8, label=f'$C={C}$')
        
    axes[1].set_xlabel('x', fontsize=11)
    axes[1].set_ylabel('y', fontsize=11)
    axes[1].set_title(r'Problem 3: $x^2 - y^2 = Cx$ Homojen Denklem Yörüngeleri', fontsize=12, fontweight='bold')
    axes[1].grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '06_Tam_ve_Homojen_Grafikleri.png')
    plt.savefig(output_path, dpi=300)
    print(f"\nGrafikler kaydedildi: {output_path}")

if __name__ == '__main__':
    test_tam_ve_homojen()
