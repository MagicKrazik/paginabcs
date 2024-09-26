from django.shortcuts import render
import os
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def audiencias(request):
    return render(request, 'audiencias.html')

def get_kml_files():
    kml_dir = os.path.join(settings.STATICFILES_DIRS[0], 'kml')
    kml_files = [f for f in os.listdir(kml_dir) if f.endswith('.kml')]
    
    # Add labels and sort alphabetically
    kml_data = [
        {
            'filename': f,
            'label': f.replace('.kml', '').replace('_', ' ').title(),
        } for f in kml_files
    ]
    
    # Sort the list based on the 'label' key
    kml_data.sort(key=lambda x: x['label'])
    
    return kml_data

def mapa(request):
    kml_files = get_kml_files()
    return render(request, 'mapa.html', {'kml_files': kml_files})

def cartografia_view(request):
    pdf_dir = os.path.join(settings.STATIC_ROOT, 'pdf')
    pdf_files = []
    for filename in os.listdir(pdf_dir):
        if filename.endswith('.pdf'):
            title = os.path.splitext(filename)[0].replace('_', ' ').title()
            pdf_files.append({
                'title': title,
                'filename': filename,
                'url': f'{settings.STATIC_URL}pdf/{filename}'
            })
    
    # Sort the pdf_files list based on the 'title' key
    pdf_files.sort(key=lambda x: x['title'])
    
    return render(request, 'cartografia.html', {'pdf_files': pdf_files})