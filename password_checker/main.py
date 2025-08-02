import random
import string

def guclu_sifre_uret(uzunluk=12, kucuk=True, buyuk=True, rakam=True, ozel=False):
    karakterler = ''
    if kucuk:
        karakterler += string.ascii_lowercase
    if buyuk:
        karakterler += string.ascii_uppercase
    if rakam:
        karakterler += string.digits
    if ozel:
        karakterler += string.punctuation

    if karakterler == '':
        return "❌ En az bir karakter türü seçmelisiniz!"

    return ''.join(random.choice(karakterler) for _ in range(uzunluk))

def sifre_guclulugu(sifre):
    puan = 0
    if any(c.islower() for c in sifre): puan += 1
    if any(c.isupper() for c in sifre): puan += 1
    if any(c.isdigit() for c in sifre): puan += 1
    if any(c in string.punctuation for c in sifre): puan += 1
    return puan

# Kullanıcıdan şifre al
sifre = input("🔐 Şifrenizi girin: ")
puan = sifre_guclulugu(sifre)

if puan == 4:
    print("✅ Şifreniz güçlü.")
else:
    print(f"⚠️ Şifreniz zayıf. Güç seviyesi: {puan}/4")

    print("\n💡 Güçlü şifre oluşturmak için tercihlerinizi belirtin:")
    kucuk = input("→ Küçük harf olsun mu? (e/h): ").lower() == 'e'
    buyuk = input("→ Büyük harf olsun mu? (e/h): ").lower() == 'e'
    rakam = input("→ Rakam olsun mu? (e/h): ").lower() == 'e'
    ozel  = input("→ Özel karakter (!,?,%) olsun mu? (e/h): ").lower() == 'e'
    
    try:
        uzunluk = int(input("→ Şifre uzunluğu kaç karakter olsun? (örn: 12): "))
    except ValueError:
        uzunluk = 12  # geçersiz giriş olursa varsayılan değer

    oneri = guclu_sifre_uret(uzunluk, kucuk, buyuk, rakam, ozel)
    print("🔑 Önerilen güçlü şifre:", oneri)
