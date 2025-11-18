
```
██████╗  ██████╗ ███╗   ███╗██████╗  █████╗  ██████╗██╗  ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║   ██║██╔████╔██║██████╔╝███████║██║     █████╔╝ 
██╔═══╝ ██║   ██║██║╚██╔╝██║██╔══██╗██╔══██║██║     ██╔═██╗ 
██║     ╚██████╔╝██║ ╚═╝ ██║██████╔╝██║  ██║╚██████╗██║  ██╗
╚═╝      ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
      Domain-Based Python Tech-Stack Installer
```

<p align="center"> <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/64/000000/external-python-computer-programming-icons-flaticons-lineal-color-flat-icons.png" /></p>

<p align="center"><img src="https://img.shields.io/badge/version-v0.1.1-blue?logo=python
" /> <img src="https://img.shields.io/pypi/dm/dompack?color=success" /> <img src="https://img.shields.io/badge/license-MIT-green" /> <img src="https://img.shields.io/badge/status-active-brightgreen" /> <img src="https://img.shields.io/pypi/pyversions/dompack" /> </p>


# 📦 Dompack – Domain-Based Python Tech-Stack Installer

Dompack installs complete Python tech stacks using short domain aliases:

```
dompack install fa      # FastAPI stack
dompack install dj      # Django stack
dompack install ml      # Machine Learning
dompack install ai      # AI / NLP
dompack install all     # Everything
```

Dompack removes the headache of installing many libraries manually.  
It gives you curated, domain-based bundles designed for fast development.

---

## 🚀 Features

### 🟦 Core Features
- 📦 Install entire Python stacks using domain aliases  
- ⚡ Clean, curated, production-ready bundles  
- 🎯 Short aliases (`fa`, `fl`, `dj`, `ml`, `ai`, `db`, …)  
- 🧪 Works on Windows, Linux, macOS  
- 🔐 Includes Security, Cryptography & Auth bundles  
- ⚙️ Supports ML, AI, DL, CV, GUI, DevOps, Web, File, Testing  
- 📦 Acts like a mini package manager (son of pip)

---

## 🆕 New Advanced CLI Features

### 🔧 Upgrade bundles
```
dompack upgrade <bundle>
```

### 🔍 Search inside bundles
```
dompack search <keyword>
```

### 🩺 Environment Doctor
```
dompack doctor
```

### 🔄 Self-update
```
dompack update-self
```

### 📝 Generate requirements.txt from bundle
```
dompack req <bundle>
```

### 🧱 Create custom bundles
```
dompack create-bundle <name> <pkg1> <pkg2> ...
```

---

## 📥 Installation

```
pip install dompack
```

Local development install:

```
pip install -e .
```

---

## 🧰 CLI Usage

### 🔍 List bundles
```
dompack list
```

### 📦 Install a bundle
```
dompack install <bundle>
```

Examples:

```
dompack install fa
dompack install dj
dompack install flask
dompack install ml
dompack install ai
dompack install db
dompack install all
```

---

## 📚 Domain Bundles

| Alias | Domain | Description |
|-------|--------|-------------|
| `db`, `da` | Databases | PostgreSQL, MySQL, MongoDB, Redis |
| `ds` | Data Science | numpy, pandas, matplotlib, scipy |
| `ml` | Machine Learning | scikit-learn, joblib |
| `ai` | AI / NLP | transformers, tokenizers |
| `dl` | Deep Learning | torch, torchvision |
| `cv` | Computer Vision | opencv-python, scikit-image, pillow |
| `gui` | GUI | PyQt5, Kivy |
| `av` | Audio / Video | librosa, moviepy |
| `web` | Web Utils | requests, httpx, beautifulsoup4 |
| `fa`, `fastapi` | FastAPI Stack | fastapi, uvicorn, pydantic |
| `fl`, `flask` | Flask Stack | flask & extensions |
| `dj`, `django` | Django Stack | django, DRF, cors headers |
| `net` | Networking | aiohttp, websockets, paramiko |
| `security`, `sec`, `auth`, `cyber` | Security | JWT, cryptography, passlib |
| `devops` | DevOps | docker, ansible |
| `testing` | Testing | pytest, black, flake8 |
| `file` | File Processing | docx, pypdf2, openpyxl |
| `utils` | Utilities | dotenv, rich, loguru |
| `fullstack` | Mixed Stack | Django + FastAPI + Flask |
| `all` | Everything | All bundles combined |

---

## 🧭 Examples

### FastAPI install
```
dompack install fa
```

### Django install
```
dompack install dj
```

### Machine Learning setup
```
dompack install ml
```

### Install EVERYTHING
```
dompack install all
```

### Upgrade a bundle
```
dompack upgrade security
```

### Search packages
```
dompack search mongo
```

### Generate requirements.txt
```
dompack req ml
```

### Environment doctor
```
dompack doctor
```

---

## 📝 License

MIT License © 2025 Veeresh Hanni

---

## ⭐ Support

If Dompack helps you:

- ⭐ Star it on GitHub  
- 🛠 Contribute new bundles  
- 📦 Share it with the Python community  

