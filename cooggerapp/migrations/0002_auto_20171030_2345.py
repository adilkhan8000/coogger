# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-30 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooggerapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category2',
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('muhendislik', 'Mühendislik'), ('tp', 'Tıp'), ('fen-edebiyat', 'Fen edebiyat'), ('iktisadi-ve-idari-bilimleri', 'İktisadi ve idari bilimleri'), ('egitim', 'Eğitim'), ('dis-hekimligi', 'Diş hekimliği'), ('mimarlk', 'Mimarlık'), ('islahiye-iktisadi-ve-idari-bilimleri', 'İslahiye iktisadi ve idari bilimleri'), ('guzel-sanatlar', 'Güzel sanatlar'), ('saglk-bilimleri', 'Sağlık bilimleri'), ('hukuk', 'Hukuk'), ('ilahiyat', 'İlahiyat'), ('iletisim', 'İletişim'), ('havaclk-ve-uzay-muhendisligi', 'Havacılık ve uzay mühendisliği'), ('turizm', 'Turizm')], max_length=30, verbose_name='Fakülteler'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subcategory',
            field=models.CharField(blank=True, choices=[('makine', 'Makine'), ('elektrik-ve-elektronik', 'Elektrik ve elektronik'), ('gda', 'Gıda'), ('fizik', 'Fizik'), ('insaat', 'İnşaat'), ('tekstil', 'Tekstil'), ('endustri', 'Endüstri'), ('bigisayar', 'Bigisayar'), ('yazlm', 'Yazılım'), ('metalurji-ve-malzeme', 'Metalurji ve malzeme'), ('enerji-sistemleri', 'Enerji sistemleri'), ('biyoproses-ve-kimya', 'Biyoproses ve kimya'), ('optik-ve-akustik', 'Optik ve akustik'), ('dahili-tp-birimleri', 'Dahili tıp birimleri'), ('cerrahi-tp-birimleri', 'Cerrahi tıp birimleri'), ('temel-tp-birimleri', 'Temel tıp birimleri'), ('tarih', 'Tarih'), ('matematik', 'Matematik'), ('turk-dili-ve-edebiyat', 'Türk dili ve edebiyat'), ('biyoloji', 'Biyoloji'), ('bat-dilleri-ve-edebiyat', 'Batı dilleri ve edebiyat'), ('kimya', 'Kimya'), ('arkeoloji', 'Arkeoloji'), ('sosyoloji', 'Sosyoloji'), ('kultur-varlklarn-koruma-ve-onarm', 'Kültür varlıklarını koruma ve onarım'), ('istatislik', 'İstatislik'), ('psikoloji', 'Psikoloji'), ('cografya', 'Çoğrafya'), ('felsefe', 'Felsefe'), ('dogu-dilleri-ve-edebiyat', 'Doğu dilleri ve edebiyatı'), ('iktisat', 'İktisat'), ('isletme', 'İşletme'), ('uluslar-aras-ticaret-ve-lojistik', 'Uluslar arası ticaret ve lojistik'), ('kamu-yonetim', 'Kamu yönetim'), ('maliye', 'Maliye'), ('kuresel-siyaset-ve-uluslararas-iliskiler', 'Küresel siyaset ve uluslararası ilişkiler'), ('matematik-ve-fen-bilimleri', 'Matematik ve fen bilimleri'), ('guzel-sanatlar', 'Güzel sanatlar'), ('turkce-ve-sosyal-bilimler', 'Türkçe ve sosyal bilimler'), ('yabanc-diller', 'Yabancı diller'), ('egitim-yonetimi-anabilim-dal', 'Eğitim yönetimi anabilim dalı'), ('egitim-programlar-ve-ogretim-adabilim-dal', 'Eğitim programları ve öğretim adabilim dalı'), ('rehberlik-ve-psikojik-dansma-anabilim-dal', 'Rehberlik ve psikojik danışma anabilim dalı'), ('egitimin-felsefesisosyal-ve-tarihi-temelleri-anabilim-dal', 'Eğitimin felsefesi,sosyal ve tarihi temelleri anabilim dalı'), ('hayat-boyu-ogrenme-ve-yetiskin-egitimi-anabilim-dal', 'Hayat boyu öğrenme ve yetişkin eğitimi anabilim dalı'), ('ogretim-teknolojileri-anabilim-dal', 'Öğretim teknolojileri anabilim dalı'), ('egitimde-olcme-ve-degerlendirme-anabilim-dal', 'Eğitimde ölçme ve değerlendirme anabilim dalı'), ('bilgisayar-ve-ogretim-teknolojileri', 'Bilgisayar ve öğretim teknolojileri'), ('okul-oncesi-egitimi-anabilim-dal', 'Okul öncesi eğitimi anabilim dalı'), ('snf-egitimi-anabilim-dal', 'Sınıf eğitimi anabilim dalı'), ('ozel-yetenekliler-egitimi-anabilim-dal', 'Özel yetenekliler eğitimi anabilim dalı'), ('zihinsel-engelliler-egitimi-anabilim-dal', 'Zihinsel engelliler eğitimi anabilim dalı'), ('gorme-engelliler-egitimi-anabilim-dal', 'Görme engelliler eğitimi anabilim dalı'), ('isitme-engelliler-egitimi-anabilim-dal', 'İşitme engelliler eğitimi anabilim dalı'), ('egitimi-anabilim-dal', 'eğitimi anabilim dalı'), ('agz-dis-ve-cene-cerrahisi-ad', 'Ağız Diş ve Çene Cerrahisi AD.'), ('endodonti-ad', 'Endodonti AD.'), ('oral-diagnoz-ve-radyoloji-ad', 'Oral Diagnoz ve Radyoloji AD.'), ('ortodonti-ad', 'Ortodonti AD.'), ('pedodonti-ad', 'Pedodonti AD.'), ('periodontoloji-ad', 'Periodontoloji AD.'), ('protetik-dis-tedavisi-ad', 'Protetik Diş Tedavisi AD.'), ('restoratif-dis-tedavisi-ad', 'Restoratif Diş Tedavisi AD.'), ('sehir-ve-bolge-planlama-bolumu', 'ŞEHİR VE BÖLGE PLANLAMA BÖLÜMÜ'), ('endustri-urunleri-tasarimi-bolumu', 'ENDÜSTRİ ÜRÜNLERİ TASARIMI BÖLÜMÜ'), ('mimarlik-bolumu', 'MİMARLIK BÖLÜMÜ'), ('ic-mimarlik-bolumu', 'İÇ MİMARLIK BÖLÜMÜ'), ('ekonometri', 'EKONOMETRİ'), ('uluslararasi-iliskiler', 'ULUSLARARASI İLİŞKİLER'), ('maliye', 'MALİYE'), ('kamu-yonetimi', 'KAMU YÖNETİMİ'), ('iktisat', 'İKTİSAT'), ('isletme', 'İŞLETME'), ('gastronomi-ve-mutfak-sanatlari-bolumu', 'GASTRONOMİ VE MUTFAK SANATLARI BÖLÜMÜ'), ('moda-ve-tekstil-tasarimi-bolumu', 'MODA VE TEKSTİL TASARIMI BÖLÜMÜ'), ('sahne-ve-gosteri-sanatlari-bolumu', 'SAHNE VE GÖSTERİ SANATLARI BÖLÜMÜ'), ('geleneksel-turk-el-sanatlari-bolumu', 'GELENEKSEL TÜRK EL SANATLARI BÖLÜMÜ'), ('sinema-ve-televizyon-bolumu', 'SİNEMA VE TELEVİZYON BÖLÜMÜ'), ('fotograf-bolumu', 'FOTOĞRAF BÖLÜMÜ'), ('seramik-ve-cam-bolumu', 'SERAMİK VE CAM BÖLÜMÜ'), ('resim-bolumu', 'RESİM BÖLÜMÜ'), ('heykel-bolumu', 'HEYKEL BÖLÜMÜ'), ('grafik-bolumu', 'GRAFİK BÖLÜMÜ'), ('fizyoterapi-ve-rehabilitasyon', 'FİZYOTERAPİ VE REHABİLİTASYON'), ('dil-ve-konusma-terapisi', 'DİL VE KONUŞMA TERAPİSİ'), ('odyoloji', 'ODYOLOJİ'), ('beslenme-ve-diyetetik', 'BESLENME VE DİYETETİK'), ('saglik-yonetimi', 'SAĞLIK YÖNETİMİ'), ('solunum-terapistligi', 'SOLUNUM TERAPİSTLİĞİ'), ('ebelik', 'EBELİK'), ('hemsirelik', 'HEMŞİRELİK'), ('hukuk-fakultesi', 'HUKUK FAKÜLTESİ'), ('anayasa-hukuku-anabilim-dali', 'ANAYASA HUKUKU ANABİLİM DALI'), ('ceza-ve-ceza-muhakemesi-hukuku-anabilim-dali', 'CEZA VE CEZA MUHAKEMESİ HUKUKU ANABİLİM DALI'), ('genel-kamu-hukuku-anabilim-dali', 'GENEL KAMU HUKUKU ANABİLİM DALI'), ('hukuk-felsefesi-ve-sosyolojisi-anabilim-dali', 'HUKUK FELSEFESİ VE SOSYOLOJİSİ ANABİLİM DALI'), ('hukuk-tarihi-anabilim-dali', 'HUKUK TARİHİ ANABİLİM DALI'), ('mali-hukuk-anabilim-dali', 'MALİ HUKUK ANABİLİM DALI'), ('milletlerarasi-hukuk-anabilim-dali', 'MİLLETLERARASI HUKUK ANABİLİM DALI'), ('idare-hukuku-anabilim-dali', 'İDARE HUKUKU ANABİLİM DALI'), ('insan-haklari-anabilim-dali', 'İNSAN HAKLARI ANABİLİM DALI'), ('islam-hukuku-anabilim-dali', 'İSLAM HUKUKU ANABİLİM DALI'), ('ticaret-hukuku-anabilim-dali', 'TİCARET HUKUKU ANABİLİM DALI'), ('avrupa-birligi-hukuku-anabilim-dali', 'AVRUPA BİRLİĞİ HUKUKU ANABİLİM DALI'), ('deniz-hukuku-anabilim-dali', 'DENİZ HUKUKU ANABİLİM DALI'), ('karsilastirmali-hukuk-anabilim-dali', 'KARŞILAŞTIRMALI HUKUK ANABİLİM DALI'), ('medeni-hukuk-anabilim-dali', 'MEDENİ HUKUK ANABİLİM DALI'), ('medeni-usul-ve-icra-iflas-hukuku-anabilim-dali', 'MEDENİ USUL VE İCRA İFLAS HUKUKU ANABİLİM DALI'), ('milletlerarasi-ozel-hukuk-anabilim-dali', 'MİLLETLERARASI ÖZEL HUKUK ANABİLİM DALI'), ('roma-hukuku-anabilim-dali', 'ROMA HUKUKU ANABİLİM DALI'), ('is-ve-sosyal-guvenlik-hukuku-anabilim-dali', 'İŞ VE SOSYAL GÜVENLİK HUKUKU ANABİLİM DALI'), ('tefsir', 'Tefsir'), ('hadis', 'Hadis'), ('kelam', 'Kelam'), ('islam-hukuku', 'İslam Hukuku'), ('islam-mezhepleri-tarihi', 'İslam Mezhepleri Tarihi'), ('tasavvuf', 'Tasavvuf'), ('arap-dili-ve-belagat', 'Arap Dili ve Belagatı'), ('kuran-kerim-okuma-ve-kraat-ilmi', 'Kuranı Kerim Okuma ve Kıraat İlmi'), ('din-egitimi', 'Din Eğitimi'), ('dinler-tarihi', 'Dinler Tarihi'), ('islam-felsefesi', 'İslam Felsefesi'), ('din-sosyolojisi', 'Din Sosyolojisi'), ('din-psikolojisi', 'Din Psikolojisi'), ('felsefe-tarihi', 'Felsefe Tarihi'), ('mantk', 'Mantık'), ('islam-tarihi', 'İslam Tarihi'), ('turk-islam-edebiyat', 'Türk İslam Edebiyatı'), ('turk-islam-sanatlar-tarihi', 'Türk İslam Sanatları Tarihi'), ('turk-din-musikisi', 'Türk Din Musikisi'), ('gazetecilik', 'Gazetecilik'), ('halkla-iliskiler-ve-tantm', 'Halkla ilişkiler ve tanıtım'), ('radyo-tv-ve-sinema', 'Radyo, tv ve sinema'), ('iletisim-enformatigi', 'İletişim enformatiği'), ('reklamclk', 'Reklamcılık'), ('havacilik-yonetimi-bolumu', 'HAVACILIK YÖNETİMİ BÖLÜMÜ'), ('ucak-ve-uzay-muhendisligi-bolumu', 'UÇAK VE UZAY MÜHENDİSLİĞİ BÖLÜMÜ'), ('pilotaj-bolumu', 'PİLOTAJ BÖLÜMÜ')], max_length=50, null=True, verbose_name='Bölümler'),
        ),
    ]
