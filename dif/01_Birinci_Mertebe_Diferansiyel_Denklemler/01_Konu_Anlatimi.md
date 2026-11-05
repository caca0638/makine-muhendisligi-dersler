# BÖLÜM 1: BİRİNCİ MERTEBEDEN DİFERANSİYEL DENKLEMLER
**Ders:** Diferansiyel Denklemler (MTH 2303 / Mühendislik Matematiği)  
**Kapsam:** Makine Mühendisliği Lisans Programı

---

## 1. TEMEL KAVRAMLAR VE MATEMATİKSEL SINIFLANDIRMA

### 1.1 Diferansiyel Denklemin Tanımı
Bir veya daha fazla bağımsız değişken, bir bağımlı değişken ve bu bağımlı değişkenin bağımsız değişkene göre türevlerini içeren matematiksel bağıntılara **diferansiyel denklem** denir.
- Tek bir bağımsız değişken içeriyorsa: **Adi Diferansiyel Denklem (Ordinary Differential Equation - ODE)**
- Birden fazla bağımsız değişken ve kısmi türevler içeriyorsa: **Kısmi Diferansiyel Denklem (Partial Differential Equation - PDE)**

### 1.2 Mertebe (Order) ve Derece (Degree)
* **Mertebe (Order):** Denklemde yer alan en yüksek türevin basamağıdır.
  $$\frac{d^2 y}{dx^2} + 3\left(\frac{dy}{dx}\right)^3 - 4y = 0 \quad \implies \text{Mertebe: } 2$$
* **Derece (Degree):** Diferansiyel denklem tüm türevlerine göre rasyonel ve kesirli üslerden arındırılmış polinom formuna getirildikten sonra, en yüksek mertebeli türevin sahip olduğu kuvvettir (üssüdür).
  $$\left[\frac{d^2 y}{dx^2}\right]^1 + 3\left(\frac{dy}{dx}\right)^3 - 4y = 0 \quad \implies \text{Derece: } 1$$

### 1.3 Doğrusallık (Linearity)
$n$. mertebeden bir diferansiyel denklemin genel formu:
$$a_n(x) \frac{d^n y}{dx^n} + a_{n-1}(x) \frac{d^{n-1} y}{dx^{n-1}} + \dots + a_1(x) \frac{dy}{dx} + a_0(x) y = g(x)$$
şeklinde yazılabiliyorsa bu denklem **doğrusaldır (lineerdir)**. Doğrusallık kriterleri:
1. Bağımlı değişken $y$ ve tüm türevleri ($y', y'', \dots$) yalnızca 1. dereceden olmalıdır.
2. Bağımlı değişken ve türevleri birbirleriyle çarpım halinde bulunamaz ($y \cdot y'$ veya $(y')^2$ olamaz).
3. Bağımlı değişken lineer olmayan transandant fonksiyonların (örn. $\sin(y)$, $e^y$, $\ln(y)$) argümanı olamaz.

### 1.4 Başlangıç Değer Problemi (IVP) ve Picard-Lindelöf Varlık-Teklik Teoremi
1. mertebeden bir Başlangıç Değer Problemi (Initial Value Problem):
$$\frac{dy}{dx} = f(x, y), \quad y(x_0) = y_0$$
* **Teorem (Picard-Lindelöf):**  
  Eğer $(x_0, y_0)$ noktasını içeren açık bir $R = \{(x, y) \mid |x - x_0| \le a, \, |y - y_0| \le b\}$ bölgesinde;
  1. $f(x, y)$ fonksiyonu sürekli ise,
  2. $\frac{\partial f}{\partial y}$ kısmi türevi sürekli ise,  
  bu durumda $x_0$ noktasını içeren belirli bir aralıkta problemin **tek bir (unique)** $y = \phi(x)$ çözümü mevcuttur.

---

## 2. DEĞİŞKENLERİNE AYRILABİLİR DİFERANSİYEL DENKLEMLER (SEPARABLE EQUATIONS)

### 2.1 Standart Form ve Analitik Çözüm
Eğer denklem aşağıdaki biçimde ifade edilebiliyorsa:
$$\frac{dy}{dx} = g(x) \cdot h(y) \quad \text{veya} \quad M(x) dx + N(y) dy = 0$$
Değişkenler diferansiyelleriyle birlikte ayrıştırılır:
$$\frac{1}{h(y)} \, dy = g(x) \, dx \quad (h(y) \neq 0)$$
Her iki tarafın doğrudan belirsiz integrali alınarak genel çözüm elde edilir:
$$\int \frac{1}{h(y)} \, dy = \int g(x) \, dx + C$$

*Not:* $h(y) = 0$ denklemini sağlayan $y = c$ sabitleri denklemin **tekil (singular)** veya denge (equilibrium) çözümleridir.

---

## 3. HOMOJEN DİFERANSİYEL DENKLEMLER

### 3.1 Homojenlik Tanımı
Bir $f(x, y)$ fonksiyonunda $\forall t > 0$ için $f(tx, ty) = t^k f(x, y)$ sağlanıyorsa, $f$ fonksiyonu $k$. dereceden homojendir.  
$M(x, y)dx + N(x, y)dy = 0$ denkleminde $M$ ve $N$ aynı dereceden homojen ise denklem homojen diferansiyel denklemdir ve şu formda yazılabilir:
$$\frac{dy}{dx} = F\left(\frac{y}{x}\right)$$

### 3.2 Çözüm Algoritması (Değişken Değiştirme)
$$v = \frac{y}{x} \implies y = v \cdot x \implies \frac{dy}{dx} = v + x \frac{dv}{dx}$$
Bu ifade denklemde yerine konulduğunda denklem değişkenlerine ayrılabilir hale gelir:
$$v + x \frac{dv}{dx} = F(v) \implies \frac{1}{F(v) - v} \, dv = \frac{1}{x} \, dx$$
İntegrasyon tamamlandıktan sonra $v = y/x$ geri dönüşümü uygulanır.

---

## 4. BİRİNCİ MERTEBEDEN DOĞRUSAL DİFERANSİYEL DENKLEMLER

### 4.1 Standart Form
$$\frac{dy}{dx} + P(x) y = Q(x)$$
Eğer $Q(x) = 0$ ise denklem homojendir; $Q(x) \neq 0$ ise homojen değildir.

### 4.2 İntegrasyon Çarpanı (Integrating Factor) Metodu
Denklemin her iki tarafı henüz bilinmeyen bir $\mu(x)$ fonksiyonu ile çarpılır:
$$\mu(x) \frac{dy}{dx} + \mu(x) P(x) y = \mu(x) Q(x)$$
Sol tarafın bir çarpımın türevi $\frac{d}{dx}[\mu(x) y] = \mu(x) \frac{dy}{dx} + \frac{d\mu}{dx} y$ olması şartı koşulursa:
$$\frac{d\mu}{dx} = \mu(x) P(x) \implies \frac{d\mu}{\mu} = P(x) dx \implies \mu(x) = \exp\left(\int P(x) dx\right)$$
Böylece diferansiyel denklem:
$$\frac{d}{dx}[\mu(x) \cdot y] = \mu(x) Q(x)$$
Her iki tarafın integrali alınarak **Genel Çözüm** bulunur:
$$y(x) = \frac{1}{\mu(x)} \left[ \int \mu(x) Q(x) \, dx + C \right]$$

---

## 5. TAM DİFERANSİYEL DENKLEMLER VE İNTEGRASYON ÇARPANLARI

### 5.1 Tamlık (Exactness) Kriteri
$$M(x, y) dx + N(x, y) dy = 0$$
Eğer öyle bir skaler potansiyel fonksiyonu $u(x, y)$ varsa ki:
$$du = \frac{\partial u}{\partial x} dx + \frac{\partial u}{\partial y} dy = M(x, y) dx + N(x, y) dy = 0$$
oluyorsa, bu denkleme **tam diferansiyel denklem** denir.  
Schwarz teoremine göre karışık ikinci kısmi türevlerin eşitliği ($\frac{\partial^2 u}{\partial y \partial x} = \frac{\partial^2 u}{\partial x \partial y}$):
$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$$
Bu eşitlik sağlandığı anda denklem tamdır ve genel çözüm $u(x, y) = C$ seviye eğrisidir.

### 5.2 Çözüm Adımları
1. $u(x, y) = \int M(x, y) dx + k(y)$
2. Her iki tarafın $y$'ye göre kısmi türevi alınır: $\frac{\partial u}{\partial y} = \frac{\partial}{\partial y}\left[\int M dx\right] + k'(y) = N(x, y)$
3. Buradan $k'(y)$ ve integrasyonla $k(y)$ bulunur. Genel çözüm: $u(x, y) = C$.

### 5.3 Özel İntegrasyon Çarpanı $\mu$
Eğer $\frac{\partial M}{\partial y} \neq \frac{\partial N}{\partial x}$ ise denklem tam değildir. Ancak uygun bir $\mu(x, y)$ çarpanı ile tam hale getirilebilir:
- Eğer $\frac{\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}}{N} = f(x)$ (yalnızca $x$'e bağlı) ise:
  $$\mu(x) = \exp\left(\int f(x) dx\right)$$
- Eğer $\frac{\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}}{M} = g(y)$ (yalnızca $y$'ye bağlı) ise:
  $$\mu(y) = \exp\left(\int g(y) dy\right)$$

---

## 6. ÖZEL LİNEER OLMAYAN DENKLEMLER: BERNOULLI VE RICCATI

### 6.1 Bernoulli Diferansiyel Denklemi
$$\frac{dy}{dx} + P(x) y = Q(x) y^n \quad (n \in \mathbb{R}, \, n \neq 0, 1)$$
* **Lineerleştirme Adımı:** Her iki taraf $y^n$'e bölünür:
  $$y^{-n} \frac{dy}{dx} + P(x) y^{1-n} = Q(x)$$
* **Değişken Değiştirme:** $u = y^{1-n} \implies \frac{du}{dx} = (1-n) y^{-n} \frac{dy}{dx}$
  $$\frac{1}{1-n} \frac{du}{dx} + P(x) u = Q(x) \implies \frac{du}{dx} + (1-n) P(x) u = (1-n) Q(x)$$
Bu denklem $u(x)$ değişkenine göre 1. mertebeden doğrusal bir diferansiyel denklemdir ve integrasyon çarpanı yöntemiyle çözülür.

### 6.2 Riccati Diferansiyel Denklemi
$$\frac{dy}{dx} = P(x) + Q(x) y + R(x) y^2$$
Genel analitik çözümü kapalı formda integrasyonla doğrudan bulunamaz. Ancak denklemi sağlayan bilinen bir **özel çözüm** $y_1(x)$ mevcutsa:
$$y(x) = y_1(x) + \frac{1}{u(x)} \implies \frac{dy}{dx} = y_1'(x) - \frac{1}{u^2} \frac{du}{dx}$$
Bu dönüşüm denklemi $u(x)$ için 1. mertebe lineer diferansiyel denkleme indirger:
$$\frac{du}{dx} + [Q(x) + 2 R(x) y_1(x)] u = -R(x)$$

---

## 7. MAKİNE MÜHENDİSLİĞİ FİZİKSEL UYGULAMALARI

### 7.1 Newton Soğuma Kanunu (Isıl İşlem Uygulaması)
Sıcak bir cismin çevresiyle olan ısı transferi (düşük sıcaklık farklarında taşınım baskınken):
$$\frac{dT}{dt} = -k (T(t) - T_\infty)$$
- $T(t)$: Cismin $t$ anındaki üniform sıcaklığı ($^\circ\text{C}$ veya $\text{K}$)
- $T_\infty$: Çevre ortam sıcaklığı
- $k = \frac{h A_s}{\rho V c_p} > 0$: Isıl zaman sabiti katsayısı ($\text{s}^{-1}$)
- Çözüm: $T(t) = T_\infty + (T_0 - T_\infty) e^{-k t}$

### 7.2 Viskoz Sönümlü Düşen Kütle Dinamiği (Akışkan Direnci)
Bir akışkan içinde serbest düşen $m$ kütleli parçacık:
$$m \frac{dv}{dt} = m g - c v$$
- $c$: Viskoz sönüm (sürüklenme) katsayısı ($\text{N}\cdot\text{s/m}$)
- Limit hız (terminal velocity): $\frac{dv}{dt} = 0 \implies v_{term} = \frac{mg}{c}$
- Hız profili: $v(t) = \frac{mg}{c} \left(1 - e^{-\frac{c}{m}t}\right)$
