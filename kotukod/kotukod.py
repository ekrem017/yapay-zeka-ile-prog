import os
from google import genai
from google.genai import errors, types


def kod_optimize_et(spagetti_kod: str) -> None:
    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 75)
    print(" YAPAY ZEKA DESTEKLİ KOD İYİLEŞTİRME VE OPTİMİZASYON ".center(75))
    print("=" * 75)

    api_anahtari = "AQ.Ab8RN6JRfFjxCaG51mHDrUlJaP6H2ls0lxSRO1E2ZA6JY11AVQ"

    if not api_anahtari:
        print("\n[HATA] GEMINI_API_KEY tanımlanmamış!")
        return

    # 1. DÜZELTME: client nesnesi başlatıldı
    client = genai.Client(api_key=api_anahtari)

    sistem_mesaji = """
    Sen kıdemli bir Yazılım Mimarı ve Performans Uzmanısın.

    Kullanıcının gönderdiği kötü yazılmış (spagetti)
    Python kodunu analiz et.

    1. Değişken isimlerini anlamlı hale getir (Clean Code).
    2. Algoritmanın çalışma hızını iyileştir.
       Örneğin O(n^2) yerine mümkünse O(n) kullan.
    3. Type Hint (Tip belirteçleri) ekle.
    4. Kodun mevcut işlevselliğini koru.
    5. Gereksiz döngüleri ortadan kaldır.

    Çıktın KESİNLİKLE sadece düzeltilmiş saf Python kodu olmalıdır.
    Ek açıklama veya Markdown (```python ... ```) yazma.
    """

    print("\n[AŞAMA 1] OPTİMİZE EDİLECEK SPAGETTİ KOD SİSTEME ALINDI...")
    print("\n[AŞAMA 2] REFACTORING İÇİN YAPAY ZEKAYA BAĞLANILIYOR...\n")

    try:
        # 2. DÜZELTME: Model adı boşluksuz yazıldı
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"Optimize edilecek kod:\n{spagetti_kod}",
            config=types.GenerateContentConfig(
                system_instruction=sistem_mesaji,
                temperature=0.2,
            ),
        )

        temiz_kod = response.text

        if not temiz_kod:
            print("\n[HATA] Yapay zeka boş cevap döndürdü.")
            return

        # Varsa Markdown işaretlerini temizle
        temiz_kod = (
            temiz_kod.replace("```python", "").replace("```", "").strip()
        )

        print("=" * 75)
        print(" [AŞAMA 3] OPTİMİZE EDİLMİŞ CLEAN CODE ".center(75))
        print("=" * 75)
        print(temiz_kod)
        print("=" * 75)

    except errors.APIError as e:
        print(f"\n[API HATASI] {e}")
    except Exception as e:
        print(f"\n[SİSTEM HATASI] Beklenmeyen hata: {e}")


# ========================================================
# 3. DÜZELTME: Fonksiyonun dışına taşındı ve __name__ düzeltildi
# ========================================================
if __name__ == "__main__":
    # Test edilecek spagetti kod örneği
    kotu_kod = """
def bul(l):
    r = []
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] == l[j] and l[i] not in r:
                r.append(l[i])
    return r
"""
    kod_optimize_et(kotu_kod)