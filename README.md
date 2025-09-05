"# Pocket
## 👥 สมาชิกกลุ่ม
1. นายนนทพัทธ์ นะทีศรี  6712732108  
2. นายวทัญญู ช่างเกวียน  6712732117  
3. นายนิลรักษ์ บุตรโพธิ์ศรี  6712732130  
4. นางสาวจีรนันท์ เกิดกล้า  6712732121  

📁 โครงสร้างโปรเจกต์
bash🏗️ pocket/
│
├── 📄 manage.py                    # Django management script
├── 📋 requirements.txt             # Python dependencies  
├── 🗃️ db.sqlite3                  # ฐานข้อมูล SQLite
├── 📂 env/                         # Virtual environment
│
├── 📂 pocket/                      # 🏛️ โปรเจกต์หลัก
│   ├── ⚙️  settings.py            #    การตั้งค่าระบบ
│   ├── 🌐 urls.py                 #    URL routing หลัก
│   ├── 🔧 wsgi.py                 #    WSGI configuration
│   └── 🔧 asgi.py                 #    ASGI configuration
│
├── 📂 wallet/                      # 💰 Django app หลัก
│   ├── 🎯 models.py               #    โมเดลฐานข้อมูล
│   ├── 👁️  views.py               #    Logic การทำงาน
│   ├── 🌐 urls.py                 #    URL routing app
│   ├── 🔧 admin.py                #    ระบบแอดมิน
│   ├── 🧪 tests.py                #    การทดสอบ
│   └── 📦 migrations/             #    Database migrations
│
├── 📂 templates/                   # 🎨 HTML Templates
│   ├── 🏠 base.html               #    Template หลัก
│   ├── 🏠 home.html               #    หน้าหลัก
│   ├── 🔐 login.html              #    หน้าล็อกอิน
│   └── 📝 register.html           #    หน้าสมัครสมาชิก
│
├── 📂 static/                      # 🎭 Static Files (Development)
│   ├── 🎨 css/                    #    Stylesheets
│   │   └── 💅 style.css          #    ไฟล์ CSS หลัก
│   ├── ⚡ js/                     #    JavaScript Files
│   │   └── 🚀 script.js          #    ไฟล์ JS หลัก
│   └── 🖼️  images/                #    รูปภาพและไอคอน
│       └── 📸 logo.png           #    โลโก้เว็บไซต์
│
└── 📂 staticfiles/                 # 📦 Static Files (Production)
    └── 🏭 รวบรวมไฟล์ static สำหรับ deploy
Pocket เป็นเว็บแอปพลิเคชัน Django สำหรับจัดการระบบ wallet และผู้ใช้

## โครงสร้างโปรเจกต์
- `manage.py` - สคริปต์หลักสำหรับจัดการโปรเจกต์ Django
- `requirements.txt` - รายการ dependencies ที่ใช้ในโปรเจกต์
- `pocket/` - โฟลเดอร์โปรเจกต์หลัก (settings, urls, wsgi, asgi)
- `wallet/` - Django app สำหรับฟีเจอร์ wallet
- `templates/` - เทมเพลต HTML สำหรับหน้าเว็บ
- `static/` - ไฟล์ static เช่น CSS, JS, รูปภาพ
- `db.sqlite3` - ฐานข้อมูล SQLite
- `env/` - Python virtual environment

## โครงสร้างเว็บไซต์
- หน้า Home (`home.html`): แสดงรายการธุรกรรม, ยอดเงิน, เพิ่ม/ลบธุรกรรม
- หน้า Login (`login.html`): สำหรับเข้าสู่ระบบผู้ใช้
- หน้า Register (`register.html`): สำหรับสมัครสมาชิกใหม่
- Template หลัก (`base.html`): โครงสร้างพื้นฐานของทุกหน้า
- Static Files: ไฟล์ CSS, JS, รูปภาพ สำหรับตกแต่งหน้าเว็บ

## ฟีเจอร์หลัก
- สมัครสมาชิก / ล็อกอิน / ล็อกเอาท์
- เพิ่มธุรกรรม (รายรับ/รายจ่าย)
- ลบธุรกรรม
- แสดงยอดเงินรวม, รายรับ, รายจ่าย
- ระบบแอดมิน Django สำหรับจัดการข้อมูล

## โครงสร้างฐานข้อมูล
- **Transaction**
  - user: ผู้ใช้ที่สร้างธุรกรรม (ForeignKey)
  - name: ชื่อธุรกรรม
  - description: รายละเอียด
  - amount: จำนวนเงิน
  - transaction_type: ประเภท (1=รายรับ, -1=รายจ่าย)
  - created_at, updated_at: เวลาสร้าง/แก้ไข

## URL Routing
- `/` : หน้า Home (wallet.views.home)
- `/login/` : หน้า Login (wallet.views.login_view)
- `/register/` : หน้า Register (wallet.views.register_view)
- `/delete_transaction/<id>/` : ลบธุรกรรม
- `/logout/` : ออกจากระบบ

## วิธีติดตั้งและรันโปรเจกต์
1. สร้าง virtual environment และติดตั้ง dependencies:
   ```
   python -m venv env
   .\env\Scripts\activate
   pip install -r requirements.txt
   ```
2. รัน migrations:
   ```
   python manage.py migrate
   ```
3. รันเซิร์ฟเวอร์:
   ```
   python manage.py runserver
   ```
4. เข้าใช้งานที่ http://127.0.0.1:8000/

## การใช้งาน
- สมัครสมาชิกใหม่ที่หน้า Register
- ล็อกอินเข้าสู่ระบบ
- เพิ่มธุรกรรม (ระบุชื่อ, จำนวนเงิน, ประเภท)
- ดูยอดเงินรวม, รายรับ, รายจ่าย
- ลบธุรกรรมที่ไม่ต้องการ

## ส่วนของแอดมิน
- เข้าสู่ระบบแอดมินที่ `/admin/` ด้วย superuser
- จัดการข้อมูลธุรกรรมและผู้ใช้

## License
MIT
