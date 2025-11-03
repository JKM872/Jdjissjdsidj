# 👥 Tryb GOŚCI - Dokumentacja

## 🎯 Co nowego?

### **DUAL MODE: Analiza Gospodarzy + Gości = 2 Emaile!** 🏠👥

Wcześniej scraper analizował **tylko gospodarzy**. Teraz automatycznie sprawdza:
- 🏠 **Gospodarze** - czy mają ≥80% H2H
- 👥 **Goście** - czy mają ≥60% H2H (łatwiejsze kryteria!)

**Rezultat:** Otrzymujesz **2 osobne emaile**:
1. `[GOSPODARZE 🏠] Typy Bukmacherskie` - mecze gdzie gospodarz dominuje
2. `[GOŚCIE 👥] Typy Bukmacherskie` - mecze gdzie gość dominuje

---

## 📋 Funkcje

### 1. **Osobne Wymagania dla Gości**

Goście mają **łatwiejsze** kryteria kwalifikacji:

| Kryterium | Gospodarze 🏠 | Goście 👥 |
|---|---|---|
| **Wygrane H2H** | ≥4/5 (80%) | ≥3/5 (60%) |
| **Win Rate** | ≥80% | ≥60% |
| **Min. H2H** | 5 meczów | 3 mecze |

**Dlaczego?**
- Goście rzadziej wygrywają (trudniej u siebie)
- Jeśli gość ma 60%+ H2H = silny sygnał!

---

### 2. **Osobne Emaile**

**Email 1: GOSPODARZE 🏠**
```
Subject: [GOSPODARZE 🏠] 12 kwalifikujących się meczów - 2025-11-03

✅ Mecz 1: Zenit Kazań vs Fakieł Nowy Urengoj
   🏠 Gospodarz: Zenit Kazań
   📊 H2H: 5/5 (100%)
   💰 Kurs: 1.35
   
✅ Mecz 2: ...
```

**Email 2: GOŚCIE 👥**
```
Subject: [GOŚCIE 👥] 7 kwalifikujących się meczów - 2025-11-03

✅ Mecz 1: Podgorica vs Jarosław
   👥 Gość: Jarosław
   📊 H2H: 3/5 (60% - wystarczy dla gości!)
   💰 Kurs: 2.10
   
✅ Mecz 2: ...
```

---

### 3. **Dual Analysis - Jeden Mecz, Dwie Szanse**

Przykład:
```
Mecz: Zenit Kazań vs Fakieł Nowy Urengoj

H2H historia:
- Zenit (dom): 5 wygranych
- Fakieł (gość): 0 wygranych

✅ KWALIFIKUJE jako GOSPODARZE (Zenit 5/5 = 100%)
❌ Nie kwalifikuje jako GOŚCIE (Fakieł 0/5 = 0%)

Rezultat: Email tylko w "GOSPODARZE"
```

Inny przykład:
```
Mecz: Podgorica vs Jarosław

H2H historia:
- Podgorica (dom): 2 wygrane
- Jarosław (gość): 3 wygrane

❌ Nie kwalifikuje jako GOSPODARZE (2/5 = 40% < 80%)
✅ KWALIFIKUJE jako GOŚCIE (3/5 = 60%)

Rezultat: Email tylko w "GOŚCIE"
```

---

## ⚙️ Konfiguracja

### **Domyślne Ustawienia (scrape_and_notify.py, linia 23-45)**

```python
# ============================================================================
# KONFIGURACJA ANALIZY - GOSPODARZE vs GOŚCIE
# ============================================================================

ANALYZE_HOME_TEAM = True      # Analizuj gospodarzy
ANALYZE_AWAY_TEAM = True      # Analizuj gości
SEND_SEPARATE_EMAILS = True   # Osobne maile (True) lub jeden (False)

# Warunki kwalifikacji dla GOSPODARZY
HOME_TEAM_REQUIREMENTS = {
    'min_h2h_wins': 4,           # ≥4 wygrane
    'min_win_rate': 0.8,         # ≥80%
    'min_h2h_count': 5,          # ≥5 meczów
    'require_form_advantage': False
}

# Warunki kwalifikacji dla GOŚCI (ŁATWIEJSZE!)
AWAY_TEAM_REQUIREMENTS = {
    'min_h2h_wins': 3,           # ≥3 wygrane (łatwiej)
    'min_win_rate': 0.6,         # ≥60% (łatwiej)
    'min_h2h_count': 3,          # ≥3 mecze
    'require_form_advantage': False
}
```

---

### **Przykłady Konfiguracji**

#### **1. Tylko Gospodarze (jak dawniej)**
```python
ANALYZE_HOME_TEAM = True
ANALYZE_AWAY_TEAM = False    # Wyłącz gości
SEND_SEPARATE_EMAILS = True
```

#### **2. Tylko Goście**
```python
ANALYZE_HOME_TEAM = False    # Wyłącz gospodarzy
ANALYZE_AWAY_TEAM = True
SEND_SEPARATE_EMAILS = True
```

#### **3. Obaj, ale JEDEN EMAIL**
```python
ANALYZE_HOME_TEAM = True
ANALYZE_AWAY_TEAM = True
SEND_SEPARATE_EMAILS = False  # Jeden email z home+away
```

#### **4. Goście z WYŻSZYMI wymaganiami (trudniej)**
```python
AWAY_TEAM_REQUIREMENTS = {
    'min_h2h_wins': 5,           # Jak gospodarze!
    'min_win_rate': 0.8,         # Jak gospodarze!
    'min_h2h_count': 5,
    'require_form_advantage': True  # WYMAGA przewagi formy
}
```

#### **5. Goście z NIŻSZYMI wymaganiami (więcej typów)**
```python
AWAY_TEAM_REQUIREMENTS = {
    'min_h2h_wins': 2,           # Tylko 2 wygrane!
    'min_win_rate': 0.5,         # Tylko 50%!
    'min_h2h_count': 3,
    'require_form_advantage': False
}
```

---

## 🚀 Użycie

### **A. Lokalnie (Command Line)**

#### **1. Domyślnie (OBAJ, 2 emaile)**
```powershell
python scrape_and_notify.py --date 2025-11-03 --sports volleyball --to twoj@email.com --from-email twoj@email.com --password "haslo"
```
**Rezultat:** 2 emaile (gospodarze + goście)

#### **2. TYLKO Gospodarze**
```powershell
python scrape_and_notify.py --date 2025-11-03 --sports volleyball --to twoj@email.com --from-email twoj@email.com --password "haslo" --home-only
```
**Rezultat:** 1 email (tylko gospodarze)

#### **3. TYLKO Goście**
```powershell
python scrape_and_notify.py --date 2025-11-03 --sports volleyball --to twoj@email.com --from-email twoj@email.com --password "haslo" --away-only
```
**Rezultat:** 1 email (tylko goście)

#### **4. OBAJ w JEDNYM emailu**
```powershell
python scrape_and_notify.py --date 2025-11-03 --sports volleyball --to twoj@email.com --from-email twoj@email.com --password "haslo" --combined-email
```
**Rezultat:** 1 email (home+away razem)

---

### **B. GitHub Actions (Automatyczne)**

#### **Manual Trigger z wyborem trybu:**

1. Idź do: https://github.com/JKM872/Jdjissjdsidj/actions
2. Wybierz workflow: "Scheduled Job at 2:00 UTC"
3. Kliknij "Run workflow"
4. Wybierz tryb:
   - **both** (domyślnie) - Gospodarze + Goście (2 emaile)
   - **home-only** - Tylko gospodarze
   - **away-only** - Tylko goście
   - **combined** - Jeden email (home+away)

#### **Automatyczny run o 2:00 UTC:**
Workflow domyślnie uruchamia tryb **"both"** (2 emaile).

Aby zmienić domyślny tryb, edytuj `.github/workflows/scheduled-job.yml`:
```yaml
# Linia 44
echo "🎯 Tryb: ${{ github.event.inputs.mode || 'both' }}"

# Zmień 'both' na:
# - 'home-only' (tylko gospodarze)
# - 'away-only' (tylko goście)
# - 'combined' (jeden email)
```

---

## 📊 Przykładowe Wyniki

### **Scenariusz 1: 50 meczów volleyball**

```
📊 STATYSTYKI SCRAPINGU
====================================================================
⏱️  Całkowity czas: 14.2 minut
📦 Meczów przetworzonych: 50
🏠 Gospodarze kwalifikują: 12
👥 Goście kwalifikują: 7
✅ Łącznie kwalifikujących: 19
💾 Cache hits: 0 (0% - pierwszy run)
====================================================================

📊 CAŁKOWITE PODSUMOWANIE
====================================================================
🏠 Gospodarze: 12 meczów
👥 Goście: 7 meczów
📧 Emaili wysłanych: 2
====================================================================
```

**Emaile:**
1. `[GOSPODARZE 🏠] 12 kwalifikujących się meczów - 2025-11-03`
2. `[GOŚCIE 👥] 7 kwalifikujących się meczów - 2025-11-03`

---

### **Scenariusz 2: Drugi run tego samego dnia (cache)**

```
📊 STATYSTYKI SCRAPINGU
====================================================================
⏱️  Całkowity czas: 2.1 minut (85% szybciej!)
📦 Meczów przetworzonych: 50
🏠 Gospodarze kwalifikują: 12
👥 Goście kwalifikują: 7
✅ Łącznie kwalifikujących: 19
💾 Cache hits: 50 (100% - wszystko z cache!)
====================================================================
```

---

## 🎓 FAQ

### **Q: Czy mogę dostać JEDEN email z home+away?**
A: Tak! Użyj flagi `--combined-email`:
```powershell
python scrape_and_notify.py ... --combined-email
```
Lub ustaw w kodzie:
```python
SEND_SEPARATE_EMAILS = False
```

---

### **Q: Czy mogę mieć TAKIE SAME wymagania dla gości i gospodarzy?**
A: Tak! Skopiuj HOME_TEAM_REQUIREMENTS:
```python
AWAY_TEAM_REQUIREMENTS = HOME_TEAM_REQUIREMENTS.copy()
```

---

### **Q: Co jeśli mecz kwalifikuje się jako OBAJ (dom+gość)?**
A: Możliwe (jeśli oba zespoły mają wysokie H2H), ale rzadkie:
- Mecz pojawi się w **obu emailach**
- Każdy email pokazuje inną perspektywę (dom vs gość)

---

### **Q: Czy mogę wyłączyć tryb gości całkowicie?**
A: Tak! Ustaw:
```python
ANALYZE_AWAY_TEAM = False
```
Lub użyj flagi:
```powershell
python scrape_and_notify.py ... --home-only
```

---

### **Q: Dlaczego goście mają łatwiejsze wymagania?**
A: Bo gość zwykle gra "u wroga" (bez wsparcia fanów, długa podróż). Jeśli mimo to ma 60%+ H2H = naprawdę silny!

---

### **Q: Czy to spowalnia scraping?**
A: **NIE!** Jeden mecz = jedna analiza:
- Pobiera dane raz
- Sprawdza 2 warunki (home + away)
- Dodaje do odpowiednich list

Czas taki sam jak przedtem! 🚀

---

## 🐛 Troubleshooting

### **Problem: Dostaję tylko 1 email (zamiast 2)**
**Rozwiązanie:**
```python
# Sprawdź ustawienia (scrape_and_notify.py linia 23)
ANALYZE_HOME_TEAM = True      # Musi być True
ANALYZE_AWAY_TEAM = True      # Musi być True
SEND_SEPARATE_EMAILS = True   # Musi być True
```

---

### **Problem: Dostaję 2 puste emaile**
**Rozwiązanie:**
- Sprawdź czy wymagania nie są zbyt wysokie
- Zmniejsz `min_h2h_wins` lub `min_win_rate`
- Uruchom z `--max-matches 10` do testów

---

### **Problem: Zbyt wiele typów dla gości**
**Rozwiązanie:**
```python
# Zwiększ wymagania dla gości
AWAY_TEAM_REQUIREMENTS = {
    'min_h2h_wins': 4,      # Wyżej (było 3)
    'min_win_rate': 0.7,    # Wyżej (było 0.6)
    'min_h2h_count': 5,
    'require_form_advantage': True  # Dodaj przewagę formy
}
```

---

## ✅ Podsumowanie

| Funkcja | Status | Opis |
|---|---|---|
| **Dual Analysis** | ✅ | Sprawdza home + away |
| **Osobne Emaile** | ✅ | 2 emaile (domyślnie) |
| **Osobne Wymagania** | ✅ | Goście łatwiej (60% vs 80%) |
| **Command-Line Flagi** | ✅ | `--home-only`, `--away-only`, `--combined-email` |
| **GitHub Actions** | ✅ | Manual trigger z wyborem trybu |
| **Cache Compatible** | ✅ | Działa z cache system |
| **Adaptive Throttling** | ✅ | Działa z adaptive delays |

---

## 🎉 Przykładowy Output

```
🔄 KROK 2/3: Przetwarzanie 50 meczów...
====================================================================

[1/50] Przetwarzam: Zenit Kazań vs Fakieł Nowy Urengoj
   🏠 GOSPODARZE: KWALIFIKUJE! Zenit Kazań vs Fakieł Nowy Urengoj
      H2H: 5/5 (100%)
      Forma: Zenit [W-W-W-W-W] | Fakieł [L-L-L-L-L]
   ❌ GOŚCIE: Nie kwalifikuje (0/5)

[2/50] Przetwarzam: Podgorica vs Jarosław
   ❌ GOSPODARZE: Nie kwalifikuje (2/5 = 40%)
   👥 GOŚCIE: KWALIFIKUJE! Jarosław @ Podgorica
      H2H: 3/5 (60%)
      Forma: Podgorica [W-L-L-W-L] | Jarosław [W-W-W-L-W]

...

📊 CAŁKOWITE PODSUMOWANIE
====================================================================
🏠 Gospodarze: 12 meczów
👥 Goście: 7 meczów
📧 Emaili wysłanych: 2
====================================================================

✅ Email dla GOSPODARZY wysłany!
✅ Email dla GOŚCI wysłany!
```

---

**Status:** ✅ READY TO USE  
**Wersja:** 2.1 (z trybem GOŚCI)  
**Data:** 2025-11-03
