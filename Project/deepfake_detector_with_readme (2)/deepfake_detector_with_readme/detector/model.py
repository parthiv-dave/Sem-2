import matplotlib
matplotlib.use('Agg')  # <- Force non-GUI backend
import matplotlib.pyplot as plt
import numpy as np
import random
import os

def load_model():
    model = "dummy_model_loaded"
    return model

def predict_deepfake(file_path, model):
    prediction = random.choice(["Fake", "Real"])
    confidence = round(random.uniform(70, 99), 2)
    heatmap_path = generate_dummy_heatmap(file_path)
    return prediction, confidence, heatmap_path

def generate_dummy_heatmap(file_path):
    data = np.random.rand(10, 10)
    plt.imshow(data, cmap='hot', interpolation='nearest')
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    heatmap_name = f"heatmap_{name}.png"
    heatmap_full_path = os.path.join('media/', heatmap_name)
    plt.axis('off')
    plt.savefig(heatmap_full_path, bbox_inches='tight', pad_inches=0)
    plt.close()
    return heatmap_full_path
