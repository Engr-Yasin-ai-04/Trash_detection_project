<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcoVision AI - README</title>
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            line-height: 1.6;
            padding: 40px 20px;
        }

        .readme-container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 30px;
            box-shadow: 0 30px 60px rgba(0,0,0,0.3);
            overflow: hidden;
            animation: slideIn 0.8s ease-out;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Header Section */
        .readme-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 60px 40px;
            text-align: center;
            color: white;
            position: relative;
            overflow: hidden;
        }

        .readme-header::before {
            content: '';
            position: absolute;
            top: -50px;
            right: -50px;
            width: 200px;
            height: 200px;
            background: rgba(255,255,255,0.1);
            border-radius: 50%;
        }

        .readme-header::after {
            content: '';
            position: absolute;
            bottom: -50px;
            left: -50px;
            width: 200px;
            height: 200px;
            background: rgba(255,255,255,0.1);
            border-radius: 50%;
        }

        .header-icon {
            font-size: 80px;
            margin-bottom: 20px;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .readme-header h1 {
            font-size: 3.5rem;
            margin-bottom: 10px;
            font-weight: 800;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        .header-badges {
            margin-top: 30px;
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
        }

        .badge {
            padding: 10px 25px;
            border-radius: 50px;
            background: rgba(255,255,255,0.2);
            backdrop-filter: blur(10px);
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            border: 1px solid rgba(255,255,255,0.3);
            transition: transform 0.3s;
        }

        .badge:hover {
            transform: translateY(-3px);
            background: rgba(255,255,255,0.3);
        }

        /* Content Sections */
        .readme-content {
            padding: 50px 40px;
        }

        .section {
            margin-bottom: 50px;
            animation: fadeIn 0.8s ease-out;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .section-title {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 3px solid #f0f0f0;
        }

        .section-title i {
            font-size: 2rem;
            color: #667eea;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .section-title h2 {
            font-size: 2rem;
            font-weight: 700;
            color: #333;
        }

        .section-title h2 span {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Feature Grid */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 30px;
        }

        .feature-card {
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            transition: all 0.3s;
            border: 1px solid rgba(102, 126, 234, 0.1);
        }

        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(102, 126, 234, 0.2);
            border-color: #667eea;
        }

        .feature-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            color: white;
            font-size: 2rem;
        }

        .feature-card h3 {
            font-size: 1.3rem;
            margin-bottom: 15px;
            color: #333;
        }

        .feature-card p {
            color: #666;
            font-size: 0.95rem;
        }

        /* Tech Stack */
        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 20px;
        }

        .tech-item {
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            padding: 12px 25px;
            border-radius: 50px;
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 500;
            border: 1px solid rgba(102, 126, 234, 0.2);
            transition: all 0.3s;
        }

        .tech-item:hover {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            transform: scale(1.05);
        }

        .tech-item i {
            font-size: 1.2rem;
        }

        /* Code Blocks */
        .code-block {
            background: #1e1e2f;
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            position: relative;
            overflow-x: auto;
        }

        .code-block pre {
            color: #fff;
            font-family: 'Courier New', monospace;
            font-size: 0.95rem;
            line-height: 1.5;
        }

        .code-block .comment {
            color: #6c757d;
        }

        .code-block .keyword {
            color: #ff79c6;
        }

        .code-block .string {
            color: #50fa7b;
        }

        .copy-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background: rgba(255,255,255,0.1);
            border: none;
            color: white;
            padding: 8px 15px;
            border-radius: 5px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 5px;
            transition: all 0.3s;
        }

        .copy-btn:hover {
            background: rgba(255,255,255,0.2);
        }

        /* Installation Steps */
        .steps {
            counter-reset: step;
            list-style: none;
        }

        .step-item {
            counter-increment: step;
            margin-bottom: 20px;
            padding-left: 60px;
            position: relative;
        }

        .step-item::before {
            content: counter(step);
            position: absolute;
            left: 0;
            top: 0;
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
        }

        /* Class Badges */
        .waste-classes {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin: 30px 0;
        }

        .class-badge {
            padding: 15px 30px;
            border-radius: 50px;
            color: white;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.3s;
            flex: 1 1 auto;
            min-width: 200px;
        }

        .class-badge:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }

        .badge-biodegradable { background: #27ae60; }
        .badge-cardboard { background: #f39c12; }
        .badge-glass { background: #3498db; }
        .badge-metal { background: #7f8c8d; }
        .badge-paper { background: #e67e22; }
        .badge-plastic { background: #e74c3c; }

        /* Project Structure */
        .tree {
            background: #f8f9fa;
            padding: 30px;
            border-radius: 15px;
            font-family: 'Courier New', monospace;
            line-height: 2;
            border: 1px solid #e9ecef;
        }

        .tree i {
            color: #667eea;
            margin-right: 10px;
        }

        .tree .folder {
            color: #e67e22;
            font-weight: 600;
        }

        .tree .file {
            color: #3498db;
        }

        /* Stats Cards */
        .stats-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }

        .stat-card-mini {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
        }

        .stat-number {
            font-size: 2rem;
            font-weight: 700;
            display: block;
        }

        .stat-label {
            font-size: 0.9rem;
            opacity: 0.9;
        }

        /* Footer */
        .readme-footer {
            background: #f8f9fa;
            padding: 40px;
            text-align: center;
            border-top: 1px solid #e9ecef;
        }

        .social-links {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-top: 20px;
        }

        .social-link {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            transition: all 0.3s;
        }

        .social-link:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
        }

        /* Responsive */
        @media (max-width: 768px) {
            .readme-header h1 {
                font-size: 2rem;
            }

            .readme-content {
                padding: 30px 20px;
            }

            .section-title h2 {
                font-size: 1.5rem;
            }

            .feature-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Animation for sections */
        .section {
            opacity: 0;
            animation: fadeInUp 0.8s ease-out forwards;
        }

        .section:nth-child(1) { animation-delay: 0.1s; }
        .section:nth-child(2) { animation-delay: 0.2s; }
        .section:nth-child(3) { animation-delay: 0.3s; }
        .section:nth-child(4) { animation-delay: 0.4s; }
        .section:nth-child(5) { animation-delay: 0.5s; }
        .section:nth-child(6) { animation-delay: 0.6s; }
        .section:nth-child(7) { animation-delay: 0.7s; }
        .section:nth-child(8) { animation-delay: 0.8s; }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <div class="readme-container">
        <!-- Header Section -->
        <div class="readme-header">
            <div class="header-icon">
                <i class="fas fa-recycle"></i>
            </div>
            <h1>EcoVision AI</h1>
            <p style="font-size: 1.2rem; opacity: 0.9; max-width: 600px; margin: 0 auto;">
                Advanced AI-Powered Garbage Classification System using YOLOv8
            </p>
            
            <div class="header-badges">
                <span class="badge"><i class="fab fa-python"></i> Python 3.9+</span>
                <span class="badge"><i class="fab fa-django"></i> Django 4.2</span>
                <span class="badge"><i class="fas fa-brain"></i> YOLOv8</span>
                <span class="badge"><i class="fas fa-database"></i> SQLite</span>
                <span class="badge"><i class="fas fa-robot"></i> PyTorch</span>
            </div>
        </div>

        <!-- Main Content -->
        <div class="readme-content">
            <!-- About Section -->
            <section class="section">
                <div class="section-title">
                    <i class="fas fa-info-circle"></i>
                    <h2>About <span>The Project</span></h2>
                </div>
                <p style="font-size: 1.1rem; margin-bottom: 20px;">
                    <strong>EcoVision AI</strong> is a state-of-the-art waste classification system that leverages 
                    <strong>YOLOv8 (You Only Look Once)</strong> to detect and classify different types of waste materials 
                    in real-time. The system can identify 6 distinct categories of waste with high accuracy.
                </p>
                
                <!-- Stats Cards -->
                <div class="stats-container">
                    <div class="stat-card-mini">
                        <i class="fas fa-database" style="font-size: 2rem; margin-bottom: 10px;"></i>
                        <span class="stat-number">6</span>
                        <span class="stat-label">Waste Classes</span>
                    </div>
                    <div class="stat-card-mini">
                        <i class="fas fa-chart-line" style="font-size: 2rem; margin-bottom: 10px;"></i>
                        <span class="stat-number">98%</span>
                        <span class="stat-label">Accuracy</span>
                    </div>
                    <div class="stat-card-mini">
                        <i class="fas fa-bolt" style="font-size: 2rem; margin-bottom: 10px;"></i>
                        <span class="stat-number">Real-time</span>
                        <span class="stat-label">Detection</span>
                    </div>
                    <div class="stat-card-mini">
                        <i class="fas fa-cloud" style="font-size: 2rem; margin-bottom: 10px;"></i>
                        <span class="stat-number">5MB</span>
                        <span class="stat-label">Max File Size</span>
                    </div>
                </div>
            </section>

            <!-- Features Section -->
            <section class="section">
                <div class="section-title">
                    <i class="fas fa-star"></i>
                    <h2>Key <span>Features</span></h2>
                </div>
                
                <div class="feature-grid">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-robot"></i>
                        </div>
                        <h3>AI-Powered Detection</h3>
                        <p>Advanced YOLOv8 model for accurate waste identification with confidence scores</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-paint-brush"></i>
                        </div>
                        <h3>Image Annotation</h3>
                        <p>Automatic bounding box drawing with labels and confidence percentages</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-chart-bar"></i>
                        </div>
                        <h3>Analytics Dashboard</h3>
                        <p>Real-time statistics, recent detections, and waste type distribution</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-history"></i>
                        </div>
                        <h3>Detection History</h3>
                        <p>Save and review all previous detections with timestamps</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-mobile-alt"></i>
                        </div>
                        <h3>Responsive Design</h3>
                        <p>Works seamlessly on desktop, tablet, and mobile devices</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-moon"></i>
                        </div>
                        <h3>Dark Mode</h3>
                        <p>Automatic dark mode support for better user experience</p>
                    </div>
                </div>
            </section>

            <!-- Waste Classes Section -->
            <section class="section">
                <div class="section-title">
                    <i class="fas fa-tags"></i>
                    <h2>Waste <span>Classification Classes</span></h2>
                </div>
                
                <div class="waste-classes">
                    <div class="class-badge badge-biodegradable">
                        <i class="fas fa-leaf"></i>
                        BIODEGRADABLE
                    </div>
                    <div class="class-badge badge-cardboard">
                        <i class="fas fa-box"></i>
                        CARDBOARD
                    </div>
                    <div class="class-badge badge-glass">
                        <i class="fas fa-wine-bottle"></i>
                        GLASS
                    </div>
                    <div class="class-badge badge-metal">
                        <i class="fas fa-cog"></i>
                        METAL
                    </div>
                    <div class="class-badge badge-paper">
                        <i class="fas fa-newspaper"></i>
                        PAPER
                    </div>
                    <div class="class-badge badge-plastic">
                        <i class="fas fa-tint"></i>
                        PLASTIC
                    </div>
                </div>
                
                <p style="margin-top: 20px; color: #666;">
                    <i class="fas fa-database" style="color: #667eea;"></i> 
                    Dataset Source: Roboflow - Garbage Classification Dataset (Version 2)
                </p>
            </section>

            <!-- Tech Stack Section -->
            <section class="section">
                <div class="section-title">
                    <i class="fas fa-cogs"></i>
                    <h2>Technology <span>Stack</span></h2>
                </div>
                
                <div class="tech-stack">
                    <span class="tech-item"><i class="fab fa-python"></i> Python 3.9+</span>
                    <span class="tech-item"><i class="fab fa-django"></i> Django 4.2</span>
                    <span class="tech-item"><i class="fas fa-brain"></i> YOLOv8</span>
                    <span class="tech-item"><i class="fas fa-database"></i> SQLite</span>
                    <span class="tech-item"><i class="fas fa-fire"></i> PyTorch 2.1</span>
                    <span class="tech-item"><i class="fas fa-chart-line"></i> NumPy</span>
                    <span class="tech-item"><i class="fas fa-image"></i> Pillow</span>
                    <span class="tech-item"><i class="fas fa-camera"></i> OpenCV</span>
                    <span class="tech-item"><i class="fas fa-code"></i> Django REST</span>
                    <span class="tech-item"><i class="fas fa-exchange-alt"></i> CORS Headers</span>
                    <span class="tech-item"><i class="fas fa-lock"></i> JWT Auth</span>
                    <span class="tech-item"><i class="fas fa-paint-brush"></i> Font Awesome</span>
                </div>
            </section>

            <!-- Installation Section -->
            <section class="section">
                <div class="section-title">
                    <i class="fas fa-download"></i>
                    <h2>Installation <span>Guide</span></h2>
                </div>
                
                <div class="steps">
                    <div class="step-item">
                        <strong>Clone the repository</strong>
                        <div class="code-block">
                            <button class="copy-btn" onclick="copyCode(this)">
                                <i class="far fa-copy"></i> Copy
                            </button>
                            <pre>git clone https://github.com/YOUR_USERNAME/trash-detection-ai.git
cd trash-detection-ai</pre>
                        </div>
                    </div>
                    
                    <div class="step-item">
                        <strong>Create virtual environment</strong>
                        <div class="code-block">
                            <button class="copy-btn" onclick="copyCode(this)">
                                <i class="far fa-copy"></i> Copy
                            </button>
                            <pre><span class="comment"># Windows</span>
python -m venv venv
venv\Scripts\activate

<span class="comment"># Linux/Mac</span>
<span class="comment"># python3 -m venv venv</span>
<span class="comment"># source venv/bin/activate</span></pre>
                        </div>
                    </div>
                    
                    <div class="step-item">
                        <strong>Install dependencies</strong>
                        <div class="code-block">
                            <button class="copy-btn" onclick="copyCode(this)">
                                <i class="far fa-copy"></i> Copy
                            </button>
                            <pre>pip install -r requirements.txt</pre>
                        </div>
                    </div>
                    
                    <div class="step-item">
                        <strong>Environment setup</strong>
                        <div class="code-block">
                            <button class="copy-btn" onclick="copyCode(this)">
                                <i class="far fa-copy"></i> Copy
                            </button>
                            <pre><span class="comment"># Copy .env.example to .env</span>
copy .env.example .env

<span class="comment"># Edit .env file with your settings</span>
<span class="comment"># SECRET_KEY=your-secret-key</span>
<span class="comment"># DEBUG=True</span></pre>
                        </div>
                    </div>
                    
                    <div class="step-item">
                        <strong>Run migrations</strong>
                        <div class="code-block">
                            <button class="copy-btn" onclick="copyCode(this)">
                                <i class="far fa-copy"></i> Copy
                            </button>
                            <pre>python manage.py makemigrations accounts
python manage.py makemigrations detection
python manage.py migrate</pre>
                        </div>
                    </div>
                    
                    <div class="step-item">
                        <strong>Create superuser (optional)</strong>
                        <div class="code-block">
                            <button class="copy-btn" onclick="copyCode(this)">
                                <i class="far fa-copy"></i> Copy
                            </button>
                            <pre>python manage.py createsuperuser</pre>
                        </div>
                    </div>
                    
                    <div class="step-item">
                        <strong>Run development server</strong>
                        <div class="code-block">
                            <button class="copy-btn" onclick="copyCode(this)">
                                <i class="far fa-copy"></i> Copy
                            </button>
                            <pre>python manage.py runserver</pre>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Project Structure -->
            <section class="section">
                <div class="section-title">
                    <i class="fas fa-folder-tree"></i>
                    <h2>Project <span>Structure</span></h2>
                </div>
                
                <div class="tree">
                    <i class="fas fa-folder folder"></i> <span class="folder">trash_detection_project/</span><br>
                    &nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> manage.py<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> requirements.txt<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> .env<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> .gitignore<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-folder folder"></i> core/<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> settings.py<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> urls.py<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> wsgi.py<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-folder folder"></i> apps/<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-folder folder"></i> accounts/<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-folder folder"></i> detection/<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> models.py<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> views.py<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> services.py<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> urls.py<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-folder folder"></i> ml_models/<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> final_model_25epochs.pt<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-folder folder"></i> media/<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-folder folder"></i> detections/<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-folder folder"></i> templates/<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-file file"></i> index.html<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-folder folder"></i> static/<br>
                </div>
            </section>

            <!-- API Endpoints -->
            <section class="section">
                <div class="section-title">
                    <i class="fas fa-code-branch"></i>
                    <h2>API <span>Endpoints</span></h2>
                </div>
                
                <div style="background: #f8f9fa; padding: 20px; border-radius: 15px;">
                    <table style="width: 100%; border-collapse: collapse;">
                        <tr style="border-bottom: 2px solid #667eea;">
                            <th style="text-align: left; padding: 10px;">Method</th>
                            <th style="text-align: left; padding: 10px;">Endpoint</th>
                            <th style="text-align: left; padding: 10px;">Description</th>
                        </tr>
                        <tr style="border-bottom: 1px solid #ddd;">
                            <td style="padding: 10px;"><span style="background: #27ae60; color: white; padding: 3px 8px; border-radius: 5px;">GET</span></td>
                            <td style="padding: 10px;"><code>/api/detection/detections/</code></td>
                            <td style="padding: 10px;">List all detections</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #ddd;">
                            <td style="padding: 10px;"><span style="background: #f39c12; color: white; padding: 3px 8px; border-radius: 5px;">POST</span></td>
                            <td style="padding: 10px;"><code>/api/detection/detections/detect/</code></td>
                            <td style="padding: 10px;">Analyze image</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #ddd;">
                            <td style="padding: 10px;"><span style="background: #f39c12; color: white; padding: 3px 8px; border-radius: 5px;">POST</span></td>
                            <td style="padding: 10px;"><code>/api/detection/detections/detect_with_annotation/</code></td>
                            <td style="padding: 10px;">Analyze with bounding boxes</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #ddd;">
                            <td style="padding: 10px;"><span style="background: #27ae60; color: white; padding: 3px 8px; border-radius: 5px;">GET</span></td>
                            <td style="padding: 10px;"><code>/api/detection/detections/recent/</code></td>
                            <td style="padding: 10px;">Get recent detections</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #ddd;">
                            <td style="padding: 10px;"><span style="background: #27ae60; color: white; padding: 3px 8px; border-radius: 5px;">GET</span></td>
                            <td style="padding: 10px;"><code>/api/detection/detections/stats/</code></td>
                            <td style="padding: 10px;">Get system statistics</td>
                        </tr>
                    </table>
                </div>
            </section>

            <!-- Usage Guide -->
            <section class="section">
                <div class="section-title">
                    <i class="fas fa-play-circle"></i>
                    <h2>How to <span>Use</span></h2>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                    <div style="text-align: center;">
                        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; color: white; font-size: 1.5rem; font-weight: 700;">1</div>
                        <h4>Upload Image</h4>
                        <p style="color: #666;">Drag & drop or click to upload an image (JPG, PNG, max 5MB)</p>
                    </div>
                    
                    <div style="text-align: center;">
                        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; color: white; font-size: 1.5rem; font-weight: 700;">2</div>
                        <h4>Choose Analysis Type</h4>
                        <p style="color: #666;">"Analyze Image" for text results or "Analyze with Annotation" for bounding boxes</p>
                    </div>
                    
                    <div style="text-align: center;">
                        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; color: white; font-size: 1.5rem; font-weight: 700;">3</div>
                        <h4>View Results</h4>
                        <p style="color: #666;">See detected items with confidence scores and waste types</p>
                    </div>
                    
                    <div style="text-align: center;">
                        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; color: white; font-size: 1.5rem; font-weight: 700;">4</div>
                        <h4>Track Statistics</h4>
                        <p style="color: #666;">Monitor detection history and system performance</p>
                    </div>
                </div>
            </section>

            <!-- Contributing -->
            <section class="section">
                <div class="section-title">
                    <i class="fas fa-handshake"></i>
                    <h2>Contributing <span>Guidelines</span></h2>
                </div>
                
                <p>We welcome contributions! Here's how you can help:</p>
                
                <ol style="margin-left: 20px; margin-top: 15px;">
                    <li>Fork the repository</li>
                    <li>Create a feature branch (<code>git checkout -b feature/amazing-feature</code>)</li>
                    <li>Commit your changes (<code>git commit -m 'Add amazing feature'</code>)</li>
                    <li>Push to branch (<code>git push origin feature/amazing-feature</code>)</li>
                    <li>Open a Pull Request</li>
                </ol>
            </section>

            <!-- License -->
            <section class="section">
                <div class="section-title">
                    <i class="fas fa-balance-scale"></i>
                    <h2>License</h2>
                </div>
                
                <div style="background: #f8f9fa; padding: 20px; border-radius: 15px;">
                    <p><i class="fas fa-copyright"></i> This project is licensed under the <strong>MIT License</strong> - see the <a href="#" style="color: #667eea; text-decoration: none;">LICENSE</a> file for details.</p>
                </div>
            </section>

            <!-- Author -->
            <section class="section">
                <div class="section-title">
                    <i class="fas fa-user-circle"></i>
                    <h2>Author</h2>
                </div>
                
                <div style="display: flex; align-items: center; gap: 20px; background: linear-gradient(135deg, #f8f9fa, #e9ecef); padding: 30px; border-radius: 20px;">
                    <div style="width: 100px; height: 100px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem;">
                        <i class="fas fa-user"></i>
                    </div>
                    <div>
                        <h3>Yaseen</h3>
                        <p style="color: #666; margin-bottom: 10px;">AI/ML Developer & Django Expert</p>
                        <div style="display: flex; gap: 10px;">
                            <a href="#" style="color: #667eea; font-size: 1.5rem;"><i class="fab fa-github"></i></a>
                            <a href="#" style="color: #0077b5; font-size: 1.5rem;"><i class="fab fa-linkedin"></i></a>
                            <a href="#" style="color: #1da1f2; font-size: 1.5rem;"><i class="fab fa-twitter"></i></a>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Acknowledgments -->
            <section class="section">
                <div class="section-title">
                    <i class="fas fa-heart"></i>
                    <h2>Acknowledgments</h2>
                </div>
                
                <div style="display: flex; flex-wrap: wrap; gap: 15px;">
                    <span class="tech-item"><i class="fas fa-database"></i> Roboflow</span>
                    <span class="tech-item"><i class="fas fa-brain"></i> Ultralytics YOLOv8</span>
                    <span class="tech-item"><i class="fab fa-django"></i> Django Community</span>
                    <span class="tech-item"><i class="fas fa-fire"></i> PyTorch Team</span>
                </div>
            </section>
        </div>

        <!-- Footer -->
        <div class="readme-footer">
            <p style="margin-bottom: 20px;">Made with <i class="fas fa-heart" style="color: #e74c3c;"></i> for a cleaner planet</p>
            <div class="social-links">
                <a href="#" class="social-link"><i class="fab fa-github"></i></a>
                <a href="#" class="social-link"><i class="fab fa-linkedin-in"></i></a>
                <a href="#" class="social-link"><i class="fab fa-twitter"></i></a>
                <a href="#" class="social-link"><i class="fas fa-globe"></i></a>
            </div>
            <p style="margin-top: 30px; color: #999; font-size: 0.9rem;">
                <i class="fas fa-code"></i> with <i class="fas fa-heart" style="color: #e74c3c;"></i> by Engr: Muhammad Yasin Khan
            </p>
        </div>
    </div>

    <script>
        function copyCode(button) {
            const codeBlock = button.parentElement.querySelector('pre');
            const text = codeBlock.innerText;
            
            navigator.clipboard.writeText(text).then(() => {
                button.innerHTML = '<i class="fas fa-check"></i> Copied!';
                setTimeout(() => {
                    button.innerHTML = '<i class="far fa-copy"></i> Copy';
                }, 2000);
            });
        }
    </script>
</body>
</html>
