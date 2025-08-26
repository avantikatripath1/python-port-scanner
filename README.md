# 🔎 Python Port Scanner

A simple yet powerful **multi-threaded port scanner** written in Python.  
This tool scans a target host for open TCP ports and attempts to grab service banners.

---

## ✨ Features
- ✅ Multi-threaded scanning (fast + efficient)  
- ✅ Banner grabbing (detects running services if available)  
- ✅ Customizable port range (default: 1–1024)  
- ✅ Colored terminal output with `colorama`  
- ✅ Option to save results to a file  

---

## ⚙️ Installation
Clone the repository and install dependencies:
bash:
git clone https://github.com/avantikatripath1/python-port-scanner.git
cd python-port-scanner
pip install -r requirements.txt

## 🚀 Usage

Run the scanner with:

python scanner.py -t <target> -p <start-end> -o results.txt

## Example:
python scanner.py -t scanme.nmap.org -p 20-100

## Output:
Scanning target scanme.nmap.org (45.33.32.156) from port 20 to 100...

[OPEN] 45.33.32.156:22 | OpenSSH 6.6.1
[OPEN] 45.33.32.156:80 | Apache httpd

## 📂 Project Structure
.
├── scanner.py       # Main port scanner script
├── LICENSE          # License file
├── .gitignore       # Ignore Python cache & environment files

## 📜 License

This project is licensed under the MIT License.
Feel free to use, modify, and share!

