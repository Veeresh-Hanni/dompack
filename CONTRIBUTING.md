# 🤝 Contributing to Dompack

Thank you for your interest in contributing!  
Follow this guide to contribute safely and effectively.

---

## 🛠 Requirements

- Python 3.8+
- pip / venv
- GitHub account
- Basic understanding of Python packaging

---

## 🚀 Getting Started

### 1. Fork the repository
Click **Fork** on GitHub.

### 2. Clone your fork
```
git clone https://github.com/<your-username>/dompack.git
cd dompack
```

### 3. Create a virtual environment
```
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate       # Windows
```

### 4. Install in editable mode
```
pip install -e .
```

---

## 🧪 Running Tests
(Tests coming soon)

```
pytest
```

---

## 📦 Adding New Bundles

Add new bundles in:

```
dompack/bundles.py
```

Each bundle must:
- Have a short alias  
- Be added to `EXTRAS = {}`  
- Contain production-ready, safe packages  

Example:
```python
EXTRAS["automation"] = [
    "selenium",
    "pyautogui",
    "playsound"
]
```

---

## 🧾 Commit Guidelines

- Use descriptive messages
- Prefix types:
  - `feat:` new feature
  - `fix:` bug fix
  - `docs:` documentation
  - `refactor:` code improvements
  - `perf:` performance
  - `test:` test-related

Example:
```
feat: added new AI bundle
```

---

## 🚀 Creating Releases

```
git tag v0.2.0
git push --tags
```

GitHub Actions will publish to PyPI automatically.

---

## ❤️ Thank You
Your contributions help grow Dompack into a universal Python stack manager.
