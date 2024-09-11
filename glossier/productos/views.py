from django.shortcuts import render


def index(request):
    return render(request,'templateApp/index.html')

def productos(request,categoria):
    listado = {
        'balsamo': [
            {'nombre': "labial"},
            {'descripcion': "balsamo labial"},
        ],
        'serum': [
            {'nombre': "serum facial"},
            {'descripcion': "serum hidratante"},
        ],
        'mascara': [
            {'nombre': "mascara de ojos"},
            {'descripcion': "mascara volumen"},
        ]}
    
    productos = listado.get(categoria, [])
    return render(request,'templateApp/productos.html', productos)