# DERS NOTU: METAL DÖKÜMÜNÜN ESASLARI VE MÜHENDİSLİK HESAPLAMALARI
**Ders:** Üretim Yöntemleri / İmal Usulleri (Manufacturing Processes)  
**Referans Kitap:** Mikell P. Groover, *Fundamentals of Modern Manufacturing* (Materials, Processes, and Systems)  
**İçerik:** Prof. Dr. Murat Vural Döküm Notları & Groover Döküm Ödevi Problemleri  

---

## 1. Ergime ve Döküm Isı Enerjisi (Heating and Pouring)
Metali oda sıcaklığından ($T_0$) döküm sıcaklığına ($T_p$) getirmek için eklenmesi gereken ısı enerjisi 3 bileşenden oluşur:
$$H = m \cdot [ C_s (T_m - T_0) + H_f + C_l (T_p - T_m) ]$$

1. **Katı Halde Isınma Enerjisi:** $m \cdot C_s (T_m - T_0)$ (Ergime sıcaklığına kadar sıcaklık artışı)
2. **Ergime Gizli Isısı (Heat of Fusion):** $m \cdot H_f$ (Katıdan sıvıya izotermal faz dönüşümü)
3. **Sıvı Aşırı Isıtma Enerjisi (Superheat):** $m \cdot C_l (T_p - T_m)$ (Kalıba dökülürken erken donmayı önlemek için verilen aşırı ısı)

---

## 2. Sıvı Metal Akış Dinamiği ve Yolluk Tasarımı
Sıvı metalin kalıp boşluğuna türbülanssız ve hava emişi (aspirasyon) olmadan dolması gerekir.

### A. Düşey Yolluk Çıkış Hızı (Bernoulli Yasası)
Yolluk yüksekliği $h$ olan bir sistemde sürtünmeler ihmal edildiğinde serbest düşüş hızı:
$$v = \sqrt{2 g h}$$

### B. Hacimsel Debi ve Kalıp Dolum Süresi (Süreklilik Denklemi)
$$Q = v \cdot A$$
$$T_{\text{fill}} = \frac{V_{\text{kalıp}}}{Q} = \frac{V_{\text{kalıp}}}{A \sqrt{2 g h}}$$

### C. Düşey Yolluk Konikliği (Tapered Sprue - Aspirasyonun Önlenmesi)
Metal aşağı doğru akarken hızı artar ($v_2 > v_1$). Süreklilik gereği ($Q = A_1 v_1 = A_2 v_2$) akış daralır. Eğer yolluk silindirik yapılırsa metal cidardan ayrılır, vakum oluşur ve kalıp kumu arasından hava emilir (gaz gözenekliliği hatası).
Bunu engellemek için yolluk aşağı doğru konik yapılmalıdır:
$$\frac{A_1}{A_2} = \frac{v_2}{v_1} = \sqrt{\frac{h_2}{h_1}}$$

---

## 3. Katılaşma Süresi ve Chvorinov Kuralı
Metalin katılaşma süresi ($T_{ts}$), parçanın hacminin ($V$) ısıyı dışarıya attığı soğuma yüzey alanına ($A$) oranına bağlıdır:
$$T_{ts} = C_m \left( \frac{V}{A} \right)^n \quad (n \approx 2)$$

- $C_m$: Kalıp sabiti ($s/m^2$ veya $min/cm^2$). Kalıp malzemesi, metal ısıl iletkenliği ve döküm sıcaklığına bağlıdır.
- Modül: $M = \frac{V}{A}$ (Parçanın geometrik modülü)

### Besleyici (Riser) Tasarımının Altın Kuralı
Besleyici, kalıp boşluğundaki çekintiyi (shrinkage) beslemek için tasarlanan sıvı metal rezervuarıdır.
Besleyici katılaşmadan önce kalıp donmalıdır! Bu nedenle:
$$T_{ts(\text{riser})} \ge 1.25 \cdot T_{ts(\text{döküm})}$$
Bu durum, besleyicinin modülünün döküm parçasının modülünden en az %12 daha büyük olmasını zorunlu kılar:
$$\left(\frac{V}{A}\right)_{\text{riser}} \ge 1.12 \left(\frac{V}{A}\right)_{\text{döküm}}$$

---

## 4. Maça Kaldırma Kuvveti (Archimedes Prensibi)
İç boşlukları oluşturmak için yerleştirilen kum maça, yüksek yoğunluklu sıvı metal içinde yukarıya doğru çok büyük bir kaldırma kuvvetine maruz kalır.

1. **Maçanın Ağırlığı (Dökümden Önce Aşağı Yönlü):**
   $$W_c = \rho_{\text{maça}} \cdot g \cdot V_c$$
2. **Kaldırma Kuvveti (Archimedes):**
   $$F_b = \rho_{\text{sıvı metal}} \cdot g \cdot V_c$$
3. **Net Yukarı Yönlü Kuvvet (Döküm Esnasında):**
   $$F_{\text{net}} = F_b - W_c = (\rho_{\text{sıvı metal}} - \rho_{\text{maça}}) \cdot g \cdot V_c$$

- **Alt Destekler (Lower Caplets):** Dökümden önce maçanın ağırlığını taşır: $n_{\text{alt}} = \lceil W_c / F_{\text{caplet}} \rceil$
- **Üst Destekler (Upper Caplets):** Sıvı metal dolduğunda maça yüzmesin diye yukarı net kuvveti dengeler: $n_{\text{üst}} = \lceil F_{\text{net}} / F_{\text{caplet}} \rceil$

---

## 5. Santrifüj Döküm Mekaniği (Centrifugal Casting)
Yatay santrifüj dökümde sıvı metalin kalıp cidarında homojen bir silindir boru oluşturması için merkezkaç kuvvetinin yerçekimi kuvvetine oranı (G-Faktörü / Gravitational Factor) 60 ila 80 arasında seçilmelidir:
$$GF = \frac{\omega^2 R}{g} = \frac{2 \pi^2 N^2 D}{g} \implies N = \frac{30}{\pi} \sqrt{\frac{2 g GF}{D_{\text{iç}}}}$$
