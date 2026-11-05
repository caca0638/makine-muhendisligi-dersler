"""
Makine Muhendisligi Lisans Mufredati - Uretim Yontemleri (Manufacturing Processes)
Modul 01: Metal Dokumunun Esaslari ve Dokum Mekanigi Hesaplamalari
Referans: Mikell P. Groover, 'Fundamentals of Modern Manufacturing'
          Prof. Dr. Murat Vural, Dokum Ders Notlari ve Dokum Odevi
"""

import math

def calculate_heating_energy(V_cm3, rho_g_cm3, Cs_J_gC, Cl_J_gC, Hf_J_g, Tm_C, Tp_C, T0_C=25.0, extra_pct=5.0):
    """
    Dokum icin gereken toplam isi enerjisi (H) hesabi:
    H = m * [ Cs*(Tm - T0) + Hf + Cl*(Tp - Tm) ]
    """
    V_total_cm3 = V_cm3 * (1.0 + extra_pct / 100.0)
    mass_g = V_total_cm3 * rho_g_cm3
    
    Q_solid = Cs_J_gC * (Tm_C - T0_C)
    Q_fusion = Hf_J_g
    Q_liquid = Cl_J_gC * (Tp_C - Tm_C)
    
    total_energy_J = mass_g * (Q_solid + Q_fusion + Q_liquid)
    return {
        'total_volume_cm3': V_total_cm3,
        'mass_kg': mass_g / 1000.0,
        'energy_MJ': total_energy_J / 1e6,
        'energy_J': total_energy_J
    }

def calculate_sprue_mechanics(h_sprue_m, A_sprue_bottom_m2, V_mold_total_m3):
    """
    Bernoulli ve Sureklilik Denklemi ile dusey yolluk cikis hizi, debi ve dolum suresi.
    v = sqrt(2 * g * h)
    Q = v * A
    T_fill = V_mold / Q
    """
    g = 9.81  # m/s^2
    v_theoretical = math.sqrt(2.0 * g * h_sprue_m)
    Q_theoretical_m3_s = v_theoretical * A_sprue_bottom_m2
    t_fill_theoretical_s = V_mold_total_m3 / Q_theoretical_m3_s
    return {
        'v_theoretical_m_s': v_theoretical,
        'Q_theoretical_L_s': Q_theoretical_m3_s * 1000.0,
        't_fill_theoretical_s': t_fill_theoretical_s
    }

def chvorinov_solidification_time(volume_m3, area_m2, Cm_s_per_m2=2.0e6, n=2.0):
    """
    Chvorinov Katilasma Kurali:
    T_ts = Cm * (V / A)^n
    """
    modulus = volume_m3 / area_m2  # V/A (Karakteristik modul)
    t_ts = Cm_s_per_m2 * (modulus ** n)
    return {
        'modulus_m': modulus,
        'solidification_time_s': t_ts
    }

def core_buoyancy_and_caplets(V_core_m3, rho_metal_kg_m3, rho_core_kg_m3, F_caplet_capacity_N=45.0):
    """
    Maca kaldirma kuvveti (Archimedes) ve alt/ust caplet (destek) sayisi hesabi.
    W_core = rho_core * g * V_core (Asagi dogru agirlik)
    F_buoyancy = rho_metal * g * V_core (Yukari dogru kaldirma)
    F_net_up = (rho_metal - rho_core) * g * V_core (Dokum sirasinda net yukari kuvvet)
    """
    g = 9.81  # m/s^2
    W_core = rho_core_kg_m3 * g * V_core_m3
    F_buoyancy = rho_metal_kg_m3 * g * V_core_m3
    F_net_up = F_buoyancy - W_core
    
    n_lower = math.ceil(W_core / F_caplet_capacity_N)
    n_upper = math.ceil(F_net_up / F_caplet_capacity_N)
    
    return {
        'W_core_N': W_core,
        'F_buoyancy_N': F_buoyancy,
        'F_net_up_N': F_net_up,
        'n_lower_caplets': n_lower,
        'n_upper_caplets': n_upper
    }

def run_acceptance_tests():
    print("=== TEST 1: Groover Dokum Odevi Soru 1 (Aluminyum Isi Enerjisi) ===")
    V_disk_cm3 = math.pi * (20.0**2) * 5.0
    res1 = calculate_heating_energy(
        V_cm3=V_disk_cm3,
        rho_g_cm3=2.70,
        Cs_J_gC=0.90,
        Cl_J_gC=1.08,
        Hf_J_g=389.3,
        Tm_C=660.0,
        Tp_C=800.0,
        T0_C=25.0,
        extra_pct=5.0
    )
    print(f"Mass of poured Al: {res1['mass_kg']:.2f} kg")
    print(f"Total Heating Energy: {res1['energy_MJ']:.2f} MJ")
    assert abs(res1['mass_kg'] - 17.81) < 0.1
    print("TEST 1 PASSED: Aluminum heating calculation verified.")

    print("=== TEST 2: Yolluk Akis Mekanigi (Bernoulli & Continuity) ===")
    res2 = calculate_sprue_mechanics(h_sprue_m=0.20, A_sprue_bottom_m2=3.75e-4, V_mold_total_m3=1.405e-3)
    print(f"Theoretical velocity at sprue base: {res2['v_theoretical_m_s']:.3f} m/s")
    print(f"Theoretical Flow rate: {res2['Q_theoretical_L_s']:.3f} L/s")
    print(f"Theoretical fill time: {res2['t_fill_theoretical_s']:.3f} s")
    assert abs(res2['v_theoretical_m_s'] - 1.981) < 0.01
    print("TEST 2 PASSED: Sprue velocity and flow rate verified.")

    print("=== TEST 3: Chvorinov Kurali - Geometri Karsilastirmasi ===")
    D = 0.10
    V_sphere = (4.0/3.0) * math.pi * ((D/2.0)**3)
    A_sphere = 4.0 * math.pi * ((D/2.0)**2)
    
    V_cyl = math.pi * ((D/2.0)**2) * D
    A_cyl = 2.0 * math.pi * ((D/2.0)**2) + math.pi * D * D
    
    V_cube = D**3
    A_cube = 6.0 * (D**2)
    
    t_sphere = chvorinov_solidification_time(V_sphere, A_sphere)
    t_cyl = chvorinov_solidification_time(V_cyl, A_cyl)
    t_cube = chvorinov_solidification_time(V_cube, A_cube)
    
    print(f"Sphere modulus (V/A): {t_sphere['modulus_m']*100:.3f} cm, Time: {t_sphere['solidification_time_s']:.2f} s")
    print(f"Cylinder modulus (V/A): {t_cyl['modulus_m']*100:.3f} cm, Time: {t_cyl['solidification_time_s']:.2f} s")
    print(f"Cube modulus (V/A): {t_cube['modulus_m']*100:.3f} cm, Time: {t_cube['solidification_time_s']:.2f} s")
    assert abs(t_sphere['modulus_m'] - t_cube['modulus_m']) < 1e-5
    print("TEST 3 PASSED: Chvorinov geometry moduli verified identically equal.")

    print("=== TEST 4: Groover Dokum Odevi Soru 25 (Maca Kaldirma & Caplet) ===")
    res4 = core_buoyancy_and_caplets(
        V_core_m3=5.075e-3,
        rho_metal_kg_m3=8620.0,
        rho_core_kg_m3=1600.0,
        F_caplet_capacity_N=45.0
    )
    print(f"Core weight W_c: {res4['W_core_N']:.2f} N => Lower caplets: {res4['n_lower_caplets']}")
    print(f"Net upward force F_net: {res4['F_net_up_N']:.2f} N => Upper caplets: {res4['n_upper_caplets']}")
    assert res4['n_lower_caplets'] == 2
    assert res4['n_upper_caplets'] == 8
    print("TEST 4 PASSED: Caplet requirements verified (2 bottom, 8 top).")

    print("ALL CASTING MECHANICS ACCEPTANCE CRITERIA VERIFIED SUCCESSFULLY.")

if __name__ == '__main__':
    run_acceptance_tests()
