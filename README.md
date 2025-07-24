# 🔧 Generator Efficiency Calculator

A simple Windows GUI application to calculate Diesel Generator parameters:  
- **Electrical Output (kWe)**
- **Mechanical Input (kWm)**
- **Efficiency (%)**

Built with **Python Tkinter** for educational and engineering purposes.

---

## 📊 **Functions Available**
| Option                  | Input                          | Output               |
|--------------------------|--------------------------------|-----------------------|
| **Calculate kWe**        | Mechanical Input (kWm), Efficiency (%) | Electrical Output (kWe) |
| **Calculate kWm**        | Electrical Output (kWe), Efficiency (%) | Mechanical Input (kWm) |
| **Calculate Efficiency** | Electrical Output (kWe), Mechanical Input (kWm) | Efficiency (%)         |

---

## 💻 **How to Run**
### 1️⃣ Install Python 3.11+  
[Download Python](https://www.python.org/downloads/)

---

### 2️⃣ Install Dependencies
No external dependencies needed beyond standard Python.  
Tkinter is included in standard Python distributions.

---

### 3️⃣ Run the App (Python Script)
```bash
python Alternator_Efficiency_kWm_to_kWe_GUI.py
```

---

## 📦 **Build `.exe` with PyInstaller**
Requires **PyInstaller**:

```bash
pip install pyinstaller
```

### ✅ Safer Build (Recommended)
```bash
pyinstaller --noconfirm --windowed --onedir ^
  --icon=black.ico ^
  --version-file=version.txt ^
  Alternator_Efficiency_kWm_to_kWe_GUI.py
```

The `.exe` will appear in the `dist/Alternator_Efficiency_kWm_to_kWe_GUI/` directory.  
This method avoids antivirus false positives caused by temp file unpacking in `--onefile`.

---

## 🔐 **Self-Sign the EXE (Optional)**

You can self-sign the executable to reduce security warnings using OpenSSL and `osslsigncode`.

### 🛠 1. Generate Self-Signed Certificate
```bash
openssl req -new -newkey rsa:2048 -nodes -x509 -days 365 \
  -keyout my_private.key -out my_cert.crt
```

### 🔐 2. Create `.p12` Package
```bash
openssl pkcs12 -export -out my_cert.p12 \
  -inkey my_private.key -in my_cert.crt
```

### ✍️ 3. Sign the Executable
```bash
osslsigncode sign \
  -pkcs12 my_cert.p12 \
  -pass your_password \
  -n "Alternator Efficiency GUI" \
  -i "https://daikai.com" \
  -t http://timestamp.digicert.com \
  -in dist/Alternator_Efficiency_kWm_to_kWe_GUI/Alternator_Efficiency_kWm_to_kWe_GUI.exe \
  -out dist/Alternator_Efficiency_kWm_to_kWe_GUI/Alternator_Efficiency_kWm_to_kWe_signed.exe
```

---

### ✅ Verify the Signature (Linux)
```bash
osslsigncode verify dist/.../your_signed.exe
```

### ✅ Verify on Windows
```powershell
Get-AuthenticodeSignature .\your_signed.exe
```

If `Status` shows `UnknownError`, import the `my_cert.crt` into the **Windows Trusted Root Certification Authorities** to trust the self-signed cert.

---

## 📂 **Project Structure**
```
/your-folder/
├─ Alternator_Efficiency_kWm_to_kWe_GUI.py
├─ black.ico
├─ version.txt
├─ my_cert.crt
├─ my_cert.p12
├─ my_private.key
└─ README.md
```

---

## 🖼️ **Sample Screenshot**
<img width="398" height="329" alt="image" src="https://github.com/user-attachments/assets/0a44c34b-76b7-493c-a15c-dc0cefae9274" />


---

## 🛠 **Features**
✅ Simple & Lightweight  
✅ GUI-based (No terminal needed)  
✅ Engineering-friendly  
✅ Includes version info, icon, and metadata  
✅ Optionally signed `.exe` for improved trustworthiness

---

## 👤 **Author**
**Romel Mendoza**  
Created for learning and practical engineering tools.

---

## 📝 **License**
Feel free to modify and distribute for educational or non-commercial use.
