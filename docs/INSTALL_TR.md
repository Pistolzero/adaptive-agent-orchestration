# Windows Codex kurulumu (Türkçe)

Bu Skill tüm projelerde kullanılabilir; Superbox veya başka bir proje dosyasına bağımlı değildir.

## Kolay kurulum

1. ZIP'i çıkar.
2. `.agents/skills/adaptive-agent-orchestration` klasörünü `%USERPROFILE%\.agents\skills\` içine kopyala. Son konumda `SKILL.md` ve `references/` olmalı.
3. Codex'i yeniden aç veya yeni oturum başlat. Şunu yaz:

   `adaptive-agent-orchestration skill'ini kullan; görev küçükse alt ajan açma, bütçe bilinmiyorsa tasarruf modunda kal; her alt ajandan eksiksiz hata raporu iste.`

4. Codex'in beceriyi tanıdığını kontrol et; tanımıyorsa dizin konumu ve Skill başlığını incele.

## İsteğe bağlı model ve ajan ayarları

- `agents/` içindeki ayrı TOML dosyalarını **yalnızca model erişimin doğrulandıysa** `%USERPROFILE%\.codex\agents\` içine kopyala.
- `examples/config-snippet.toml` dosyasının içeriğini mevcut `%USERPROFILE%\.codex\config.toml` içine **birleştir**. Var olan ayarları silme veya üzerine yazma; `[agents]` bölümü zaten varsa tekrar ekleme.
- Alt ajanların model ve düşünme düzeyleri ana ajandan farklı olabilir. **Sabit TOML değerleri önceliklidir:** Kotaya göre araştırmacı rolünü `aao_researcher_balanced` (Sol/medium) veya `aao_researcher` (Sol/high) olarak seç. Builder için `aao_builder` (medium) ve `aao_builder_deep` (high) varyantları var. Skill bu yeteneği kendi başına etkinleştirmez; ilgili Codex sürümü ve ayarları gerekir.

## Limit kullanımı

Resmî Codex durumunu kullanıcı kendi arayüzünden veya desteklenen yerde `/status` ile kontrol edebilir. İsterse kalan kullanım yüzdesini ve hangi modele/zaman penceresine ait olduğunu ajana söyleyebilir. Bu bilgi yoksa ajan `UNKNOWN/CONSERVE` davranır ve kalan kullanım oranı uydurmaz. Limit azaldığında yeni alt ajan sayısını azaltır; gerekli kalite kontrollerini sessizce atlamaz.

## GitHub'da kullanma

Bütün bu repo yayınlanabilir. Kullanıcı, GitHub'da yeni depoya `README.md`, `.agents`, `agents`, `docs`, `examples`, `tests`, `LICENSE`, `CONTRIBUTING.md` ve `SECURITY.md` içeriğini yüklemelidir. Özellikle `.agents` klasörünün korunması önemlidir. **GitHub yalnızca repo dosyalarını barındırır; Skill yerel Codex'e ayrıca kurulmalıdır.**

## Güvenlik

Bu paket otomatik script çalıştırmaz, kullanıcı şifresi okumaz ve ödeme yapmaz. Dışarıdan alınan ek repo ve MCP eklentileri ayrıca incelenmelidir. Alt ajanlar ana oturumun gerçek izinlerini devralabilir; metin talimatı ayrı bir güvenlik izolasyonu değildir.
