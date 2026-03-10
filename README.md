<h1 align="center">♻️ EcoVision AI - Garbage Classification System</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Django-4.2-green" alt="Django Version">
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-orange" alt="YOLOv8">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

<hr>

<h2>📋 Table of Contents</h2>
<ul>
  <li><a href="#features">Features</a></li>
  <li><a href="#waste-classes">Waste Classes</a></li>
  <li><a href="#tech-stack">Tech Stack</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#api-endpoints">API Endpoints</a></li>
  <li><a href="#project-structure">Project Structure</a></li>
  <li><a href="#model-details">Model Details</a></li>
  <li><a href="#license">License</a></li>
</ul>

<hr>

<h2 id="features">✨ Features</h2>
<ul>
  <li><strong>🤖 AI-Powered Detection</strong> - YOLOv8 model for accurate waste identification</li>
  <li><strong>🎨 Image Annotation</strong> - Automatic bounding box drawing with labels</li>
  <li><strong>📊 Analytics Dashboard</strong> - Real-time statistics and tracking</li>
  <li><strong>📱 Responsive Design</strong> - Works on all devices</li>
  <li><strong>🌙 Dark Mode</strong> - Automatic dark mode support</li>
</ul>

<hr>

<h2 id="waste-classes">🗑️ Waste Classes</h2>
<ul>
  <li><strong>BIODEGRADABLE</strong> 🌱 - Organic waste, food scraps</li>
  <li><strong>CARDBOARD</strong> 📦 - Cardboard boxes, packaging</li>
  <li><strong>GLASS</strong> 🍾 - Bottles, jars</li>
  <li><strong>METAL</strong> ⚙️ - Cans, metal containers</li>
  <li><strong>PAPER</strong> 📰 - Newspapers, office paper</li>
  <li><strong>PLASTIC</strong> 🧴 - Plastic bottles, bags</li>
</ul>

<hr>

<h2 id="tech-stack">🛠️ Tech Stack</h2>
<h3>Backend</h3>
<ul>
  <li>Python 3.9+</li>
  <li>Django 4.2</li>
  <li>Django REST Framework</li>
  <li>SQLite / PostgreSQL</li>
</ul>

<h3>Machine Learning</h3>
<ul>
  <li>YOLOv8 (Ultralytics)</li>
  <li>PyTorch 2.1</li>
  <li>OpenCV</li>
  <li>NumPy</li>
</ul>

<h3>Frontend</h3>
<ul>
  <li>HTML5</li>
  <li>CSS3</li>
  <li>JavaScript</li>
  <li>Font Awesome Icons</li>
</ul>

<hr>

<h2 id="installation">📦 Installation</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3.9+</li>
  <li>pip</li>
  <li>Git</li>
</ul>

<h3>Step-by-Step</h3>

<pre><code># 1. Clone repository
git clone https://github.com/YOUR_USERNAME/trash-detection-ai.git
cd trash-detection-ai

# 2. Create virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
echo SECRET_KEY=your-secret-key > .env
echo DEBUG=True >> .env

# 5. Run migrations
python manage.py makemigrations accounts
python manage.py makemigrations detection
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Run server
python manage.py runserver
</code></pre>

<p>Access the app at: <strong>http://localhost:8000</strong></p>

<hr>

<h2 id="usage">🎯 Usage</h2>
<ol>
  <li><strong>Upload Image</strong> - Click or drag & drop (JPG, PNG, max 5MB)</li>
  <li><strong>Choose Analysis</strong>
    <ul>
      <li><em>Analyze Image</em> - Get text results with confidence scores</li>
      <li><em>Analyze with Annotation</em> - Get image with bounding boxes</li>
    </ul>
  </li>
  <li><strong>View Results</strong> - See detected items with confidence percentages</li>
  <li><strong>Track Statistics</strong> - Monitor detection history and performance</li>
</ol>

<hr>

<h2 id="api-endpoints">🔌 API Endpoints</h2>

<table border="1" cellpadding="10" cellspacing="0">
  <tr>
    <th>Method</th>
    <th>Endpoint</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/detection/detections/</td>
    <td>List all detections</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/detection/detections/recent/?limit=5</td>
    <td>Get recent detections</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/detection/detections/stats/</td>
    <td>Get system statistics</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/detection/detections/status/</td>
    <td>Check model status</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>/api/detection/detections/detect/</td>
    <td>Analyze image</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>/api/detection/detections/detect_with_annotation/</td>
    <td>Analyze with annotation</td>
  </tr>
</table>

<h3>Example API Call</h3>
<pre><code>import requests

url = "http://localhost:8000/api/detection/detections/detect/"
files = {'image': open('test.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())</code></pre>

<hr>

<h2 id="project-structure">📁 Project Structure</h2>

<pre><code>trash-detection-ai/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── apps/
│       ├── accounts/
│       │   ├── models.py
│       │   ├── views.py
│       │   └── urls.py
│       └── detection/
│           ├── models.py
│           ├── views.py
│           ├── services.py
│           └── urls.py
├── ml_models/
│   └── final_model_25epochs.pt
├── media/
│   └── detections/
├── templates/
│   └── index.html
└── static/</code></pre>

<hr>

<h2 id="model-details">🧠 Model Details</h2>

<ul>
  <li><strong>Architecture:</strong> YOLOv8</li>
  <li><strong>Framework:</strong> Ultralytics</li>
  <li><strong>Training Epochs:</strong> 25</li>
  <li><strong>Input Size:</strong> 640x640</li>
  <li><strong>Classes:</strong> 6 waste types</li>
  <li><strong>File Size:</strong> 49.62 MB</li>
  <li><strong>Location:</strong> <code>ml_models/final_model_25epochs.pt</code></li>
</ul>

<h3>Performance</h3>
<ul>
  <li>mAP@0.5: ~95%</li>
  <li>Precision: ~93%</li>
  <li>Recall: ~91%</li>
  <li>Inference Time: ~30ms per image</li>
</ul>

<hr>

<h2 id="license">📄 License</h2>
<p>This project is licensed under the <strong>MIT License</strong>.</p>

<pre><code>MIT License

Copyright (c) 2024 Yaseen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...</code></pre>

<hr>

<h2>👨‍💻 Author</h2>
<p><strong>Yaseen</strong></p>
<ul>
  <li>GitHub: <a href="https://github.com/yourusername">
Engr-Yasin-ai-04</a></li>
  <li>Email: engr.yasin.ai@gmail.com</li>
</ul>

<hr>

<h2>🙏 Acknowledgments</h2>
<ul>
  <li>Roboflow for the dataset</li>
  <li>Ultralytics for YOLOv8</li>
  <li>Django Community</li>
  <li>PyTorch Team</li>
</ul>

<hr>

<p align="center">Made with ❤️ for a cleaner planet</p>
