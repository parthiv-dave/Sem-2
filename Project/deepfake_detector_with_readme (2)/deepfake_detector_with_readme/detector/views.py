from django.shortcuts import render
from django.conf import settings
from .model import load_model, predict_deepfake
import os
from django.core.files.storage import FileSystemStorage

model = load_model()

IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.avif')

def upload_file(request):
    if request.method == 'POST' and request.FILES['media']:
        media = request.FILES['media']
        fs = FileSystemStorage()
        filename = fs.save(media.name, media)
        uploaded_file_url = fs.url(filename)
        
        file_path = os.path.join(settings.MEDIA_ROOT, filename)
        prediction, confidence, heatmap_path = predict_deepfake(file_path, model)

        if filename.lower().endswith((IMAGE_EXTENSIONS)):
            media_type = "image"
        else:
            media_type = "video"

        return render(request, 'result.html', {
            'prediction': prediction,
            'confidence': confidence,
            'media_url': uploaded_file_url,
            'heatmap_url': heatmap_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL),
            'media_type': media_type
        })

    return render(request, 'upload.html')
