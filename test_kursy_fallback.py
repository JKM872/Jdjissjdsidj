"""
Test szybki - sprawdzenie nowego systemu fallback dla kursów
"""

from livesport_odds_api_client import LiveSportOddsAPI

print("="*70)
print("🎲 TEST NOWEGO SYSTEMU POBIERANIA KURSÓW")
print("="*70)

# Przykładowe URLe z załączonego JSON (mecze które miały NULL)
test_urls = [
    # Mecze które NIE miały kursów (teraz powinny mieć):
    "https://www.livesport.com/pl/mecz/siatkowka/jedinstvo-QZJOsBri/podgorica-dfQqb0kJ/?mid=xK8m5sr3",
    "https://www.livesport.com/pl/mecz/siatkowka/bar-8jAqMeog/herceg-novi-hxDW60YS/?mid=v3sJ0MiA",
    "https://www.livesport.com/pl/mecz/siatkowka/kemerovo-hbFonVBi/mgtu-moscow-OSDwWRtI/?mid=KItZq18e",
    
    # Mecz który MAJ kurs (dla porównania):
    "https://www.livesport.com/pl/mecz/siatkowka/sao-jose-dos-campos-xfxfdEus/suzano-volei-p298ASFI/?mid=dhX45fke",
]

print("\n🔍 Testowanie z FALLBACK (próbuje wielu bukmacherów):\n")

client = LiveSportOddsAPI()

for i, url in enumerate(test_urls, 1):
    print(f"\n[{i}/{len(test_urls)}] Test meczu:")
    print(f"URL: {url[:80]}...")
    
    # Test Z fallback
    odds = client.get_odds_from_url(url, use_fallback=True)
    
    if odds:
        print(f"✅ SUKCES!")
        print(f"   Bukmacher: {odds['bookmaker_name']}")
        print(f"   Home: {odds.get('home_odds')}")
        print(f"   Away: {odds.get('away_odds')}")
        if odds.get('draw_odds'):
            print(f"   Draw: {odds.get('draw_odds')}")
    else:
        print(f"❌ Brak kursów (sprawdzono 5 bukmacherów)")

print("\n" + "="*70)
print("✅ Test zakończony!")
print("="*70)
print("\nGDY już wszystko jest na GitHub:")
print("1. Workflow uruchomi się o 2:00 UTC")
print("2. Kursy będą pobierane z fallback")
print("3. Sprawdź logi w Actions → scheduled-job")
