# GitHub'a yayımlama (Türkçe)

**Önemli:** Bu belge, yayını otomatik gerçekleştirmez. ZIP'in hazırlanmış olması GitHub'da depo açıldığı anlamına gelmez.

1. GitHub hesabında **New repository** seçeneğini aç.
2. Depo adını `adaptive-agent-orchestration` olarak belirle. Açık kaynak yayın için **Public** seç. İstersen önce Private olarak tutup içerik gözden geçirdikten sonra Public yap.
3. Paket zaten `README.md`, `.gitignore` ve `LICENSE` içerdiği için GitHub'da **Initialize this repository with a README** ve **Add a license** gibi başlangıç seçeneklerini seçme.
4. İndirilen ZIP'i bir klasöre çıkart. `.agents/` klasörünü silme veya `SKILL.md` dosyasını yerinden taşıma.
5. Repo boşken, yerel klasörü Codex'te açarak şu mesajı kullanabilirsin:

   > Bu klasördeki Adaptive Agent Orchestration projesini GitHub'a yayımlamak istiyorum. Önce içeriği, gizli veri risklerini, lisansı ve `python -m unittest discover -s tests -v` testlerini kontrol et. Hiçbir kullanıcı veya proje verisini ekleme. Ardından yalnızca benim belirteceğim boş GitHub repository URL'sine `main` dalı üzerinden ilk commit ve push işlemini yap. Her uzak depoya yazma işlemi öncesi bana onay sor; hata halinde zorla push yapma veya var olan uzak geçmişi silme.

6. Repo yayına geçtikten sonra `README.md`, `LICENSE`, `SECURITY.md` ve Skill'in `references/` klasörünün GitHub'da gerçekten bulunduğunu kontrol et. Başka cihazdan yalnızca bu deposu kullanarak Skill'in kurulumunun çalışıp çalışmadığını test et.

Not: Yayımlanan açık depo herkese görünür; kişisel kullanım yüzdelerini, hesap ekranlarını, API anahtarlarını, gerçek kullanıcı dosyalarını veya modem testleri gibi özel verileri burada paylaşma. Üçüncü taraf `fable-orchestration` dosyasını lisansı doğrulanmadan bu depoya yükleme.
