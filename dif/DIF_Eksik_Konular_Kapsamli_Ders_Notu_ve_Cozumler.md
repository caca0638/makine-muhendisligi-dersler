# DİFERANSİYEL DENKLEMLER - EKSİK KONULAR DERS NOTU VE ÇÖZÜMLÜ PROBLEMLER
*MTH 2303 Müfredatı & Boyce-DiPrima / Dennis Zill Temel Kaynakları*

---

## 1. 1. MERTEBEDEN DİFERANSİYEL DENKLEMLER (BÖLÜM 1 - 4)

### 1.1 Temel Tanımlar ve Sınıflandırma
* **Mertebe:** Denklemdeki en yüksek türevin derecesidir (örn: y'' + 3y' = 0 denklemi 2. mertebedendir).
* **Derece:** En yüksek mertebeli türevin üssüdür.
* **Doğrusallık (Lineerlik):** Bağımlı değişken y ve tüm türevleri (y', y'', ...) 1. dereceden olmalı, birbiriyle çarpım halinde bulunmamalıdır:
  `a_n(x) y^(n) + ... + a_1(x) y' + a_0(x) y = g(x)`
* **Picard-Lindelöf Varlık ve Teklik Teoremi:** dy/dx = f(x, y), y(x₀) = y₀ probleminde f(x, y) ve ∂f/∂y sürekli ise x₀ civarında tek bir çözüm vardır.

### 1.2 Değişkenlerine Ayrılabilir Denklemler
`dy / dx = g(x) · h(y)  =>  [ 1 / h(y) ] dy = g(x) dx`
Her iki tarafın integrali alınarak genel çözüm elde edilir:
`∫ [ 1 / h(y) ] dy = ∫ g(x) dx + C`

### 1.3 Homojen Diferansiyel Denklemler
M(x, y) dx + N(x, y) dy = 0 denkleminde M ve N aynı dereceden homojen ise denklem dy/dx = F(y / x) formunda yazılabilir.
* **Dönüşüm:** `v = y / x  =>  y = v · x  =>  dy/dx = v + x (dv/dx)`
* `v + x (dv/dx) = F(v)  =>  [ 1 / (F(v) - v) ] dv = (1 / x) dx`

### 1.4 Tam Diferansiyel Denklemler ve İntegrasyon Çarpanı
M(x, y) dx + N(x, y) dy = 0 denkleminde:
* **Tamlık Şartı (Euler):** `∂M / ∂y = ∂N / ∂x`
* Sağlanıyorsa u(x, y) = ∫ M dx + k(y) yazılıp ∂u/∂y = N(x, y) eşitliğinden k(y) bulunur. Genel çözüm: `u(x, y) = C`.
* **İntegrasyon Çarpanı μ(x, y):**
  * `[ (∂M/∂y - ∂N/∂x) / N ] = P(x)  =>  μ(x) = e^(∫ P(x) dx)`
  * `[ (∂N/∂x - ∂M/∂y) / M ] = Q(y)  =>  μ(y) = e^(∫ Q(y) dy)`

### 1.5 Birinci Mertebeden Doğrusal Denklemler
* **Standart Form:** `y' + P(x) y = Q(x)`
* **İntegrasyon Çarpanı:** `μ(x) = e^(∫ P(x) dx)`
* **Genel Çözüm:** `y(x) = [ 1 / μ(x) ] · ∫ [ μ(x) · Q(x) dx ] + C / μ(x)`

---

## 2. ÖZEL DENKLEMLER VE MÜHENDİSLİK UYGULAMALARI (BÖLÜM 7)

### 2.1 Clairaut ve Lagrange Denklemleri
* **Clairaut Denklemi:** `y = x · y' + f(y')  (p = y' => y = x·p + f(p))`
  * **Genel Çözüm:** `y = C · x + f(C)` (Doğru ailesi).
  * **Tekil Çözüm (Zarf):** `x + f'(p) = 0` ve `y = x·p + f(p)` denklem sisteminden p yok edilerek elde edilen zarf eğrisidir.
* **Lagrange Denklemi:** `y = x · φ(y') + ψ(y')  (φ(p) ≠ p)`

### 2.2 Geometrik ve Fiziksel Uygulamalar
* **Ortogonal Yörüngeler:** F(x, y, C) = 0 ailesinin diferansiyel denkleminde `dy/dx` yerine `-dx/dy` yazılarak dik kesen eğriler ailesi bulunur.
* **Newton Soğuma Kanunu:** `dT / dt = -k · (T - T_çevre)  =>  T(t) = T_çevre + (T₀ - T_çevre) · e^(-k·t)`
* **Karışım Problemleri:** `dQ / dt = (r_giriş · c_giriş) - [ r_çıkış · ( Q(t) / V(t) ) ]`

---

## 3. LAPLACE DÖNÜŞÜMLERİ VE SİSTEM ÇÖZÜMLERİ (BÖLÜM 15 - 16)

### 3.1 Tanım ve Temel Dönüşümler
`L{ f(t) } = F(s) = ∫₀^∞ e^(-s·t) f(t) dt`

| f(t) (t ≥ 0) | F(s) |
|---|---|
| 1 | 1 / s |
| t^n | n! / s^(n+1) |
| e^(a·t) | 1 / (s - a) |
| sin(w·t) | w / (s² + w²) |
| cos(w·t) | s / (s² + w²) |
| u(t - c) (Birim Basamak) | e^(-c·s) / s |
| δ(t - c) (Dirac Delta) | e^(-c·s) |

### 3.2 Türevin Laplace Dönüşümleri
* `L{ f'(t) } = s · F(s) - f(0)`
* `L{ f''(t) } = s² · F(s) - s · f(0) - f'(0)`
* `L{ f'''(t) } = s³ · F(s) - s² · f(0) - s · f'(0) - f''(0)`
* **1. Öteleme:** `L{ e^(at) f(t) } = F(s - a)`
* **2. Öteleme:** `L{ f(t - c) u(t - c) } = e^(-c·s) F(s)`
* **Konvolüsyon:** `L{ (f * g)(t) } = F(s) · G(s)`

---

## 4. SAYISAL ÇÖZÜM YÖNTEMLERİ (BÖLÜM 17)

### 4.1 Standart Euler Yöntemi
`y_(n+1) = y_n + h · f(x_n, y_n)`

### 4.2 Geliştirilmiş Euler (Heun) Yöntemi
* Tahmin: `y*_(n+1) = y_n + h · f(x_n, y_n)`
* Düzeltme: `y_(n+1) = y_n + (h / 2) · [ f(x_n, y_n) + f(x_(n+1), y*_(n+1)) ]`

### 4.3 4. Mertebe Runge-Kutta (RK4) Yöntemi
* `k₁ = f(x_n, y_n)`
* `k₂ = f(x_n + h/2, y_n + (h/2) · k₁)`
* `k₃ = f(x_n + h/2, y_n + (h/2) · k₂)`
* `k₄ = f(x_n + h, y_n + h · k₃)`
* `y_(n+1) = y_n + (h / 6) · (k₁ + 2k₂ + 2k₃ + k₄)`

---

## 5. ÇÖZÜMLÜ SINAV PROBLEMLERİ

### PROBLEM 1: Tam Diferansiyel Denklem ve İntegrasyon Çarpanı
`(3x² y + 2xy + y³) dx + (x² + y²) dy = 0`
* Çözüm: `[ (∂M/∂y - ∂N/∂x) ] / N = 3  =>  μ(x) = e^(3x)`
* Genel Çözüm: `e^(3x) · ( x² y + y³ / 3 ) = C`

### PROBLEM 2: Homojen Diferansiyel Denklem
`(x² + y²) dx - 2xy dy = 0,  y(1) = 2`
* v = y/x dönüşümü ile: `x² - y² = C · x`
* Başlangıç şartı: y(1) = 2 => C = -3 => `y² = x² + 3x`

### PROBLEM 3: Clairaut Denklemi
`y = x · y' + (y')²`
* Genel Çözüm: `y = C · x + C²` (Doğru ailesi)
* Tekil Çözüm: `x + 2p = 0 => p = -x/2 => y = -x² / 4` (Parabol zarf)

### PROBLEM 4: Laplace ile Başlangıç Değer Problemi
`y'' - 4y' + 4y = e^(2t),  y(0) = 0, y'(0) = 0`
* `(s - 2)² Y(s) = 1 / (s - 2) => Y(s) = 1 / (s - 2)³`
* Çözüm: `y(t) = (1 / 2) · t² · e^(2t)`

### PROBLEM 5: Ortogonal Yörüngeler
`y = C · x²` parabol ailesinin dik kesen yörüngeleri:
* `dy/dx = 2y/x => -dx/dy = 2y/x => x dx + 2y dy = 0`
* Çözüm: `x² + 2y² = C*` (Elips ailesi)

### PROBLEM 6: Runge-Kutta 4 (RK4) Sayısal Çözüm
`dy/dx = x + y,  y(0) = 1, h = 0.1`
* `k₁ = 1.0000, k₂ = 1.1000, k₃ = 1.1050, k₄ = 1.2105`
* `y(0.1) = 1 + (0.1/6) · (6.6205) = 1.11034` (Tam analitik değer: 1.110342)
