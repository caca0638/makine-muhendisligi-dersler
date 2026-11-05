# BÖLÜM 2: İKİNCİ MERTEBEDEN DOĞRUSAL DİFERANSİYEL DENKLEMLER
**Ders:** Diferansiyel Denklemler (MTH 2303 / Mühendislik Matematiği)  
**Kapsam:** Makine Mühendisliği Lisans Programı (Mekanik Titreşimler Temeli)

---

## 1. GENEL TEORİ VE DOĞRUSALLIK

### 1.1 İkinci Mertebeden Doğrusal Diferansiyel Denklem Formu
$$P(x) \frac{d^2 y}{dx^2} + Q(x) \frac{dy}{dx} + R(x) y = G(x)$$
$P(x) \neq 0$ olan aralıkta denklem standart forma bölünür:
$$\frac{d^2 y}{dx^2} + p(x) \frac{dy}{dx} + q(x) y = g(x)$$
- $g(x) = 0$ ise: **Homojen Denklem**
- $g(x) \neq 0$ ise: **Homojen Olmayan (Non-homogeneous) Denklem**

### 1.2 Süperpozisyon İlkesi (Superposition Principle)
Homojen denklem $y'' + p(x)y' + q(x)y = 0$ için; eğer $y_1(x)$ ve $y_2(x)$ iki çözüm ise, keyfi $C_1, C_2$ sabitleri için bunların doğrusal bileşimi de bir çözümdür:
$$y(x) = C_1 y_1(x) + C_2 y_2(x)$$

### 1.3 Wronskian Determinantı ve Doğrusal Bağımsızlık
İki fonksiyonun $I$ aralığında doğrusal bağımsız olabilmesi için Wronskian determinantı sıfırdan farklı olmalıdır:
$$W(y_1, y_2)(x) = \begin{vmatrix} y_1(x) & y_2(x) \\ y_1'(x) & y_2'(x) \end{vmatrix} = y_1(x) y_2'(x) - y_2(x) y_1'(x)$$
- Eğer $W(y_1, y_2)(x) \neq 0$ ise $\{y_1, y_2\}$ çözümleri **Temel Çözüm Kümesini (Fundamental Solution Set)** oluşturur.
- **Abel Teoremi:** $W(x) = C \exp\left(-\int p(x) dx\right)$

### 1.4 Mertebe İndirgeme Yöntemi (Reduction of Order - D'Alembert)
Homojen denklemin bir $y_1(x)$ çözümü biliniyorsa, ikinci bağımsız çözüm $y_2(x) = v(x) y_1(x)$ formunda aranır.  
Türevler yerine konulduğunda $w(x) = v'(x)$ değişkeni için 1. mertebe ayrılabilir bir denklem elde edilir:
$$y_2(x) = y_1(x) \int \frac{\exp\left(-\int p(x) dx\right)}{[y_1(x)]^2} \, dx$$

---

## 2. SABİT KATSAYILI HOMOJEN DENKLEMLER

$$a \frac{d^2 y}{dx^2} + b \frac{dy}{dx} + c y = 0 \quad (a \neq 0, \, a, b, c \in \mathbb{R})$$
Çözüm $y = e^{r x}$ formunda aranırsa:
$$e^{r x} (a r^2 + b r + c) = 0 \implies a r^2 + b r + c = 0 \quad \text{(Karakteristik Denklem)}$$
Kökler:
$$r_{1, 2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}, \quad \Delta = b^2 - 4ac$$

### Durum 1: İki Farklı Reel Kök ($\Delta > 0$)
Kökler $r_1 \neq r_2$ gerçel sayılardır. Temel çözümler $y_1 = e^{r_1 x}, y_2 = e^{r_2 x}$.
$$y_h(x) = C_1 e^{r_1 x} + C_2 e^{r_2 x}$$

### Durum 2: Çakışık (Katlı) Reel Kök ($\Delta = 0$)
$r_1 = r_2 = r = -\frac{b}{2a}$. Mertebe indirgemeden dolayı ikinci bağımsız çözüm $y_2 = x e^{r x}$ olur.
$$y_h(x) = (C_1 + C_2 x) e^{r x}$$

### Durum 3: Kompleks Eşlenik Kökler ($\Delta < 0$)
$r_{1, 2} = \lambda \pm i \mu \quad \left(\lambda = -\frac{b}{2a}, \, \mu = \frac{\sqrt{4ac - b^2}}{2a}\right)$.  
Euler formülü ($e^{i \mu x} = \cos(\mu x) + i \sin(\mu x)$) uygulanarak reel temel çözümlere geçilir:
$$y_h(x) = e^{\lambda x} \left( C_1 \cos(\mu x) + C_2 \sin(\mu x) \right)$$
veya genlik-faz formunda:
$$y_h(x) = A e^{\lambda x} \cos(\mu x - \phi)$$

---

## 3. MAKİNE MÜHENDİSLİĞİ FİZİKSEL UYGULAMASI: SERBEST MEKANİK TİTREŞİMLER

### 3.1 Dinamik Model (Kütle - Yay - Sönümleyici Sistemi)
Tek serbestlik dereceli (1-DOF) öteleme mekanik sistemi:
- Kütle: $m$ ($\text{kg}$)
- Viskoz sönüm elemanı (damper): $c$ ($\text{N}\cdot\text{s/m}$)
- Doğrusal elastik yay: $k$ ($\text{N/m}$)
- Denge konumundan yer değiştirme: $x(t)$ ($\text{m}$)

Newton'un 2. Yasası ($\sum F_x = m \ddot{x}$):
$$- k x - c \dot{x} = m \ddot{x} \implies m \frac{d^2 x}{dt^2} + c \frac{dx}{dt} + k x = 0$$

Standart Mühendislik Parametreleri:
- **Doğal Dairesel Frekans (Undamped Natural Frequency):**
  $$\omega_n = \sqrt{\frac{k}{m}} \quad (\text{rad/s})$$
- **Kritik Sönüm Katsayısı (Critical Damping Coefficient):**
  $$c_c = 2 \sqrt{k m} = 2 m \omega_n \quad (\text{N}\cdot\text{s/m})$$
- **Boyutsuz Sönüm Oranı (Damping Ratio):**
  $$\zeta = \frac{c}{c_c} = \frac{c}{2 m \omega_n}$$

Standart Kanonik Diferansiyel Denklem Formu:
$$\ddot{x}(t) + 2 \zeta \omega_n \dot{x}(t) + \omega_n^2 x(t) = 0$$
Karakteristik kökler: $r_{1, 2} = -\zeta \omega_n \pm \omega_n \sqrt{\zeta^2 - 1}$

### 3.2 Titreşim Rejimlerinin Mühendislik Sınıflandırması

1. **Aşırı Sönümlü Durum ($\zeta > 1, \, c > c_c$):**
   - Kökler negatif reeldir: $r_{1, 2} = -\zeta \omega_n \pm \omega_n \sqrt{\zeta^2 - 1}$.
   - Salınım (oscillation) meydana gelmez. Sistem denge konumuna üstel olarak yavaş döner.
   $$x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}$$

2. **Kritik Sönümlü Durum ($\zeta = 1, \, c = c_c$):**
   - Katlı negatif reel kök: $r_1 = r_2 = -\omega_n$.
   - Sistem salınım yapmaksızın denge konumuna en hızlı şekilde döner (Mühendislikte araç amortisörleri, kapı hidrolikleri ve ibreli göstergelerde tercih edilen tasarım kriteridir).
   $$x(t) = (C_1 + C_2 t) e^{-\omega_n t}$$

3. **Eksik Sönümlü Durum ($0 \le \zeta < 1, \, c < c_c$):**
   - Kökler kompleks eşleniktir: $r_{1, 2} = -\zeta \omega_n \pm i \omega_d$.
   - **Sönümlü Doğal Frekans:** $\omega_d = \omega_n \sqrt{1 - \zeta^2}$.
   - Sistem genliği zamanla üstel azalan harmonik salınım yapar.
   $$x(t) = e^{-\zeta \omega_n t} \left( C_1 \cos(\omega_d t) + C_2 \sin(\omega_d t) \right) = X_0 e^{-\zeta \omega_n t} \cos(\omega_d t - \phi)$$
   - **Logaritmik Azalma (Logarithmic Decrement):**
     $$\delta = \ln\left(\frac{x(t)}{x(t + T_d)}\right) = \frac{2 \pi \zeta}{\sqrt{1 - \zeta^2}} \approx 2 \pi \zeta \quad (\zeta \ll 1)$$
