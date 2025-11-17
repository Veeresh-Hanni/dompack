# dompack bundle definitions (human/CLI reference)
# Keep in sync with pyproject.toml's extras.

EXTRAS = {}

# Databases (db / da)
db = [
    "psycopg2-binary",
    "pymysql",
    "pymongo",
    "motor",
    "redis",
]
EXTRAS["db"] = db
EXTRAS["da"] = db

# Data Science (ds)
ds = [
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "statsmodels",
]
EXTRAS["ds"] = ds

# Machine Learning (ml)
ml = [
    "numpy",
    "pandas",
    "scikit-learn",
    "joblib",
    "matplotlib",
]
EXTRAS["ml"] = ml

# Artificial Intelligence (ai)
ai = [
    "transformers",
    "sentencepiece",
    "tokenizers",
]
EXTRAS["ai"] = ai

# Deep Learning (dl)
dl = [
    "torch",
    "torchvision",
]
EXTRAS["dl"] = dl

# Computer Vision (cv)
cv = [
    "opencv-python",
    "scikit-image",
    "pillow",
]
EXTRAS["cv"] = cv

# GUI (gui)
gui = [
    "PyQt5",
    "kivy",
    "tkinter",
]
EXTRAS["gui"] = gui

# Audio/Video (av)
av = [
    "librosa",
    "moviepy",
    "ffmpeg-python",
]
EXTRAS["av"] = av

# Web utilities (web)
web = [
    "requests",
    "httpx",
    "beautifulsoup4",
    "lxml",
]
EXTRAS["web"] = web

# FastAPI (fa / fastapi)
fa = [
    "fastapi",
    "uvicorn[standard]",
    "pydantic",
    "python-dotenv",
    "python-multipart",
    "jinja2",
    "sqlalchemy",
]
EXTRAS["fa"] = fa
EXTRAS["fastapi"] = fa

# Flask (fl / flask)
fl = [
    "Flask",
    "Flask-CORS",
    "Flask-RESTful",
    "Flask-JWT-Extended",
    "Flask-Migrate",
]
EXTRAS["fl"] = fl
EXTRAS["flask"] = fl

# Django (dj / django)
dj = [
    "Django",
    "djangorestframework",
    "django-cors-headers",
    "django-environ",
    "whitenoise",
]
EXTRAS["dj"] = dj
EXTRAS["django"] = dj

# Networking (net)
net = [
    "aiohttp",
    "websockets",
    "dnspython",
    "paramiko",
]
EXTRAS["net"] = net

# Security / Auth (security / sec / auth / cyber / cybersec)
security = [
    "cryptography",
    "PyJWT",
    "passlib[bcrypt]",
    "pycryptodome",
]
EXTRAS["security"] = security
EXTRAS["sec"] = security
EXTRAS["auth"] = security
EXTRAS["cyber"] = security
EXTRAS["cybersec"] = security

# DevOps (devops)
devops = [
    "docker",
    "docker-compose",
    "ansible",
]
EXTRAS["devops"] = devops

# Testing & dev tools
testing = [
    "pytest",
    "pytest-cov",
    "black",
    "flake8",
    "isort",
    "mypy",
]
EXTRAS["testing"] = testing

# File tools
file = [
    "openpyxl",
    "python-docx",
    "pypdf2",
]
EXTRAS["file"] = file

# Utilities
utils = [
    "python-dotenv",
    "loguru",
    "rich",
]
EXTRAS["utils"] = utils

# fullstack
fullstack = [
    "fastapi",
    "uvicorn[standard]",
    "Django",
    "Flask",
    "SQLAlchemy",
    "psycopg2-binary",
    "pymysql",
    "pymongo",
]
EXTRAS["fullstack"] = fullstack

# curated all (final)
_all = []
for v in EXTRAS.values():
    _all.extend(v)
EXTRAS["all"] = sorted(set(_all))
