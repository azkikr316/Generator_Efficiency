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

### 4️⃣ Build `.exe` (Optional for Windows)
Requires **PyInstaller**  
```bash
pip install pyinstaller
```

**Build Command:**
```bash
pyinstaller --noconsole --onefile --icon=black.ico --version-file=version.txt Alternator_Efficiency_kWm_to_kWe_GUI.py
```
The `.exe` will appear in the `dist/` folder.

---

## 📝 **Sample Screenshot**
> *Insert screenshot of your GUI here if available*

---

## 📂 **Project Structure**
```
/your-folder/
├─ Alternator_Efficiency_kWm_to_kWe_GUI.py
├─ black.ico
├─ version.txt
└─ README.md
```

---

## 🛠 **Features**
✅ Simple & Lightweight  
✅ GUI-based (No terminal needed)  
✅ Engineering-friendly  
✅ Ready for `.exe` distribution  
✅ Includes version info, icon, and metadata

---

## 👤 **Author**
**Romel Mendoza**  
Created for learning and practical engineering tools.

---

## 📝 **License**
Feel free to modify and distribute for educational or non-commercial use.
