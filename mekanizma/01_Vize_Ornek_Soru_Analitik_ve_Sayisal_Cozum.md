# MAK 3103 MEKANİZMA TEKNİĞİ - VİZE SINAV SORUSU ÇÖZÜMÜ VE DERS NOTU
**Mekanizma Türü:** Krank-Salınım Kolu-Piston (Quick-Return / Çift Devreli Mekanizma)  
**Tarih / Durum:** $\theta_2 = 120^\circ$, Sabit hızlı motor ($\omega_2 = \text{sabit}$, $\alpha_2 = 0$).  
**Geometrik Sabitler:**  
- $|AB| = 28\text{ mm}$ (Uzuv 2 - Krank)  
- $|AC| = 32\text{ mm}$ (Şasi mesnetleri düşey mesafesi, C noktası A'nın tam üzerinde)  
- $|CD| = 38\text{ mm}$ (Uzuv 4 - Salınım kolunun pivot C'den üst uç D'ye mesafesi)  
- $|DE| = 41\text{ mm}$ (Uzuv 5 - Biyel çubuğu)  
- Piston kılavuz ekseni: C noktasından geçen yatay doğru ($y_E = y_C$).

---

## a) Düzenek Üzerinde Harflendirme
Mekanizma tekniğinde harfler mafsallara (kinematik çiftlere) verilir:
- **A:** Şasiye bağlı krank sabit dönme merkezi ($O_2$).
- **B:** Krank ucu ile 3 numaralı kayıcı blok arasındaki hareketli döner mafsal.
- **C:** Şasiye bağlı salınım kolu sabit dönme merkezi ($O_4$).
- **D:** Salınım kolu ile 5 numaralı biyel çubuğu arasındaki hareketli döner mafsal.
- **E:** Biyel çubuğu ile yatay kılavuzda kayan 6 numaralı piston arasındaki hareketli döner mafsal.

---

## b) Uzuv Numaralandırma
Kural: "1" numarası daima sabit şasiye (yer/gövde) verilir.
- **Uzuv 1 (Şasi):** A mesnedi, C mesnedi ve E kılavuzunu içeren zemin.
- **Uzuv 2 (Krank):** Motorun doğrudan tahrik ettiği $AB$ döner kolu.
- **Uzuv 3 (Kayıcı Blok / Taş):** B pimi etrafında dönen ve kol 4 üzerinde kayan parça.
- **Uzuv 4 (Salınım Kolu):** C etrafında salınan, B'den D'ye uzanan tek parça oluklu kol (üç elemanlı rijit uzuv).
- **Uzuv 5 (Biyel):** D ile E noktalarını birbirine bağlayan $DE$ rijit çubuğu.
- **Uzuv 6 (Piston / Sürgü):** Yatay eksende doğrusal ötelenen çıkış uzvu.

---

## c) Serbestlik Derecesi (DoF / Mobility) Hesabı
Düzlemsel mekanizmalar ($\lambda = 3$) için Grübler-Kutzbach bağıntısı:
$$F = 3(l - 1) - 2 j_1 - j_2$$

- **Uzuv sayısı ($l$):** $l = 6$
- **1 Serbestlikli Mafsallar ($j_1$):**
  - Döner Mafsallar ($R$): A ($R_{12}$), B ($R_{23}$), C ($R_{14}$), D ($R_{45}$), E ($R_{56}$) $\to 5$ adet
  - Kayar Mafsallar ($P$): Taş ile Kol arası ($P_{34}$), Piston ile Şasi arası ($P_{16}$) $\to 2$ adet
  - Toplam: $j_1 = 5 + 2 = 7$
- **2 Serbestlikli Mafsal ($j_2$):** $j_2 = 0$

$$F = 3(6 - 1) - 2(7) - 0 = 15 - 14 = \mathbf{1}$$
**Fiziksel Anlamı:** Mekanizma 1 serbestlik derecelidir. Yani tek bir giriş açısı ($\theta_2$) verildiğinde tüm mekanizma parçalarının konumu, hızı ve ivmesi kesin olarak belirlenir.

**Bağımsız Devre Sayısı ($L$):**
$$L = j - l + 1 = 7 - 6 + 1 = \mathbf{2}$$
Mekanizmanın tam analizi için 2 adet bağımsız kapalı vektör devresi yazılmalıdır.

---

## d) Kinematik Zincir Çizimi
Mekanizma iki kapalı döngüden oluşan bileşik (karmaşık) bir kinematik zincirdir:
- **Döngü 1:** Uzuv 1 $\to$ Uzuv 2 $\to$ Uzuv 3 $\to$ Uzuv 4 $\to$ Uzuv 1
- **Döngü 2:** Uzuv 1 $\to$ Uzuv 4 $\to$ Uzuv 5 $\to$ Uzuv 6 $\to$ Uzuv 1
(Uzuv 1 ve Uzuv 4 her iki döngüde de ortak elemandır).

---

## e) Konum Parametreleri
- **Girdi (Bağımsız) Parametre:**
  - $\theta_2$: Krank açısı (yatay $x$ ekseninden saatin tersi yönünde pozitif, $\theta_2 = 120^\circ$).
- **Bilinmeyen (Bağımlı) Konum Değişkenleri:**
  - $s_3$: Kol 4 üzerinde B taşının C pivotuna olan değişken kayma mesafesi.
  - $\theta_4$: Salınım kolu 4'ün yatay eksenle yaptığı açı.
  - $\theta_5$: Biyel çubuğu 5'in yatay eksenle yaptığı açı.
  - $s_6$: E pistonunun C noktasına göre yatay ötelenme mesafesi.

---

## f) Vektör Devre Denklemleri (Euler Formu)
Kapalı devre kuralı: $\sum \vec{r}_i = \vec{0}$

### 1. Devre (Krank - Taş - Kol Devresi):
$$\vec{r}_{AB} + \vec{r}_{BC} + \vec{r}_{CA} = \vec{0}$$
$$\mathbf{28 e^{i\theta_2} + s_3 e^{i\theta_4} - 32 i = 0}$$
*(Burada $\vec{r}_{CA} = -32 i$, çünkü C noktası A'nın $32\text{ mm}$ tam üzerindedir; C'den A'ya iniş $-32\hat{j}$'dir).*

### 2. Devre (Kol - Biyel - Piston Devresi):
$$\vec{r}_{CD} + \vec{r}_{DE} + \vec{r}_{EC} = \vec{0}$$
$$\mathbf{38 e^{i\theta_4} + 41 e^{i\theta_5} - s_6 = 0}$$
*(Burada $\vec{r}_{EC} = -s_6$, çünkü piston yatay eksende C'ye göre $s_6$ mesafesindedir).*

---

## g) Skaler Konum Denklemleri
$e^{i\theta} = \cos\theta + i\sin\theta$ dönüşümüyle reel ($x$) ve sanal ($y$) bileşenler:

### 1. Devre:
$$f_1(s_3, \theta_4) = 28 \cos\theta_2 + s_3 \cos\theta_4 = 0$$
$$f_2(s_3, \theta_4) = 28 \sin\theta_2 + s_3 \sin\theta_4 - 32 = 0$$

### 2. Devre:
$$g_1(\theta_5, s_6) = 38 \cos\theta_4 + 41 \cos\theta_5 - s_6 = 0$$
$$g_2(\theta_5, s_6) = 38 \sin\theta_4 + 41 \sin\theta_5 = 0$$

---

## h) $\theta_2 = 120^\circ$ İçin Sayısal Konum Değerleri

### 1. Devrenin Çözümü:
$$s_3 \cos\theta_4 = -28 \cos(120^\circ) = -28(-0.5) = +14.0000\text{ mm}$$
$$s_3 \sin\theta_4 = 32 - 28 \sin(120^\circ) = 32 - 24.2487 = +7.7513\text{ mm}$$

Kareleri toplayıp karekök alırsak:
$$s_3 = \sqrt{14.0000^2 + 7.7513^2} = \mathbf{16.0026\text{ mm}}$$

Açıyı bulmak için oranlarsak:
$$\tan\theta_4 = \frac{7.7513}{14.0000} = 0.55366 \implies \mathbf{\theta_4 = 28.9717^\circ} \quad (0.5057\text{ rad})$$

### 2. Devrenin Çözümü:
$$41 \sin\theta_5 = -38 \sin(28.9717^\circ) = -18.4063\text{ mm}$$
$$\sin\theta_5 = -\frac{18.4063}{41} = -0.4489 \implies \mathbf{\theta_5 = -26.6754^\circ} \quad (\text{veya } 333.3246^\circ)$$

Pistonun yatay konumu $s_6$:
$$s_6 = 38 \cos(28.9717^\circ) + 41 \cos(-26.6754^\circ) = 33.2427 + 36.6381 = \mathbf{69.8808\text{ mm}}$$

---

## ı) İteratif Yöntem (Newton-Raphson ve Jacobian Matrisi)
Analitik çözülemeyen veya bilgisayar destekli simülasyonlarda kullanılan iterasyon algoritması:
$$\vec{x}^{(k+1)} = \vec{x}^{(k)} - \mathbf{J}^{-1} \vec{f}(\vec{x}^{(k)})$$

**1. Devre için Jacobian Matrisi $\mathbf{J}_1$:**
$$\vec{x}_1 = \begin{bmatrix} s_3 \\ \theta_4 \end{bmatrix}, \quad \vec{f}_1 = \begin{bmatrix} 28 \cos\theta_2 + s_3 \cos\theta_4 \\ 28 \sin\theta_2 + s_3 \sin\theta_4 - 32 \end{bmatrix}$$
$$\mathbf{J}_1 = \begin{bmatrix} \frac{\partial f_1}{\partial s_3} & \frac{\partial f_1}{\partial \theta_4} \\ \frac{\partial f_2}{\partial s_3} & \frac{\partial f_2}{\partial \theta_4} \end{bmatrix} = \begin{bmatrix} \cos\theta_4 & -s_3 \sin\theta_4 \\ \sin\theta_4 & s_3 \cos\theta_4 \end{bmatrix}$$
Determinantı: $\det(\mathbf{J}_1) = s_3 (\cos^2\theta_4 + \sin^2\theta_4) = s_3$.

**2. Devre için Jacobian Matrisi $\mathbf{J}_2$:**
$$\vec{x}_2 = \begin{bmatrix} \theta_5 \\ s_6 \end{bmatrix}, \quad \mathbf{J}_2 = \begin{bmatrix} -41 \sin\theta_5 & -1 \\ 41 \cos\theta_5 & 0 \end{bmatrix}$$

---

## i) Hız Denklemleri (Zamana Göre 1. Türev)
Konum denklemlerinin zamana ($t$) göre türevi alınır:

### 1. Devre:
$$-28 \omega_2 \sin\theta_2 + \dot{s}_3 \cos\theta_4 - s_3 \omega_4 \sin\theta_4 = 0$$
$$28 \omega_2 \cos\theta_2 + \dot{s}_3 \sin\theta_4 + s_3 \omega_4 \cos\theta_4 = 0$$

Matris formunda (katsayılar matrisi doğrudan Jacobian $\mathbf{J}_1$'dir):
$$\begin{bmatrix} \cos\theta_4 & -s_3 \sin\theta_4 \\ \sin\theta_4 & s_3 \cos\theta_4 \end{bmatrix} \begin{bmatrix} \dot{s}_3 \\ \omega_4 \end{bmatrix} = \begin{bmatrix} 28 \omega_2 \sin\theta_2 \\ -28 \omega_2 \cos\theta_2 \end{bmatrix}$$

### 2. Devre:
$$-38 \omega_4 \sin\theta_4 - 41 \omega_5 \sin\theta_5 - \dot{s}_6 = 0$$
$$38 \omega_4 \cos\theta_4 + 41 \omega_5 \cos\theta_5 = 0$$

---

## j) Hız Değişkenlerinin Giriş Hızı ($\omega_2$) Cinsinden Değerleri

Matris tersiyle 1. devrenin çözümü:
$$\dot{s}_3 = 28 \omega_2 \sin(\theta_2 - \theta_4)$$
$$\omega_4 = \frac{28 \omega_2 \cos(\theta_2 - \theta_4)}{s_3} \cdot (-1) \implies \omega_4 = -\frac{28 \omega_2 \cos(\theta_2 - \theta_4)}{s_3}$$
$\theta_2 - \theta_4 = 120^\circ - 28.9717^\circ = 91.0283^\circ$ olduğundan:
- $\mathbf{\dot{s}_3 = +27.9955 \, \omega_2\text{ mm/s}}$ (Taş, C pivotundan uzaklaşma yönünde kaymaktadır)
- $\mathbf{\omega_4 = +0.0314 \, \omega_2\text{ rad/s}}$ (Kol 4 saat yönünün tersine yavaşça dönmektedir)

2. devrenin çözümü:
$$\omega_5 = -\frac{38 \cos\theta_4}{41 \cos\theta_5} \omega_4 = -\frac{38 \cos(28.9717^\circ)}{41 \cos(-26.6754^\circ)} (0.0314 \omega_2) = \mathbf{-0.0285 \, \omega_2\text{ rad/s}}$$
$$\dot{s}_6 = -38 \omega_4 \sin\theta_4 - 41 \omega_5 \sin\theta_5 = \mathbf{-1.1024 \, \omega_2\text{ mm/s}}$$
*(Piston sola doğru $\sim 1.1 \, \omega_2\text{ mm/s}$ hızla ilerlemektedir).*

---

## k) İvme Denklemleri ve CORİOLİS İvmesi Analizi
Hız denklemlerinin bir kez daha zamana göre türevi alınır. Motor sabit hızla döndüğü için **$\alpha_2 = \dot{\omega}_2 = 0$**'dır.

### 1. Devrenin İkinci Türevi:
- $x$ bileşeni:
  $$-28 \omega_2^2 \cos\theta_2 + \ddot{s}_3 \cos\theta_4 - \dot{s}_3 \omega_4 \sin\theta_4 - \dot{s}_3 \omega_4 \sin\theta_4 - s_3 \alpha_4 \sin\theta_4 - s_3 \omega_4^2 \cos\theta_4 = 0$$
- $y$ bileşeni:
  $$-28 \omega_2^2 \sin\theta_2 + \ddot{s}_3 \sin\theta_4 + \dot{s}_3 \omega_4 \cos\theta_4 + \dot{s}_3 \omega_4 \cos\theta_4 + s_3 \alpha_4 \cos\theta_4 - s_3 \omega_4^2 \sin\theta_4 = 0$$

### Coriolis İvmesinin Doğuşu:
Türevde iki adet $\dot{s}_3 \omega_4$ terimi toplanarak **$2 \dot{s}_3 \omega_4$** haline gelir.  
Bu terim **Coriolis İvmesidir ($a_c = 2 \vec{\omega}_4 \times \vec{v}_{rel}$)**!
- **Koşul:** Kol 4 dönerken ($\omega_4 \ne 0$), taş 3 bu dönen kol boyunca kaymaktadır ($\dot{s}_3 \ne 0$). Bu iki hareket aynı anda varsa Coriolis ivmesi zorunlu olarak doğar!

Matris formuna getirirsek:
$$\begin{bmatrix} \cos\theta_4 & -s_3 \sin\theta_4 \\ \sin\theta_4 & s_3 \cos\theta_4 \end{bmatrix} \begin{bmatrix} \ddot{s}_3 \\ \alpha_4 \end{bmatrix} = \begin{bmatrix} 28 \omega_2^2 \cos\theta_2 + s_3 \omega_4^2 \cos\theta_4 + 2 \dot{s}_3 \omega_4 \sin\theta_4 \\ 28 \omega_2^2 \sin\theta_2 + s_3 \omega_4^2 \sin\theta_4 - 2 \dot{s}_3 \omega_4 \cos\theta_4 \end{bmatrix}$$

### 2. Devrenin İkinci Türevi:
$$-38 \alpha_4 \sin\theta_4 - 38 \omega_4^2 \cos\theta_4 - 41 \alpha_5 \sin\theta_5 - 41 \omega_5^2 \cos\theta_5 - \ddot{s}_6 = 0$$
$$38 \alpha_4 \cos\theta_4 - 38 \omega_4^2 \sin\theta_4 + 41 \alpha_5 \cos\theta_5 - 41 \omega_5^2 \sin\theta_5 = 0$$

Buradan $\alpha_4$ ve $\ddot{s}_3$ bilindiği için $\alpha_5$ ve $\ddot{s}_6$ (pistonun ivmesi) doğrudan tek adımda hesaplanır.
