# ENG 3120 - Mühendislik İstatistiği
## Eksik Müfredat (Hafta 6 - 15) Kapsamlı Referans Ders Notu ve Çözümlü Problemler

**Kaynak Referanslar:**
- Ronald E. Walpole, Raymond H. Myers, Sharon L. Myers, Keying Ye, *Probability & Statistics for Engineers & Scientists*, 9th Ed., Pearson.
- Douglas C. Montgomery, George C. Runger, *Applied Statistics and Probability for Engineers*, 6th Ed., Wiley.

---

## 1. Kesikli Olasılık Dağılımları (Hafta 6-7)

Mühendislik uygulamalarında kalite kontrol muayeneleri, arıza sıklıkları, parça kusur oranları ve güvenilirlik analizlerinde kesikli rasgele değişkenler ve dağılımları kullanılır.

### 1.1. Binom Dağılımı (Binomial Distribution)
Her denemede başarı olasılığının sabit $p$ (başarısızlık $q = 1 - p$) olduğu $n$ adet bağımsız Bernoulli denemesinde, toplam başarı sayısını ($X$) modelleyen dağılımdır:
- **Olasılık Kütle Fonksiyonu (PMF):**
  $$P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k} = \frac{n!}{k!(n - k)!} p^k q^{n - k}, \quad k = 0, 1, 2, \dots, n$$
- **Beklenen Değer (Ortalama):** $\mu = E(X) = n \cdot p$
- **Varyans:** $\sigma^2 = \text{Var}(X) = n \cdot p \cdot (1 - p)$
- **Standart Sapma:** $\sigma = \sqrt{n \cdot p \cdot q}$

---

### 1.2. Poisson Dağılımı
Belirli bir zaman diliminde, hacimde veya yüzey alanında nadir gerçekleşen olayların sayısını modeller (örneğin döküm yüzeyindeki gözenek sayısı, kaynak dikişindeki mikro çatlak sayısı, boru hattı kaçakları). Birim aralıktaki ortalama frekans $\lambda$'dır:
- **Olasılık Kütle Fonksiyonu:**
  $$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \dots \quad (e \approx 2.71828)$$
- **Beklenen Değer ve Varyans:** $E(X) = \text{Var}(X) = \lambda$
- **Poisson Yaklaşımı (Binom ile ilişkisi):** $n \ge 50$ ve $p \le 0.10$ koşullarında Binom dağılımı, $\lambda = n \cdot p$ parametreli Poisson dağılımı ile mükemmel yaklaşıklık verir.

---

### 1.3. Hipergeometrik Dağılım
Toplam $N$ elemanlı sınırlı bir partiden (içinde $k$ adet hatalı parça bulunan) **iadesiz (without replacement)** olarak rastgele $n$ eleman seçildiğinde, örneklemdeki hatalı parça sayısı $x$'in dağılımıdır:
- **Olasılık Fonksiyonu:**
  $$P(X = x) = \frac{\binom{k}{x} \binom{N - k}{n - x}}{\binom{N}{n}}$$
- **Ortalama ve Varyans:**
  $$\mu = n \frac{k}{N}, \quad \sigma^2 = n \frac{k}{N} \left(1 - \frac{k}{N}\right) \left(\frac{N - n}{N - 1}\right)$$
  Burada $\frac{N - n}{N - 1}$ terimi sonlu anakütle düzeltme katsayısıdır (finite population correction factor).

---

## 2. Sürekli Olasılık Dağılımları (Hafta 8)

### 2.1. Normal Dağılım (Gauss Dağılımı)
Mühendislik ölçümlerinin, boyut toleranslarının ve malzeme dayanımlarının en temel dağılımıdır. Ortalama $\mu$ ve varyans $\sigma^2$ ile belirlenir:
- **Olasılık Yoğunluk Fonksiyonu (PDF):**
  $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}, \quad -\infty < x < +\infty$$

### 2.2. Standart Normal Dağılım ve Z-Dönüşümü
Herhangi bir $X \sim N(\mu, \sigma^2)$ rasgele değişkeni, standart normal değişkene $Z \sim N(0, 1)$ dönüştürülür:
$$Z = \frac{X - \mu}{\sigma}$$
- **Olasılık Hesabı:**
  $$P(a \le X \le b) = P\left(\frac{a - \mu}{\sigma} \le Z \le \frac{b - \mu}{\sigma}\right) = \Phi(Z_b) - \Phi(Z_a)$$
- **Empirik Kural (68 - 95 - 99.7):**
  - $[\mu - \sigma, \mu + \sigma]$ aralığı: Verilerin %68.27'si
  - $[\mu - 2\sigma, \mu + 2\sigma]$ aralığı: Verilerin %95.45'i ($\pm 1.96\sigma$ tam %95.00)
  - $[\mu - 3\sigma, \mu + 3\sigma]$ aralığı: Verilerin %99.73'ü ($\pm 2.576\sigma$ tam %99.00)

### 2.3. Üstel Dağılım (Exponential Distribution)
Arızasız çalışma süresi (Time to Failure) ve güvenilirlik (reliability) analizinde kullanılır. Birim zamandaki arıza hızı $\lambda$'dır:
- **PDF ve CDF:**
  $$f(x) = \lambda e^{-\lambda x} \quad (x \ge 0), \quad F(x) = P(X \le x) = 1 - e^{-\lambda x}$$
- **Güvenilirlik (Reliability) Fonksiyonu:** $R(t) = P(X > t) = e^{-\lambda t}$
- **Ortalama Ömür (MTBF):** $\mu = \frac{1}{\lambda}$, **Varyans:** $\sigma^2 = \frac{1}{\lambda^2}$

---

## 3. Örnekleme Dağılımları ve Merkezi Limit Teoremi (Hafta 9)

Anakütleden rastgele seçilen $n$ hacimli bağımsız örneklemlerin ortalaması $\bar{X}$ da bir rasgele değişkendir:
- **Ortalama ve Standart Hata:**
  $$\mu_{\bar{X}} = \mu, \quad \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$$
- **Merkezi Limit Teoremi (CLT):** Anakütlenin dağılımı ne olursa olsun (çarpık, bimodal, üniform), örneklem hacmi yeterince büyük olduğunda ($n \ge 30$), örneklem ortalamaları dağılımı yaklaşık olarak **Normal Dağılıma** yaklaşır:
  $$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)$$

---

## 4. Güven Aralıkları (Confidence Intervals - Hafta 10-11)

Bilinmeyen anakütle parametrelerini belirli bir $(1 - \alpha)$ güven seviyesinde (%90, %95, %99) bir aralık içinde kestirme yöntemidir.

### 4.1. Tek Kitle Ortalaması ($\mu$) İçin Güven Aralığı
1. **$\sigma$ Biliniyorsa:**
   $$\bar{X} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$
2. **$\sigma$ Bilinmiyorsa ve $n < 30$ (Küçük Örneklem, Student-t Dağılımı):**
   $$\bar{X} \pm t_{\alpha/2, \nu} \cdot \frac{s}{\sqrt{n}}, \quad \nu = n - 1 \text{ serbestlik derecesi}$$
3. **$\sigma$ Bilinmiyorsa fakat $n \ge 30$ (Büyük Örneklem):**
   $$\bar{X} \pm Z_{\alpha/2} \cdot \frac{s}{\sqrt{n}}$$

### 4.2. İki Kitle Ortalamasının Farkı ($\mu_1 - \mu_2$) İçin Güven Aralığı
- **Varyanslar Bilinmiyor ama Eşit Kabul Ediliyorsa ($\sigma_1^2 = \sigma_2^2$):**
  Ortak varyans (pooled variance):
  $$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$
  Güven Aralığı:
  $$(\bar{X}_1 - \bar{X}_2) \pm t_{\alpha/2, \nu} \cdot s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}, \quad \nu = n_1 + n_2 - 2$$

---

## 5. Hipotez Testleri (Hypothesis Testing - Hafta 12-13)

- **Sıfır Hipotezi ($H_0$):** Farkın veya etkinin olmadığını savunan temel kabul ($H_0: \mu = \mu_0$). Eşitlik her zaman $H_0$'da yer alır.
- **Alternatif Hipotez ($H_1$):** İspatlanmaya çalışılan iddia ($H_1: \mu \neq \mu_0$ [çift yönlü], $\mu > \mu_0$ [sağ kuyruk], $\mu < \mu_0$ [sol kuyruk]).
- **Hata Tipleri:**
  - **Tip I Hata ($\alpha$):** $H_0$ doğru iken reddetme riski (Anlamlılık düzeyi).
  - **Tip II Hata ($\beta$):** $H_0$ yanlış iken reddedememe riski. Testin gücü = $1 - \beta$.

### Test İstatistikleri:
- $\sigma$ biliniyorsa: $Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}$
- $\sigma$ bilinmiyorsa ($n < 30$): $t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}, \quad \nu = n - 1$
- **Karar:** $|t_{\text{hesap}}| > t_{\text{kritik}}$ veya $p\text{-değeri} \le \alpha$ ise $H_0$ reddedilir.

---

## 6. Basit Doğrusal Regresyon ve Korelasyon (Hafta 14-15)

### 6.1. Pearson Korelasyon Katsayısı ($r$)
$$r = \frac{S_{xy}}{\sqrt{S_{xx} S_{yy}}}, \quad -1 \le r \le +1$$
$$S_{xx} = \sum x_i^2 - \frac{(\sum x_i)^2}{n}, \quad S_{yy} = \sum y_i^2 - \frac{(\sum y_i)^2}{n}, \quad S_{xy} = \sum x_i y_i - \frac{(\sum x_i)(\sum y_i)}{n}$$

### 6.2. En Küçük Kareler Regresyon Doğrusu
Doğru denklemi: $\hat{y} = \beta_0 + \beta_1 x$
- **Eğim ($\beta_1$):** $\beta_1 = \frac{S_{xy}}{S_{xx}}$
- **Kesişim ($\beta_0$):** $\beta_0 = \bar{y} - \beta_1 \bar{x}$
- **Belirlilik Katsayısı ($R^2$):** $R^2 = r^2$. Bağımlı değişkendeki değişimin yüzde kaçının bağımsız değişken tarafından açıklandığını ifade eder.

---

## 7. Çözümlü Mühendislik Problemleri

### Problem 1: Binom Dağılımı ile Kalite Kontrol
CNC torna tezgâhında seri üretilen pimlerin %4'ü ıskartaya ayrılmaktadır. Rastgele seçilen 15 pimlik bir partide:
a) Tam olarak 2 pimin hatalı çıkma olasılığı nedir?
b) En fazla 1 pimin hatalı çıkma olasılığı nedir?

**Çözüm:**
$n = 15$, $p = 0.04$, $q = 0.96$.
a) $P(X = 2) = \binom{15}{2} (0.04)^2 (0.96)^{13} = 105 \cdot 0.0016 \cdot 0.5882 \approx \mathbf{0.0988 \ (\%9.88)}$
b) $P(X \le 1) = P(0) + P(1) = (0.96)^{15} + 15(0.04)(0.96)^{14} = 0.5421 + 0.3388 = \mathbf{0.8809 \ (\%88.09)}$

---

### Problem 2: Döküm Kusurları ve Poisson Dağılımı
Döküm bloklarda ortalama 100 dm² yüzeyde 2.5 mikro çatlak tespit edilmektedir ($\lambda = 2.5$).
a) Hiç çatlak çıkmama olasılığı nedir?
b) 3 veya daha fazla çatlak bulunma olasılığı nedir?

**Çözüm:**
$P(X = k) = \frac{e^{-2.5} 2.5^k}{k!}$, $e^{-2.5} \approx 0.08208$.
a) $P(X = 0) = \frac{0.08208 \cdot 1}{1} = \mathbf{0.0821 \ (\%8.21)}$
b) $P(X \ge 3) = 1 - [P(0) + P(1) + P(2)] = 1 - [0.0821 + 0.2052 + 0.2565] = 1 - 0.5438 = \mathbf{0.4562 \ (\%45.62)}$

---

### Problem 3: Mil Çapı Toleransı ve Normal Dağılım
$\mu = 25.00\text{ mm}$, $\sigma = 0.05\text{ mm}$. Kabul edilebilir aralık $[24.90, 25.08]\text{ mm}$.
a) Kabul olasılığı:
$Z_1 = \frac{24.90 - 25.00}{0.05} = -2.00 \Longrightarrow \Phi(-2.00) = 0.0228$
$Z_2 = \frac{25.08 - 25.00}{0.05} = +1.60 \Longrightarrow \Phi(1.60) = 0.9452$
$P(24.90 \le X \le 25.08) = 0.9452 - 0.0228 = \mathbf{0.9224 \ (\%92.24)}$
b) 100,000 pimin içinde şartname dışı adet: $100,000 \cdot (1 - 0.9224) = \mathbf{7,760\text{ adet}}$.

---

### Problem 4: Çekme Dayanımı İçin t-Dağılımı Güven Aralığı
$n = 9$ numune: 310, 315, 320, 312, 318, 322, 314, 316, 319 MPa.
$\bar{X} = 316.22\text{ MPa}$, $s = 3.90\text{ MPa}$.
$\nu = 8$, $\alpha = 0.05 \Longrightarrow t_{0.025, 8} = 2.306$.
Standart hata: $SE = \frac{3.90}{\sqrt{9}} = 1.30\text{ MPa}$.
Hata payı: $E = 2.306 \cdot 1.30 = 3.00\text{ MPa}$.
%95 Güven Aralığı: $316.22 \pm 3.00 \Longrightarrow \mathbf{[313.22\text{ MPa}, 319.22\text{ MPa}]}$.

---

### Problem 5: Hipotez Testi (Takım Ömrü Sınaması)
Mevcut $\mu_0 = 120\text{ saat}$. $n = 25$ test numunesi: $\bar{X} = 126\text{ saat}$, $s = 12\text{ saat}$, $\alpha = 0.05$.
$H_0: \mu = 120$ vs $H_1: \mu > 120$ (sağ kuyruk).
$t_{\text{hesap}} = \frac{126 - 120}{12 / \sqrt{25}} = \frac{6}{2.4} = \mathbf{+2.50}$.
Kritik değer: $t_{0.05, 24} = 1.711$.
$t_{\text{hesap}} = 2.50 > 1.711$ olduğundan **$H_0$ REDDEDİLİR**. Yeni takım ömrü anlamlı derecede daha uzundur.

---

### Problem 6: Doğrusal Regresyon (Enjeksiyon Basıncı - Yakıt Tüketimi)
Veriler: (100, 250), (120, 240), (140, 225), (160, 215), (180, 200).
$n = 5$, $\bar{x} = 140$, $\bar{y} = 226$.
$S_{xx} = 4000$, $S_{yy} = 1570$, $S_{xy} = -2500$.
$\beta_1 = \frac{-2500}{4000} = -0.625$.
$\beta_0 = 226 - (-0.625 \cdot 140) = 313.5$.
Regresyon Denklemi: $\mathbf{\hat{y} = 313.5 - 0.625 x}$.
$r = \frac{-2500}{\sqrt{4000 \cdot 1570}} = -0.9976$, $R^2 = 0.9952$ (%99.52 açıklama oranı).
150 bar için tahmin: $\hat{y}(150) = 313.5 - 0.625(150) = \mathbf{219.75\text{ g/kWh}}$.
