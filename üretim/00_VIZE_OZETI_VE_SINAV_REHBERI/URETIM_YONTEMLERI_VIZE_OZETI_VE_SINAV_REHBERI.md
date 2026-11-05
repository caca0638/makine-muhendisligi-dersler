# EUT 231 ÜRETİM YÖNTEMLERİ (MANUFACTURING PROCESSES)
## VİZE SINAVINA HAZIRLIK MASTER REHBERİ (PDF 01 - 16 TAM DÖKÜMÜ)
**Kaynak:** Prof. Dr. Murat Vural (İTÜ Makina Fakültesi) Ders Notları & Mikell P. Groover (*Fundamentals of Modern Manufacturing*)  
**Derlenmiş Master PDF:** `üretim\00_VIZE_OZETI_VE_SINAV_REHBERI\URETIM_YONTEMLERI_VIZE_MASTER_REHBERI.pdf`  

---

### BÖLÜM 1: İMALATIN ESASLARI VE ÜRETİM TİPLERİ (PDF 01)
- **Teknolojik Tanım:** Malzemenin geometrisini veya özelliklerini değiştiren fiziksel/kimyasal işlemler.
- **Ekonomik Tanım:** Malzemeye katma değer sağlama süreci.
- **İmalat İşlemleri Ayrımı:**
  - *Şekillendirme İşlemleri:* Katılaştırma (Döküm), Parçacık (Toz Metalurjisi), Deformasyon (Plastik Şekil Verme), Talaş Kaldırma.
  - *Montaj İşlemleri:* Kalıcı birleştirme (Kaynak, Lehim, Yapıştırma) ve Mekanik birleştirme (Cıvata, Perçin).
  - *Yüzey İşlemleri:* Isıl işlem ve kaplama.
- **P-Q İlişkisi:**
  - **Job Shop (Düşük Üretim):** Q = 1-100 adet/yıl, P çok yüksek (ürün çeşitliliği maksimum), genel amaçlı tezgahlar, usta işçilik.
  - **Batch (Orta Üretim):** Q = 100-10.000 adet/yıl, partiler halinde üretim, hücresel imalat, hazırlık (setup) süreleri kritik.
  - **Mass Production (Yüksek Üretim):** Q > 10.000 adet/yıl, transfer hatları, saniyeler mertebesinde çevrim süresi.
- **Sözel Sınav Notu (Parça Üretimi vs Montaj):** Parça üretimi tekil bileşenin geometrisini ve iç yapısını değiştirirken, montaj üretilmiş bağımsız parçaları birleştirerek mekanik bir sistem oluşturur.

---

### BÖLÜM 2: MALZEMELERİN YAPISI VE MEKANİK ÖZELLİKLERİ (PDF 02 - 07)
- **Kafes Yapıları ve Süneklik:**
  - **YMK (FCC):** Al, Cu, Ni, Östenit (g-Fe). 12 bağımsız kayma düzlemi. En yüksek süneklik ve şekillendirilebilirlik; soğuk deformasyona çok uygundur.
  - **HMK (BCC):** a-Fe (Ferrit), W, Mo, Cr. Mukavemeti yüksek, kayma düzlemleri daha az; gevrek-sünek geçiş sıcaklığı gösterir.
  - **SPH (HCP):** Ti, Mg, Zn. Yalnızca 3 bazal kayma düzlemi. Oda sıcaklığında kırılgandır, ancak ısıtılarak (sıcakta) şekillendirilebilir.
- **Plastik Deformasyonun Mikromekaniği:** Metallerde plastik şekil değiştirme dislokasyonların kayma düzlemleri boyunca hareketiyle gerçekleşir. **Dislokasyon hareketini engellemek = Malzemeyi sertleştirmek ve mukavemetini artırmaktır.**
  - *4 Temel Sertleştirme Yöntemi:* (1) Gerinim sertleşmesi (soğuk işlem), (2) Tane boyutu küçültme (Hall-Petch), (3) Katı eriyik sertleşmesi, (4) Çökelme sertleşmesi (yaşlandırma).
- **Gerilme-Gerinim Bağıntıları:**
  - Mühendislik gerilmesi: $s = F / A_0$, Gerinimi: $e = (L - L_0) / L_0$
  - Gerçek gerinim: $\epsilon = \ln(L / L_0) = \ln(1 + e)$
  - Gerçek gerilme: $\sigma = s (1 + e)$ (Hacim sabitliği $A_0 L_0 = A L$)
  - **Hollomon Akış Eğrisi:** $\sigma = K \epsilon^n$ ($K$: Mukavemet katsayısı, $n$: Gerinim sertleşmesi üssü. **Boyun verme anında $\epsilon = n$ olur!**)
  - **Ortalama Akma Gerilmesi:** $\bar{Y}_f = \frac{K \epsilon^n}{1 + n}$
- **Demir-Karbon Fazları ve Dökme Demirler (Sözel Sınav Notu):**
  - *Östenit (g-Fe):* YMK yapıda, %2.11 C çözer, sünek ve manyetik değildir.
  - *Ferrit (a-Fe):* HMK yapıda, oda sıcaklığında kararlı, yumuşaktır.
  - *Sementit (Fe3C):* %6.67 C içerir, aşırı sert ve kırılgandır.
  - *Kır (Gri) Dökme Demir:* Lamel grafitlidir. Titreşim sönümleme kabiliyeti mükemmeldir; tezgah gövdelerinde kullanılır.
  - *Küresel (Sfero) Dökme Demir:* Sıvı metale **Magnezyum (Mg) veya Seryum (Ce)** aşılanarak grafitler küre haline getirilir. Çelik gibi sünek ve darbelere dayanıklıdır!

---

### BÖLÜM 3: METAL DÖKÜMÜNÜN ESASLARI VE YÖNTEMLERİ (PDF 08 - 09)
- **Dökümde 5 Temel Hesaplama Formülü:**
  - Isı Enerjisi: $H = m [C_s(T_m - T_0) + H_f + C_l(T_p - T_m)]$
  - Bernoulli Yolluk Çıkış Hızı: $v = \sqrt{2gh}$
  - Süreklilik ve Dolum Süresi: $Q = v A \implies T_{fill} = V_{kalıp} / Q$
  - **Chvorinov Kuralı:** $T_{ts} = C_m (V / A)^n$ ($n \approx 2$). Eşit hacimde **KÜRE** en geç, **LEVHA** en erken donar!
  - **Maça Kaldırma Kuvveti:** $F_{net} = F_b - W_c = (\rho_{metal} - \rho_{maça}) g V_c$. Alt destekler $W_c$'yi, üst destekler $F_{net}$'i tutar.
  - **Savurma Döküm Hızı:** $GF = \frac{2 \pi^2 N^2 D}{g} \approx 60 - 80$.
- **Döküm Kumu 4 Özelliği (Sözel):**
  1. *Refrakterlik:* Yüksek erime sıcaklığında erimeden dayanabilme.
  2. *Geçirgenlik (Permeability):* Buhar ve sıcak gazların dışarı kaçabilmesi.
  3. *Mukavemet:* Sıvı metal akışına karşı kalıp şeklini koruma.
  4. *Dağılabilirlik (Collapsibility):* Metal katılaşıp büzülürken gerilme/çatlama yapmaması için kalıbın kolay ufalanabilmesi.
- **Hocanın Sorduğu 5 Döküm Hatası (Sözel):**
  1. *Gaz Boşluğu (Blowhole):* Geçirgenlik yetersizse veya kum nemliyse hapsolan gazlar.
  2. *Çekinti Boşluğu (Shrinkage Cavity):* Yetersiz besleyici nedeniyle en geç donan bölgede oluşan borulanma/huni.
  3. *Soğuk Birleşme (Cold Shut):* İki akış cephesinin erken soğuyup tam kaynaşamaması.
  4. *Eksik Dolum (Misrun):* Metal kalıbı tamamen dolduramadan erken katılaşması.
  5. *Kum Erozyonu (Sand Wash):* Türbülanslı akışın kum cidarlarını koparması.
- **Yolluk Konikliği Uyarısı:** $A_1 / A_2 = \sqrt{h_2 / h_1}$. Sıvı hızlandıkça kesit daralır; hava emişini (aspirasyon) önlemek için konik yapılır!
- **Besleyici Şartı:** $T_{ts(riser)} \ge 1.25 T_{ts(döküm)} \implies (V/A)_{riser} \ge 1.12 (V/A)_{döküm}$.

---

### BÖLÜM 4: POLİMER, LASTİK, CAM VE SERAMİK İŞLEME (PDF 10 - 14)
- **Ekstrüzyon Vidası 3 Bölgesi:** Besleme, Sıkıştırma/Ergitme, Basma/Ölçümleme.
- **Enjeksiyon Kalıplama:** Yüksek basınçta enjeksiyon, hızlı çevrim (10-30 s).
- **Şişirme Kalıplama:** İçi boş şişe/bidon imalatı (parison tüpü şişirme).
- **Termoform:** Düz levhayı ısıtıp vakumla kalıba çekme (yoğurt kapları).
- **Sözel Sınav Notu (Psödoplastik Akış ve Kalıp Şişmesi):**
  - *Psödoplastik (Shear-Thinning):* Polimer eriyikleri kayma hızı arttıkça viskozitesi düşen akışkanlardır; bu sayede dar kalıp boşluklarına yüksek hızda kolayca enjekte edilirler.
  - *Kalıp Şişmesi (Die Swell):* Polimer nozuldan çıktığında viskoelastik hafızası nedeniyle enine genişler (şişer). Kalıp deliği istenen ürün çapından daha küçük tasarlanır!
  - *Seramik Akıtma Döküm (Slip Casting):* Kil süspansiyon alçı kalıba dökülür; alçı suyu emdikçe cidar kalınlaşır, fazlası boşaltılır (lavabo, klozet imalatı).

---

### BÖLÜM 5: TOZ METALURJİSİ - P/M (PDF 15)
- **Aşamalar:** Toz üretimi (atomizasyon) $\to$ Presleme $\to$ Sinterleme ($0.7-0.8 T_m$ koruyucu atmosferde katı hal difüzyonu).
- **Sözel Sınav Notu:**
  - *Çift Etkili Zımba:* Kalıp çeperi sürtünmesinden kaynaklanan üst-alt yoğunluk farkını minimize eder.
  - *Koruyucu Atmosfer:* Yüksek yüzey alanına sahip tozların oksitlenmesini önlemek için hidrojen/azot/vakum kullanılır.
  - *İkincil İşlemler:* Kalibrasyon (sizing/coining - boyutsal hassasiyet için ikinci presleme) ve Bakır İnfiltrasyonu (gözenekli demire erimiş bakır emdirilerek tokluk artırma).

---

### BÖLÜM 6: PLASTİK ŞEKİL VERMENİN ESASLARI (PDF 16)
- **Akma Kriterleri:** Tresca ($\sigma_1 - \sigma_3 = Y$) ve von Mises ($Y' = 1.155 Y$).
- **Sıcak vs Soğuk Şekil Verme (Sınav Tablosu):**
  - *Soğuk ($T < 0.3 T_m$):* Gerinim sertleşmesi belirgindir ($n > 0$), mukavemet artar, dar tolerans, temiz yüzey, yüksek kuvvet gerekir.
  - *Sıcak ($T > 0.5 T_m$):* **Gerinim sertleşmesi YOKTUR ($n \approx 0$)!** Deformasyon sırasında dinamik rekristalizasyon (DRX) ile yeni taneler çekirdeklenir; düşük kuvvet gerekir, tufal oluşur, tolerans kabadır.
- **Sözel Sınav Notu (Artık Gerilmeler ve Kalıba Yapışma):**
  - *Kalıba Yapışma (Sticking Friction):* Yüksek basınç altında sürtünme gerilmesi malzemenin kayma akma dayanımına ulaşır ($\tau = k = Y / \sqrt{3}$); metal kalıba yapışır.
  - *Artık Gerilmeler (Residual Stresses):* Soğuk işlem sonrası parçada kilitli kalan iç gerilmeler çarpılmaya yol açar; gidermek için **Gerilme Giderme Tavı** uygulanır.

---

### BÖLÜM 7: VİZE SINAVI İÇİN 3 KLASİK SAYISAL PROBLEM ŞABLONU
1. **Chvorinov Kuralı:** 10 cm küre, silindir ($H=D$) ve küp geometrilerinin $(V/A) = 1.667\text{ cm}$ eşitliği nedeniyle katılaşma süreleri özdeştir.
2. **Maça Kaldırma Kuvveti:** $5000\text{ cm}^3$ kum maça ve pirinç döküm için $W_c = 78.5\text{ N} \implies n_{alt} = 2$ caplet; $F_{net} = 343.4\text{ N} \implies n_{üst} = 8$ caplet.
3. **Hollomon Akış Eğrisi:** $50\text{ mm} \to 30\text{ mm}$ basmada $\epsilon = 0.511 \implies Y_f = 525.0\text{ MPa}$ ve ortalama $\bar{Y}_f = 437.5\text{ MPa}$.
