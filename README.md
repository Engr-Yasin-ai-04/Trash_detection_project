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
  <li><a href="#classes">Waste Classes</a></li>
  <li><a href="#tech">Tech Stack</a></li>
  <li><a href="#setup">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#api">API Endpoints</a></li>
  <li><a href="#structure">Project Structure</a></li>
  <li><a href="#model">Model Details</a></li>
  <li><a href="#license">License</a></li>
</ul>

<hr>

<h2 id="features">✨ Features</h2>
<ul>
  <li><strong>🤖 AI Detection</strong> - YOLOv8 for waste identification</li>
  <li><strong>🎨 Annotation</strong> - Bounding boxes with labels</li>
  <li><strong>📊 Dashboard</strong> - Real-time statistics</li>
  <li><strong>📱 Responsive</strong> - Works on all devices</li>
</ul>

<hr>

<h2 id="classes">🗑️ Waste Classes</h2>
<ul>
  <li><strong>BIODEGRADABLE</strong> 🌱 - Organic waste</li>
  <li><strong>CARDBOARD</strong> 📦 - Boxes, packaging</li>
  <li><strong>GLASS</strong> 🍾 - Bottles, jars</li>
  <li><strong>METAL</strong> ⚙️ - Cans, containers</li>
  <li><strong>PAPER</strong> 📰 - Newspapers, office paper</li>
  <li><strong>PLASTIC</strong> 🧴 - Bottles, bags</li>
</ul>

<hr>

<h2 id="tech">🛠️ Tech Stack</h2>
<ul>
  <li><strong>Backend:</strong> Python, Django, Django REST</li>
  <li><strong>ML:</strong> YOLOv8, PyTorch, OpenCV</li>
  <li><strong>Frontend:</strong> HTML, CSS, JavaScript</li>
  <li><strong>Database:</strong> SQLite</li>
</ul>

<hr>

<h2 id="setup">📦 Installation</h2>

<pre><code>git clone https://github.com/Engr-Yasin-ai-04/Trash_detection_project.git
cd Trash_detection_project

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations accounts
python manage.py makemigrations detection
python manage.py migrate

python manage.py runserver
</code></pre>

<p>Access: <strong>http://localhost:8000</strong></p>

<hr>

<h2 id="usage">🎯 Usage</h2>
<ol>
  <li>Upload image (JPG, PNG, max 5MB)</li>
  <li>Click "Analyze Image" for results</li>
  <li>Click "Analyze with Annotation" for bounding boxes</li>
  <li>View detection history in dashboard</li>
</ol>

<hr>

<h2 id="api">🔌 API Endpoints</h2>

<table border="1" cellpadding="8">
  <tr>
    <th>Method</th>
    <th>Endpoint</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/detection/detections/</td>
    <td>All detections</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/detection/detections/recent/</td>
    <td>Recent 5 detections</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/detection/detections/stats/</td>
    <td>System statistics</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>/api/detection/detections/detect/</td>
    <td>Analyze image</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>/api/detection/detections/detect_with_annotation/</td>
    <td>Analyze with boxes</td>
  </tr>
</table>

<hr>

<h2 id="structure">📁 Project Structure</h2>

<pre><code>Trash_detection_project/
├── manage.py
├── requirements.txt
├── core/
│   ├── settings.py
│   └── apps/
│       ├── accounts/
│       └── detection/
├── ml_models/
│   └── final_model_25epochs.pt
├── templates/
│   └── index.html
└── media/</code></pre>

<hr>

<h2 id="model">🧠 Model Details</h2>
<ul>
  <li><strong>Model:</strong> YOLOv8</li>
  <li><strong>Epochs:</strong> 25</li>
  <li><strong>Classes:</strong> 6</li>
  <li><strong>Size:</strong> 49.62 MB</li>
  <li><strong>Path:</strong> <code>ml_models/final_model_25epochs.pt</code></li>
</ul>

<hr>

<h2 id="license">📄 License</h2>
<p>MIT License © 2024</p>

<hr>

<h2>👨‍💻 Author</h2>
<p><strong>Yaseen</strong><br>
GitHub: <a href="https://github.com/Engr-Yasin-ai-04">@Engr-Yasin-ai-04</a><br>
Email: engr.yasin.ai@gmail.com</p>

<hr>

<p align="center">Made with ❤️</p>
