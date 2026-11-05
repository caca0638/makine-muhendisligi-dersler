# MAK - Isı Transferi (Heat Transfer)
## Kapsamlı Referans Ders Notu, Formül Kılavuzu ve Çözümlü Problemler

**Kaynak Referanslar:**
- Yunus A. Çengel & Afshin J. Ghajar, *Heat and Mass Transfer: Fundamentals and Applications*, McGraw-Hill.
- Frank P. Incropera, David P. DeWitt, Theodore L. Bergman, Adrienne S. Lavine, *Fundamentals of Heat and Mass Transfer*, Wiley.

---

## 1. Temel Kavramlar ve Isı Geçiş Mekanizmaları

Isı, bir sistem ile çevresi veya iki ortam arasında sıcaklık farkı ($\Delta T$) nedeniyle transfer edilen termal enerjidir.

1. **İletim (Kondüksiyon - Fourier Yasası):**
   $$\dot{q} = -k A \frac{dT}{dx} \quad [\text{W}]$$
   $k$: Isıl iletkenlik [W/(m·K)], $A$: Isı geçişine dik alan [m²].
2. **Taşınım (Konveksiyon - Newton Soğuma Yasası):**
   $$\dot{q} = h A (T_s - T_\infty) \quad [\text{W}]$$
   $h$: Taşınım ısı transfer katsayısı [W/(m²·K)].
3. **Işınım (Radyasyon - Stefan-Boltzmann Yasası):**
   $$\dot{q} = \varepsilon \sigma A (T_s^4 - T_{\text{çevre}}^4) \quad [\text{W}]$$
   $\sigma = 5.670 \times 10^{-8}\text{ W/(m}^2\cdot\text{K}^4)$, $\varepsilon$: Yüzey yayma oranı (emissivity).

---

## 2. Daimi Isı İletimi ve Termal Direnç Ağları

### 2.1. Temel Geometrilerde Isıl Dirençler ($R_{th}$)
- **Düzlemsel Duvar:** $R_{\text{duvar}} = \frac{L}{k A}$
- **Silindirik Boru (Boy $L$):** $R_{\text{silindir}} = \frac{\ln(r_2 / r_1)}{2\pi k L}$
- **Küre ($r_1, r_2$):** $R_{\text{küre}} = \frac{r_2 - r_1}{4\pi k r_1 r_2}$
- **Taşınım Direnci:** $R_{\text{taşınım}} = \frac{1}{h A}$

Toplam Isı Geçişi ve Toplam Katsayı ($U$):
$$\dot{q} = \frac{T_{\infty 1} - T_{\infty 2}}{R_{\text{toplam}}} = U A \Delta T_{\text{toplam}} \Longleftrightarrow U A = \frac{1}{R_{\text{toplam}}}$$

### 2.2. Kritik Yalıtım Yarıçapı ($r_{cr}$)
Silindirik ve küresel yüzeylerde yalıtım kalınlaştıkça iletim direnci artarken taşınım alanı büyüdüğü için dış taşınım direnci azalır:
- **Silindir için:** $r_{cr} = \frac{k_{\text{yalıtım}}}{h_{\text{dış}}}$
- **Küre için:** $r_{cr,\text{küre}} = \frac{2 k_{\text{yalıtım}}}{h_{\text{dış}}}$
*Kural:* Boru dış yarıçapı $r_1 < r_{cr}$ ise yalıtım eklemek ısı kaybını artırır. Isı tasarrufu için daima $r_2 > r_{cr}$ olmalıdır.

### 2.3. Kanatçıklar (Fins / Genişletilmiş Yüzeyler)
Kanat parametresi: $m = \sqrt{\frac{h P}{k A_c}}$
- **Ucu Yalıtılmış Kanatçık:** $\dot{q}_{\text{kanat}} = \sqrt{h P k A_c} (T_b - T_\infty) \tanh(mL)$
- **Kanatçık Verimi:** $\eta_f = \frac{\dot{q}_{\text{kanat}}}{\dot{q}_{\text{maks}}} = \frac{\tanh(mL)}{mL}$
- **Kanatçık Etkinliği:** $\varepsilon_f = \frac{\dot{q}_{\text{kanat}}}{h A_c (T_b - T_\infty)}$ (Tasarımın ekonomik/yararlı olması için $\varepsilon_f \ge 2$ olmalıdır).

---

## 3. Zamana Bağlı (Geçici) Isı İletimi (Transient Conduction)

### 3.1. Yığılı Kapasite Yöntemi (Lumped System Analysis)
Karakteristik uzunluk: $L_c = \frac{V}{A_s}$.
- **Geçerlilik Kriteri:** $\text{Bi} = \frac{h L_c}{k} \le 0.10$
- **Sıcaklık Formülü:**
  $$\frac{T(t) - T_\infty}{T_i - T_\infty} = e^{-b t}, \quad b = \frac{h A_s}{\rho V c_p} = \frac{1}{\tau}$$
- **Zaman Sabiti:** $\tau = \frac{\rho V c_p}{h A_s} = R_{th} C_{th} \quad [\text{s}]$

---

## 4. Taşınımla Isı Geçişi (Konveksiyon)

### 4.1. Boyutsuz Sayılar
- **Reynolds:** $\text{Re} = \frac{\rho V L}{\mu} = \frac{V L}{\nu}$ (Eylemsizlik / Viskozite)
- **Prandtl:** $\text{Pr} = \frac{\nu}{\alpha} = \frac{\mu c_p}{k}$ (Momentum yayınımı / Isıl yayınım)
- **Nusselt:** $\text{Nu} = \frac{h L}{k_{\text{akışkan}}}$ (Taşınım / İletim)
- **Grashof:** $\text{Gr} = \frac{g \beta (T_s - T_\infty) L^3}{\nu^2}$ (Doğal taşınım kaldırma / Viskozite)
- **Rayleigh:** $\text{Ra} = \text{Gr} \cdot \text{Pr}$

### 4.2. Boru İçi Akış Ampirik Bağıntıları
- $\text{Re} < 2300$: Tam gelişmiş laminer akış (Sabit ısı akısında $\text{Nu} = 4.36$, sabit yüzey sıcaklığında $\text{Nu} = 3.66$).
- $\text{Re} > 10,000$ (Dittus-Boelter Denklemi):
  $$\text{Nu} = 0.023 \text{Re}^{0.8} \text{Pr}^n \quad (\text{Isıtma için } n = 0.4, \text{ soğutma için } n = 0.3)$$

---

## 5. Işınımla Isı Geçişi (Radyasyon)

### 5.1. Şekil Faktörü (View Factor $F_{ij}$)
- Karşılıklılık: $A_i F_{ij} = A_j F_{ji}$
- Toplam Kuralı: $\sum_{j=1}^N F_{ij} = 1$
- Düzlemsel yüzeyler: $F_{ii} = 0$.

### 5.2. İki Büyük Paralel Plaka Arası Net Radyasyon
$$\dot{q}_{12} = \frac{\sigma (T_1^4 - T_2^4)}{\frac{1}{\varepsilon_1} + \frac{1}{\varepsilon_2} - 1} A$$
- Eşit yayma oranlı $N$ adet radyasyon kalkanı eklenmesi, net ısı transferini **$(N + 1)$** kat azaltır.

---

## 6. Isı Değiştiricileri (Heat Exchangers)

### 6.1. Logaritmik Ortalama Sıcaklık Farkı (LMTD)
$$\dot{q} = U A \Delta T_{lm} F, \quad \Delta T_{lm} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$$
- **Karşıt Akış:** $\Delta T_1 = T_{h,\text{in}} - T_{c,\text{out}}$, $\Delta T_2 = T_{h,\text{out}} - T_{c,\text{in}}$.

### 6.2. $\varepsilon - \text{NTU}$ Yöntemi
$$\dot{q}_{\text{maks}} = C_{\text{min}} (T_{h,\text{in}} - T_{c,\text{in}}), \quad \varepsilon = \frac{\dot{q}}{\dot{q}_{\text{maks}}}, \quad \text{NTU} = \frac{U A}{C_{\text{min}}}$$

---

## 7. Çözümlü Problemler

### Problem 1: Buhar Borusu Yalıtımı ve Kritik Yarıçap
$D_1 = 100\text{ mm}$ ($r_1 = 50\text{ mm}$), $T_1 = 250^\circ\text{C}$, $T_\infty = 20^\circ\text{C}$, $h = 8\text{ W/(m}^2\text{K)}$, cam yünü $k = 0.05\text{ W/(m}\cdot\text{K)}$.
a) $r_{cr} = \frac{k}{h} = \frac{0.05}{8} = 0.00625\text{ m} = \mathbf{6.25\text{ mm}}$. $r_1 = 50\text{ mm} > r_{cr}$ olduğundan yalıtım doğrudan ısı kaybını azaltır.
b) Yalıtımsız: $A_1 = 2\pi(0.05)(1) = 0.3142\text{ m}^2 \Longrightarrow \dot{q}' = 8(0.3142)(230) = \mathbf{578.1\text{ W/m}}$.
c) $25\text{ mm}$ yalıtım ($r_2 = 75\text{ mm}$):
$R_{\text{yalıtım}} = \frac{\ln(75/50)}{2\pi(0.05)(1)} = 1.2906^\circ\text{C/W}$, $R_{\text{taş}} = \frac{1}{8(2\pi \cdot 0.075 \cdot 1)} = 0.2653^\circ\text{C/W}$.
$R_{\text{toplam}} = 1.5559^\circ\text{C/W} \Longrightarrow \dot{q}' = \frac{230}{1.5559} = \mathbf{147.8\text{ W/m}}$.
**Tasarruf:** $\frac{578.1 - 147.8}{578.1} \times 100 = \mathbf{\%74.4}$.

---

### Problem 2: Termokupl Tepki Süresi (Yığılı Kapasite)
Küre eklem $D = 1.2\text{ mm}$ ($r = 0.6\text{ mm}$), $\rho = 8500\text{ kg/m}^3$, $c_p = 400\text{ J/(kg}\cdot\text{K)}$, $k = 25\text{ W/(m}\cdot\text{K)}$, $h = 250\text{ W/(m}^2\cdot\text{K)}$. $T_i = 30^\circ\text{C}$, $T_\infty = 600^\circ\text{C}$, $T(t) = 580^\circ\text{C}$.
a) $L_c = \frac{r}{3} = 0.0002\text{ m}$. $\text{Bi} = \frac{250 \cdot 0.0002}{25} = \mathbf{0.002 \le 0.10}$ (Yığılı yöntem geçerli).
b) $\tau = \frac{\rho c_p L_c}{h} = \frac{8500 \cdot 400 \cdot 0.0002}{250} = \mathbf{2.72\text{ s}}$.
c) $\frac{580 - 600}{30 - 600} = 0.03509 = e^{-t / 2.72} \Longrightarrow t = 2.72 \cdot (-\ln 0.03509) = 2.72 \cdot 3.3498 = \mathbf{9.11\text{ s}}$.

---

### Problem 3: Boru İçi Türbülanslı Akışta Isı Geçişi
$D = 25\text{ mm}$, $L = 6\text{ m}$, $\dot{m} = 0.3\text{ kg/s}$, $T_s = 90^\circ\text{C}$.
Akışkan özellikleri: $\rho = 988\text{ kg/m}^3$, $c_p = 4180\text{ J/(kg}\cdot\text{K)}$, $\mu = 0.547 \times 10^{-3}\text{ kg/(m}\cdot\text{s)}$, $k = 0.643\text{ W/(m}\cdot\text{K)}$, $\text{Pr} = 3.56$.
a) $A_c = 4.9087 \times 10^{-4}\text{ m}^2$, $V = \frac{0.3}{988 \cdot 4.9087 \times 10^{-4}} = 0.6186\text{ m/s}$.
$\text{Re} = \frac{988 \cdot 0.6186 \cdot 0.025}{0.547 \times 10^{-3}} = \mathbf{27,934 > 10,000}$ (Türbülanslı).
b) Isıtma ($n = 0.4$): $\text{Nu} = 0.023(27934)^{0.8}(3.56)^{0.4} = 0.023(3572.7)(1.663) = \mathbf{136.65}$.
$h = \frac{136.65 \cdot 0.643}{0.025} = \mathbf{3,514.8\text{ W/(m}^2\cdot\text{K)}}$.
c) $A_s = \pi(0.025)(6) = \mathbf{0.4712\text{ m}^2}$.

---

### Problem 4: Radyasyon Kalkanı ile Isı Kaybının Azaltılması
$T_1 = 800\text{ K}$, $T_2 = 400\text{ K}$, $\varepsilon_1 = 0.8$, $\varepsilon_2 = 0.5$, kalkan $\varepsilon_k = 0.05$.
a) Kalkansız: $\frac{\dot{q}}{A} = \frac{5.67 \times 10^{-8}(800^4 - 400^4)}{1/0.8 + 1/0.5 - 1} = \frac{21772.8}{2.25} = \mathbf{9,676.8\text{ W/m}^2}$.
b) Kalkanlı toplam direnç: $R_{\text{toplam}} = (1/0.8 + 1/0.05 - 1) + (1/0.05 + 1/0.5 - 1) = 20.25 + 21.00 = 41.25$.
$\frac{\dot{q}_{\text{kalkan}}}{A} = \frac{21772.8}{41.25} = \mathbf{527.8\text{ W/m}^2}$ (**18.33 kat / %94.55 azalma**).
Kalkan sıcaklığı: $T_k = [800^4 - \frac{527.8 \cdot 20.25}{5.67 \times 10^{-8}}]^{0.25} = \mathbf{685.9\text{ K} \approx 412.9^\circ\text{C}}$.

---

### Problem 5: Karşıt Akışlı Eşanjör (LMTD)
$\dot{m}_h = 1.5\text{ kg/s}$, $c_{p,h} = 2100\text{ J/(kg}\cdot\text{K)}$, $120^\circ\text{C} \to 60^\circ\text{C}$.
Su $c_{p,c} = 4180\text{ J/(kg}\cdot\text{K)}$, $20^\circ\text{C} \to 45^\circ\text{C}$, $U = 450\text{ W/(m}^2\cdot\text{K)}$.
a) $\dot{q} = 1.5 \cdot 2100 \cdot (120 - 60) = \mathbf{189\text{ kW}}$.
$\dot{m}_c = \frac{189000}{4180(45 - 20)} = \mathbf{1.809\text{ kg/s}}$.
b) Karşıt akış: $\Delta T_1 = 120 - 45 = 75^\circ\text{C}$, $\Delta T_2 = 60 - 20 = 40^\circ\text{C}$.
$\Delta T_{lm} = \frac{75 - 40}{\ln(75/40)} = \frac{35}{0.6286} = \mathbf{55.68^\circ\text{C}}$.
c) $A = \frac{189000}{450 \cdot 55.68} = \mathbf{7.543\text{ m}^2}$.
