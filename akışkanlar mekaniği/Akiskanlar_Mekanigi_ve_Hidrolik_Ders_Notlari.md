# AKI?KANLAR MEKAN??? VE H?DROL?K - KAPSAMLI DERS VE PROBLEM K?TABI
*Manisa Celal Bayar ?niversitesi MAK 3151 M?fredat? & Temel Akademik Kaynaklar Referans Al?nm??t?r*

---

Akışkanlar Mekaniği ve Hidrolik - Kapsamlı Ders ve Çözümlü Problem Kitabı 

 
 

     Kapsamlı Teori, Tüm Türetimler, Formül Bankası ve Adım Adım Çözümlü Problem El Kitabı 
     
     
        **Referans Alınan Müfredat ve Temel Kaynaklar:**

        Manisa Celal Bayar Üniversitesi – MAK 3151 Akışkanlar Mekaniği Müfredatı

        Prof. Dr. Nusret Şekerdağ – *Akışkanlar Mekaniği ve Hidrolik Problemleri* (Nobel)

        Prof. Dr. Mutlu Sümer, Prof. Dr. İstemi Ünsal, Prof. Dr. Mehmetçik Bayazıt – *Hidrolik* (Birsen)

        Prof. Dr. Turhan Acatay, Prof. Dr. Adnan Akyarlı – *Akışkanlar Mekaniği* (İMO İzmir)

        Prof. Dr. Yunus A. Çengel & John M. Cimbala – *Akışkanlar Mekaniği: Temelleri ve Uygulamaları*

        Frank M. White – *Fluid Mechanics* & Schaum's 2500 Solved Problems Series
     
 

# İÇİNDEKİLER

 
    
* **Giriş ve Akışkanların Fiziksel Özellikleri:** Sürekli ortam hipotezi, viskozite, Newtonyen ve non-Newtonyen akışkanlar, sıkıştırılabilirlik, ses hızı, yüzey gerilimi ve kılcallık.
    
* **Akışkanlar Statiği (Hidrostatik):** Basınç dağılımı, manometreler, düzlem ve eğri yüzeylere gelen kuvvetler, basınç merkezi, Arşimet prensibi ve yüzen cisimlerin stabilitesi (metasantr).
    
* **Rijit Cisim Hareketi Yapan Sıvılar:** Doğrusal ivmeli öteleme yapan kaplar, sabit açısal hızla dönen silindirik kaplar ve parabolik serbest yüzey hesabı.
    
* **Akışkanlar Kinematiği:** Lagrange ve Euler yaklaşımları, akım çizgisi, yörünge, çıkış çizgisi, maddesel türev (yerel ve konvektif ivme), deformasyon hızı, girdaplık ve akım fonksiyonu.
    
* **Reynolds Transport Teoremi ve İntegral Korunum Yasaları:** Sistem-kontrol hacmi dönüşümü, kütlenin korunumu (süreklilik), çizgisel momentum denklemi, açısal momentum denklemi, enerji denklemi.
    
* **Diferansiyel Analiz ve Navier-Stokes Denklemleri:** Diferansiyel süreklilik, Navier-Stokes denklemleri, Euler denklemi, Couette ve Poiseuille akışlarının analitik çözümü.
    
* **Bernoulli Denklemi ve Uygulamaları:** Enerji çizgisi, kısıtlar, Pitot tüpü, Venturimetre, orifis debimetresi, Toricelli teoremi ve kavitasyon.
    
* **Boyut Analizi ve Benzeşim:** Buckingham Pi Teoremi, boyutsuz sayılar (Re, Fr, Eu, Ma, We), geometrik, kinematik ve dinamik benzeşim, model ölçekleme kuralları.
    
* **Borularda İç Akışlar ve Hidrolik Kayıplar:** Laminer ve türbülanslı akım, Darcy-Weisbach denklemi, Colebrook bağıntısı, Moody diyagramı, yerel kayıplar, seri/paralel boru şebekeleri, su darbesi ve pompa seçimi.
    
* **Dış Akışlar ve Sınır Tabaka Teorisi:** Sınır tabaka kalınlıkları (\(\delta, \delta^*, \theta\)), Blasius çözümü, sürtünme ve biçim direnci (drag & lift).
    
* **Açık Kanal Hidroliği:** Islak çevre, hidrolik yarıçap, Chézy ve Manning denklemleri, en ekonomik hidrolik enkesit, özgül enerji, Froude sayısı ve akım rejimleri, kritik derinlik, hidrolik sıçrama (Bélanger bağıntısı) ve su yüzeyi eğrileri.
    
* **Adım Adım Çözümlü 10 Klasik Sınav Problemi.**
 

  

# BÖLÜM 1: GİRİŞ VE AKIŞKANLARIN FİZİKSEL ÖZELLİKLERİ

### 1.1 Akışkan Tanımı ve Sürekli Ortam (Continuum) Hipotezi

Katı maddeler kayma gerilmesine karşı statik şekil değiştirme direnci gösterirken, akışkanlar (sıvılar ve gazlar) üzerlerine etki eden kayma gerilmesi (\(\tau\)) ne kadar küçük olursa olsun sürekli olarak şekil değiştiren (akan) maddelerdir. Moleküler boşlukların sistem boyutlarına göre ihmal edilebilecek kadar küçük olduğu durumlarda akışkan, boşluksuz homojen bir kütle olarak kabul edilir (Sürekli Ortam Hipotezi). Knudsen sayısı \(Kn = \lambda / L  
    
* **Yoğunluk (\(\rho\)):** Birim hacimdeki kütledir: \(\rho = \lim_{\Delta V \to 0} \frac{\Delta m}{\Delta V}\) \([\text{kg/m}^3]\). Su için \(+4^\circ\text{C}\)'de \(\rho = 1000\text{ kg/m}^3\).
    
* **Özgül Ağırlık (\(\gamma\)):** Birim hacmin ağırlığıdır: \(\gamma = \rho \cdot g\) \([\text{N/m}^3]\). Standart su için \(\gamma = 9810\text{ N/m}^3 = 9.81\text{ kN/m}^3\).
    
* **Bağıl Yoğunluk / Özgül Gravite (\(SG\) veya \(s\)):** Akışkan yoğunluğunun standart su yoğunluğuna oranıdır: \(SG = \rho / \rho_{\text{su}} = \gamma / \gamma_{\text{su}}\). (Örn: Cıva için \(SG = 13.6\), yağlar için \(SG \approx 0.85 - 0.92\)).
 

### 1.3 Viskozite ve Newton Tipi Olan/Olmayan Akışkanlar

Viskozite, akışkan tabakalarının birbiri üzerinden kaymasına karşı gösterdiği iç sürtünme direncidir. İki paralel plaka arasında kayan akışkan için kayma gerilmesi deformasyon hızı ile orantılıdır:

 
    **Newton Viskozite Bağıntısı:**
    $$\tau = \mu \frac{du}{dy}$$
    Burada:
     
        
* \(\tau\): Kayma gerilmesi \([\text{N/m}^2 = \text{Pa}]\)
        
* \(\mu\): Dinamik viskozite \([\text{Pa}\cdot\text{s} = \text{N}\cdot\text{s/m}^2 = \text{kg/(m}\cdot\text{s)}]\)
        
* \(\frac{du}{dy}\): Hız gradyanı / kayma deformasyonu hızı \([\text{s}^{-1}]\)
     
    **Kinematik Viskozite (\(\nu\)):** Dinamik viskozitenin yoğunluğa oranıdır:
    $$\nu = \frac{\mu}{\rho} \quad [\text{m}^2/\text{s}] \quad (1\text{ Stokes} = 10^{-4}\text{ m}^2/\text{s})$$
 

**Akışkan Türleri:**

 
    
* **Newtonyen Akışkanlar:** Kayma gerilmesi ile hız gradyanı doğrusal orantılıdır (\(\mu = \text{sabit}\)). Örnek: Su, hava, benzin, yağ.
    
* **Newtonyen Olmayan (Non-Newtonian) Akışkanlar:** \(\tau = k (du/dy)^n\).
         
             *Psödoplastik (Kayma ile incelen, \(n   1\)):* Nişasta-su karışımı, ıslak kum.
            
* *Bingham Plastiği:* Akması için bir başlangıç akma gerilmesi (\(\tau_0\)) gerekir. Örnek: Diş macunu, çamur, mayonez.
         
     
    
* **Sıcaklığın Viskoziteye Etkisi:** Sıvılarda moleküller arası çekim kuvvetleri baskın olduğundan sıcaklık arttıkça viskozite *azalır*. Gazlarda ise moleküler momentum transferi baskın olduğundan sıcaklık arttıkça viskozite *artar*.
 

### 1.4 Sıkıştırılabilirlik Modülü ve Ses Hızı

 
    **Hacimsel Esneklik Modülü (Bulk Modulus - \(E_v\)):**
    $$E_v = -\Delta P \frac{V}{\Delta V} = \rho \frac{dP}{d\rho} \quad [\text{Pa}]$$
    Su için \(E_v \approx 2.15 \times 10^9\text{ Pa}\) (oldukça yüksek olduğundan sıvılar pratik olarak sıkıştırılamaz kabul edilir).

    **Ses Hızı (\(c\)):** Küçük basınç dalgalarının ortamdaki yayılma hızıdır:
    $$c = \sqrt{\frac{E_v}{\rho}} = \sqrt{k R T} \quad (\text{İdeal Gazlar İçin})$$
 

### 1.5 Yüzey Gerilimi ve Kılcallık (Kapilarite)

Sıvı yüzeyindeki moleküllerin dengelenmemiş iç çekim kuvvetleri nedeniyle oluşan yüzey gerilimi (\(\sigma\)), birim uzunluğa gelen kuvvettir \([\text{N/m}]\). \(R\) yarıçaplı dairesel bir cam tüpte sıvının kapiler yükselmesi/alçalması:

 
    $$h = \frac{2 \sigma \cos\theta}{\rho g R} = \frac{4 \sigma \cos\theta}{\gamma D}$$
    Burada \(\theta\) temas açısıdır. Su-cam için \(\theta \approx 0^\circ\) (\(h > 0\), yükselme - ıslatan sıvı), Cıva-cam için \(\theta \approx 130^\circ\) (\(h  

  

# BÖLÜM 2: AKIŞKANLAR STATİĞİ (HİDROSTATİK)

### 2.1 Basınç ve Temel Hidrostatik Denklemi

Durgun bir akışkanda kayma gerilmesi sıfırdır (\(\tau = 0\)). Bir noktadaki basınç tüm doğrultularda eşittir (Pascal İlkesi). Yalnızca yerçekimi ivmesi etkisi altındaki durgun sıkıştırılamaz akışkanda:

 
    $$\frac{dP}{dz} = -\gamma = -\rho g \implies P = P_0 + \gamma h$$
    $$P_{\text{mutlak}} = P_{\text{etkin}} + P_{\text{atm}}$$
 

### 2.2 Manometreler ve Basınç Ölçümü

 
    
* **Piezometre:** Düşük basınçlı sıvılar için atmosfere açık düşey tüptür: \(P = \gamma h\).
    
* **U-Tüplü Manometre:** Ağır bir sıvı (cıva) kullanılarak orta ve yüksek basınçların ölçülmesidir.
    
* **Diferansiyel Manometre:** İki boru veya hazne arasındaki basınç farkını ölçer. Hesap kuralı: *"Aynı sürekli akışkan içinde aynı yatay seviyedeki basınçlar eşittir. Aşağı inildikçe \(\gamma h\) eklenir, yukarı çıkıldıkça \(\gamma h\) çıkarılır."*
 

### 2.3 Düzlem Yüzeylere Gelen Hidrostatik Kuvvet ve Basınç Merkezi

 
    **Bileşke Hidrostatik Kuvvet (\(F_R\)):**
    $$F_R = P_G \cdot A = (\gamma \cdot h_G) \cdot A$$
    **Basınç Merkezinin Konumu (\(y_P\)):**
    $$y_P = y_G + \frac{I_{xx,G}}{y_G \cdot A}$$
    $$x_P = x_G + \frac{I_{xy,G}}{y_G \cdot A}$$
    Burada:
     
        
* \(h_G\): Yüzeyin ağırlık merkezinin serbest su yüzeyine düşey derinliği
        
* \(y_G\): Yüzey doğrultusu boyunca serbest su yüzeyi eksenine olan eğik mesafe
        
* \(I_{xx,G}\): Ağırlık merkezinden geçen yatay eksene göre atalet momenti (Dikdörtgen için \(b h^3 / 12\), Daire için \(\pi D^4 / 64\))
     
    *Önemli Kural:* Basınç merkezi (\(P\)), hidrostatik basınç derinlikle arttığı için daima ağırlık merkezinin (\(G\)) altındadır (\(y_P > y_G\)).
 

### 2.4 Eğri Yüzeylere Gelen Hidrostatik Kuvvetler

Eğri yüzeylerde basınç vektörlerinin yönü sürekli değiştiğinden kuvvet bileşenlerine ayrılır:

 
    
* **Yatay Bileşen (\(F_x\)):** Eğri yüzeyin düşey düzlem izdüşüm alanına etkiyen kuvvettir: \(F_x = \gamma \cdot h_{Gx} \cdot A_{\text{düşey}}\).
    
* **Düşey Bileşen (\(F_y\)):** Eğri yüzey ile serbest su yüzeyi arasında kalan gerçek veya hayali akışkan hacminin ağırlığıdır: \(F_y = \gamma \cdot V_{\text{hacim}}\). (Sıvı yüzeyin üstündeyse aşağı doğru, altındaysa yukarı doğrudur).
    
* **Bileşke Kuvvet ve Doğrultusu:** \(F_R = \sqrt{F_x^2 + F_y^2}\), \(\tan\theta = F_y / F_x\). Dairesel silindirik kapaklarda hidrostatik basınç kuvveti daima eğrilik merkezinden geçer.
 

### 2.5 Kaldırma Kuvveti (Arşimet Prensibi) ve Kararlılık (Stabilite)

 
    **Kaldırma Kuvveti (\(F_B\)):**
    $$F_B = \gamma_{\text{akışkan}} \cdot V_{\text{batan}} = \rho_{\text{akışkan}} g V_{\text{batan}}$$
    Kaldırma kuvveti, batan hacmin ağırlık merkezine (Kaldırma Merkezi - \(B\)) etki eder.
 

**Yüzen Cisimlerin Kararlılığı:**

 
    
* Bir cisim devrilme açısı (\(\theta\)) kadar eğildiğinde, batan hacmin geometrisi değişir ve kaldırma merkezi \(B\) noktasından \(B'\) noktasına kayar. Kaldırma kuvvetinin düşey etki çizgisinin cisim simetri eksenini kestiği noktaya **Metasantr Noktası (\(M\))** denir.
    
* **Metasantrik Yükseklik (\(\overline{GM}\)):**
        $$\overline{GM} = \overline{BM} - \overline{BG} = \frac{I_{yy}}{V_{\text{batan}}} - \overline{BG}$$
        Burada \(I_{yy}\), cismin su hattı kesit alanının eğilme eksenine göre atalet momentidir.
    
    
* \(\overline{GM} > 0\) (\(M\) noktası \(G\)'nin üstünde): **Kararlı Denge** (Doğrultucu moment oluşur).
    
* \(\overline{GM} = 0\) (\(M\) ile \(G\) çakışık): **Nötr Denge**.
    
* \(\overline{GM}  

  

# BÖLÜM 3: RİJİT CİSİM HAREKETİ YAPAN SIVILAR

Akışkan içeren bir kap ivmeli hareket yaptığında veya sabit açısal hızla döndüğünde, akışkan tabakaları arasında bağıl hareket yoksa kayma gerilmesi oluşmaz (\(\tau = 0\)). Sıvı rijit bir cisim gibi davranır ve hidrostatik kuralları uygulanabilir.

### 3.1 Doğrusal İvmeli Hareket Yapan Kaplar

Kap \(a_x\) yatay ve \(a_z\) düşey ivmeleriyle hareket ederken hareket denklemleri:

 
    $$\frac{\partial P}{\partial x} = -\rho a_x, \quad \frac{\partial P}{\partial y} = 0, \quad \frac{\partial P}{\partial z} = -\rho (g + a_z)$$
    Eşbasınç yüzeylerinin ve serbest sıvı yüzeyinin yatayla yaptığı eğim (\(\theta\)):
    $$\tan\theta = \frac{dz}{dx} = -\frac{a_x}{g + a_z}$$
    İki nokta arasındaki basınç farkı:
    $$P_2 - P_1 = -\rho a_x (x_2 - x_1) - \rho (g + a_z) (z_2 - z_1)$$
 

### 3.2 Düşey Eksen Etrafında Sabit Açısal Hızla Dönen Silindirik Kaplar

\(R\) yarıçaplı silindirik bir kap düşey \(z\) ekseni etrafında \(\omega\) açısal hızıyla \([\text{rad/s}]\) döndürüldüğünde, merkezkaç ivmesi nedeniyle sıvı çeperlere doğru yükselir ve merkezde çökerek bir dönel paraboloid oluşturur:

 
    $$\frac{\partial P}{\partial r} = \rho r \omega^2, \quad \frac{\partial P}{\partial z} = -\rho g$$
    **Serbest Yüzey Paraboloid Denklemi:**
    $$z(r) = z_0 + \frac{\omega^2 r^2}{2g}$$
    Burada \(z_0\), dönme eksenindeki (\(r = 0\)) minimum su yüksekliğidir.

    **Önemli Geometrik Özellik:** Sıvı taşmıyorsa hacmin korunumu ilkesine göre, paraboloidin tepe noktasındaki çökme miktarı (\(h_0\)), çeperdeki yükselme miktarına (\(h_R\)) eşittir:
    $$z(R) - z_{\text{durgun}} = z_{\text{durgun}} - z_0 = \frac{\omega^2 R^2}{4g}$$
    Tabandaki basınç dağılımı: \(P(r) = P_0 + \rho g z_0 + \frac{1}{2} \rho \omega^2 r^2\).
 

  

# BÖLÜM 4: AKIŞKANLAR KİNEMATİĞİ

### 4.1 Akış Alanı Tanımları: Lagrange ve Euler Yaklaşımları

 
    
* **Lagrange Yaklaşımı:** Her bir akışkan parçacığının uzaydaki konumu ve hızı zaman içinde tek tek takip edilir: \(\vec{r} = \vec{r}(t)\).
    
* **Euler Yaklaşımı:** Akışkanlar mekaniğinde standart kullanılan yaklaşımdır. Belirli bir kontrol hacmine veya uzaydaki sabit noktalara odaklanılır ve bu noktalardan geçen akışkanın hız alanı \(\vec{V}(x, y, z, t)\), basınç alanı \(P(x, y, z, t)\) incelenir.
 

### 4.2 Maddesel (Maddi) Türev ve İvme Alanı

Euler yaklaşımında bir akışkan parçacığının toplam ivmesi, zamana bağlı yerel ivme ile konuma bağlı konvektif (taşınımsal) ivmenin toplamıdır:

 
    $$\frac{D\vec{V}}{Dt} = \underbrace{\frac{\partial \vec{V}}{\partial t}}_{\text{Yerel İvme}} + \underbrace{(\vec{V} \cdot \nabla)\vec{V}}_{\text{Konvektif İvme}} = \frac{\partial \vec{V}}{\partial t} + u \frac{\partial \vec{V}}{\partial x} + v \frac{\partial \vec{V}}{\partial y} + w \frac{\partial \vec{V}}{\partial z}$$
 

### 4.3 Akış Çizgileri ve Görselleştirme

 
    
* **Akım Çizgisi (Streamline):** Her noktasındaki teğeti o andaki hız vektörüne paralel olan eğridir: \(\frac{dx}{u} = \frac{dy}{v} = \frac{dz}{w}\).
    
* **Yörünge Çizgisi (Pathline):** Belirli bir akışkan parçacığının belirli bir zaman aralığında kat ettiği gerçek fiziksel yoldur.
    
* **Çıkış / İz Çizgisi (Streakline):** Uzayda sabit bir noktadan (örn: duman/boya enjektörü) ardışık olarak geçen tüm parçacıkların oluşturduğu anlık çizgidir.
    
* *Not:* Kararlı (steady) akımlarda akım çizgisi, yörünge çizgisi ve iz çizgisi birbiriyle çakışır.
 

### 4.4 Akış Deformasyonu, Girdaplık ve Akım Fonksiyonu

 
    
* **Hacimsel Genleşme Hızı:** \(\nabla \cdot \vec{V} = \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z}\) (Sıkıştırılamaz akışta sıfırdır).
    
* **Girdaplık Vektörü (Vorticity - \(\vec{\zeta}\)):** Akışkanın dönme hızının iki katıdır:
        $$\vec{\zeta} = \nabla \times \vec{V} = 2 \vec{\omega}$$
        \(\vec{\zeta} = 0\) olan akımlara **Girdapsız (İrrotasyonel) Akım** denir.
    
    
* **Hız Potansiyeli (\(\phi\)):** Girdapsız akımlarda hız vektörü bir skaler potansiyelin gradyanı olarak yazılabilir: \(\vec{V} = \nabla \phi\). Sıkıştırılamazsa Laplace denklemini sağlar: \(\nabla^2 \phi = 0\).
    
* **Akım Fonksiyonu (\(\psi\)):** 2-boyutlu sıkıştırılamaz akışlarda süreklilik denklemini otomatik sağlayan fonksiyondur:
        $$u = \frac{\partial \psi}{\partial y}, \quad v = -\frac{\partial \psi}{\partial x}$$
        İki akım çizgisi arasındaki debi: \(q = \psi_2 - \psi_1\).
    
 

  

# BÖLÜM 5: REYNOLDS TRANSPORT TEOREMİ VE İNTEGRAL KORUNUM YASALARI

### 5.1 Reynolds Transport Teoremi (RTT)

Termodinamik ve fizikte temel yasalar sabit kütleli kapalı sistemler için tanımlanmıştır. Mühendislikte ise kütle giriş-çıkışının olduğu kontrol hacimleri (\(CV\)) incelenir. RTT, sistem türevi ile kontrol hacmi arasındaki temel dönüşüm köprüsüdür:

 
    **Genel RTT Formülasyonu:**
    $$\frac{dB_{\text{sys}}}{dt} = \frac{d}{dt} \int_{CV} \rho b \, dV + \int_{CS} \rho b (\vec{V}_r \cdot \vec{n}) \, dA$$
    Burada \(B\) herhangi bir yaygın özellik (kütle, momentum, enerji), \(b = B/m\) ise birim kütledeki yoğun özelliktir. \(\vec{V}_r\) kontrol yüzeyine göre bağıl hızdır.
 

### 5.2 Kütlenin Korunumu (Süreklilik Denklemi)

\(B = m\) ve \(b = 1\) alındığında sistem kütlesi sabit olduğundan (\(dm_{\text{sys}}/dt = 0\)):

 
    $$\frac{d}{dt} \int_{CV} \rho \, dV + \int_{CS} \rho (\vec{V} \cdot \vec{n}) \, dA = 0$$
    Kararlı ve sıkıştırılamaz akımlarda:
    $$\sum \dot{m}_{\text{giriş}} = \sum \dot{m}_{\text{çıkış}} \implies Q_1 = Q_2 \implies A_1 V_1 = A_2 V_2$$
 

### 5.3 Çizgisel Momentum Denklemi

\(B = m \vec{V}\) ve \(b = \vec{V}\) alındığında Newton'un 2. Yasası (\(\sum \vec{F} = d(m\vec{V})/dt\)):

 
    $$\sum \vec{F} = \frac{d}{dt} \int_{CV} \vec{V} \rho \, dV + \int_{CS} \vec{V} \rho (\vec{V} \cdot \vec{n}) \, dA$$
    Kararlı akışta kontrol hacmine etki eden net kuvvet:
    $$\sum \vec{F} = \sum (\dot{m} \vec{V})_{\text{çıkış}} - \sum (\dot{m} \vec{V})_{\text{giriş}}$$
    $$\sum F_x = \dot{m} (V_{2x} - V_{1x}) + P_1 A_1 \cos\theta_1 - P_2 A_2 \cos\theta_2 + R_x$$
    Burada \(\sum \vec{F}\); yüzey kuvvetleri (basınç kuvvetleri, cidar tutucu kuvveti \(R\)) ve kütle kuvvetlerini (yerçekimi ağırlığı \(W\)) içerir.
 

### 5.4 Açısal Momentum Denklemi

 
    $$\sum \vec{M} = \sum (\vec{r} \times \vec{V})_{\text{çıkış}} \dot{m} - \sum (\vec{r} \times \vec{V})_{\text{giriş}} \dot{m}$$
    Radyal türbin ve pompa çarklarında (Euler Türbin Denklemi): Mil torku \(T_{\text{mil}} = \dot{m} (r_2 V_{\theta 2} - r_1 V_{\theta 1})\).
 

  

# BÖLÜM 6: DİFERANSİYEL ANALİZ VE NAVIER-STOKES DENKLEMLERİ

### 6.1 Diferansiyel Süreklilik Denklemi

 
    $$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{V}) = 0$$
    Kartezyen koordinatlarda sıkıştırılamaz akış (\(\rho = \text{sabit}\)) için:
    $$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$$
 

### 6.2 Navier-Stokes Denklemleri (Sıkıştırılamaz Newtonyen Akışkan)

Doğrusal momentumun diferansiyel kontrol hacmine uygulanmasıyla elde edilen akışkanlar mekaniğinin ana hareket denklemidir:

 
    $$\rho \frac{D\vec{V}}{Dt} = -\nabla P + \rho \vec{g} + \mu \nabla^2 \vec{V}$$
    Bileşenler halinde (Kartezyen):
    $$x\text{-yönü: } \rho \left( \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} \right) = -\frac{\partial P}{\partial x} + \rho g_x + \mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right)$$
    $$y\text{-yönü: } \rho \left( \frac{\partial v}{\partial t} + u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} + w \frac{\partial v}{\partial z} \right) = -\frac{\partial P}{\partial y} + \rho g_y + \mu \left( \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} + \frac{\partial^2 v}{\partial z^2} \right)$$
    $$z\text{-yönü: } \rho \left( \frac{\partial w}{\partial t} + u \frac{\partial w}{\partial x} + v \frac{\partial w}{\partial y} + w \frac{\partial w}{\partial z} \right) = -\frac{\partial P}{\partial z} + \rho g_z + \mu \left( \frac{\partial^2 w}{\partial x^2} + \frac{\partial^2 w}{\partial y^2} + \frac{\partial^2 w}{\partial z^2} \right)$$
 

### 6.3 Özel İndirgemeler ve Tam Analitik Çözümler

 
    
* **Euler Denklemi:** Viskozite ihmal edildiğinde (\(\mu = 0\)): \(\rho \frac{D\vec{V}}{Dt} = -\nabla P + \rho \vec{g}\).
    
* **Couette Akışı (İki plaka arası kesme akışı):** Alt plaka sabit, üst plaka \(U\) hızıyla çekildiğinde basınç gradyansız laminer akış:
        $$u(y) = U \frac{y}{h}, \quad \tau = \mu \frac{U}{h} = \text{sabit}$$
    
    
* **Poiseuille Akışı (Sabit iki plaka arası basınç tahrikli akış):**
        $$u(y) = \frac{1}{2\mu} \left(-\frac{dP}{dx}\right) (h y - y^2)$$
        Hız profili paraboliktir; maksimum hız kanal merkezindedir (\(y = h/2\)): \(u_{\max} = 1.5 V_{\text{ort}}\).
    
 

  

# BÖLÜM 7: BERNOULLİ DENKLEMİ VE UYGULAMALARI

### 7.1 Bernoulli Denklemi ve Kısıtları

Euler denkleminin bir akım çizgisi boyunca integrali alınarak elde edilir:

 
    $$\frac{P_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + z_2 = \text{sabit}$$
    **Kullanım Kısıtları:**
     
        
* Sürtünmesiz akış (\(\mu \approx 0\), viskoz kayıplar ihmal).
        
* Kararlı akış (\(\partial / \partial t = 0\)).
        
* Sıkıştırılamaz akış (\(\rho = \text{sabit}\)).
        
* Aynı akım çizgisi boyunca uygulanmalıdır (akım dönmesiz ise tüm akış alanında geçerlidir).
        
* Isı transferi, pompa/türbin gibi mil işi olmamalıdır.
     
 

### 7.2 Basınç Türleri ve Pitot-Statik Tüpü

 
    
* **Statik Basınç (\(P\)):** Akışkanın termodinamik gerçek basıncıdır (çeperdeki piezometre ile ölçülür).
    
* **Dinamik Basınç (\(\frac{1}{2}\rho V^2\)):** Akış kinetik enerjisinin basınca dönüşmüş halidir.
    
* **Durgunluk (Stagnation) Basıncı (\(P_0\)):** Akışkanın sürtünmesiz durdurulduğu noktadaki toplam basınçtır: \(P_0 = P + \frac{1}{2}\rho V^2\).
    
* **Pitot-Statik Tüpü Hız Ölçümü:**
        $$V = \sqrt{\frac{2(P_0 - P)}{\rho}} = \sqrt{\frac{2 \Delta P}{\rho}} = \sqrt{2 g \Delta h \left(\frac{\rho_{\text{man}}}{\rho} - 1\right)}$$
    
 

### 7.3 Venturimetre, Orifis ve Boşalma Katsayısı

Boru hatlarında debi ölçümü için daralan enkesit oluşturulup basınç farkı ölçülür:

 
    **Teorik Debi:**
    $$Q_{\text{teorik}} = A_2 \sqrt{\frac{2 (P_1 - P_2) / \rho}{1 - (A_2 / A_1)^2}} = A_2 \sqrt{\frac{2 g \Delta h}{1 - (D_2 / D_1)^4}}$$
    **Gerçek Debi ve Boşalma Katsayısı (\(C_d\)):**
    $$Q_{\text{gerçek}} = C_d \cdot Q_{\text{teorik}}$$
    Venturimetreler için \(C_d \approx 0.96 - 0.98\) (akış çizgileri yumuşaktır, kayıp çok azdır). Orifisler için \(C_d \approx 0.60 - 0.65\) (akış ayrılması ve vena contracta daralması nedeniyle kayıp fazladır).
 

### 7.4 Toricelli Teoremi ve Kavitasyon Riski

Büyük bir açık depodan \(h\) derinliğindeki bir orifisten serbest ortama boşalan sıvının hızı: \(V = \sqrt{2gh}\).

**Kavitasyon:** Akış alanında hızın aşırı arttığı bölgelerde (örn: venturi boğazı, pompa emiş ağzı, orifis) yerel basınç sıvının o sıcaklıktaki doymuş buhar basıncına (\(P_v\)) düşerse (\(P \le P_v\)) sıvı kaynayarak buhar kabarcıkları oluşturur. Bu kabarcıklar yüksek basınç bölgesine ulaştığında şiddetle patlayarak mekanik hasara, gürültüye ve erozyona yol açar.

  

# BÖLÜM 8: BOYUT ANALİZİ VE BENZEŞİM

### 8.1 Birim Homojenliği ve Buckingham Pi Teoremi

Fiziksel bir olay \(n\) adet parametre (\(q_1, q_2, \dots, q_n\)) ile tanımlanıyorsa ve bu parametreler \(m\) adet temel boyut (Kütle \(M\), Uzunluk \(L\), Zaman \(T\) veya Kuvvet \(F\), \(L\), \(T\)) içeriyorsa, bu olay \((n - m)\) adet bağımsız boyutsuz \(\Pi\) grubu ile ifade edilebilir:

 
    $$\Pi_1 = f(\Pi_2, \Pi_3, \dots, \Pi_{n-m})$$
 

### 8.2 Tekrarlanan Değişkenler Yöntemi Algoritması

 
    
* Olayı etkileyen tüm değişkenleri (\(n\)) ve temel boyutlarını listele.
    
* Temel boyut sayısını (\(m\)) belirle.
    
* \(m\) adet tekrarlanan değişken seç (Kurallar: Biri geometrik büyüklük örn: \(D\), biri kinematik büyüklük örn: \(V\), biri dinamik büyüklük örn: \(\rho\) olmalıdır; kendi aralarında boyutsuz grup oluşturamazlar).
    
* Kalan her bir değişkeni tekrarlanan değişkenlerin üsleri ile çarparak boyutsuz \(\Pi\) gruplarını oluştur (\(\Pi = q_i \cdot D^a V^b \rho^c\)). Boyutsuzluk şartından (\(M^0 L^0 T^0\)) üsleri çöz.
 

### 8.3 Önemli Boyutsuz Parametreler ve Fiziksel Anlamları

 
     
         Boyutsuz Sayı 
         Formül 
         Kuvvetler Oranı 
         Önemli Olduğu Akış Alanları 
     
     
         **Reynolds (\(Re\))** 
         \(\frac{\rho V L}{\mu} = \frac{V L}{\nu}\) 
         \(\frac{\text{Atalet Kuvveti}}{\text{Viskozite Kuvveti}}\) 
         Borular, kanatlar, denizaltılar, tüm sürtünmeli iç/dış akışlar 
     
     
         **Froude (\(Fr\))** 
         \(\frac{V}{\sqrt{g L}}\) 
         \(\frac{\text{Atalet Kuvveti}}{\text{Yerçekimi Kuvveti}}\) 
         Açık kanallar, gemi dalga direnci, savaklar, baraj dolu savakları 
     
     
         **Euler (\(Eu\))** 
         \(\frac{\Delta P}{\rho V^2}\) 
         \(\frac{\text{Basınç Kuvveti}}{\text{Atalet Kuvveti}}\) 
         Basınç düşüşleri, kavitasyon incelemeleri 
     
     
         **Mach (\(Ma\))** 
         \(\frac{V}{c}\) 
         \(\frac{\text{Atalet Kuvveti}}{\text{Sıkıştırılabilirlik}}\) 
         Yüksek hızlı gaz akımları, havacılık (\(Ma > 0.3\)) 
     
     
         **Weber (\(We\))** 
         \(\frac{\rho V^2 L}{\sigma}\) 
         \(\frac{\text{Atalet Kuvveti}}{\text{Yüzey Gerilimi}}\) 
         Damlacık oluşumu, püskürtme memeleri, kılcal dalgalar 
     
 

### 8.4 Benzeşim Türleri ve Model Ölçekleme

Bir model (\(m\)) ile gerçek prototip (\(p\)) arasında tam dinamik benzerlik için:

 
    
* **Geometrik Benzerlik:** Tüm doğrusal boyutlar sabit bir \(\lambda_L = L_p / L_m\) ölçeği ile orantılı olmalıdır.
    
* **Kinematik Benzerlik:** Karşılıklı noktalardaki hız vektörlerinin yönü aynı, oranları sabit (\(\lambda_V\)) olmalıdır.
    
* **Dinamik Benzerlik:** Etki eden tüm kuvvetlerin oranları eşit olmalıdır. Bunun için baskın boyutsuz sayılar eşitlenir:
         
             *Boru ve hava aracı testlerinde:* \(Re_m = Re_p \implies \frac{V_m L_m}{\nu_m} = \frac{V_p L_p}{\nu_p}\).
            
* *Gemi modeli ve açık kanal testlerinde:* \(Fr_m = Fr_p \implies \frac{V_m}{\sqrt{g L_m}} = \frac{V_p}{\sqrt{g L_p}} \implies \lambda_V = \sqrt{\lambda_L}\). Debi ölçeği: \(\lambda_Q = \lambda_A \lambda_V = \lambda_L^{5/2}\).
         
     
 

  

# BÖLÜM 9: BORULARDA İÇ AKIŞLAR VE HİDROLİK KAYIPLAR

### 9.1 Giriş Bölgesi ve Tam Gelişmiş Akış

Boru girişinde cidar sürtünmesi nedeniyle sınır tabaka kalınlaşır ve merkezde birleşir. Hidrodinamik giriş uzunluğundan (\(L_h\)) sonra hız profili eksen boyunca değişmez (tam gelişmiş akış):

 
    
* Laminer akımda: \(L_{h,\text{laminer}} \approx 0.05 \cdot Re \cdot D\)
    
* Türbülanslı akımda: \(L_{h,\text{türb}} \approx 10 D - 60 D\)
 

### 9.2 Dairesel Boruda Tam Gelişmiş Laminer Akım (Hagen-Poiseuille)

 
    **Hız Dağılımı:**
    $$u(r) = 2 V_{\text{ort}} \left( 1 - \frac{r^2}{R^2} \right) = u_{\max} \left( 1 - \frac{r^2}{R^2} \right) \implies u_{\max} = 2 V_{\text{ort}}$$
    **Basınç Düşüşü ve Sürtünme Faktörü:**
    $$\Delta P = \frac{32 \mu L V_{\text{ort}}}{D^2} \implies f = \frac{64}{Re}$$
 

### 9.3 Türbülanslı Akım ve Darcy-Weisbach Denklemi

Boru boyunca viskoz sürtünmeden kaynaklanan sürekli yük kaybı:

 
    $$h_f = f \frac{L}{D} \frac{V^2}{2g}$$
    Burada \(f\) sürtünme faktörüdür:
     
        
* Laminer akış: \(f = 64/Re\)
        
* Türbülanslı akış (Colebrook Denklemi):
            $$\frac{1}{\sqrt{f}} = -2.0 \log_{10} \left( \frac{\epsilon / D}{3.7} + \frac{2.51}{Re \sqrt{f}} \right)$$
        
        
* İterasyonsuz hesap için **Haaland Yaklaşımı:**
            $$\frac{1}{\sqrt{f}} \approx -1.8 \log_{10} \left[ \left(\frac{\epsilon/D}{3.7}\right)^{1.11} + \frac{6.9}{Re} \right]$$
        
     
 

### 9.4 Yerel Yük Kayıpları

Armatürler, dirsekler ve vanalardaki girdap kayıpları:

 
    $$h_m = K_L \frac{V^2}{2g}$$
    Toplam kayıp: \(h_L = h_f + \sum h_m = \left( f \frac{L}{D} + \sum K_L \right) \frac{V^2}{2g}\).
 

### 9.5 Boru Sistemleri, EGL/HGL ve Su Darbesi

 
    
* **Enerji Eğim Çizgisi (EGL):** \(EGL = \frac{P}{\gamma} + \frac{V^2}{2g} + z\). Daima akış yönünde kayıp miktarınca aşağı eğimlidir (pompa olan yerde yukarı sıçrar, türbinde düşer).
    
* **Hidrolik Eğim Çizgisi (HGL):** \(HGL = \frac{P}{\gamma} + z\). EGL'nin \(V^2/(2g)\) kadar altındadır. Boru HGL'nin altına düşerse pozitif basınçtadır; boru HGL'nin üzerine çıkarsa negatif basınç (vakum/sifon) oluşur.
    
* **Seri Borular:** \(Q = \text{sabit}\), \(h_{L,\text{toplam}} = h_{L1} + h_{L2} + \dots\)
    
* **Paralel Borular:** \(h_{L1} = h_{L2} = \dots = h_{L}\), \(Q_{\text{toplam}} = Q_1 + Q_2 + \dots\)
    
* **Su Darbesi (Water Hammer):** Hızlı vana kapanmasında kinetik enerjinin basınç dalgasına dönüşmesidir. Joukowsky formülü:
        $$\Delta P = \rho \cdot c \cdot \Delta V$$
    
 

  

# BÖLÜM 10: DIŞ AKIŞLAR VE SINIR TABAKA TEORİSİ

### 10.1 Sınır Tabaka Kavramı ve Kalınlık Tanımları

Yüksek Reynolds sayılarında viskoz etkiler yalnızca katı cidarın hemen yanındaki ince bir sınır tabaka içinde yoğunlaşır; dış bölgede akış sürtünmesiz (potansiyel) kabul edilir.

 
    
* **Sınır Tabaka Kalınlığı (\(\delta\)):** Hızın serbest akım hızının %99'una ulaştığı (\(u = 0.99 U\)) mesafedir.
    
* **Yer Değiştirme Kalınlığı (\(\delta^*\)):** Sınır tabakadaki debi azalmasını telafi etmek için akım çizgilerinin ötelenme miktarıdır:
        $$\delta^* = \int_0^\infty \left(1 - \frac{u}{U}\right) dy$$
    
    
* **Momentum Kalınlığı (\(\theta\)):** Sınır tabaka sürtünmesinden kaynaklanan momentum kaybı kalınlığıdır:
        $$\theta = \int_0^\infty \frac{u}{U} \left(1 - \frac{u}{U}\right) dy$$
    
 

### 10.2 Düz Levha Üzerinde Laminer Akım (Blasius Çözümü)

 
    $$Re_x = \frac{U x}{\nu}  

### 10.3 Sürükleme (Drag) ve Taşıma (Lift) Kuvvetleri

 
    **Sürükleme Kuvveti:**
    $$F_D = \frac{1}{2} C_D \rho A V^2$$
    **Taşıma Kuvveti:**
    $$F_L = \frac{1}{2} C_L \rho A V^2$$
    Toplam sürükleme = Yüzey sürtünme sürüklemesi + Basınç (biçim) sürüklemesi. Küt cisimlerde (küre, silindir) akış ayrılması nedeniyle basınç sürüklemesi baskındır.
 

  

# BÖLÜM 11: AÇIK KANAL HİDROLİĞİ

### 11.1 Geometri ve Manning Denklemi

 
    $$R_h = \frac{A}{P} \quad [\text{m}]$$
    **Manning Denklemi (Üniform Akış):**
    $$V = \frac{1}{n} R_h^{2/3} S_0^{1/2} \quad [\text{m/s}], \quad Q = \frac{1}{n} A R_h^{2/3} S_0^{1/2} \quad [\text{m}^3/\text{s}]$$
 

### 11.2 En Ekonomik (En Verimli) Hidrolik Enkesitler

Verilen bir debiyi minimum ıslak çevre (\(P\)) ve minimum kazı alanı ile geçiren kesittir:

 
    
* **Dikdörtgen Kanal:** Genişlik derinliğin iki katı olmalıdır: \(b = 2y\), \(R_h = y/2\).
    
* **Yamuk Kanal:** Yarı altıgen kesittir: Kenar şev eğimi \(\theta = 60^\circ\) (\(1:\sqrt{3}\)), \(R_h = y/2\).
 

### 11.3 Özgül Enerji, Froude Sayısı ve Kritik Akım

 
    $$E = y + \frac{V^2}{2g} = y + \frac{Q^2}{2g A^2}$$
    **Kritik Akım Koşulu (\(E = E_{\min}\)):**
    $$\frac{Q^2 T}{g A^3} = 1 \iff Fr = \frac{V}{\sqrt{g y_h}} = 1 \quad \left(y_h = \frac{A}{T}\right)$$
    Dikdörtgen kanalda birim genişlik debisi \(q = Q/b\) olmak üzere:
    $$y_c = \sqrt[3]{\frac{q^2}{g}}, \quad V_c = \sqrt{g y_c}, \quad E_{\min} = 1.5 y_c$$
 

### 11.4 Hidrolik Sıçrama (Bélanger Denklemi)

Kanalda sel rejiminden (\(Fr_1 > 1\)) nehir rejimine (\(Fr_2  
    $$\frac{y_2}{y_1} = \frac{1}{2} \left( \sqrt{1 + 8 Fr_1^2} - 1 \right)$$
    Sıçramadaki yük kaybı:
    $$\Delta E = E_1 - E_2 = \frac{(y_2 - y_1)^3}{4 y_1 y_2}$$
 

  

# BÖLÜM 12: ADIM ADIM ÇÖZÜMLÜ 10 KLASİK SINAV PROBLEMİ

 
    

#### PROBLEM 1: Çok Sıvılı Diferansiyel U-Manometresi

    

A borusunda yağ (\(SG_1 = 0.88\)) ve B borusunda su (\(SG_2 = 1.0\)) akmaktadır. İki boru arasına bağlanan U-manometresinde cıva (\(SG_{\text{cıva}} = 13.6\)) kullanılmaktadır. A borusu merkezinin sol manometre kolundaki cıva seviyesine mesafesi \(h_1 = 30\text{ cm}\), manometredeki cıva sütunu farkı \(h_2 = 20\text{ cm}\), sağ koldaki cıva seviyesinin B borusu merkezine mesafesi \(h_3 = 15\text{ cm}\)'dir. A ve B boruları arasındaki basınç farkını (\(P_A - P_B\)) \([\text{kPa}]\) hesaplayınız.

    

**ÇÖZÜM:**

    

Sol koldaki alt cıva seviyesinden başlayarak hidrostatik denklemi yazalım:

    $$P_A + \gamma_{\text{yağ}} h_1 + \gamma_{\text{cıva}} h_2 - \gamma_{\text{su}} (h_3 + h_2) = P_B$$
    $$P_A - P_B = \gamma_{\text{su}} (h_3 + h_2) - \gamma_{\text{yağ}} h_1 - \gamma_{\text{cıva}} h_2$$
    Sayısal değerleri yerine koyalım (\(\gamma_{\text{su}} = 9.81\text{ kN/m}^3\)):
    $$\gamma_{\text{yağ}} = 0.88 \times 9.81 = 8.633\text{ kN/m}^3, \quad \gamma_{\text{cıva}} = 13.6 \times 9.81 = 133.416\text{ kN/m}^3$$
    $$P_A - P_B = [9.81 \times (0.15 + 0.20)] - [8.633 \times 0.30] - [133.416 \times 0.20]$$
    $$P_A - P_B = 3.4335 - 2.590 - 26.683 = \mathbf{-25.84\text{ kPa}} \quad (P_B - P_A = 25.84\text{ kPa})$$
 

 
    

#### PROBLEM 2: Eğimli Dairesel Kapağa Gelen Hidrostatik Kuvvet ve Basınç Merkezi

    

Yatayla \(\theta = 45^\circ\) açı yapan eğimli bir rezervuar duvarında \(D = 2\text{ m}\) çapında dairesel bir kapak bulunmaktadır. Kapağın ağırlık merkezi serbest su yüzeyinden düşey olarak \(h_G = 5\text{ m}\) derinliktedir. Kapağa gelen toplam hidrostatik kuvveti ve basınç merkezinin ağırlık merkezine olan mesafesini bulunuz. (\(\gamma_{\text{su}} = 9.81\text{ kN/m}^3\))

    

**ÇÖZÜM:**

    

1. Kapak Alanı: \(A = \frac{\pi D^2}{4} = \frac{\pi (2)^2}{4} = \pi \approx 3.1416\text{ m}^2\).

    

2. Toplam Hidrostatik Kuvvet:

    $$F_R = \gamma h_G A = 9.81\text{ kN/m}^3 \times 5\text{ m} \times 3.1416\text{ m}^2 = \mathbf{154.1\text{ kN}}$$
    

3. Kapağın eğik düzlem boyunca serbest yüzeye mesafesi (\(y_G\)):

    $$y_G = \frac{h_G}{\sin 45^\circ} = \frac{5}{\sqrt{2}/2} = 5\sqrt{2} \approx 7.071\text{ m}$$
    

4. Dairenin kendi merkezine göre atalet momenti: \(I_{xx,G} = \frac{\pi D^4}{64} = \frac{\pi (2)^4}{64} = \frac{\pi}{4} \approx 0.7854\text{ m}^4\).

    

5. Basınç merkezinin ağırlık merkezine uzaklığı (\(y_P - y_G\)):

    $$y_P - y_G = \frac{I_{xx,G}}{y_G \cdot A} = \frac{0.7854}{7.071 \times 3.1416} = \frac{0.7854}{22.214} = \mathbf{0.0353\text{ m}} = \mathbf{3.53\text{ cm}}$$
 

 
    

#### PROBLEM 3: Dönen Silindirik Tankta Sıvı Yükselmesi ve Taşma Hesabı

    

Yarıçapı \(R = 0.5\text{ m}\), yüksekliği \(H = 1.8\text{ m}\) olan silindirik bir kap \(h_0 = 1.2\text{ m}\) yüksekliğine kadar suyla doludur. Kap düşey simetri ekseni etrafında döndürülmektedir. Suyun kenarlardan taşmaya başladığı andaki açısal hızı (\(\omega\)) \([\text{rad/s}]\) ve devir sayısını (\(N\)) \([\text{dev/dak}]\) bulunuz.

    

**ÇÖZÜM:**

    

Hacmin korunumu ilkesine göre, paraboloidin çeperdeki yükselme miktarı merkezdeki çökme miktarına eşittir. Taşma sınırında çeperdeki su yüksekliği tank boyuna ulaşır (\(z(R) = H = 1.8\text{ m}\)):

    $$\Delta z_{\text{yükselme}} = H - h_0 = 1.8 - 1.2 = 0.6\text{ m}$$
    Paraboloidin toplam derinliği: \(h_{\text{parabol}} = z(R) - z_0 = 2 \times \Delta z_{\text{yükselme}} = 2 \times 0.6 = 1.2\text{ m}\).
    $$h_{\text{parabol}} = \frac{\omega^2 R^2}{2g} \implies 1.2 = \frac{\omega^2 (0.5)^2}{2 \times 9.81}$$
    $$\omega^2 = \frac{1.2 \times 19.62}{0.25} = 94.176 \implies \omega = \mathbf{9.704\text{ rad/s}}$$
    $$N = \frac{60 \omega}{2\pi} = \frac{60 \times 9.704}{2\pi} = \mathbf{92.67\text{ d/d}}$$
 

 
    

#### PROBLEM 4: 2B Akışta Hız Potansiyeli ve Akım Fonksiyonu

    

Bir akış alanının hız bileşenleri \(u = 2xy\) ve \(v = a - y^2\) olarak verilmiştir.

    a) Bu akışın sıkıştırılamaz olması için \(a\) sabitine gerek var mıdır? Akış sıkıştırılamaz mıdır?

    b) Akış dönmesiz (irrotasyonel) midir?

    c) Akım fonksiyonunu (\(\psi\)) bulunuz.

    

**ÇÖZÜM:**

    

a) Süreklilik denklemi: \(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = \frac{\partial(2xy)}{\partial x} + \frac{\partial(a - y^2)}{\partial y} = 2y - 2y = 0\). Süreklilik denklemi her \(a\) değeri için sağlandığından akış **sıkıştırılamazdır**.

    

b) Dönme / Girdaplık: \(\zeta_z = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} = \frac{\partial(a - y^2)}{\partial x} - \frac{\partial(2xy)}{\partial y} = 0 - 2x = -2x \ne 0\). Akış \(x \ne 0\) için dönmelidir (irrotasyonel değildir).

    

c) Akım fonksiyonu: \(u = \frac{\partial \psi}{\partial y} = 2xy \implies \psi = x y^2 + f(x)\).

    $$v = -\frac{\partial \psi}{\partial x} = -(y^2 + f'(x)) = a - y^2 \implies -f'(x) = a \implies f(x) = -ax + C$$
    $$\psi(x, y) = \mathbf{x y^2 - a x + C}$$
 

 
    

#### PROBLEM 5: Açılı Boru Dirseğine Etki Eden Kuvvet (Momentum Denklemi)

    

Yatay düzlemde bulunan \(90^\circ\)'lik bir boru dirseğinde su (\(\rho = 1000\text{ kg/m}^3\)) akmaktadır. Dirsek giriş çapı \(D_1 = 300\text{ mm}\), çıkış çapı \(D_2 = 200\text{ mm}\)'dir. Girişteki debi \(Q = 0.30\text{ m}^3/\text{s}\) ve manometrik basınç \(P_1 = 200\text{ kPa}\)'dır. Dirsekte sürtünme kaybı ihmal edildiğinde dirseği yerinde tutmak için flanşlara etkiyen bileşke reaksiyon kuvvetini bulunuz.

    

**ÇÖZÜM:**

    

1. Kesit Alanları ve Hızlar:

    $$A_1 = \frac{\pi (0.3)^2}{4} = 0.0707\text{ m}^2, \quad V_1 = \frac{0.30}{0.0707} = 4.244\text{ m/s}$$
    $$A_2 = \frac{\pi (0.2)^2}{4} = 0.0314\text{ m}^2, \quad V_2 = \frac{0.30}{0.0314} = 9.554\text{ m/s}$$
    

2. Çıkış Basıncı (Yatay düzlemde \(z_1 = z_2\) için Bernoulli):

    $$P_2 = P_1 + \frac{1}{2}\rho (V_1^2 - V_2^2) = 200,000 + 500 \times (4.244^2 - 9.554^2) = 200,000 - 36,634 = 163,366\text{ Pa} \approx 163.4\text{ kPa}$$
    

3. Momentum Denklemi (\(\sum \vec{F} = \dot{m} (\vec{V}_2 - \vec{V}_1)\), \(\dot{m} = \rho Q = 300\text{ kg/s}\)):

    Giriş \(x\) yönünde (\(\vec{V}_1 = V_1 \hat{i}\)), çıkış \(y\) yönünde (\(\vec{V}_2 = V_2 \hat{j}\)):
    $$x\text{-yönü: } P_1 A_1 + R_x = \dot{m} (0 - V_1) \implies R_x = -P_1 A_1 - \dot{m} V_1$$
    $$R_x = -(200,000 \times 0.0707) - (300 \times 4.244) = -14,140 - 1,273 = \mathbf{-15.41\text{ kN}}$$
    $$y\text{-yönü: } -P_2 A_2 + R_y = \dot{m} (V_2 - 0) \implies R_y = P_2 A_2 + \dot{m} V_2$$
    $$R_y = (163,366 \times 0.0314) + (300 \times 9.554) = 5,130 + 2,866 = \mathbf{+8.00\text{ kN}}$$
    Bileşke Tutucu Kuvvet: \(R = \sqrt{R_x^2 + R_y^2} = \sqrt{(-15.41)^2 + (8.00)^2} = \mathbf{17.36\text{ kN}}\).
 

  

 
    

#### PROBLEM 6: Venturimetre ile Boruda Debi Ölçümü

    

İç çapı \(D_1 = 200\text{ mm}\) olan yatay bir boru hattına boğaz çapı \(D_2 = 100\text{ mm}\) olan bir Venturimetre bağlanmıştır. Giriş ve boğaz arasına bağlanan cıvalı (\(SG = 13.6\)) diferansiyel manometrede yükseklik farkı \(h = 22\text{ cm}\) okunmaktadır. Venturimetrenin boşalma katsayısı \(C_d = 0.98\) olduğuna göre borudan geçen su debisini (\(\text{L/s}\)) bulunuz.

    

**ÇÖZÜM:**

    

1. Basınç yükü farkı (\(\Delta h_w\)):

    $$\frac{P_1 - P_2}{\gamma_{\text{su}}} = h \left(\frac{\gamma_{\text{cıva}}}{\gamma_{\text{su}}} - 1\right) = 0.22\text{ m} \times (13.6 - 1) = 0.22 \times 12.6 = 2.772\text{ m su}$$
    

2. Boğaz Alanı ve Çap Oranı:

    $$A_2 = \frac{\pi (0.10)^2}{4} = 0.007854\text{ m}^2, \quad \frac{D_2}{D_1} = \frac{100}{200} = 0.5$$
    

3. Gerçek Debi Formülü:

    $$Q = C_d A_2 \sqrt{\frac{2 g \Delta h_w}{1 - (D_2/D_1)^4}} = 0.98 \times 0.007854 \times \sqrt{\frac{2 \times 9.81 \times 2.772}{1 - (0.5)^4}}$$
    $$Q = 0.007697 \times \sqrt{\frac{54.386}{1 - 0.0625}} = 0.007697 \times \sqrt{58.01} = 0.007697 \times 7.616 = \mathbf{0.0586\text{ m}^3/\text{s}} = \mathbf{58.6\text{ L/s}}$$
 

 
    

#### PROBLEM 7: Buckingham Pi Teoremi ile Basınç Düşüşü Bağıntısı

    

Yatay pürüzsüz bir dairesel boruda oluşan basınç düşüşünün (\(\Delta P\)); boru çapı (\(D\)), boru uzunluğu (\(L\)), akışkan hızı (\(V\)), akışkan yoğunluğu (\(\rho\)) ve dinamik viskozitesine (\(\mu\)) bağlı olduğu bilinmektedir. Buckingham Pi teoremini uygulayarak boyutsuz denklemi türetiniz.

    

**ÇÖZÜM:**

    

1. Değişkenler (\(n = 6\)): \(\Delta P, D, L, V, \rho, \mu\). Temel boyutlar (\(m = 3\)): \(M, L, T\).

    $$\Delta P: [M L^{-1} T^{-2}], \quad D: [L], \quad L: [L], \quad V: [L T^{-1}], \quad \rho: [M L^{-3}], \quad \mu: [M L^{-1} T^{-1}]$$
    

2. Boyutsuz grup sayısı: \(n - m = 6 - 3 = 3\) adet \(\Pi\) grubu oluşacaktır.

    

3. Tekrarlanan değişkenler (\(m = 3\)): \(D, V, \rho\).

     
        
* \(\Pi_1 = \Delta P \cdot D^a V^b \rho^c \implies [M L^{-1} T^{-2}] [L]^a [L T^{-1}]^b [M L^{-3}]^c = M^0 L^0 T^0\)
            $$M: 1 + c = 0 \implies c = -1; \quad T: -2 - b = 0 \implies b = -2; \quad L: -1 + a + b - 3c = 0 \implies a = 0$$
            $$\Pi_1 = \frac{\Delta P}{\rho V^2} \quad (\text{Euler Sayısı})$$
        
        
* \(\Pi_2 = L \cdot D^a V^b \rho^c \implies [L] [L]^a \dots \implies \Pi_2 = \frac{L}{D}\)
        
* \(\Pi_3 = \mu \cdot D^a V^b \rho^c \implies [M L^{-1} T^{-1}] [L]^a [L T^{-1}]^b [M L^{-3}]^c = M^0 L^0 T^0\)
            $$c = -1, \quad b = -1, \quad a = -1 \implies \Pi_3 = \frac{\mu}{\rho V D} = \frac{1}{Re}$$
        
     
    

Sonuç: \(\frac{\Delta P}{\rho V^2} = \phi\left(\frac{L}{D}, Re\right) \implies \mathbf{\Delta P = f \frac{L}{D} \frac{\rho V^2}{2}}\) (Darcy-Weisbach denklemi doğrulanmış olur).

 

 
    

#### PROBLEM 8: Pompa Basma Yüksekliği ve Elektrik Gücü Hesabı

    

Bir su haznesinden (kot \(z_1 = 10\text{ m}\)) diğer bir yüksek hazneye (kot \(z_2 = 45\text{ m}\)) su (\(\rho = 1000\text{ kg/m}^3\), \(\nu = 1.0 \times 10^{-6}\text{ m}^2/\text{s}\)) basılmaktadır. Boru hattı: \(L = 350\text{ m}\), iç çap \(D = 200\text{ mm}\), çelik pürüzlülüğü \(\epsilon = 0.045\text{ mm}\), iletilen debi \(Q = 60\text{ L/s} = 0.06\text{ m}^3/\text{s}\)'dir. Yerel kayıplar: Keskin giriş (\(K_1 = 0.5\)), 4 adet \(90^\circ\) standart dirsek (\(K_2 = 4 \times 0.75 = 3.0\)), 1 adet açık çekvalf (\(K_3 = 2.0\)), çıkış kaybı (\(K_4 = 1.0\)). Pompa verimi \(\eta = 0.78\) olduğuna göre gerekli motor gücünü bulunuz.

    

**ÇÖZÜM:**

    

1. Hız ve Reynolds Sayısı:

    $$A = \frac{\pi (0.2)^2}{4} = 0.031416\text{ m}^2, \quad V = \frac{0.06}{0.031416} = 1.91\text{ m/s}$$
    $$\frac{V^2}{2g} = \frac{(1.91)^2}{2 \times 9.81} = 0.1859\text{ m}$$
    $$Re = \frac{V D}{\nu} = \frac{1.91 \times 0.20}{10^{-6}} = 382,000 \quad (\text{Türbülanslı})$$
    

2. Sürtünme Katsayısı (\(f\)):

    $$\frac{\epsilon}{D} = \frac{0.045}{200} = 0.000225 \implies \text{Haaland'dan } f \approx \mathbf{0.0163}$$
    

3. Yük Kayıpları:

    $$h_f = f \frac{L}{D} \frac{V^2}{2g} = 0.0163 \times \frac{350}{0.20} \times 0.1859 = 28.525 \times 0.1859 = 5.30\text{ m}$$
    $$\sum K_L = 0.5 + 3.0 + 2.0 + 1.0 = 6.5 \implies h_m = 6.5 \times 0.1859 = 1.21\text{ m}$$
    $$h_L = 5.30 + 1.21 = \mathbf{6.51\text{ m}}$$
    

4. Pompa Net Yüksekliği ve Güç:

    $$H_m = (z_2 - z_1) + h_L = (45 - 10) + 6.51 = 35 + 6.51 = \mathbf{41.51\text{ m}}$$
    $$P_{\text{hidrolik}} = \gamma Q H_m = 9810 \times 0.06 \times 41.51 = 24,432\text{ W} = 24.43\text{ kW}$$
    $$P_{\text{motor}} = \frac{P_{\text{hidrolik}}}{\eta} = \frac{24.43}{0.78} = \mathbf{31.32\text{ kW}}$$
 

 
    

#### PROBLEM 9: Düz Levha Üzerinde Sınır Tabaka Kalınlığı ve Sürükleme Direnci

    

Genişliği \(W = 1.5\text{ m}\), uzunluğu \(L = 2.0\text{ m}\) olan düz ince bir plaka, \(U = 3.0\text{ m/s}\) hızındaki su akımına paralel yerleştirilmiştir (\(\rho = 1000\text{ kg/m}^3\), \(\nu = 10^{-6}\text{ m}^2/\text{s}\)).

    a) Plaka sonundaki sınır tabaka kalınlığını (\(\delta\)) ve yer değiştirme kalınlığını (\(\delta^*\)) bulunuz.

    b) Plakanın her iki yüzeyine etkiyen toplam sürtünme direncini (\(F_D\)) hesaplayınız.

    

**ÇÖZÜM:**

    

a) Plaka sonundaki Reynolds sayısı:

    $$Re_L = \frac{U L}{\nu} = \frac{3.0 \times 2.0}{10^{-6}} = 6 \times 10^6 > 5 \times 10^5 \quad (\text{Plaka üzerinde türbülanslı akış oluşur})$$
    Geçiş noktasını \(Re_{\text{geçiş}} = 5 \times 10^5\) kabul edelim. Pratik mühendislik bağıntısı (türbülanslı sınır tabaka):
    $$\delta(L) = \frac{0.38 L}{Re_L^{1/5}} = \frac{0.38 \times 2.0}{(6 \times 10^6)^{0.2}} = \frac{0.76}{22.61} = 0.0336\text{ m} = \mathbf{33.6\text{ mm}}$$
    $$\delta^*(L) \approx \frac{\delta}{8} = \frac{33.6}{8} = \mathbf{4.2\text{ mm}}$$
    

b) Karışık sınır tabaka ortalama sürtünme katsayısı:

    $$C_f = \frac{0.074}{Re_L^{1/5}} - \frac{1740}{Re_L} = \frac{0.074}{22.61} - \frac{1740}{6 \times 10^6} = 0.00327 - 0.00029 = 0.00298$$
    Plakanın iki yüzeyi vardır (\(A_{\text{toplam}} = 2 \times W \times L = 2 \times 1.5 \times 2.0 = 6.0\text{ m}^2\)):
    $$F_D = C_f \cdot \frac{1}{2} \rho U^2 \cdot A_{\text{toplam}} = 0.00298 \times \frac{1}{2}(1000)(3.0)^2 \times 6.0 = 0.00298 \times 4500 \times 6.0 = \mathbf{80.46\text{ N}}$$
 

 
    

#### PROBLEM 10: Yamuk Kanalda Manning Debisi ve Hidrolik Sıçrama

    

Taban genişliği \(b = 3.0\text{ m}\), yan şev eğimi \(1:1\) (yatay:düşey), taban eğimi \(S_0 = 0.001\) ve Manning pürüzlülük katsayısı \(n = 0.015\) olan bir yamuk kanalda su derinliği \(y_1 = 0.5\text{ m}\)'dir. Bu derinlikte suyun sel rejiminde aktığı ve ileride bir hidrolik sıçrama meydana geldiği bilinmektedir.

    a) Kanaldan geçen debiyi bulunuz.

    b) Sıçrama öncesi Froude sayısını (\(Fr_1\)) hesaplayınız.

    c) Sıçrama sonrası derinliği (\(y_2\)) ve sıçramadaki enerji kaybını (\(\Delta E\)) hesaplayınız.

    

**ÇÖZÜM:**

    

1. Kesit Özellikleri (\(m = 1\)):

    $$A_1 = (b + m y_1) y_1 = (3.0 + 1 \times 0.5) \times 0.5 = 3.5 \times 0.5 = 1.75\text{ m}^2$$
    $$P_1 = b + 2 y_1 \sqrt{1 + m^2} = 3.0 + 2(0.5)\sqrt{2} = 3.0 + 1.414 = 4.414\text{ m}$$
    $$R_{h1} = \frac{A_1}{P_1} = \frac{1.75}{4.414} = 0.3965\text{ m}$$
    

2. Manning Hızı ve Debi:

    $$V_1 = \frac{1}{n} R_{h1}^{2/3} S_0^{1/2} = \frac{1}{0.015} (0.3965)^{2/3} (0.001)^{1/2} = 66.67 \times 0.5398 \times 0.03162 = \mathbf{1.138\text{ m/s}}$$
    $$Q = A_1 V_1 = 1.75 \times 1.138 = \mathbf{1.992\text{ m}^3/\text{s}} \approx \mathbf{2.0\text{ m}^3/\text{s}}$$
    

3. Froude Sayısı:

    Serbest yüzey genişliği: \(T_1 = b + 2 m y_1 = 3.0 + 2(0.5) = 4.0\text{ m}\). Hidrolik derinlik: \(y_{h1} = A_1 / T_1 = 1.75 / 4.0 = 0.4375\text{ m}\).
    $$Fr_1 = \frac{V_1}{\sqrt{g y_{h1}}} = \frac{1.138}{\sqrt{9.81 \times 0.4375}} = \frac{1.138}{\sqrt{4.292}} = \frac{1.138}{2.072} = \mathbf{0.549}$$
    *Not:* \(Fr_1