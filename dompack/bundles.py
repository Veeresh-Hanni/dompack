# dompack bundle definitions (human/CLI reference)
# Keep this in sync with pyproject.toml [project.optional-dependencies].

from typing import Dict, List

EXTRAS: Dict[str, List[str]] = {}

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
    "torch; python_version >= '3.9' and python_version < '3.14'",
    "torchvision; python_version >= '3.9' and python_version < '3.14'",
]
EXTRAS["dl"] = dl

# Computer Vision (cv)
cv = [
    "opencv-python; platform_python_implementation == 'CPython'",
    "scikit-image",
    "pillow",
]
EXTRAS["cv"] = cv

# GUI (gui)
gui = [
    "PyQt5; python_version < '3.13'",
    "kivy; python_version < '3.13'",
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

# Common/core stack (common / core / base)
common = [
    "requests",
    "httpx",
    "python-dotenv",
    "pydantic",
    "rich",
    "loguru",
]
EXTRAS["common"] = common
EXTRAS["core"] = common
EXTRAS["base"] = common

# Python bootstrap tooling (bootstrap / boot / pytools)
bootstrap = [
    "pip",
    "setuptools",
    "wheel",
    "build",
    "packaging",
    "virtualenv",
    "pip-tools",
    "twine",
]
EXTRAS["bootstrap"] = bootstrap
EXTRAS["boot"] = bootstrap
EXTRAS["pytools"] = bootstrap

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

# Full stack
fullstack = [
    "fastapi",
    "uvicorn[standard]",
    "Django",
    "Flask",
    "sqlalchemy",
    "psycopg2-binary",
    "pymysql",
    "pymongo",
]
EXTRAS["fullstack"] = fullstack

# Curated all (deduplicated)
_all: List[str] = []
for value in EXTRAS.values():
    _all.extend(value)
EXTRAS["all"] = sorted(set(_all), key=str.lower)
