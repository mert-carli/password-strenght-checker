# 🔐 Password Strength Checker & Generator

A simple yet powerful Python application that helps users evaluate the strength of their passwords and generate secure ones based on custom preferences.

## 🧰 Features

- ✅ Analyze the strength of any password (scale: 0 to 4)
- 🔄 Generate strong passwords based on:
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Symbols
  - Custom length
- 📚 Learn about password best practices
- 🧑‍💻 Interactive CLI experience

## 🚀 How It Works

1. User enters a password  
2. System checks and rates the password's strength  
3. If the password is weak, the system asks:
   - Do you want lowercase letters?
   - Do you want uppercase letters?
   - Do you want digits?
   - Do you want symbols?
   - Desired password length  
4. A strong password is generated based on these inputs

---

### 🔎 Sample Interaction

```bash
🔐 Şifrenizi girin: mert123
⚠️ Şifreniz zayıf. Güç seviyesi: 2/4

💡 Güçlü şifre oluşturmak için tercihlerinizi belirtin:
→ Küçük harf olsun mu? (e/h): e
→ Büyük harf olsun mu? (e/h): e
→ Rakam olsun mu? (e/h): e
→ Özel karakter (!,?,%) olsun mu? (e/h): e
→ Şifre uzunluğu kaç karakter olsun? (örn: 12): 10

🔑 Önerilen güçlü şifre: Z!3eGv9u@K
