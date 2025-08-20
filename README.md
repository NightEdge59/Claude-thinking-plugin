# 🧠 Claude-Enhanced OpenWebUI Plugin

Bu eklenti lokal LLM modellerine **Claude 4 seviyesinde düşünme ve agentic yetenekler** kazandıran gelişmiş bir OpenWebUI eklentisidir.

## ✨ Özellikler

### 🔍 Claude-4 Tarzı Düşünme
- **Chain-of-Thought Reasoning**: Adım adım mantıksal düşünme
- **Multi-step Analysis**: Karmaşık problemleri parçalara ayırma
- **Confidence Scoring**: Her adım için güven skorları
- **Self-reflection**: Kendi düşünme sürecini değerlendirme

### 🛠️ Dinamik Araç Sistemi
- **Auto-discovery**: Mevcut araçları otomatik keşfetme
- **Intelligent Selection**: Göreve en uygun araçları seçme
- **Learning Capability**: Araç kullanımından öğrenme
- **Effectiveness Tracking**: Araç etkinliğini izleme

### 🎯 Agentic Planlama
- **Strategic Planning**: Uzun vadeli stratejik planlama
- **Goal Management**: Hedef belirleme ve takip
- **Risk Assessment**: Risk analizi ve yönetimi
- **Adaptive Execution**: Koşullara göre plan uyarlama

### 🌍 Gerçek Hayat Adaptasyonu
- **Context Awareness**: Durum farkındalığı
- **Environmental Analysis**: Çevresel faktör analizi
- **Continuous Learning**: Sürekli öğrenme ve iyileştirme
- **Pattern Recognition**: Kalıp tanıma ve öğrenme

## 🚀 Kurulum

### 1. Dosyaları OpenWebUI Functions Dizinine Kopyalayın

```bash
# OpenWebUI functions dizinine gidin
cd /path/to/openwebui/functions

# Plugin dosyalarını kopyalayın
cp claude-enhanced-plugin/functions.py .
cp claude-enhanced-plugin/config.json .
```

### 2. Gerekli Paketleri Yükleyin

```bash
pip install -r requirements.txt
```

### 3. OpenWebUI'yi Yeniden Başlatın

```bash
# Docker kullanıyorsanız
docker-compose restart

# Ya da manuel olarak
systemctl restart openwebui
```

## 📋 Kullanım

### 🧠 Claude-Enhanced Thinking

Gelişmiş düşünme ve analiz için:

```python
# Basit kullanım
claude_enhanced_thinking("Machine learning modellerinin avantajları nelerdir?")

# Gelişmiş kullanım
claude_enhanced_thinking(
    query="Şirketimiz için en uygun AI stratejisi nedir?",
    reasoning_depth=5,
    enable_critical_thinking=True
)
```

### 🛠️ Dinamik Araç Kullanımı

Araçları otomatik keşfetme ve kullanma:

```python
discover_and_use_tools(
    task_description="Web sitesindeki performans sorunlarını analiz et",
    available_apis=["lighthouse_api", "gtmetrix_api"]
)
```

### 🎯 Agentic Planlama

Stratejik planlama ve hedef yönetimi:

```python
agentic_planning(
    objective="Yeni ürün lansmanı için pazarlama stratejisi geliştir",
    constraints=["Bütçe: $50K", "Süre: 3 ay", "Hedef: B2B"],
    time_horizon="medium"
)
```

### 🌍 Gerçek Hayat Adaptasyonu

Context-aware davranış ve adaptasyon:

```python
real_world_adaptation(
    context="Pandemi sonrası uzaktan çalışma ortamı",
    environmental_factors=["Dağıtık ekipler", "Dijital araçlar", "Hibrit model"],
    adaptation_goals=["Verimlilik artışı", "Ekip uyumu", "İletişim iyileştirmesi"]
)
```

## ⚙️ Yapılandırma

`config.json` dosyasında eklenti ayarlarını özelleştirebilirsiniz:

```json
{
  "settings": {
    "reasoning": {
      "default_depth": 3,
      "enable_critical_thinking": true
    },
    "tools": {
      "enable_auto_discovery": true,
      "max_tools_per_task": 5
    }
  }
}
```

## 🔧 Gelişmiş Özellikler

### Öğrenme ve Adaptasyon
- Plugin kullanım kalıplarından öğrenir
- Başarılı stratejileri hatırlar
- Zamanla performansını iyileştirir

### Güvenlik
- Girdi doğrulaması
- Çıktı sanitizasyonu
- Rate limiting
- Güvenli kod yürütme

### Performans
- Asenkron işlem
- Paralel araç çağrıları
- Sonuç önbellekleme
- Optimized memory usage

## 📊 İzleme ve Analitik

Plugin aşağıdaki metrikleri takip eder:

- **Düşünme Performansı**: Reasoning chain effectiveness
- **Araç Kullanımı**: Tool usage patterns
- **Plan Başarısı**: Strategic planning success rates
- **Adaptasyon Hızı**: Real-world adaptation speed

## 🐛 Hata Ayıklama

### Log Dosyası
```bash
tail -f claude_enhanced.log
```

### Yaygın Sorunlar

1. **Import Errors**: Requirements.txt'deki paketlerin yüklü olduğundan emin olun
2. **Memory Issues**: config.json'da memory limitlerini ayarlayın
3. **Performance**: Paralel işlem ayarlarını optimize edin

## 🤝 Katkıda Bulunma

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 🆘 Destek

- **Issues**: GitHub issues sayfasını kullanın
- **Discussions**: Community discussions for questions
- **Wiki**: Detaylı dokümantasyon için wiki sayfasını inceleyin

## 🔮 Gelecek Özellikler

- [ ] Multi-modal reasoning (metin + görsel)
- [ ] Advanced memory systems
- [ ] External API integrations
- [ ] Custom tool development framework
- [ ] Real-time collaboration features
- [ ] Enhanced security features

---

**⚡ Claude-Enhanced Plugin ile lokal LLM'lerinizi Claude 4 seviyesine çıkarın!**
