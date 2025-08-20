"""
Claude-Enhanced OpenWebUI Plugin Usage Examples
==============================================

Bu dosya eklentinin nasıl kullanılacağına dair detaylı örnekler içerir.
Gerçek senaryolarda nasıl etkili bir şekilde kullanabileceğinizi gösterir.

Usage:
    python examples.py
"""

import json
from datetime import datetime
from functions import (
    claude_enhanced_thinking,
    discover_and_use_tools,
    agentic_planning,
    real_world_adaptation,
    get_plugin_info
)

def example_basic_thinking():
    """Temel düşünme özelliklerini gösteren örnek"""
    print("🧠 Örnek 1: Temel Claude-Enhanced Thinking")
    print("=" * 50)
    
    query = """
    Machine learning modellerinin performansını değerlendirmek için 
    hangi metrikleri kullanmalıyım ve neden?
    """
    
    result = claude_enhanced_thinking(query)
    print(result)
    print("\n" + "="*50 + "\n")

def example_advanced_reasoning():
    """Gelişmiş reasoning özellikleri örneği"""
    print("🧠 Örnek 2: Gelişmiş Reasoning ve Eleştirel Düşünme")
    print("=" * 60)
    
    complex_query = """
    Şirketimiz e-ticaret sektöründe faaliyet gösteriyor. Son 6 ayda 
    satışlarımız %20 düştü. Rakiplerimiz AI tabanlı kişiselleştirme 
    sistemleri kullanıyor. Bizim de acil olarak AI entegrasyonu yapmamız 
    gerekiyor. 50K$ bütçemiz ve 3 aylık süremiz var. En iyi strateji nedir?
    """
    
    result = claude_enhanced_thinking(
        query=complex_query,
        reasoning_depth=5,
        enable_critical_thinking=True
    )
    print(result)
    print("\n" + "="*60 + "\n")

def example_tool_discovery():
    """Dinamik araç keşif ve kullanım örneği"""
    print("🛠️ Örnek 3: Dinamik Araç Keşif ve Kullanım")
    print("=" * 50)
    
    # Mevcut API'ları simüle et
    available_apis = [
        {
            "name": "google_analytics",
            "description": "Web sitesi analitik verileri",
            "parameters": {"metric": "str", "date_range": "str"}
        },
        {
            "name": "social_media_api",
            "description": "Sosyal medya etkileşim verileri",
            "parameters": {"platform": "str", "content_type": "str"}
        },
        {
            "name": "competitor_analysis",
            "description": "Rakip analizi ve pazar verileri",
            "parameters": {"competitor": "str", "metric": "str"}
        },
        {
            "name": "seo_tools",
            "description": "SEO analizi ve anahtar kelime araştırması",
            "parameters": {"url": "str", "keywords": "list"}
        }
    ]
    
    task = """
    Web sitemizin organik trafiği son 3 ayda %30 düştü. 
    Nedenlerini araştır ve çözüm önerileri geliştir.
    """
    
    result = discover_and_use_tools(
        task_description=task,
        available_apis=available_apis
    )
    print(result)
    print("\n" + "="*50 + "\n")

def example_strategic_planning():
    """Agentic planlama ve stratejik düşünme örneği"""
    print("🎯 Örnek 4: Agentic Strategic Planning")
    print("=" * 45)
    
    objective = """
    Yeni bir SaaS ürünü geliştirerek pazara sunmak. 
    Hedef: İlk yıl 1000 aktif kullanıcı ve $100K ARR.
    """
    
    constraints = [
        "Geliştirme ekibi: 3 kişi",
        "Bütçe: $200K",
        "Süre: 12 ay",
        "Hedef pazar: B2B küçük işletmeler",
        "Teknik sınırlama: Cloud-first yaklaşım"
    ]
    
    result = agentic_planning(
        objective=objective,
        constraints=constraints,
        time_horizon="long"
    )
    print(result)
    print("\n" + "="*45 + "\n")

def example_real_world_adaptation():
    """Gerçek hayat adaptasyonu örneği"""
    print("🌍 Örnek 5: Real-World Adaptation")
    print("=" * 40)
    
    context = """
    COVID-19 sonrası hibrit çalışma modeline geçen teknoloji şirketi. 
    Ekip üyeleri farklı şehirlerde, farklı zaman dilimlerinde çalışıyor. 
    Proje yönetimi ve iletişimde zorlanıyoruz.
    """
    
    environmental_factors = [
        "Zaman farkları (3-6 saat)",
        "Farklı çalışma kültürleri",
        "İnternet bağlantı kalitesi farklılıkları",
        "Ev ortamında çalışma zorlukları",
        "Asenkron iletişim gereksinimleri"
    ]
    
    adaptation_goals = [
        "Ekip verimliliğini artırma",
        "İletişim kalitesini iyileştirme", 
        "Proje teslim sürelerini kısaltma",
        "Çalışan memnuniyetini artırma",
        "Hibrit model sürdürülebilirliği"
    ]
    
    result = real_world_adaptation(
        context=context,
        environmental_factors=environmental_factors,
        adaptation_goals=adaptation_goals
    )
    print(result)
    print("\n" + "="*40 + "\n")

def example_startup_scenario():
    """Startup senaryosu - Bütünleşik örnek"""
    print("🚀 Örnek 6: Startup Senaryosu - Bütünleşik Kullanım")
    print("=" * 55)
    
    print("📋 Durum: Yeni bir AI startup kurma süreci")
    print("-" * 30)
    
    # 1. İlk analiz
    print("\n1️⃣ Pazar Analizi ve Strateji Belirleme:")
    initial_analysis = claude_enhanced_thinking(
        query="""
        AI alanında yenilikçi bir startup kurmak istiyorum. 
        Hangi sektörlerde boşluklar var ve hangi AI teknolojileri 
        şu anda undervalued durumda?
        """,
        reasoning_depth=4
    )
    print(initial_analysis[:500] + "...\n")
    
    # 2. Araç belirleme
    print("2️⃣ Gerekli Araç ve Kaynakların Belirlenmesi:")
    tools_result = discover_and_use_tools(
        task_description="AI startup kurmak için gerekli araçları ve kaynakları belirle",
        available_apis=[
            {"name": "market_research", "description": "Pazar araştırma verileri"},
            {"name": "patent_search", "description": "Patent ve IP araştırması"},
            {"name": "funding_database", "description": "Yatırım ve fon veritabanı"},
            {"name": "tech_stack_analyzer", "description": "Teknoloji yığını analizi"}
        ]
    )
    print(tools_result[:500] + "...\n")
    
    # 3. Detaylı planlama
    print("3️⃣ Stratejik Plan Geliştirme:")
    strategic_plan = agentic_planning(
        objective="Computer Vision tabanlı retail analytics SaaS ürünü geliştirmek",
        constraints=[
            "Seed funding: $500K",
            "Ekip: 5 kişi",
            "Süre: 18 ay",
            "Hedef: Enterprise müşteriler"
        ],
        time_horizon="long"
    )
    print(strategic_plan[:500] + "...\n")
    
    # 4. Adaptasyon stratejisi
    print("4️⃣ Pazar Koşullarına Adaptasyon:")
    adaptation = real_world_adaptation(
        context="Rekabetçi AI pazarında yeni startup",
        environmental_factors=[
            "Büyük teknoloji şirketlerinin dominantlığı",
            "Hızla değişen AI teknolojileri",
            "Veri gizliliği düzenlemeleri",
            "Yetenek sıkıntısı"
        ],
        adaptation_goals=[
            "Benzersiz değer önerisi yaratma",
            "Hızlı ürün iterasyonu",
            "Müşteri yakınlığı kurma"
        ]
    )
    print(adaptation[:500] + "...\n")
    
    print("✅ Startup senaryosu analizi tamamlandı!")
    print("=" * 55 + "\n")

def example_technical_problem_solving():
    """Teknik problem çözme örneği"""
    print("⚙️ Örnek 7: Teknik Problem Çözme")
    print("=" * 40)
    
    technical_problem = """
    Web uygulamamızda performans sorunu yaşıyoruz:
    - Sayfa yükleme süresi 8-12 saniye
    - Veritabanı sorguları yavaş
    - Kullanıcı sayısı arttıkça sistem çöküyor
    - Frontend React, Backend Node.js, DB PostgreSQL
    - AWS üzerinde deploy edilmiş
    """
    
    # Teknik analiz
    result = claude_enhanced_thinking(
        query=technical_problem,
        reasoning_depth=5,
        enable_critical_thinking=True
    )
    print(result)
    print("\n" + "="*40 + "\n")

def example_business_strategy():
    """İş stratejisi geliştirme örneği"""
    print("💼 Örnek 8: İş Stratejisi Geliştirme")
    print("=" * 40)
    
    business_context = """
    Geleneksel perakende şirketi olan firmamız pandemi sonrası 
    dijital dönüşüm yapmak zorunda. E-ticaret satışlarımız henüz 
    toplam satışların %15'i. Rakiplerimiz %60-70 seviyesinde.
    """
    
    # İş stratejisi planlaması
    strategy = agentic_planning(
        objective="Dijital dönüşümü hızlandırarak 2 yıl içinde e-ticaret payını %50'ye çıkarmak",
        constraints=[
            "Mevcut fiziksel mağaza ağı korunacak",
            "Bütçe: $2M",
            "Mevcut ekip: 50 kişi",
            "Teknoloji altyapısı sıfırdan kurulacak"
        ],
        time_horizon="medium"
    )
    print(strategy)
    print("\n" + "="*40 + "\n")

def run_all_examples():
    """Tüm örnekleri sırayla çalıştır"""
    print("🎉 CLAUDE-ENHANCED PLUGIN KULLANIM ÖRNEKLERİ")
    print("=" * 60)
    print(f"⏰ Başlangıç: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n")
    
    # Plugin bilgisini göster
    print(get_plugin_info())
    print("\n")
    
    examples = [
        example_basic_thinking,
        example_advanced_reasoning,
        example_tool_discovery,
        example_strategic_planning,
        example_real_world_adaptation,
        example_startup_scenario,
        example_technical_problem_solving,
        example_business_strategy
    ]
    
    for i, example_func in enumerate(examples, 1):
        try:
            print(f"🚀 Örnek {i} çalıştırılıyor...")
            example_func()
            print(f"✅ Örnek {i} başarıyla tamamlandı!\n")
        except Exception as e:
            print(f"❌ Örnek {i} hata verdi: {e}\n")
    
    print("🎯 TÜM ÖRNEKLER TAMAMLANDI!")
    print(f"⏰ Bitiş: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

def interactive_demo():
    """İnteraktif demo modu"""
    print("🎮 İNTERAKTİF DEMO MODU")
    print("=" * 30)
    
    while True:
        print("\nHangi özelliği test etmek istiyorsuniz?")
        print("1. Claude Enhanced Thinking")
        print("2. Tool Discovery") 
        print("3. Agentic Planning")
        print("4. Real World Adaptation")
        print("5. Tüm örnekleri çalıştır")
        print("0. Çıkış")
        
        choice = input("\nSeçiminiz (0-5): ").strip()
        
        if choice == "0":
            print("👋 Demo sona erdi!")
            break
        elif choice == "1":
            query = input("Düşünmesini istediğiniz soruyu yazın: ")
            result = claude_enhanced_thinking(query)
            print("\n" + result[:1000] + "...\n")
        elif choice == "2":
            task = input("Hangi görev için araç keşfi yapılsın: ")
            result = discover_and_use_tools(task)
            print("\n" + result[:1000] + "...\n")
        elif choice == "3":
            objective = input("Hedefi yazın: ")
            result = agentic_planning(objective)
            print("\n" + result[:1000] + "...\n")
        elif choice == "4":
            context = input("Adaptasyon bağlamını yazın: ")
            result = real_world_adaptation(context)
            print("\n" + result[:1000] + "...\n")
        elif choice == "5":
            run_all_examples()
        else:
            print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_demo()
    else:
        run_all_examples()
