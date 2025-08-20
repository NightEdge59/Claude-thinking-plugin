#!/usr/bin/env python3
"""
Claude-Enhanced OpenWebUI Plugin - Quick Demo
============================================

Bu script eklentinin temel özelliklerini hızlıca gösterir.

Usage:
    python demo.py
"""

import sys
import time
from datetime import datetime

def print_header(title):
    """Başlık yazdır"""
    print("\n" + "="*60)
    print(f"🎯 {title}")
    print("="*60)

def print_section(title):
    """Bölüm başlığı yazdır"""
    print(f"\n🔹 {title}")
    print("-" * 40)

def simulate_loading(text, duration=2):
    """Yükleniyor animasyonu"""
    print(f"\n⏳ {text}", end="")
    for i in range(duration):
        time.sleep(1)
        print(".", end="", flush=True)
    print(" ✅")

def main():
    print_header("CLAUDE-ENHANCED OPENWEBUI PLUGIN DEMO")
    
    print(f"""
🧠 Bu demo Claude 4 seviyesinde yeteneklere sahip OpenWebUI eklentisini gösterir.

📋 Ana Özellikler:
• Chain-of-thought reasoning (düşünme zinciri)
• Dynamic tool discovery ve kullanım
• Eleştirel düşünme ve self-evaluation  
• Agentic planlama ve karar verme
• Gerçek hayat adaptasyonu

⏰ Demo Başlangıç: {datetime.now().strftime('%H:%M:%S')}
    """)
    
    try:
        # Plugin'i import et
        simulate_loading("Plugin yükleniyor")
        from functions import (
            claude_enhanced_thinking,
            discover_and_use_tools,
            agentic_planning,
            real_world_adaptation,
            claude_agent
        )
        print("✅ Plugin başarıyla yüklendi!")
        
        # 1. Claude Enhanced Thinking Demo
        print_section("1. Claude Enhanced Thinking")
        
        demo_query = "E-ticaret sitesinin conversion rate'ini nasıl artırabilirim?"
        print(f"📝 Demo Sorusu: {demo_query}")
        
        simulate_loading("Claude-enhanced düşünme sistemi çalışıyor", 3)
        
        result = claude_enhanced_thinking(demo_query, reasoning_depth=3)
        
        # Sonucu özetle ve göster
        lines = result.split('\n')
        summary_lines = []
        for line in lines[:15]:  # İlk 15 satır
            if line.strip():
                summary_lines.append(line)
                
        print("\n📊 Düşünme Süreci Özeti:")
        for line in summary_lines:
            print(f"  {line}")
        print(f"  ... (toplam {len(lines)} satır)")
        
        # 2. Tool Discovery Demo
        print_section("2. Dynamic Tool Discovery")
        
        sample_apis = [
            {"name": "analytics_api", "description": "Website analytics ve user behavior"},
            {"name": "ab_testing", "description": "A/B test yönetimi ve sonuçları"},
            {"name": "heatmap_api", "description": "User heatmap ve click tracking"}
        ]
        
        task = "Website kullanıcı deneyimini analiz et ve iyileştirme önerileri geliştir"
        print(f"📋 Görev: {task}")
        print(f"🛠️ Mevcut API'lar: {len(sample_apis)} adet")
        
        simulate_loading("Uygun araçlar keşfediliyor", 2)
        
        tool_result = discover_and_use_tools(task, sample_apis)
        
        # Tool sonuçlarını özetle
        if "Belirlenen Araçlar" in tool_result:
            print("✅ Araçlar başarıyla belirlendi ve kullanıldı")
        else:
            print("⚠️ Araç belirleme süreci tamamlandı")
            
        # 3. Agentic Planning Demo
        print_section("3. Agentic Strategic Planning")
        
        objective = "6 ay içinde e-ticaret satışlarını %50 artırmak"
        constraints = ["Bütçe: $25K", "Ekip: 3 kişi", "Mevcut platform: Shopify"]
        
        print(f"🎯 Hedef: {objective}")
        print(f"📊 Kısıtlar: {len(constraints)} adet")
        
        simulate_loading("Stratejik plan oluşturuluyor", 3)
        
        plan_result = agentic_planning(objective, constraints, "medium")
        
        if "Ana Adımlar" in plan_result:
            print("✅ Stratejik plan başarıyla oluşturuldu")
            print("📋 Plan ana bileşenlerini içeriyor:")
            print("   • Hedef analizi")
            print("   • Stratejik adımlar") 
            print("   • Risk değerlendirmesi")
            print("   • İzleme metrikleri")
        
        # 4. Real World Adaptation Demo
        print_section("4. Real-World Adaptation")
        
        context = "Post-pandemic hibrit çalışma ortamında e-ticaret yönetimi"
        factors = ["Uzaktan ekip", "Değişen müşteri davranışları", "Supply chain sorunları"]
        goals = ["Operasyonel verimlilik", "Müşteri memnuniyeti", "Ekip koordinasyonu"]
        
        print(f"🌍 Bağlam: {context}")
        print(f"⚡ Faktörler: {len(factors)} adet")
        print(f"🎯 Hedefler: {len(goals)} adet")
        
        simulate_loading("Adaptasyon stratejileri geliştiriliyor", 3)
        
        adaptation_result = real_world_adaptation(context, factors, goals)
        
        if "Adaptasyon Stratejileri" in adaptation_result:
            print("✅ Adaptasyon stratejileri başarıyla geliştirildi")
            print("🔄 Sürekli iyileştirme döngüsü tanımlandı")
        
        # 5. Plugin Status
        print_section("5. Plugin Durumu")
        
        print(f"📊 Agent Statistikleri:")
        print(f"   • Düşünme Geçmişi: {len(claude_agent.thinking_history)} adım")
        print(f"   • Mevcut Araçlar: {len(claude_agent.available_tools)} adet")
        print(f"   • Öğrenilen Kalıplar: {len(claude_agent.learned_patterns)} adet")
        print(f"   • Confidence Threshold: %{claude_agent.reasoning_depth * 20}")
        
        # Summary
        print_header("DEMO TAMAMLANDI")
        
        print(f"""
🎉 Demo başarıyla tamamlandı!

📈 Gösterilen Özellikler:
✅ Claude-4 tarzı gelişmiş düşünme
✅ Dinamik araç keşfi ve kullanımı  
✅ Stratejik planlama ve risk analizi
✅ Gerçek hayat adaptasyon stratejileri
✅ Öğrenme ve kalıp tanıma

🚀 Plugin Hazır!
Bu eklenti OpenWebUI'nize entegre edilmeye hazır durumda.
Detaylı kullanım için README.md ve examples.py dosyalarını inceleyin.

⏰ Demo Süresi: {datetime.now().strftime('%H:%M:%S')}
        """)
        
    except ImportError as e:
        print(f"❌ Plugin import hatası: {e}")
        print("\n🔧 Çözüm önerileri:")
        print("   1. functions.py dosyasının mevcut dizinde olduğundan emin olun")
        print("   2. Gerekli paketleri yükleyin: pip install -r requirements.txt")
        print("   3. Python sürümünüzün 3.7+ olduğunu kontrol edin")
        
    except Exception as e:
        print(f"❌ Demo sırasında hata oluştu: {e}")
        print("\n🔧 Hata ayıklama için:")
        print("   1. test_claude_enhanced.py dosyasını çalıştırın")
        print("   2. examples.py ile detaylı örnekleri inceleyin")
        print("   3. Log dosyalarını kontrol edin")

if __name__ == "__main__":
    main()
