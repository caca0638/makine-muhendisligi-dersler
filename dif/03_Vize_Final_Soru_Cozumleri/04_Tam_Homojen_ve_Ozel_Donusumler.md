# DİFERANSİYEL DENKLEMLER - VİZE VE FİNAL SORULARI (BÖLÜM 2)
**Konu:** Tam Diferansiyel Denklemler, İntegral Çarpanı Bulma ve Homojen Denklemler ($y = vx$)  
**Kapsam:** Makine Mühendisliği Müfredatı & Sınav Çözüm Teknikleri

---

## SORU 1: Tam Diferansiyel Denklem ve Başlangıç Değer Problemi (IVP)

### Soru:
Aşağıda verilen diferansiyel denklemin tam olduğunu gösteriniz ve verilen başlangıç şartı altındaki özel çözümünü bulunuz:
$$(2xy + 3) dx + (x^2 - 1) dy = 0, \quad y(2) = 1$$

### Adım Adım Analitik Çözüm:

#### 1. Adım: Tamlık (Exactness) Kontrolü
Denklem $M(x, y) dx + N(x, y) dy = 0$ formundadır.
- $M(x, y) = 2xy + 3 \implies \frac{\partial M}{\partial y} = 2x$
- $N(x, y) = x^2 - 1 \implies \frac{\partial N}{\partial x} = 2x$

$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} = 2x$$
Kısmi türevler eşit olduğundan verilen diferansiyel denklem **tamdır (exact)**.

#### 2. Adım: Potansiyel Fonksiyon $u(x, y)$'nin Kurulması
Tam denklemlerde $du = \frac{\partial u}{\partial x} dx + \frac{\partial u}{\partial y} dy = 0$ olduğundan genel çözüm $u(x, y) = C$ seviye eğrisidir.
$$\frac{\partial u}{\partial x} = M(x, y) = 2xy + 3$$
Bu ifadenin $x$'e göre kısmî integralini alıyoruz ($y$ sabit kabul edilir):
$$u(x, y) = \int (2xy + 3) \, dx + k(y) = x^2 y + 3x + k(y)$$
Buradaki $k(y)$, $x$'e göre türev alındığında sıfırlanan $y$'ye bağlı integrasyon sabitidir.

#### 3. Adım: $k(y)$ Fonksiyonunun Bulunması
Elde ettiğimiz $u(x, y)$'nin $y$'ye göre kısmî türevi $N(x, y)$'ye eşit olmalıdır:
$$\frac{\partial u}{\partial y} = \frac{\partial}{\partial y}[x^2 y + 3x + k(y)] = x^2 + k'(y)$$
Bu ifadeyi $N(x, y) = x^2 - 1$ ile eşitliyoruz:
$$x^2 + k'(y) = x^2 - 1 \implies k'(y) = -1$$
Her iki tarafın $y$'ye göre integralini alırsak:
$$k(y) = \int (-1) \, dy = -y$$

Böylece potansiyel fonksiyon:
$$u(x, y) = x^2 y + 3x - y$$
**Genel Çözüm:**
$$x^2 y + 3x - y = C$$

#### 4. Adım: Başlangıç Şartının $y(2) = 1$ Uygulanması
$x = 2$ ve $y = 1$ değerlerini genel çözümde yerine koyarak $C$ sabitini hesaplıyoruz:
$$(2)^2 (1) + 3(2) - (1) = C \implies 4 + 6 - 1 = C \implies C = 9$$

#### 5. Adım: $y(x)$'in Açık Olarak Çekilmesi (Özel Çözüm)
$$y(x^2 - 1) + 3x = 9 \implies y(x^2 - 1) = 9 - 3x$$
$$y(x) = \frac{9 - 3x}{x^2 - 1}$$

---

## SORU 2: Tam Olmayan Denklemde İntegrasyon Çarpanı $\mu(x)$ Bulma

### Soru:
Aşağıdaki diferansiyel denklemin tam olmadığını gösteriniz, uygun integrasyon çarpanını bularak genel çözümünü elde ediniz:
$$(3xy + y^2) dx + (x^2 + xy) dy = 0$$

### Adım Adım Analitik Çözüm:

#### 1. Adım: Tamlık Kontrolü
- $M(x, y) = 3xy + y^2 \implies \frac{\partial M}{\partial y} = 3x + 2y$
- $N(x, y) = x^2 + xy \implies \frac{\partial N}{\partial x} = 2x + y$

$$\frac{\partial M}{\partial y} \neq \frac{\partial N}{\partial x} \implies \text{Denklem tam değildir!}$$

#### 2. Adım: İntegrasyon Çarpanı $\mu$ Arama
Kısmi türevlerin farkını inceliyoruz:
$$\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x} = (3x + 2y) - (2x + y) = x + y$$

Bu farkı $N(x, y)$'ye bölüyoruz:
$$\frac{\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}}{N} = \frac{x + y}{x^2 + xy} = \frac{x + y}{x(x + y)} = \frac{1}{x} = f(x)$$
Sonuç sadece $x$'e bağlı bir fonksiyon ($f(x) = \frac{1}{x}$) çıktığı için integrasyon çarpanı $\mu(x)$ şu formülle bulunur:
$$\mu(x) = e^{\int f(x) dx} = e^{\int \frac{1}{x} dx} = e^{\ln|x|} = x$$

#### 3. Adım: Denklemi $\mu(x) = x$ ile Çarpıp Tam Hale Getirme
Verilen denklemin her terimini $x$ ile çarpıyoruz:
$$\left(3x^2 y + x y^2\right) dx + \left(x^3 + x^2 y\right) dy = 0$$
Yeni $M$ ve $N$ terimleri:
- $M^* = 3x^2 y + x y^2 \implies \frac{\partial M^*}{\partial y} = 3x^2 + 2xy$
- $N^* = x^3 + x^2 y \implies \frac{\partial N^*}{\partial x} = 3x^2 + 2xy$
$$\frac{\partial M^*}{\partial y} = \frac{\partial N^*}{\partial x} \implies \text{Yeni denklem artık tamdır!}$$

#### 4. Adım: Potansiyel Fonksiyon $u(x, y)$ Hesabı
$$u(x, y) = \int M^* dx + k(y) = \int (3x^2 y + x y^2) dx + k(y) = x^3 y + \frac{1}{2} x^2 y^2 + k(y)$$
$y$'ye göre türev alıp $N^*$'a eşitliyoruz:
$$\frac{\partial u}{\partial y} = x^3 + x^2 y + k'(y) = x^3 + x^2 y \implies k'(y) = 0 \implies k(y) = C_0$$

**Genel Çözüm:**
$$x^3 y + \frac{1}{2} x^2 y^2 = C \quad \text{veya} \quad 2x^3 y + x^2 y^2 = C$$

---

## SORU 3: Homojen Diferansiyel Denklem ve $y = v \cdot x$ Dönüşümü

### Soru:
Aşağıdaki diferansiyel denklemin genel çözümünü bulunuz:
$$(x^2 + y^2) dx - 2xy dy = 0$$

### Adım Adım Analitik Çözüm:

#### 1. Adım: Homojenlik Kontrolü
- $M(tx, ty) = (tx)^2 + (ty)^2 = t^2 (x^2 + y^2) = t^2 M(x, y)$ (2. dereceden homojen)
- $N(tx, ty) = -2(tx)(ty) = t^2 (-2xy) = t^2 N(x, y)$ (2. dereceden homojen)
Tüm terimler 2. dereceden homojen olduğundan denklem bir **homojen diferansiyel denklemdir**.

#### 2. Adım: Değişken Değiştirme
$$y = v \cdot x \implies dy = v \, dx + x \, dv$$
Bu ifadeleri denklemde $y$ ve $dy$ yerine yazıyoruz:
$$(x^2 + v^2 x^2) dx - 2x (v x) (v \, dx + x \, dv) = 0$$
$x^2$ parantezine alıyoruz:
$$x^2 (1 + v^2) dx - 2x^2 v (v \, dx + x \, dv) = 0$$
$x \neq 0$ için her iki tarafı $x^2$'ye bölüyoruz:
$$(1 + v^2) dx - 2v^2 dx - 2vx dv = 0$$
$$(1 - v^2) dx - 2vx dv = 0 \implies (1 - v^2) dx = 2vx dv$$

#### 3. Adım: Değişkenlerine Ayırma ve İntegrasyon
$$\frac{1}{x} dx = \frac{2v}{1 - v^2} dv$$
Her iki tarafın integralini alıyoruz:
$$\int \frac{1}{x} dx = \int \frac{2v}{1 - v^2} dv$$
Sağ taraftaki integral için $w = 1 - v^2 \implies dw = -2v dv$:
$$\ln|x| = -\ln|1 - v^2| + C_1$$
$$\ln|x| + \ln|1 - v^2| = C_1 \implies \ln|x (1 - v^2)| = C_1$$
Üstel fonksiyona geçilirse:
$$x (1 - v^2) = C \quad (C = \pm e^{C_1})$$

#### 4. Adım: $v = \frac{y}{x}$ Geri Dönüşümü
$$x \left( 1 - \frac{y^2}{x^2} \right) = C \implies x \left( \frac{x^2 - y^2}{x^2} \right) = C$$
$$\frac{x^2 - y^2}{x} = C \implies x^2 - y^2 = C x$$

**Genel Çözüm:**
$$x^2 - C x - y^2 = 0 \quad \text{veya} \quad \left(x - \frac{C}{2}\right)^2 - y^2 = \frac{C^2}{4}$$
Bu eğriler ailesi merkezi $x$ ekseni üzerinde bulunan bir **hiperboller ailesidir**.
