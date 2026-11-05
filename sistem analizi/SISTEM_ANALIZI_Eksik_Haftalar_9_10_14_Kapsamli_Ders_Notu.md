# MAK 3131 - Sistem Dinamiği ve Kontrol
## Eksik Haftalar (9, 10, 14) Kapsamlı Referans Ders Notu ve Çözümlü Problemler

**Kaynak Referanslar:** 
- Katsuhiko Ogata, *Modern Control Engineering*, 5th Ed., Prentice Hall.
- Richard C. Dorf & Robert H. Bishop, *Modern Control Systems*, 12th Ed., Pearson.
- Gene F. Franklin, J. David Powell, Abbas Emami-Naeini, *Feedback Control of Dynamic Systems*, 7th Ed.

---

## 1. Hafta 9: Zaman Tanım Alanı Geçici Hal ve Kararlı Hal Cevabı (Transient & Steady-State Response)

Kontrol sistemlerinin dinamik davranışı ve performansı standart test girişlerine (basamak, rampa, darbe/impuls) verilen zaman cevabı ile ölçülür.

### 1.1. Birinci Dereceden Sistemler (First-Order Systems)
Genel transfer fonksiyonu:
$$G(s) = \frac{C(s)}{R(s)} = \frac{K}{\tau s + 1}$$
Burada $\tau$ sistemin zaman sabitidir (time constant), $K$ ise statik kazançtır (DC gain).

- **Birim Basamak Girişi [$R(s) = 1/s$]:**
  $$C(s) = \frac{1}{s(\tau s + 1)} = \frac{1}{s} - \frac{\tau}{\tau s + 1} = \frac{1}{s} - \frac{1}{s + 1/\tau}$$
  Zaman tanım alanında:
  $$c(t) = 1 - e^{-t/\tau} \quad (t \ge 0)$$
- **Kritik Zaman Noktaları:**
  - $t = \tau \rightarrow c(\tau) = 1 - e^{-1} \approx 0.632$ (%63.2)
  - $t = 2\tau \rightarrow c(2\tau) = 1 - e^{-2} \approx 0.865$ (%86.5)
  - $t = 3\tau \rightarrow c(3\tau) = 1 - e^{-3} \approx 0.950$ (%95.0)
  - $t = 4\tau \rightarrow c(4\tau) = 1 - e^{-4} \approx 0.982$ (%98.2 - %2 tolerans bandına giriş)

---

### 1.2. İkinci Dereceden Standart Sistemler (Standard Second-Order Systems)
Standart kapalı çevrim transfer fonksiyonu:
$$\frac{C(s)}{R(s)} = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$
Burada:
- $\omega_n$: Sönümsüz doğal frekans (undamped natural frequency, rad/s)
- $\zeta$: Sönüm oranı (damping ratio, boyutsuz)

Karakteristik denklemin kökleri (kutuplar):
$$s_{1,2} = -\zeta\omega_n \pm \omega_n \sqrt{\zeta^2 - 1} = -\sigma \pm j\omega_d$$
Burada $\sigma = \zeta\omega_n$ (sönüm faktörü), $\omega_d = \omega_n \sqrt{1 - \zeta^2}$ (sönümlü doğal frekans).

#### Sönüm Rejimleri:
1. **Sönümsüz ($\zeta = 0$):** $s_{1,2} = \pm j\omega_n$. Saf sanal kutuplar; sistem sonsuza kadar $\omega_n$ frekansında sinüzoidal salınım yapar.
2. **Eksik Sönümlü ($0 < \zeta < 1$):** Karmaşık eşlenik kutuplar ($s_{1,2} = -\sigma \pm j\omega_d$). Salınımlı fakat sönümlenen basamak cevabı. Çoğu kontrol sisteminin hedef çalışma bölgesidir.
3. **Kritik Sönümlü ($\zeta = 1$):** Çakışık gerçek kutuplar ($s_{1,2} = -\omega_n$). Aşmasız (overshoot olmadan) en hızlı cevaptır.
4. **Aşırı Sönümlü ($\zeta > 1$):** İki farklı negatif gerçek kutup. Salınımsız ve hantal, yavaş basamak cevabı.

---

### 1.3. Eksik Sönümlü Sistemlerin Performans Kriterleri ($0 < \zeta < 1$)
Birim basamak cevabı:
$$c(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1 - \zeta^2}} \sin(\omega_d t + \beta), \quad \beta = \tan^{-1}\left(\frac{\sqrt{1 - \zeta^2}}{\zeta}\right)$$

1. **Yükselme Zamanı ($t_r$ - Rise Time):** Çıkışın nihai değerinin %10'undan %90'ına (veya %0'dan %100'üne) çıkması için geçen süre:
   $$t_r = \frac{\pi - \beta}{\omega_d}$$
2. **Tepe Zamanı ($t_p$ - Peak Time):** Çıkışın ilk yerel maksimum tepeye ulaştığı an ($dc/dt = 0$):
   $$t_p = \frac{\pi}{\omega_d} = \frac{\pi}{\omega_n \sqrt{1 - \zeta^2}}$$
3. **Maksimum Aşma Yüzdesi ($\%M_p$ - Maximum Percent Overshoot):** Çıkışın nihai değeri ne kadar aştığının yüzdesi:
   $$M_p = \frac{c(t_p) - c(\infty)}{c(\infty)} = e^{-\left(\frac{\pi\zeta}{\sqrt{1 - \zeta^2}}\right)}$$
   $$\%M_p = 100 \cdot e^{-\left(\frac{\pi\zeta}{\sqrt{1 - \zeta^2}}\right)}$$
   *Ters formül (istenilen aşmadan sönüm oranını bulma):*
   $$\zeta = \frac{-\ln(M_p)}{\sqrt{\pi^2 + \ln^2(M_p)}}$$
4. **Yerleşme Zamanı ($t_s$ - Settling Time):** Çıkışın nihai değer etrafındaki tolerans bandı içine girip bir daha çıkmaması için geçen süre:
   - **%2 Tolerans Bandı:** $t_s \approx \frac{4}{\zeta\omega_n} = \frac{4}{\sigma}$
   - **%5 Tolerans Bandı:** $t_s \approx \frac{3}{\zeta\omega_n} = \frac{3}{\sigma}$

---

## 2. Hafta 10: Temel Kontrol Etkileri, Blok Diyagramları ve Mason Formülü

### 2.1. Endüstriyel Kontrol Etkileri (P, I, D)
Hata sinyali: $e(t) = r(t) - y(t)$. Kontrolör çıkışı: $u(t)$.

1. **Oransal Kontrolör (P - Proportional):**
   $$u(t) = K_p e(t) \quad \Longrightarrow \quad G_c(s) = K_p$$
   - Yükselme zamanını azaltır, sistemi hızlandırır.
   - Tipik sistemlerde kalıcı hal hatasını tamamen yok edemez, azaltır. Aşırı kazanç kararsızlığa yol açabilir.
2. **İntegral Kontrolör (I - Integral):**
   $$u(t) = K_i \int_0^t e(\tau) d\tau \quad \Longrightarrow \quad G_c(s) = \frac{K_i}{s}$$
   - Sistemin tipini 1 artırır; basamak girişinde kalıcı hal hatasını ($e_{ss}$) sıfıra indirir.
   - Sisteme orijinde kutup eklediği için kararlılık payını azaltır, aşmayı artırır.
3. **Türevsel Kontrolör (D - Derivative):**
   $$u(t) = K_d \frac{de(t)}{dt} \quad \Longrightarrow \quad G_c(s) = K_d s$$
   - Hatanın değişim hızını sezip önceden frenleme etkisi yapar.
   - Sönümü artırır, aşmayı azaltır, yerleşme zamanını kısaltır. Yüksek frekanslı ölçüm gürültülerini yükseltir; tek başına kullanılamaz.
4. **PID Kontrolör (Proportional-Integral-Derivative):**
   $$u(t) = K_p e(t) + K_i \int_0^t e(\tau) d\tau + K_d \frac{de(t)}{dt} = K_p \left[ e(t) + \frac{1}{T_i} \int_0^t e(\tau) d\tau + T_d \frac{de(t)}{dt} \right]$$
   $$G_c(s) = K_p + \frac{K_i}{s} + K_d s = \frac{K_d s^2 + K_p s + K_i}{s}$$

---

### 2.2. Blok Diyagramı İndirgeme Kuralları
- **Seri (Kaskat) Bağlantı:** $G_{es}(s) = G_1(s) \cdot G_2(s)$
- **Paralel Bağlantı:** $G_{es}(s) = G_1(s) \pm G_2(s)$
- **Geri Besleme Çevrimi (Negatif Feedback):**
  $$T(s) = \frac{C(s)}{R(s)} = \frac{G(s)}{1 + G(s)H(s)}$$
  *(Pozitif geri beslemede paydadaki işaret $-$ olur).*
- **Toplama Noktasını Bloğun Önüne/Arkasına Taşıma:**
  - Bir bloğun ($G$) sonrasından öncesine taşıma: Geri besleme koluna $1/G$ eklenir.
  - Bir bloğun ($G$) öncesinden sonrasına taşıma: Koldaki sinyal $G$ ile çarpılır.

---

### 2.3. Mason Kazanç Formülü (Mason's Gain Formula)
Karmaşık sinyal akış çizgeleri (Signal Flow Graph - SFG) için genel kazanç bağıntısı:
$$P = \frac{C(s)}{R(s)} = \frac{\sum_{k} P_k \Delta_k}{\Delta}$$
Burada:
- $P_k$: $k$. ileri yolun (forward path) kazancı (girişten çıkışa hiçbir düğümden iki kez geçmeyen yol).
- $\Delta$: Sistemin determinantı:
  $$\Delta = 1 - \sum L_a + \sum L_b L_c - \sum L_d L_e L_f + \dots$$
  - $\sum L_a$: Tüm tekil geri besleme çevrim kazançlarının toplamı.
  - $\sum L_b L_c$: Birbirine temas etmeyen (ortak düğümü bulunmayan) ikişerli çevrim kombinasyonlarının kazanç çarpımlarının toplamı.
  - $\sum L_d L_e L_f$: Birbirine temas etmeyen üçerli çevrimlerin çarpımlarının toplamı.
- $\Delta_k$: $k$. ileri yola temas etmeyen çevrimler hesaba katılarak $\Delta$ formülünden hesaplanan alt determinant.

---

## 3. Hafta 14: Kararlılık Analizi (Routh-Hurwitz) ve Köklerin Yer Eğrisi (Root Locus)

### 3.1. Routh-Hurwitz Kararlılık Kriteri
Kapalı çevrim karakteristik denklemi:
$$q(s) = a_n s^n + a_{n-1} s^{n-1} + \dots + a_1 s + a_0 = 0$$

- **Gerekli Koşul (Stodola Koşulu):** Tüm $a_i$ katsayıları mevcut ve aynı işaretli olmalıdır. Katsayılardan biri eksik veya zıt işaretli ise sistem kesinlikle kararsızdır veya sınırda kararlıdır.
- **Routh Tablosu Kurulumu:**
  $$\begin{array}{c|ccc}
  s^n & a_n & a_{n-2} & a_{n-4} & \dots \\
  s^{n-1} & a_{n-1} & a_{n-3} & a_{n-5} & \dots \\
  s^{n-2} & b_1 & b_2 & b_3 & \dots \\
  s^{n-3} & c_1 & c_2 & c_3 & \dots \\
  \vdots & \vdots & \vdots & \vdots & \ddots
  \end{array}$$
  Katsayı formülleri:
  $$b_1 = \frac{a_{n-1} a_{n-2} - a_n a_{n-3}}{a_{n-1}}, \quad b_2 = \frac{a_{n-1} a_{n-4} - a_n a_{n-5}}{a_{n-1}}$$
  $$c_1 = \frac{b_1 a_{n-3} - a_{n-1} b_2}{b_1}, \quad c_2 = \frac{b_1 a_{n-5} - a_{n-1} b_3}{b_1}$$
- **Kararlılık Kuralı:** Routh tablosunun **birinci sütunundaki işaret değişim sayısı**, karakteristik denklemin sağ yarı s-düzleminde ($Re\{s\} > 0$) bulunan kararsız köklerinin sayısına eşittir. Sistemin kararlı olması için **birinci sütundaki tüm elemanlar pozitif (aynı işaretli)** olmalıdır.

#### Özel Durumlar:
1. **İlk elemanın sıfır olması:** $b_1 = 0$ iken satırda sıfırdan farklı başka eleman varsa, sıfır yerine çok küçük pozitif bir $\epsilon > 0$ yazılarak tablo devam ettirilir ve $\epsilon \to 0$ limiti incelenir. Alternatif olarak $s = 1/z$ değişken dönüşümü yapılır.
2. **Bütün bir satırın sıfır olması:** Bu durum imajiner eksende simetrik kutupların ($\pm j\omega$) varlığını gösterir. Bir önceki satırdaki katsayılardan yardımcı polinom $A(s)$ kurulur, türevi $dA(s)/ds$ alınarak sıfır satırının yerine yazılır.

---

### 3.2. Köklerin Yer Eğrisi (Root Locus) Çizim Esasları
Karakteristik denklem: $1 + K G(s)H(s) = 0 \Longleftrightarrow G(s)H(s) = -\frac{1}{K}$.
- **Genlik Koşulu:** $|G(s)H(s)| = \frac{1}{K}$
- **Açı Koşulu:** $\angle G(s)H(s) = \pm 180^\circ (2k + 1), \quad k = 0, 1, 2, \dots$

#### Temel Çizim Kuralları:
1. **Dal Sayısı:** Açık çevrim kutup sayısı $n$, sıfır sayısı $m$ ise eğrinin dal sayısı $n$'dir ($n \ge m$).
2. **Başlangıç ve Bitiş:** Kök eğrileri $K = 0$ iken açık çevrim kutuplarından başlar; $K \to \infty$ iken $m$ tanesi açık çevrim sıfırlarında biter, geriye kalan $n - m$ dal ise sonsuza gider.
3. **Reel Eksen Üzerindeki Bölümler:** Reel eksen üzerindeki herhangi bir noktanın sağında kalan toplam kutup ve sıfır sayısı **tek** ise o nokta kök eğrisi üzerindedir.
4. **Asimptotlar ($n > m$):** Sonsuza giden $n - m$ dalın asimptot açıları:
   $$\theta_a = \frac{(2k + 1) 180^\circ}{n - m}, \quad k = 0, 1, \dots, (n - m - 1)$$
   Asimptotların reel ekseni kestiği merkez nokta ($\sigma_a$):
   $$\sigma_a = \frac{\sum (\text{Kutuplar}) - \sum (\text{Sıfırlar})}{n - m}$$
5. **Ayrılma ve Birleşme Noktaları (Breakaway / Break-in Points):** Karakteristik denklemden $K$ çekilip reel eksene göre türevi sıfıra eşitlenir:
   $$\frac{dK}{ds} = 0$$
6. **Sanal Ekseni Kesme Noktaları:** Routh tablosundaki sıfır satırı analizi veya $s = j\omega$ konularak reel ve sanal kısımlar ayrı ayrı sıfıra eşitlenerek bulunur.

---

## 4. Detaylı Çözümlü Problemler

### Problem 1: İkinci Dereceden Mekanik Sistemin Zaman Cevabı Analizi
Bir servomekanizmanın kapalı çevrim transfer fonksiyonu aşağıda verilmiştir:
$$T(s) = \frac{C(s)}{R(s)} = \frac{25}{s^2 + 6s + 25}$$
Bu sisteme birim basamak girişi uygulandığında:
a) Sönümsüz doğal frekans ($\omega_n$), sönüm oranı ($\zeta$) ve sönümlü doğal frekans ($\omega_d$) nedir?
b) Tepe zamanı ($t_p$), maksimum aşma yüzdesi ($\%M_p$), yükselme zamanı ($t_r$) ve %2 tolerans bandına göre yerleşme zamanını ($t_s$) hesaplayınız.

**Çözüm:**
a) Standart payda: $s^2 + 2\zeta\omega_n s + \omega_n^2 = s^2 + 6s + 25$
- $\omega_n^2 = 25 \Longrightarrow \omega_n = 5\text{ rad/s}$
- $2\zeta\omega_n = 6 \Longrightarrow 2\zeta(5) = 6 \Longrightarrow \zeta = 0.6$
$0 < \zeta < 1$ olduğundan sistem eksik sönümlüdür.
- $\omega_d = \omega_n \sqrt{1 - \zeta^2} = 5 \sqrt{1 - 0.6^2} = 5 \sqrt{0.64} = 5 \cdot 0.8 = 4\text{ rad/s}$.

b) Performans parametreleri:
- **Tepe Zamanı ($t_p$):**
  $$t_p = \frac{\pi}{\omega_d} = \frac{3.1416}{4} \approx 0.785\text{ s}$$
- **Maksimum Aşma ($\%M_p$):**
  $$M_p = e^{-\left(\frac{\pi \cdot 0.6}{\sqrt{1 - 0.36}}\right)} = e^{-\left(\frac{1.88496}{0.8}\right)} = e^{-2.3562} \approx 0.0948 \Longrightarrow \%M_p = 9.48\%$$
- **Yükselme Zamanı ($t_r$):**
  $$\beta = \tan^{-1}\left(\frac{\sqrt{1 - \zeta^2}}{\zeta}\right) = \tan^{-1}\left(\frac{0.8}{0.6}\right) = \tan^{-1}(1.333) \approx 0.9273\text{ rad}$$
  $$t_r = \frac{\pi - \beta}{\omega_d} = \frac{3.1416 - 0.9273}{4} = \frac{2.2143}{4} \approx 0.554\text{ s}$$
- **Yerleşme Zamanı (%2 kriteri):**
  $$t_s = \frac{4}{\zeta\omega_n} = \frac{4}{0.6 \cdot 5} = \frac{4}{3} \approx 1.333\text{ s}$$

---

### Problem 2: Mason Kazanç Formülü ile Transfer Fonksiyonu Çıkarımı
Aşağıdaki çevrim ve ileri yollara sahip bir geri beslemeli sistem verilmiştir:
- İleri Yol: $P_1 = G_1 G_2 G_3$ (Girişten çıkışa)
- Geri Besleme Çevrimleri:
  - $L_1 = -G_1 H_1$
  - $L_2 = -G_2 H_2$
  - $L_3 = -G_3 H_3$
  $L_1$ ve $L_3$ çevrimleri ortak bir düğüme sahip değildir (temassız çevrimlerdir). $L_2$ ise hem $L_1$ hem de $L_3$ ile ortak düğüme sahiptir.
Sistemin kapalı çevrim transfer fonksiyonunu $C(s)/R(s)$ bulunuz.

**Çözüm:**
1. İleri yol kazancı: $P_1 = G_1 G_2 G_3$.
2. Çevrim kazançları: $L_1 = -G_1 H_1$, $L_2 = -G_2 H_2$, $L_3 = -G_3 H_3$.
3. Temassız çevrimler: Yalnızca $L_1$ ve $L_3$ birbirine temas etmemektedir:
   $$L_1 L_3 = (-G_1 H_1)(-G_3 H_3) = G_1 G_3 H_1 H_3$$
4. Sistemin ana determinantı ($\Delta$):
   $$\Delta = 1 - (L_1 + L_2 + L_3) + (L_1 L_3) = 1 + G_1 H_1 + G_2 H_2 + G_3 H_3 + G_1 G_3 H_1 H_3$$
5. İleri yola temas etmeyen çevrim: $P_1$ ileri yolu bütün düğümlerden geçtiği için hiçbir çevrim temassız kalamaz. Dolayısıyla:
   $$\Delta_1 = 1 - 0 = 1$$
6. Mason formülü:
   $$\frac{C(s)}{R(s)} = \frac{P_1 \Delta_1}{\Delta} = \frac{G_1 G_2 G_3}{1 + G_1 H_1 + G_2 H_2 + G_3 H_3 + G_1 G_3 H_1 H_3}$$

---

### Problem 3: Routh-Hurwitz ile Kararlılık Sınırı ve Salınım Frekansı
Açık çevrim transfer fonksiyonu $G(s) = \frac{K}{s(s + 3)(s + 5)}$ ve $H(s) = 1$ olan bir birlik geri beslemeli sistem verilmiştir.
a) Sistemin kararlı kalmasını sağlayan $K$ kazanç aralığını belirleyiniz.
b) Sistemin sınırda kararlı olduğu andaki kritik $K_{kr}$ kazancını ve sürekli salınım frekansını ($\omega$) bulunuz.

**Çözüm:**
a) Karakteristik denklem: $1 + G(s)H(s) = 0$
$$s(s + 3)(s + 5) + K = 0 \Longrightarrow s(s^2 + 8s + 15) + K = 0 \Longrightarrow s^3 + 8s^2 + 15s + K = 0$$
Routh tablosunu kuralım:
$$\begin{array}{c|cc}
s^3 & 1 & 15 \\
s^2 & 8 & K \\
s^1 & \frac{8 \cdot 15 - 1 \cdot K}{8} = \frac{120 - K}{8} & 0 \\
s^0 & K & 0
\end{array}$$

Kararlılık için birinci sütunun tamamı pozitif olmalıdır:
1. $s^1$ satırından: $\frac{120 - K}{8} > 0 \Longrightarrow 120 - K > 0 \Longrightarrow K < 120$
2. $s^0$ satırından: $K > 0$

Sistemin kararlı olma koşulu: **$0 < K < 120$**.

b) Kritik kazanç:
$K = 120$ olduğunda $s^1$ satırı sıfır olur (sınırda kararlılık).
Bir üst satırdan ($s^2$) yardımcı polinomu oluşturalım:
$$A(s) = 8s^2 + K = 8s^2 + 120 = 0$$
$$8s^2 = -120 \Longrightarrow s^2 = -\frac{120}{8} = -15 \Longrightarrow s_{1,2} = \pm j\sqrt{15} \approx \pm j 3.873\text{ rad/s}$$
Sürekli salınım frekansı: $\omega = \sqrt{15} \approx 3.873\text{ rad/s}$.

---

### Problem 4: Köklerin Yer Eğrisi (Root Locus) Detaylı Analizi
Açık çevrim transfer fonksiyonu $G(s) = \frac{K}{s(s + 2)(s + 4)}$, $H(s) = 1$ olan sistem için:
a) Kök eğrisinin asimptot açılarını ve kesişim noktasını bulunuz.
b) Reel eksenden ayrılma noktasını ($s_b$) hesaplayınız.

**Çözüm:**
a) Kutuplar: $p_1 = 0$, $p_2 = -2$, $p_3 = -4 \Longrightarrow n = 3$.
Sıfırlar: Yok ($m = 0$).
Sonsuza giden dal sayısı: $n - m = 3 - 0 = 3$.

- Asimptot açıları:
  $$\theta_a = \frac{(2k + 1)180^\circ}{3}, \quad k = 0, 1, 2$$
  - $k = 0 \rightarrow \theta_1 = 60^\circ$
  - $k = 1 \rightarrow \theta_2 = 180^\circ$
  - $k = 2 \rightarrow \theta_3 = 300^\circ = -60^\circ$
- Asimptot merkezi:
  $$\sigma_a = \frac{\sum p_i - \sum z_i}{n - m} = \frac{(0 - 2 - 4) - 0}{3} = \frac{-6}{3} = -2$$

b) Reel eksen bölgeleri:
$[-2, 0]$ aralığında sağdaki kutup sayısı 1 (tek) olduğundan kök eğrisi mevcuttur. $[-4, -2]$ aralığında sağdaki kutup sayısı 2 (çift) olduğundan kök eğrisi yoktur. $(-\infty, -4]$ aralığında sağdaki kutup sayısı 3 (tek) olduğundan kök eğrisi mevcuttur.
Bu nedenle 0 ve -2 kutuplarından çıkan dallar birbiriyle karşılaşarak ayrılma (breakaway) noktası oluşturacaktır.

Karakteristik denklemden $K$'yı çekelim:
$$s(s^2 + 6s + 8) + K = 0 \Longrightarrow K = -(s^3 + 6s^2 + 8s)$$
Ayrılma noktası için türevi sıfıra eşitleyelim:
$$\frac{dK}{ds} = -(3s^2 + 12s + 8) = 0 \Longrightarrow 3s^2 + 12s + 8 = 0$$
İkinci derece denklem çözümü:
$$s = \frac{-12 \pm \sqrt{144 - 4 \cdot 3 \cdot 8}}{2 \cdot 3} = \frac{-12 \pm \sqrt{144 - 96}}{6} = \frac{-12 \pm \sqrt{48}}{6} = \frac{-12 \pm 6.9282}{6}$$
- $s_1 = \frac{-12 + 6.9282}{6} = \frac{-5.0718}{6} \approx -0.845$
- $s_2 = \frac{-12 - 6.9282}{6} = \frac{-18.9282}{6} \approx -3.155$

Kök eğrisinin reel eksen parçası $[-2, 0]$ arasında olduğu için geçerli ayrılma noktası:
$$s_b = -0.845$$
($s_2 = -3.155$ noktası kök eğrisi üzerinde yer almayan bölgededir, elenir).
Ayrılma noktasındaki kazanç:
$$K_b = -((-0.845)^3 + 6(-0.845)^2 + 8(-0.845)) = -(-0.6035 + 4.2842 - 6.76) = -(-3.0793) \approx 3.079 > 0$$
Bu sonuç ayrılma noktasının fiziksel olarak geçerli olduğunu doğrular.
