# DİFERANSİYEL DENKLEMLER - VİZE VE FİNALDE ÇIKABİLECEK SORULAR (BÖLÜM 1)
**Kaynak:** BUders / Üniversite Diferansiyel Denklemler Vize Soru Havuzu  
**Hedef Kitle:** Makine Mühendisliği Lisans Öğrencisi  
**Pedagojik Not:** Her soru önce sınav kağıdında yazılması gereken klasik matematiksel adımlarla çözülmüş, ardından bir makine mühendisinin Python'u nasıl pratik bir hesap aracı olarak kullanacağı satır satır açıklanmıştır.

---

## SORU 1: Mertebe, Derece ve Lineerlik Tayini (Klasik Vize Soru 1)

### Soru Metni:
Aşağıda verilen diferansiyel denklemlerin **mertebesini (order)**, **derecesini (degree)** bulunuz ve **lineer (doğrusal)** olup olmadıklarını nedenleriyle belirtiniz:
a) $x^2 \frac{d^3 y}{dx^3} + \left(\frac{dy}{dx}\right)^4 - y = \sin(x)$  
b) $\sqrt{1 + \left(\frac{dy}{dx}\right)^2} = \frac{d^2 y}{dx^2}$  
c) $\frac{d^2 y}{dx^2} + 4x \frac{dy}{dx} + \cos(y) = 0$

---

### 1. Analitik Teori ve Kağıt Üzerinde Çözüm:

#### (a) $x^2 y''' + (y')^4 - y = \sin(x)$
* **Mertebe (Order):** Denklemdeki en yüksek türev 3. türevdir ($y'''$).  
  $$\implies \text{Mertebe} = 3$$
* **Derece (Degree):** En yüksek mertebeli türevin ($y'''$) kuvveti 1'dir.  
  $$\implies \text{Derece} = 1$$
* **Lineerlik:** Lineer değildir (**Non-linear**). Çünkü bağımlı değişkenin türevi olan $(y')^4$ dördüncü dereceden bir kuvvete sahiptir. (Doğrusallık kuralı: Bağımlı değişken $y$ ve türevleri yalnızca 1. kuvvetten olmalıdır).

#### (b) $\sqrt{1 + (y')^2} = y''$
* **Kritik Kural:** Derece hesabı yapılmadan önce denklem kesirli veya köklü ifadelerden kurtarılarak polinom haline getirilmelidir!
* Her iki tarafın karesi alınır:
  $$1 + (y')^2 = (y'')^2 \implies (y'')^2 - (y')^2 - 1 = 0$$
* **Mertebe:** En yüksek türev 2. türevdir ($y''$).  
  $$\implies \text{Mertebe} = 2$$
* **Derece:** En yüksek türevin üssü 2'dir ($(y'')^2$).  
  $$\implies \text{Derece} = 2$$
* **Lineerlik:** Lineer değildir (**Non-linear**). $(y'')^2$ ve $(y')^2$ terimleri mevcuttur.

#### (c) $y'' + 4x y' + \cos(y) = 0$
* **Mertebe:** 2.
* **Derece:** 1.
* **Lineerlik:** Lineer değildir (**Non-linear**). Çünkü bağımlı değişken $y$, doğrusal olmayan trigonometrik bir fonksiyonun içine girmiştir ($\cos(y)$).

---

### 2. Hesaplamalı Çözüm (Python Scripting & Mühendislik Anlatımı):

Bir makine mühendisi olarak Python'a "bu denklem lineer mi, derecesi kaç?" diye sormak için `sympy` (Symbolic Python) kütüphanesini kullanırız.

```python
import sympy as sp

# 1. Adım: Kağıttaki x ve y değişkenlerini tanımlıyoruz
x = sp.Symbol('x')             # Bağımsız değişken (örn: konum veya zaman)
y = sp.Function('y')(x)        # x'e bağlı fonksiyonumuz (bağımlı değişken)

# 2. Adım: Türevleri tanımlıyoruz
# y.diff(x, 3) demek matematikteki d^3 y / dx^3 demektir.
ode_a = x**2 * y.diff(x, 3) + (y.diff(x, 1))**4 - y - sp.sin(x)

# 3. Adım: Python'un yerleşik fonksiyonları ile sorguluyoruz
mertebe = sp.ode_order(ode_a, y)        # En yüksek türevi bulur -> 3
lineer_mi = sp.classify_ode(sp.Eq(ode_a, 0), y) # Denklemin tipini sınıflandırır
```

* **Mühendislik Açıklaması:**
  - `sp.Symbol('x')`: Bilgisayara $x$'in bir sayı olmadığını, harf (sembol) olduğunu söyler.
  - `y.diff(x, n)`: Kağıtta aldığımız $n$. türevin bilgisayardaki karşılığıdır.

---

## SORU 2: Değişkenlerine Ayrılabilir Diferansiyel Denklem (Vize Soru 3 Tipi)

### Soru Metni:
Aşağıda verilen başlangıç değer probleminin (IVP) çözümünü bulunuz:
$$\frac{dy}{dx} = \frac{x (y^2 + 1)}{y (x^2 + 1)}, \quad y(0) = 1$$

---

### 1. Analitik Teori ve Kağıt Üzerinde Çözüm:

* **Denklem Tipi:** 1. Mertebeden Değişkenlerine Ayrılabilir (Separable).
* **Adım 1: Değişkenleri ve diferansiyelleri iki tarafa ayırıyoruz:**
  $$\frac{y}{y^2 + 1} \, dy = \frac{x}{x^2 + 1} \, dx$$
* **Adım 2: Her iki tarafın integralini alıyoruz:**
  $$\int \frac{y}{y^2 + 1} \, dy = \int \frac{x}{x^2 + 1} \, dx$$
* **Adım 3: Değişken değiştirme ile integralleri çözüyoruz:**
  Sol taraf için: $u = y^2 + 1 \implies du = 2y \, dy \implies y \, dy = \frac{du}{2}$
  Sağ taraf için: $v = x^2 + 1 \implies dv = 2x \, dx \implies x \, dx = \frac{dv}{2}$
  $$\frac{1}{2} \ln(y^2 + 1) = \frac{1}{2} \ln(x^2 + 1) + C_1$$
* **Adım 4: Her iki tarafı 2 ile çarpıp üstel fonksiyona geçiyoruz:**
  $$\ln(y^2 + 1) = \ln(x^2 + 1) + 2C_1$$
  $$e^{\ln(y^2 + 1)} = e^{\ln(x^2 + 1) + 2C_1} = e^{\ln(x^2 + 1)} \cdot e^{2C_1}$$
  $$y^2 + 1 = C (x^2 + 1) \quad (C = e^{2C_1} > 0)$$
  **Genel Çözüm:** $y^2 = C(x^2 + 1) - 1$

* **Adım 5: Başlangıç Şartını $y(0) = 1$ uygulayarak $C$ sabitini buluyoruz:**
  $$x = 0 \text{ ve } y = 1 \implies (1)^2 + 1 = C (0^2 + 1) \implies 2 = C(1) \implies C = 2$$
* **Özel Çözüm (Particular Solution):**
  $$y^2 + 1 = 2(x^2 + 1) \implies y^2 = 2x^2 + 2 - 1 = 2x^2 + 1$$
  $y(0) = +1$ pozitif verildiği için pozitif kök seçilir:
  $$y(x) = \sqrt{2x^2 + 1}$$

---

### 2. Hesaplamalı Çözüm (Python Scripting & Mühendislik Anlatımı):

Makine mühendisliğinde bu çözümün Python karşılığı şu şekildedir:

```python
import sympy as sp

# 1. Sembolleri ve fonksiyonu tanımla
x = sp.Symbol('x', real=True)
y = sp.Function('y')(x)

# 2. Diferansiyel denklemi kur: dy/dx = (x*(y^2 + 1)) / (y*(x^2 + 1))
# sp.Eq(sol_taraf, sag_taraf) şeklinde yazılır
ode = sp.Eq(y.diff(x), (x * (y**2 + 1)) / (y * (x**2 + 1)))

# 3. Genel çözümü dsolve fonksiyonu ile al (Kağıttaki integrali kendi alır)
genel_cozum = sp.dsolve(ode, y)

# 4. Başlangıç şartını besle: ics = {y(0): 1} (Initial Condition System)
ozel_cozum = sp.dsolve(ode, y, ics={y.subs(x, 0): 1})
```

* **Mühendislik Açıklaması:**
  - `y.diff(x)`: Bizim kağıtta $\frac{dy}{dx}$ diye yazdığımız ifadedir.
  - `sp.Eq(A, B)`: $A = B$ matematiksel eşitliğini kurar.
  - `sp.dsolve(ode, y)`: Bizim elle değişkenleri ayırıp $u$-dönüşümü yaptığımız integralleri saniyenin binde birinde analitik olarak çözer.
  - `ics={y.subs(x, 0): 1}`: Soru kökündeki $y(0)=1$ şartını koda verip $C$ sabitini ($C=2$) otomatik hesaplatır.

---

## SORU 3: İntegral Çarpanı Metodu ile 1. Derece Lineer Denklem (Vize Soru 7 Tipi)

### Soru Metni:
Aşağıda verilen diferansiyel denklemin genel çözümünü bulunuz:
$$x \frac{dy}{dx} + 2y = 4x^2 \quad (x > 0)$$

---

### 1. Analitik Teori ve Kağıt Üzerinde Çözüm:

* **Adım 1: Denklemi standart lineer forma ($y' + P(x)y = Q(x)$) getiriyoruz:**
  Her terimi $x$'e bölüyoruz ($x \neq 0$):
  $$\frac{dy}{dx} + \frac{2}{x} y = 4x$$
  Buradan: $P(x) = \frac{2}{x}$ ve $Q(x) = 4x$.
* **Adım 2: İntegrasyon Çarpanı $\mu(x)$ hesabı:**
  $$\mu(x) = e^{\int P(x) dx} = e^{\int \frac{2}{x} dx} = e^{2 \ln(x)} = e^{\ln(x^2)} = x^2$$
* **Adım 3: Denklemi $\mu(x) = x^2$ ile çarpıyoruz:**
  $$x^2 \frac{dy}{dx} + 2x y = 4x^3 \implies \frac{d}{dx}\left[x^2 y\right] = 4x^3$$
* **Adım 4: Her iki tarafın integralini alıyoruz:**
  $$\int \frac{d}{dx}\left[x^2 y\right] dx = \int 4x^3 dx$$
  $$x^2 y = x^4 + C$$
* **Adım 5: $y(x)$'i yalnız bırakıyoruz:**
  $$y(x) = \frac{x^4 + C}{x^2} = x^2 + \frac{C}{x^2}$$

---

### 2. Hesaplamalı Çözüm (Python Scripting & Mühendislik Anlatımı):

```python
import sympy as sp

x = sp.Symbol('x', positive=True)
y = sp.Function('y')(x)

# Denklem: x * y' + 2*y = 4*x^2
ode = sp.Eq(x * y.diff(x) + 2*y, 4 * x**2)

# Çözüm
cozum = sp.dsolve(ode, y)
# Sonuç: y(x) = C1/x^2 + x^2
```

---

## 3. Akademik Yorum (Makine Mühendisliği Bakış Açısı)

- **Soru 1:** Diferansiyel denklemlerin sınıflandırılması, makine dinamik modellemesinde simülasyon stratejimizi belirler. Lineer denklemler analitik olarak çözülebilirken, $y^4$ veya $\cos(y)$ gibi non-lineer terimler (büyük yer değiştirmeli sarkaçlar veya sürtünmeli akışlar) sayısal entegrasyonu (RK45) zorunlu kılar.
- **Soru 2:** Elde edilen çözüm $y(x) = \sqrt{2x^2 + 1}$ bir hiperbol eğrisi tanımlar. $x \to \infty$ iken $y(x) \approx \sqrt{2}x$ asimptotuna yaklaşır. Bu davranış, gerinim sertleşmesi (strain hardening) gösteren malzemelerin plastik deformasyon rejimindeki gerilme-şekil değiştirme eğrilerine tam benzerlik gösterir.
- **Soru 3:** Çözüm $y(x) = x^2 + \frac{C}{x^2}$ şeklindedir. $x^2$ terimi dış yükün oluşturduğu **özel zorlanmış cevabı (particular response)**, $\frac{C}{x^2}$ terimi ise sistemin kendi iç yapısından gelen **homojen geçici cevabı (transient response)** temsil eder.
