"""
Diferansiyel Denklemler - Bölüm 2: İkinci Mertebeden Doğrusal Diferansiyel Denklemler
Mekanik Titreşimler (1-DOF Sönümlü Harmonik Salınım) Analitik ve Sayısal Çözüm Betiği
"""

import os
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def symbolic_analysis():
    """
    Karakteristik denklem, Wronskian determinantı ve sembolik analitik çözüm.
    """
    print("=" * 65)
    print("İKİNCİ MERTEBEDEN LİNEER DENKLEM: SEMBOLİK FORMÜLASYON VE WRONSKIAN")
    print("=" * 65)
    
    t = sp.Symbol('t', positive=True)
    m, c, k = sp.symbols('m c k', positive=True)
    x = sp.Function('x')(t)
    
    # Diferansiyel denklem: m*x'' + c*x' + k*x = 0
    ode = sp.Eq(m * x.diff(t, 2) + c * x.diff(t) + k * x, 0)
    print("1. Standart Dinamik Denklem:")
    sp.pprint(ode)
    
    # Karakteristik denklem kökleri
    r = sp.Symbol('r')
    char_eq = sp.Eq(m * r**2 + c * r + k, 0)
    roots = sp.solve(char_eq, r)
    print("\n2. Karakteristik Denklem Kökleri (r1, r2):")
    sp.pprint(roots)
    
    # Wronskian Doğrusal Bağımsızlık Testi (Eksik sönüm durumu için: x1 = exp(-zeta*wn*t)*cos(wd*t), x2 = exp(-zeta*wn*t)*sin(wd*t))
    zeta, wn, wd = sp.symbols('zeta omega_n omega_d', positive=True)
    x1 = sp.exp(-zeta * wn * t) * sp.cos(wd * t)
    x2 = sp.exp(-zeta * wn * t) * sp.sin(wd * t)
    W = sp.simplify(x1 * x2.diff(t) - x2 * x1.diff(t))
    print("\n3. Eksik Sönümlü Temel Çözümler İçin Wronskian Determinantı W(x1, x2)(t):")
    sp.pprint(W)
    print(f"   Wronskian Sonucu: wd * exp(-2*zeta*wn*t) != 0  -> Çözümler lineer bağımsızdır.")

def engineering_vibration_simulation():
    """
    Fiziksel Parametrelerle 3 Farklı Titreşim Rejiminin Simülasyonu
    """
    print("\n" + "=" * 65)
    print("SERBEST TİTREŞİM ANALİZİ (EKSİK, KRİTİK VE AŞIRI SÖNÜM REJİMLERİ)")
    print("=" * 65)
    
    # Mühendislik Parametreleri (SI Birimleri)
    m = 10.0      # kg (kütle)
    k = 1000.0    # N/m (yay rijitliği)
    x0 = 0.05     # m (50 mm başlangıç yer değiştirmesi)
    v0 = 0.0      # m/s (durgun halden serbest bırakma)
    
    # Temel Frekans ve Kritik Sönüm
    omega_n = np.sqrt(k / m)  # rad/s
    c_crit = 2.0 * np.sqrt(k * m)  # N*s/m
    print(f"Doğal Açısal Frekans (omega_n): {omega_n:.4f} rad/s")
    print(f"Doğal Frekans (f_n): {omega_n / (2 * np.pi):.4f} Hz")
    print(f"Kritik Sönüm Katsayısı (c_crit): {c_crit:.4f} N*s/m")
    
    # 3 Rejim Parametreleri:
    cases = [
        {"name": "Eksik Sönüm (Underdamped)", "zeta": 0.15, "c": 0.15 * c_crit, "color": "blue"},
        {"name": "Kritik Sönüm (Critically Damped)", "zeta": 1.0, "c": 1.0 * c_crit, "color": "green"},
        {"name": "Aşırı Sönüm (Overdamped)", "zeta": 2.5, "c": 2.5 * c_crit, "color": "red"}
    ]
    
    t_span = (0.0, 3.0)  # 0 ile 3 saniye arası
    t_eval = np.linspace(0.0, 3.0, 600)
    
    results = []
    
    for case in cases:
        zeta = case["zeta"]
        c_val = case["c"]
        
        # Sayısal Çözüm (SciPy solve_ivp)
        # Durum değişkenleri: y = [x, x_dot]
        # dy/dt = [x_dot, -(c/m)*x_dot - (k/m)*x]
        def rhs(t_val, y_val):
            return [y_val[1], -(c_val / m) * y_val[1] - (k / m) * y_val[0]]
        
        sol = solve_ivp(rhs, t_span, [x0, v0], t_eval=t_eval, method='RK45', rtol=1e-8, atol=1e-10)
        
        # Analitik Kapalı Form Çözümü
        if zeta < 1.0:
            omega_d = omega_n * np.sqrt(1.0 - zeta**2)
            # x(t) = exp(-zeta*wn*t) * (C1*cos(wd*t) + C2*sin(wd*t))
            # x(0) = C1 = x0
            # x'(0) = -zeta*wn*C1 + wd*C2 = v0 -> C2 = (v0 + zeta*wn*x0) / wd
            C1 = x0
            C2 = (v0 + zeta * omega_n * x0) / omega_d
            x_analytic = np.exp(-zeta * omega_n * t_eval) * (C1 * np.cos(omega_d * t_eval) + C2 * np.sin(omega_d * t_eval))
            log_dec = (2 * np.pi * zeta) / np.sqrt(1 - zeta**2)
            print(f"\n[Case 1: Eksik Sönüm, zeta={zeta}]:")
            print(f"  Sönümlü Frekans (omega_d): {omega_d:.4f} rad/s")
            print(f"  Logaritmik Azalma (delta): {log_dec:.4f}")
        elif np.isclose(zeta, 1.0):
            # x(t) = (C1 + C2*t) * exp(-wn*t)
            # x(0) = C1 = x0
            # x'(0) = C2 - wn*C1 = v0 -> C2 = v0 + wn*x0
            C1 = x0
            C2 = v0 + omega_n * x0
            x_analytic = (C1 + C2 * t_eval) * np.exp(-omega_n * t_eval)
            print(f"\n[Case 2: Kritik Sönüm, zeta={zeta}]:")
            print(f"  Sistem salınımsız en hızlı sönüme ulaşıyor.")
        else:
            # zeta > 1.0
            r1 = -zeta * omega_n + omega_n * np.sqrt(zeta**2 - 1.0)
            r2 = -zeta * omega_n - omega_n * np.sqrt(zeta**2 - 1.0)
            # x(t) = C1*exp(r1*t) + C2*exp(r2*t)
            # x0 = C1 + C2
            # v0 = r1*C1 + r2*C2 -> C1 = (v0 - r2*x0)/(r1 - r2), C2 = x0 - C1
            C1 = (v0 - r2 * x0) / (r1 - r2)
            C2 = x0 - C1
            x_analytic = C1 * np.exp(r1 * t_eval) + C2 * np.exp(r2 * t_eval)
            print(f"\n[Case 3: Aşırı Sönüm, zeta={zeta}]:")
            print(f"  Karakteristik kökler: r1 = {r1:.4f} 1/s, r2 = {r2:.4f} 1/s")
        
        max_err = np.max(np.abs(sol.y[0] - x_analytic))
        print(f"  Sayısal ve Analitik Çözüm Arası Maks. Mutlak Hata: {max_err:.4e} m")
        
        results.append({
            "name": case["name"],
            "color": case["color"],
            "zeta": zeta,
            "t": t_eval,
            "x_num": sol.y[0],
            "v_num": sol.y[1],
            "x_ana": x_analytic
        })
        
    return results

def plot_vibration_results(results):
    """Grafikleri 2 panel halinde çizer: Zaman Yanıtı ve Faz Portresi (Phase Portrait)."""
    fig, axes = plt.subplots(1, 2, figsize=(15, 5.5))
    
    # 1. Panel: Yer değiştirme - Zaman x(t)
    for res in results:
        axes[0].plot(res["t"], res["x_ana"] * 1000.0, color=res["color"], linewidth=2, label=f'{res["name"]} ($\\zeta={res["zeta"]}$)')
        # Sayısal RK45 noktalarını seyrek sembollerle göster
        axes[0].plot(res["t"][::30], res["x_num"][::30] * 1000.0, 'o', color=res["color"], markersize=4, alpha=0.6)
        
    axes[0].axhline(0, color='black', linestyle='--', linewidth=0.8)
    axes[0].set_xlabel('Zaman $t$ (s)', fontsize=11)
    axes[0].set_ylabel('Yer Değiştirme $x(t)$ (mm)', fontsize=11)
    axes[0].set_title('1-DOF Kütle-Yay-Sönümleyici Serbest Titreşim Yanıtı', fontsize=12, fontweight='bold')
    axes[0].grid(True, linestyle=':', alpha=0.6)
    axes[0].legend(fontsize=9)
    
    # 2. Panel: Faz Portresi (Phase Portrait: x vs x_dot)
    for res in results:
        axes[1].plot(res["x_num"] * 1000.0, res["v_num"], color=res["color"], linewidth=2, label=f'{res["name"]}')
        # Başlangıç noktasını işaretle
        axes[1].plot(res["x_num"][0] * 1000.0, res["v_num"][0], 'ks', markersize=6)
        
    axes[1].plot(results[0]["x_num"][0] * 1000.0, results[0]["v_num"][0], 'ks', markersize=6, label='Başlangıç ($x_0=50$ mm, $v_0=0$)')
    axes[1].axhline(0, color='black', linestyle='--', linewidth=0.8)
    axes[1].axvline(0, color='black', linestyle='--', linewidth=0.8)
    axes[1].set_xlabel('Yer Değiştirme $x$ (mm)', fontsize=11)
    axes[1].set_ylabel('Hız $\\dot{x}$ (m/s)', fontsize=11)
    axes[1].set_title('Faz Düzlemi Yörüngeleri (Phase Plane Trajectories)', fontsize=12, fontweight='bold')
    axes[1].grid(True, linestyle=':', alpha=0.6)
    axes[1].legend(fontsize=9)
    
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '03_Titresim_Rejimleri_Grafikleri.png')
    plt.savefig(output_path, dpi=300)
    print(f"\nGrafik dosyası başarıyla oluşturuldu: {output_path}")

if __name__ == '__main__':
    symbolic_analysis()
    res = engineering_vibration_simulation()
    plot_vibration_results(res)
