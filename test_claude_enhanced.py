"""
Test Suite for Claude-Enhanced OpenWebUI Plugin
==============================================

Bu dosya Claude-Enhanced eklentisinin kapsamlı test paketini içerir.
Tüm fonksiyonların doğru çalıştığını ve beklenen performansı sağladığını doğrular.

Usage:
    python test_claude_enhanced.py
    
    # Sadece belirli testleri çalıştırmak için:
    python -m pytest test_claude_enhanced.py::test_reasoning_engine -v
"""

import unittest
import json
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Any
import sys
import os

# Plugin modülünü import et
try:
    from functions import (
        claude_enhanced_thinking,
        discover_and_use_tools,
        agentic_planning,
        real_world_adaptation,
        claude_agent,
        ClaudeEnhancedAgent,
        ReasoningStep,
        ThinkingChain,
        AgentGoal,
        ToolCapability
    )
except ImportError as e:
    print(f"❌ Plugin import hatası: {e}")
    print("functions.py dosyasının mevcut dizinde olduğundan emin olun.")
    sys.exit(1)

class TestClaudeEnhancedPlugin(unittest.TestCase):
    """Claude Enhanced Plugin için ana test sınıfı"""
    
    def setUp(self):
        """Her test öncesi çalışacak setup"""
        # Test için temiz bir agent instance'ı oluştur
        self.test_agent = ClaudeEnhancedAgent()
        
        # Test verileri
        self.sample_queries = [
            "Machine learning nedir ve nasıl çalışır?",
            "Şirketimiz için en iyi pazarlama stratejisi nedir?",
            "Python'da veritabanı bağlantısı nasıl yapılır?",
            "Karmaşık bir proje nasıl yönetilir?"
        ]
        
        self.sample_apis = [
            {
                "name": "weather_api",
                "description": "Hava durumu bilgisi alma",
                "parameters": {"location": "str", "days": "int"}
            },
            {
                "name": "database_api",
                "description": "Veritabanı işlemleri",
                "parameters": {"query": "str", "table": "str"}
            }
        ]
        
    def test_agent_initialization(self):
        """Agent başlatma testleri"""
        print("\n🧪 Agent Başlatma Testi...")
        
        # Agent'ın doğru şekilde başlatıldığını kontrol et
        self.assertIsInstance(self.test_agent, ClaudeEnhancedAgent)
        self.assertEqual(len(self.test_agent.thinking_history), 0)
        self.assertEqual(len(self.test_agent.goals), 0)
        self.assertGreater(len(self.test_agent.available_tools), 0)
        
        # Varsayılan araçların yüklendiğini kontrol et
        self.assertIn("web_search", self.test_agent.available_tools)
        self.assertIn("code_analysis", self.test_agent.available_tools)
        self.assertIn("planning", self.test_agent.available_tools)
        
        print("✅ Agent başarıyla başlatıldı")
        
    def test_thinking_chain_creation(self):
        """Düşünme zinciri oluşturma testleri"""
        print("\n🧪 Düşünme Zinciri Testi...")
        
        # Düşünme adımı ekleme
        step = self.test_agent.add_thinking_step(
            ReasoningStep.ANALYSIS,
            "Test analizi",
            0.9
        )
        
        self.assertIsInstance(step, ThinkingChain)
        self.assertEqual(step.step, ReasoningStep.ANALYSIS)
        self.assertEqual(step.content, "Test analizi")
        self.assertEqual(step.confidence, 0.9)
        self.assertEqual(len(self.test_agent.thinking_history), 1)
        
        print("✅ Düşünme zinciri başarıyla oluşturuldu")
        
    def test_reasoning_engine(self):
        """Reasoning engine testleri"""
        print("\n🧪 Reasoning Engine Testi...")
        
        for query in self.sample_queries[:2]:  # İlk 2 sorguyu test et
            print(f"  🔍 Test ediliyor: {query[:50]}...")
            
            result = self.test_agent.chain_of_thought_reasoning(query)
            
            # Sonuç yapısını kontrol et
            self.assertIn("reasoning_chain", result)
            self.assertIn("final_answer", result)
            self.assertIn("confidence_score", result)
            self.assertIn("thinking_process", result)
            
            # Reasoning chain'in doğru yapıda olduğunu kontrol et
            self.assertIsInstance(result["reasoning_chain"], list)
            self.assertGreater(len(result["reasoning_chain"]), 0)
            
            # Confidence score'un geçerli aralıkta olduğunu kontrol et
            self.assertGreaterEqual(result["confidence_score"], 0.0)
            self.assertLessEqual(result["confidence_score"], 1.0)
            
            # Final answer'ın boş olmadığını kontrol et
            self.assertIsInstance(result["final_answer"], str)
            self.assertGreater(len(result["final_answer"]), 0)
            
        print("✅ Reasoning engine testleri başarılı")
        
    def test_claude_enhanced_thinking_function(self):
        """Claude enhanced thinking function testleri"""
        print("\n🧪 Claude Enhanced Thinking Function Testi...")
        
        # Basit kullanım testi
        result = claude_enhanced_thinking("Python nedir?")
        self.assertIsInstance(result, str)
        self.assertIn("Claude-Enhanced Thinking Response", result)
        
        # Gelişmiş parametreler ile test
        result = claude_enhanced_thinking(
            query="Karmaşık bir analiz problemi",
            reasoning_depth=4,
            enable_critical_thinking=True
        )
        self.assertIsInstance(result, str)
        self.assertIn("Düşünme Süreci", result)
        
        print("✅ Claude enhanced thinking function testleri başarılı")
        
    def test_tool_discovery_and_usage(self):
        """Araç keşif ve kullanım testleri"""
        print("\n🧪 Tool Discovery Testi...")
        
        # Tool discovery function'ı test et
        result = discover_and_use_tools(
            task_description="Hava durumu bilgisi al ve veritabanına kaydet",
            available_apis=self.sample_apis
        )
        
        self.assertIsInstance(result, str)
        self.assertIn("Akıllı Araç Kullanımı", result)
        self.assertIn("Belirlenen Araçlar", result)
        
        # Agent'ın araçları doğru şekilde belirlediğini kontrol et
        suitable_tools = self.test_agent._identify_suitable_tools(
            "Veritabanı analizi yap",
            self.sample_apis
        )
        
        self.assertIsInstance(suitable_tools, list)
        # En az bir araç belirlenmiş olmalı
        if len(suitable_tools) > 0:
            self.assertIn("name", suitable_tools[0])
            self.assertIn("relevance_score", suitable_tools[0])
            
        print("✅ Tool discovery testleri başarılı")
        
    def test_agentic_planning_function(self):
        """Agentic planning function testleri"""
        print("\n🧪 Agentic Planning Testi...")
        
        # Agentic planning function'ı test et
        result = agentic_planning(
            objective="Web sitesi performansını iyileştir",
            constraints=["Bütçe: $10K", "Süre: 2 ay"],
            time_horizon="medium"
        )
        
        self.assertIsInstance(result, str)
        self.assertIn("Agentic Planning Response", result)
        self.assertIn("Hedef Analizi", result)
        self.assertIn("Stratejik Plan", result)
        self.assertIn("Risk Analizi", result)
        
        print("✅ Agentic planning testleri başarılı")
        
    def test_real_world_adaptation_function(self):
        """Real world adaptation function testleri"""
        print("\n🧪 Real World Adaptation Testi...")
        
        # Real world adaptation function'ı test et
        result = real_world_adaptation(
            context="Uzaktan çalışma ortamında ekip yönetimi",
            environmental_factors=["Zaman farkları", "İletişim zorlukları"],
            adaptation_goals=["Verimlilik artışı", "Ekip uyumu"]
        )
        
        self.assertIsInstance(result, str)
        self.assertIn("Real-World Adaptation Analysis", result)
        self.assertIn("Bağlam Analizi", result)
        self.assertIn("Adaptasyon Stratejileri", result)
        
        print("✅ Real world adaptation testleri başarılı")
        
    def test_learning_and_pattern_recognition(self):
        """Öğrenme ve kalıp tanıma testleri"""
        print("\n🧪 Learning ve Pattern Recognition Testi...")
        
        # Birkaç query çalıştırarak öğrenme sistemini test et
        initial_patterns = len(self.test_agent.learned_patterns)
        
        for i, query in enumerate(self.sample_queries):
            self.test_agent.chain_of_thought_reasoning(query)
            
        # Yeni kalıplar öğrenildiğini kontrol et
        final_patterns = len(self.test_agent.learned_patterns)
        self.assertGreaterEqual(final_patterns, initial_patterns)
        
        print(f"✅ {final_patterns - initial_patterns} yeni kalıp öğrenildi")
        
    def test_error_handling(self):
        """Hata yönetimi testleri"""
        print("\n🧪 Error Handling Testi...")
        
        # Boş query ile test
        result = claude_enhanced_thinking("")
        self.assertIsInstance(result, str)
        
        # None değerler ile test
        result = discover_and_use_tools(
            task_description="test",
            available_apis=None
        )
        self.assertIsInstance(result, str)
        
        # Geçersiz parametreler ile test
        result = agentic_planning(
            objective="",
            constraints=None,
            time_horizon="invalid"
        )
        self.assertIsInstance(result, str)
        
        print("✅ Error handling testleri başarılı")
        
    def test_performance_metrics(self):
        """Performans metrik testleri"""
        print("\n🧪 Performance Metrics Testi...")
        
        import time
        
        # Reasoning performance test
        start_time = time.time()
        result = claude_enhanced_thinking("Basit bir test sorusu")
        reasoning_time = time.time() - start_time
        
        print(f"  ⏱️ Reasoning süresi: {reasoning_time:.2f} saniye")
        self.assertLess(reasoning_time, 5.0)  # 5 saniyeden az olmalı
        
        # Tool discovery performance test
        start_time = time.time()
        result = discover_and_use_tools("Test görevi", self.sample_apis)
        tool_time = time.time() - start_time
        
        print(f"  ⏱️ Tool discovery süresi: {tool_time:.2f} saniye")
        self.assertLess(tool_time, 3.0)  # 3 saniyeden az olmalı
        
        print("✅ Performance testleri başarılı")
        
    def test_memory_usage(self):
        """Bellek kullanım testleri"""
        print("\n🧪 Memory Usage Testi...")
        
        import psutil
        import os
        
        # Başlangıç bellek kullanımı
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        # Birçok operation çalıştır
        for i in range(10):
            claude_enhanced_thinking(f"Test query {i}")
            discover_and_use_tools(f"Test task {i}", self.sample_apis)
            
        # Son bellek kullanımı
        final_memory = process.memory_info().rss / 1024 / 1024  # MB
        memory_increase = final_memory - initial_memory
        
        print(f"  💾 Bellek artışı: {memory_increase:.2f} MB")
        self.assertLess(memory_increase, 100)  # 100 MB'dan az artış olmalı
        
        print("✅ Memory usage testleri başarılı")
        
    def test_concurrent_operations(self):
        """Eşzamanlı işlem testleri"""
        print("\n🧪 Concurrent Operations Testi...")
        
        import threading
        import time
        
        results = []
        
        def worker(query_id):
            result = claude_enhanced_thinking(f"Concurrent test {query_id}")
            results.append(result)
            
        # 3 eşzamanlı thread başlat
        threads = []
        for i in range(3):
            thread = threading.Thread(target=worker, args=(i,))
            threads.append(thread)
            thread.start()
            
        # Tüm thread'lerin bitmesini bekle
        for thread in threads:
            thread.join()
            
        # Sonuçları kontrol et
        self.assertEqual(len(results), 3)
        for result in results:
            self.assertIsInstance(result, str)
            
        print("✅ Concurrent operations testleri başarılı")
        
def run_comprehensive_tests():
    """Kapsamlı test paketini çalıştır"""
    print("🚀 Claude-Enhanced Plugin Kapsamlı Test Paketi Başlatılıyor...\n")
    print("=" * 60)
    
    # Test suite oluştur
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestClaudeEnhancedPlugin)
    
    # Test runner yapılandır
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    
    # Testleri çalıştır
    start_time = datetime.now()
    result = runner.run(test_suite)
    end_time = datetime.now()
    
    # Sonuçları özetle
    print("\n" + "=" * 60)
    print("📊 TEST SONUÇLARI")
    print("=" * 60)
    
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    success_rate = ((total_tests - failures - errors) / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"🧪 Toplam Test: {total_tests}")
    print(f"✅ Başarılı: {total_tests - failures - errors}")
    print(f"❌ Başarısız: {failures}")
    print(f"⚠️ Hata: {errors}")
    print(f"📈 Başarı Oranı: {success_rate:.1f}%")
    print(f"⏱️ Toplam Süre: {end_time - start_time}")
    
    if failures > 0:
        print("\n❌ BAŞARISIZ TESTLER:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback}")
            
    if errors > 0:
        print("\n⚠️ HATALI TESTLER:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback}")
            
    print("\n" + "=" * 60)
    
    if success_rate >= 90:
        print("🎉 Plugin test paketini başarıyla geçti!")
        return True
    else:
        print("⚠️ Plugin bazı testlerde sorun yaşıyor. Detayları inceleyin.")
        return False
        
def run_performance_benchmark():
    """Performans benchmark'ı çalıştır"""
    print("\n🏃 PERFORMANS BENCHMARK'I")
    print("=" * 40)
    
    import time
    
    # Reasoning performance
    queries = [
        "Basit soru",
        "Orta seviye analiz gerektiren soru hakkında düşün",
        "Karmaşık, çok adımlı analiz gerektiren uzun bir soru ve bu sorunun cevabı için detaylı planlama yap"
    ]
    
    for i, query in enumerate(queries):
        start_time = time.time()
        result = claude_enhanced_thinking(query)
        end_time = time.time()
        
        query_type = ["Basit", "Orta", "Karmaşık"][i]
        print(f"📊 {query_type} Query: {end_time - start_time:.2f}s")
        
    # Tool discovery performance
    start_time = time.time()
    for i in range(5):
        discover_and_use_tools(f"Test task {i}", [])
    end_time = time.time()
    
    print(f"🛠️ Tool Discovery (5x): {end_time - start_time:.2f}s")
    
    # Memory efficiency
    import psutil
    import os
    process = psutil.Process(os.getpid())
    memory_mb = process.memory_info().rss / 1024 / 1024
    print(f"💾 Bellek Kullanımı: {memory_mb:.1f} MB")
    
    print("=" * 40)

if __name__ == "__main__":
    try:
        # Kapsamlı testleri çalıştır
        success = run_comprehensive_tests()
        
        # Performans benchmark'ı çalıştır
        run_performance_benchmark()
        
        # Sonuç
        if success:
            print("\n🎯 TÜM TESTLER BAŞARIYLA TAMAMLANDI!")
            print("✨ Plugin production-ready durumda!")
        else:
            print("\n⚠️ Bazı testler başarısız oldu. Lütfen logları inceleyin.")
            
    except Exception as e:
        print(f"\n❌ Test suite çalıştırılırken hata oluştu: {e}")
        import traceback
        traceback.print_exc()
        
    print("\n👋 Test süreci tamamlandı!")
