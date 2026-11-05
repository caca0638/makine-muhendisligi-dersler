"""
Diferansiyel Denklemler - Bölüm 1: 1. Mertebeden Diferansiyel Denklemler
Makine Mühendisliği Analitik ve Sayısal Çözüm Betiği
"""

import os
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def problem_1_newton_cooling():
    """
    Problem 1: Isıl İşlem Gören Bir Makine Parçasının Soğuma Süreci (Newton Soğuma Yasası)
    Formülasyon: dT/dt + k*T = k*T_inf,  T(0) = T_0
    """
    print("=" * 60)
    print("PROBLEM 1: NEWTON SOĞUMA YASASI (ISIL İŞLEM ANALİZİ)")
    print("=" * 60)
    
    # Sembolik Tanımlar (SymPy)
    t = sp.Symbol('t', positive=True)
    k = sp.Symbol('k', positive=True)
    T_inf = sp.Symbol('T_inf', real=True)
    T = sp.Function('T')(t)
    
    # Diferansiyel denklem
    ode = sp.Eq(T.diff(t) + k * (T - T_inf), 0)
    print("1. Diferansiyel Denklem:")
    sp.pprint(ode)
    
    # Genel Çözüm
    gen_sol = sp.dsolve(ode, T)
    print("\n2. Sembolik Genel Çözüm:")
    sp.pprint(gen_sol)
    
    # Başlangıç Değer Problemi: T(0) = T_0
    T_0 = sp.Symbol('T_0', real=True)
    particular_sol = sp.dsolve(ode, T, ics={T.subs(t, 0): T_0})
    print("\n3. Başlangıç Şartı T(0)=T_0 ile Özel Çözüm:")
    sp.pprint(particular_sol)
    
    # Sayısal Değerler (Mühendislik Parametreleri)
    # T_0 = 850 °C (Östenitleme sıcaklığı)
    # T_inf = 25 °C (Ortam havası / soğuma banyosu)
    # k = 0.035 s^-1 (h*A / (rho*V*c_p))
    T0_num = 850.0  # °C
    Tinf_num = 25.0  # °C
    k_num = 0.035    # 1/s
    
    # Sayısal Çözüm (SciPy solve_ivp)
    def ode_fun(t_eval, T_val):
        return -k_num * (T_val - Tinf_num)
    
    t_span = (0.0, 150.0) # 0 ile 150 saniye arası
    t_eval = np.linspace(0.0, 150.0, 300)
    sol_num = solve_ivp(ode_fun, t_span, [T0_num], t_eval=t_eval, method='RK45')
    
    # Analitik Değerler
    analytical_fun = sp.lambdify(t, particular_sol.rhs.subs({T_0: T0_num, T_inf: Tinf_num, k: k_num}), 'numpy')
    T_analytic = analytical_fun(t_eval)
    
    # Maksimum mutlak ve bağıl hata
    max_err = np.max(np.abs(sol_num.y[0] - T_analytic))
    print(f"\n4. Sayısal ve Analitik Çözüm Karşılaştırması:")
    print(f"   Maksimum Mutlak Hata |T_sayisal - T_analitik|: {max_err:.4e} °C")
    
    # Fiziksel Yorum İçin Örnek Noktalar
    # Zaman sabiti tau = 1/k
    tau = 1.0 / k_num
    T_at_tau = analytical_fun(tau)
    print(f"   Isıl Zaman Sabiti (tau = 1/k): {tau:.2f} s")
    print(f"   t = tau anındaki sıcaklık: {T_at_tau:.2f} °C")
    print(f"   Beklenen teorik düşüş: %63.2 soğuma -> {Tinf_num + (T0_num - Tinf_num)*np.exp(-1):.2f} °C")
    
    return t_eval, T_analytic, sol_num.y[0]

def problem_2_viscous_fall():
    """
    Problem 2: Viskoz Akışkanda Karesel Direnç ile Serbest Düşüş (Bernoulli / Ayrılabilir ODE)
    Formülasyon: m * dv/dt = m*g - k_d * v^2,  v(0) = 0
    """
    print("\n" + "=" * 60)
    print("PROBLEM 2: AKIŞKAN İÇİNDE DÜŞÜŞ VE LİMİT HIZ (BERNOULLI / LINEER OLMAYAN)")
    print("=" * 60)
    
    # Parametreler (SI Birimleri)
    m = 2.5      # kg (kütle)
    g = 9.81     # m/s^2 (yerçekimi ivmesi)
    k_d = 0.05   # kg/m (aerodinamik / hidrodinamik direnç katsayısı)
    
    # Limit Hız (dv/dt = 0)
    v_term = np.sqrt((m * g) / k_d)
    print(f"1. Analitik Limit Hız Hesabı (dv/dt = 0):")
    print(f"   v_terminal = sqrt(m*g / k_d) = sqrt({m} * {g} / {k_d}) = {v_term:.4f} m/s")
    
    # Sembolik Analitik Çözüm (Değişkenlerine Ayrılabilir İntegrasyon)
    t = sp.Symbol('t', positive=True)
    v_sym = sp.Symbol('v', positive=True)
    v_d = sp.Symbol('v_d', positive=True)
    m_s, g_s, kd_s = sp.symbols('m g k_d', positive=True)
    
    # Değişkenlerine ayırarak integral alma: int(1/(g - (kd/m)*v^2) dv) = int(dt)
    lhs_int = sp.integrate(1 / (g_s - (kd_s / m_s) * v_d**2), (v_d, 0, v_sym))
    rhs_int = t
    
    # Kapalı form çözümü
    v_closed = sp.solve(sp.Eq(lhs_int, rhs_int), v_sym)[0]
    print("\n2. Değişkenlerine Ayırma ile Elde Edilen Analitik Çözüm v(t):")
    sp.pprint(sp.Eq(sp.Function('v')(t), v_closed))
    
    # Sayısal Entegrasyon
    def fall_ode(t_val, y_val):
        return [g - (k_d / m) * (y_val[0]**2)]
    
    t_eval = np.linspace(0.0, 15.0, 300)
    sol_fall = solve_ivp(fall_ode, (0.0, 15.0), [0.0], t_eval=t_eval, method='RK45')
    
    v_analytic = v_term * np.tanh((np.sqrt(m * g * k_d) / m) * t_eval)
    max_err = np.max(np.abs(sol_fall.y[0] - v_analytic))
    print(f"\n3. Sayısal / Analitik Karşılaştırma:")
    print(f"   Maksimum Mutlak Hata: {max_err:.4e} m/s")
    print(f"   t = 15 s anındaki hız: {sol_fall.y[0][-1]:.4f} m/s (Limit hıza oranı: %{sol_fall.y[0][-1]/v_term*100:.2f})")
    
    return t_eval, v_analytic, sol_fall.y[0], v_term

def plot_and_save_results(p1_data, p2_data):
    """Grafikleri çizer ve akademik formata uygun olarak kaydeder."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Grafik 1: Newton Soğuma
    t1, T_ana, T_num = p1_data
    axes[0].plot(t1, T_ana, 'b-', linewidth=2, label='Analitik Çözüm (Kapalı Form)')
    axes[0].plot(t1[::15], T_num[::15], 'ro', markersize=4, label='Sayısal Çözüm (RK45)')
    axes[0].axhline(25.0, color='gray', linestyle='--', label=r'Ortam Sıcaklığı ($T_{\infty} = 25^\circ\mathrm{C}$)')
    axes[0].set_xlabel('Zaman $t$ (s)', fontsize=11)
    axes[0].set_ylabel(r'Sıcaklık $T$ ($^\circ\mathrm{C}$)', fontsize=11)
    axes[0].set_title('Problem 1: Newton Soğuma Eğrisi', fontsize=12, fontweight='bold')
    axes[0].grid(True, linestyle=':', alpha=0.6)
    axes[0].legend(fontsize=9)
    
    # Grafik 2: Karesel Dirençli Düşüş
    t2, v_ana, v_num, v_lim = p2_data
    axes[1].plot(t2, v_ana, 'g-', linewidth=2, label='Analitik Hız ($v(t) = v_{term} \tanh(\\dots)$)')
    axes[1].plot(t2[::15], v_num[::15], 'mo', markersize=4, label='Sayısal Çözüm (RK45)')
    axes[1].axhline(v_lim, color='red', linestyle='--', label=f'Limit Hız ($v_{{term}} = {v_lim:.2f}$ m/s)')
    axes[1].set_xlabel('Zaman $t$ (s)', fontsize=11)
    axes[1].set_ylabel('Hız $v$ (m/s)', fontsize=11)
    axes[1].set_title('Problem 2: Akışkanda Serbest Düşüş ve Limit Hız', fontsize=12, fontweight='bold')
    axes[1].grid(True, linestyle=':', alpha=0.6)
    axes[1].legend(fontsize=9)
    
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '03_Cozum_Grafikleri.png')
    plt.savefig(output_path, dpi=300)
    print(f"\nGrafikler yüksek çözünürlükle kaydedildi: {output_path}")

if __name__ == '__main__':
    p1 = problem_1_newton_cooling()
    p2 = problem_2_viscous_fall()
    plot_and_save_results(p1, p2)
