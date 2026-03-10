import os
import sys
import torch
import django
from pathlib import Path

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.conf import settings

print("="*60)
print("TRASH DETECTION MODEL DIAGNOSTIC")
print("="*60)

# 1. Check current directory
print(f"\n1. CURRENT DIRECTORY:")
print(f"   {os.getcwd()}")

# 2. Check BASE_DIR
print(f"\n2. DJANGO BASE_DIR:")
print(f"   {settings.BASE_DIR}")

# 3. Check ML_MODELS_PATH
print(f"\n3. ML_MODELS_PATH:")
print(f"   {settings.ML_MODELS_PATH}")
print(f"   Exists: {os.path.exists(settings.ML_MODELS_PATH)}")

# 4. Check all possible model paths
print(f"\n4. CHECKING ALL POSSIBLE MODEL PATHS:")

possible_paths = [
    os.path.join(settings.BASE_DIR, 'ml_models', 'final_model_2Sepochs.pt'),
    os.path.join(settings.BASE_DIR, 'final_model_2Sepochs.pt'),
    'ml_models/final_model_2Sepochs.pt',
    './ml_models/final_model_2Sepochs.pt',
    '../ml_models/final_model_2Sepochs.pt',
    os.path.join(settings.BASE_DIR.parent, 'ml_models', 'final_model_2Sepochs.pt') if hasattr(settings.BASE_DIR, 'parent') else None,
]

for i, path in enumerate(possible_paths):
    if path:
        exists = os.path.exists(path)
        status = "✓ EXISTS" if exists else "✗ NOT FOUND"
        print(f"   Path {i+1}: {path}")
        print(f"   Status: {status}")
        if exists:
            size = os.path.getsize(path) / (1024*1024)  # Size in MB
            print(f"   Size: {size:.2f} MB")

# 5. List all files in ml_models directory
print(f"\n5. FILES IN ml_models DIRECTORY:")
ml_models_dir = settings.ML_MODELS_PATH
if os.path.exists(ml_models_dir):
    files = os.listdir(ml_models_dir)
    if files:
        for file in files:
            file_path = os.path.join(ml_models_dir, file)
            size = os.path.getsize(file_path) / (1024*1024)
            print(f"   - {file} ({size:.2f} MB)")
    else:
        print("   Directory is empty")
else:
    print(f"   Directory does not exist: {ml_models_dir}")

# 6. Try to load with torch directly
print(f"\n6. ATTEMPTING TO LOAD WITH TORCH:")
model_path = os.path.join(settings.ML_MODELS_PATH, 'final_model_2Sepochs.pt')
if os.path.exists(model_path):
    try:
        checkpoint = torch.load(model_path, map_location='cpu')
        print(f"   ✓ Torch loaded successfully!")
        print(f"   Type: {type(checkpoint)}")
        
        if isinstance(checkpoint, dict):
            print(f"   Keys: {list(checkpoint.keys())}")
            
            # Check for common YOLO keys
            yolo_keys = ['model', 'epoch', 'best_fitness', 'results', 'optimizer']
            for key in yolo_keys:
                if key in checkpoint:
                    print(f"   Found YOLO key: {key}")
                    
        elif hasattr(checkpoint, 'named_parameters'):
            print("   This appears to be a model object")
            params = list(checkpoint.named_parameters())
            print(f"   Number of parameters: {len(params)}")
            
    except Exception as e:
        print(f"   ✗ Torch loading failed: {e}")
        import traceback
        traceback.print_exc()
else:
    print("   Model file not found, skipping torch load")

# 7. Try to load with ultralytics YOLO
print(f"\n7. ATTEMPTING TO LOAD WITH ULTRALYTICS YOLO:")
if os.path.exists(model_path):
    try:
        from ultralytics import YOLO
        print(f"   Attempting to load: {model_path}")
        model = YOLO(model_path)
        print(f"   ✓ YOLO loaded successfully!")
        print(f"   Model type: {type(model)}")
        
        # Test with dummy image
        print(f"\n8. TESTING INFERENCE WITH DUMMY IMAGE:")
        import numpy as np
        dummy = np.zeros((640, 640, 3), dtype=np.uint8)
        results = model(dummy, verbose=False)
        print(f"   ✓ Inference successful!")
        print(f"   Results type: {type(results)}")
        print(f"   Number of results: {len(results)}")
        
    except ImportError:
        print("   ✗ ultralytics not installed")
    except Exception as e:
        print(f"   ✗ YOLO loading failed: {e}")
        import traceback
        traceback.print_exc()
else:
    print("   Model file not found, skipping YOLO load")

print("\n" + "="*60)
print("DIAGNOSTIC COMPLETE")
print("="*60)