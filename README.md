- `app.py`: Flask backend fayli, API endpointlari, broker bilan integratsiya, va foydalanuvchi buyurtmalarini boshqaradi.

- `config.py`: API kalitlari, broker sozlamalari va konfiguratsiya parametrlarini saqlaydi.

- `utils.py`: Forex tahlili uchun kerakli yordamchi funksiyalar (masalan, Moving Average, RSI) mavjud.

- `templates/index.html`: Foydalanuvchi interfeysi (HTML) bu fayl orqali taqdim etiladi. UI foydalanuvchidan ma'lumotlar olish va savdo buyurtmalarini yuborish uchun kerakli maydonlarni taqdim etadi.

- `static/styles.css`: Web interfeysining dizaynini o'rnatadi.

- `static/app.js`: JavaScript kodi, HTML elementlar bilan ishlash va Flask API bilan o'zaro aloqalar uchun.

- `requirements.txt`: Flask, ccxt, pandas kabi kutubxonalarni o'rnatish uchun kerakli ro'yxat.

- `.env`: Muhim muhit o'zgaruvchilari (API kalitlari, sirlar, va boshqalar) saqlanadi.




Forex-Bot/
├── app.py (Flask backend asosiy fayli)
├── config.py (Loyihaning konfiguratsiya fayli)
├── utils.py (Yordamchi funksiyalar)
├── templates/
│   └── index.html (Frontend HTML fayli)
├── static/
│   ├── styles.css (CSS fayl)
│   └── app.js (JavaScript fayl)
├── requirements.txt (Python kutubxonalari ro'yxati)
└── .env (Muhim muhit o'zgaruvchilari uchun fayl)
