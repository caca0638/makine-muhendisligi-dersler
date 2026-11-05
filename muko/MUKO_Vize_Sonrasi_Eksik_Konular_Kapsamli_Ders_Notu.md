# MUKAVEMET I - VİZE SONRASI EKSİK KONULAR DERS NOTU VE PROBLEM SETİ
*MAK 2119 Müfredatı & Beer-Johnston Mechanics of Materials*

---

## 1. KİRİŞLERDE EĞİLME GERİLMELERİ VE KOMPOZİT KİRİŞLER (HAFTA 8 - 9)

### 1.1 Saf Eğilme ve Tarafsız Eksen
* **Saf Eğilme:** Yalnızca eğilme momenti M vardır, kesme kuvveti V = 0'dır.
* **Tarafsız Eksen (Neutral Axis - NA):** Boyuna normal gerilmenin sıfır olduğu eksendir (σ_x = 0). Homojen kesitlerde geometrik ağırlık merkezinden geçer.
* Birim Şekil Değiştirme: `ε_x = - y / ρ` (y: tarafsız eksenden mesafe, ρ: eğrilik yarıçapı).

### 1.2 Elastik Eğilme Formülü (Navier Bağıntısı)
* `σ_x = - ( M · y ) / I_z`
* `σ_maks = ( |M| · c ) / I_z = |M| / W_z`
  * **M:** Eğilme momenti [N·m]
  * **I_z:** Tarafsız eksene göre atalet momenti [m⁴] (Dikdörtgen için `b h³ / 12`)
  * **c:** En dış lif mesafesi [m] (Dikdörtgen için `h / 2`)
  * **W_z:** Mukavemet momenti (Elastik kesit modülü): `W_z = I_z / c` (Dikdörtgen için `b h² / 6`)

### 1.3 Kompozit (Sandviç) Kirişler - Dönüştürülmüş Kesit Yöntemi
* **Modüler Oran:** `n = E₂ / E₁`
* 2. malzemenin genişliği n katına çıkarılır: `b'₂ = n · b₂`.
* Dönüştürülmüş kesitin ağırlık merkezi ve I_dön atalet momenti bulunur:
  * Referans malzeme gerilmesi: `σ₁ = - (M · y) / I_dön`
  * Dönüştürülen malzeme gerilmesi: `σ₂ = - n · (M · y) / I_dön`

### 1.4 Eksantrik Eksenel Yükleme
`σ = ( P / A ) ± ( M · y / I ) = ( P / A ) ± ( P · e · y / I )`

---

## 2. KESME KUVVETİ VE MOMENT DİYAGRAMLARI (HAFTA 10 - 11)

### 2.1 Diferansiyel Bağıntılar
* `dV / dx = - w(x)`  => Kesme diyagramının eğimi yayılı yüke eşittir.
* `dM / dx = V(x)`  => Moment diyagramının eğimi kesme kuvvetine eşittir.
* **Maksimum Moment:** Kesme kuvvetinin sıfır olduğu (V = 0) kesitte oluşur.

### 2.2 Prizmatik Kiriş Tasarımı
* Emniyet gerilmesi σ_em için: `W_gerekli = |M_maks| / σ_em`
* Profil tablosundan `W_seçilen ≥ W_gerekli` şartı sağlanır.

---

## 3. KİRİŞLERDE ENİNE KAYMA GERİLMESİ (HAFTA 12 - 13)

### 3.1 Jourawski Formülü
* `τ = ( V · Q ) / ( I · b )`
* **Kayma Akışı:** `q = τ · b = ( V · Q ) / I`  [N/m]
  * **V:** Kesme kuvveti
  * **I:** Toplam atalet momenti
  * **b:** İncelenen seviyedeki kesit kalınlığı
  * **Q:** İncelenen seviyenin dışında kalan alanın 1. statik momenti: `Q = A' · y'G`

### 3.2 Tipik Kesitlerde Maksimum Kayma Gerilmesi (Tarafsız Eksende)
* **Dikdörtgen (b × h):** `τ_maks = 1.5 · ( V / A ) = 3 V / ( 2 b h )`
* **Dairesel (R):** `τ_maks = ( 4 / 3 ) · ( V / A ) = 4 V / ( 3 π R² )`
* **Bağlantı Elemanlarında (Cıvata, Çivi) Taşıma Kuvveti:** `F_bağlantı = q · s = [ (V · Q) / I ] · s`

---

## 4. KAYMA MERKEZİ VE ASİMETRİK EĞİLME (HAFTA 14)

### 4.1 Kayma Merkezi (Shear Center)
Tek simetri eksenli açık ince cidarlı kesitlerde (örn: U-profil) enine yükün kirişi burulmadan yalnızca eğmeye zorlaması için uygulanması gereken noktadır.
* U-profil için kayma merkezi mesafesi: `e = ( 3 b² ) / ( 6 b + h )` (Gövdenin dış tarafında).

### 4.2 Asimetrik Eğilme
`σ_x = - ( M_z · y ) / I_z + ( M_y · z ) / I_y`
Tarafsız eksen eğimi: `tan α = ( I_z / I_y ) · tan θ`

---

## 5. GERİLME DÖNÜŞÜMLERİ VE MOHR DAİRESİ

### 5.1 Düzlem Gerilme Dönüşüm Denklemleri
* `σ_x' = ( σ_x + σ_y ) / 2 + [ ( σ_x - σ_y ) / 2 ] · cos(2θ) + τ_xy · sin(2θ)`
* `τ_x'y' = - [ ( σ_x - σ_y ) / 2 ] · sin(2θ) + τ_xy · cos(2θ)`

### 5.2 Asal Gerilmeler ve Maksimum Kayma
* `tan(2θ_p) = ( 2 τ_xy ) / ( σ_x - σ_y )`
* `σ₁,₂ = ( σ_x + σ_y ) / 2 ± √[ ( (σ_x - σ_y) / 2 )² + τ_xy² ]`
* `τ_maks = √[ ( (σ_x - σ_y) / 2 )² + τ_xy² ] = ( σ₁ - σ₂ ) / 2`
* Mohr Dairesi Merkezi: `C = ( (σ_x + σ_y) / 2, 0 )`, Yarıçapı `R = τ_maks`.

---

## 6. KİRİŞLERDE SEHİM (ELASTİK EĞRİ DENKLEMİ)

* `E · I · ( d²y / dx² ) = M(x)`
* Eğim: `θ(x) = dy/dx = ( 1 / EI ) · ∫ M(x) dx + C₁`
* Sehim: `y(x) = ( 1 / EI ) · ∫ [ ∫ M(x) dx ] dx + C₁ x + C₂`

---

## 7. ÇÖZÜMLÜ MUKAVEMET PROBLEMLERİ

### PROBLEM 1: Basit Mesnetli Kirişte V-M ve Maksimum Normal Gerilme
* L = 6 m, w = 12 kN/m, ortada P = 18 kN, kesit 150 × 300 mm.
* `R_A = R_B = 45 kN`.
* `V_maks = 45 kN`, `M_maks = 81 kN·m`.
* `I = 3.375 × 10⁻⁴ m⁴, W = 0.00225 m³`.
* `σ_maks = 81,000 / 0.00225 = 36.0 MPa` (Üstte 36 MPa basma, altta 36 MPa çekme).

### PROBLEM 2: Dikdörtgen Kesitte Kayma Gerilmesi
* V = 45 kN, kesit 150 × 300 mm.
* Tarafsız eksende maksimum kayma: `τ_maks = 1.5 · (45,000 / 0.045) = 1.50 MPa`.
* y = 75 mm seviyesinde: `Q = 1.2656 × 10⁻³ m³ => τ = 1.125 MPa`.

### PROBLEM 3: Kompozit Ahşap-Çelik Kiriş
* Ahşap: 100 × 150 mm (E = 10 GPa), Çelik: 100 × 10 mm (E = 200 GPa), M = 6 kN·m.
* `n = 20 => b' = 2000 mm`.
* Ağırlık merkezi `y_G = 39.29 mm` (alttan). `I_dön = 8.314 × 10⁻⁵ m⁴`.
* Ahşapta maksimum basma: `σ_ahşap = 8.71 MPa`.
* Çelikte maksimum çekme: `σ_çelik = 20 × 2.835 = 56.7 MPa`.

### PROBLEM 4: Düzlem Gerilme ve Mohr Dairesi
* `σ_x = 80 MPa, σ_y = -40 MPa, τ_xy = 45 MPa`.
* Merkez: `σ_ort = 20.0 MPa`, Yarıçap: `R = 75.0 MPa`.
* Asal Gerilmeler: `σ₁ = 20 + 75 = 95.0 MPa`, `σ₂ = 20 - 75 = -55.0 MPa`.
* `τ_maks = 75.0 MPa`, Asal Açı `θ_p1 = +18.43°`.

### PROBLEM 5: Konsol Kirişte Sehim (Çift İntegrasyon)
* Serbest uçta P yükü, açıklık L.
* `EI (d²y/dx²) = - P (L - x)`.
* Sınır şartları: x = 0'da y = 0, y' = 0.
* Serbest uçta eğim: `θ(L) = - P L² / (2 EI)`.
* Serbest uçta sehim: `y_maks = - P L³ / (3 EI)`.
