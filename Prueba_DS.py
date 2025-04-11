import os
import datetime
from jinja2 import Environment, FileSystemLoader

def generar_informe():
    # Configuración
    autor = "Tu Nombre"
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Datos automáticos (puedes modificarlos para que vengan de una base de datos o archivo)
    datos = [
        {"nombre": "Temperatura", "valor": 23.5, "unidad": "°C"},
        {"nombre": "Presión", "valor": 1013, "unidad": "hPa"},
        {"nombre": "Humedad", "valor": 45, "unidad": "%"}
    ]
    
    # Manejo de imágenes (asume que están en una carpeta 'imagenes')
    imagenes = []
    img_folder = "imagenes"
    if os.path.exists(img_folder):
        for i, img_file in enumerate(os.listdir(img_folder)):
            if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                imagenes.append({
                    "ruta": os.path.join(img_folder, img_file),
                    "descripcion": f"Imagen {i+1} del experimento",
                    "etiqueta": f"imagen{i+1}"
                })
    
    # Secciones para completar manualmente
    print("Por favor, complete las siguientes secciones:")
    observaciones = input("Observaciones:\n")
    analisis = input("Análisis:\n")
    conclusiones = input("Conclusiones:\n")
    
    # Renderizar plantilla
    env = Environment(
        loader=FileSystemLoader('.'),
        block_start_string='\BLOCK{',
        block_end_string='}',
        variable_start_string='\VAR{',
        variable_end_string='}',
        comment_start_string='\#{',
        comment_end_string='}',
        trim_blocks=True,
        autoescape=False
    )
    
    template = env.get_template('plantilla_informe.tex')
    output = template.render(
        autor=autor,
        fecha=fecha,
        datos=datos,
        imagenes=imagenes,
        observaciones=observaciones,
        analisis=analisis,
        conclusiones=conclusiones
    )
    
    # Guardar archivo LaTeX
    output_file = f"informe_{fecha}.tex"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"Informe generado en {output_file}")
    print("Compile con pdflatex para generar el PDF.")

if __name__ == "__main__":
    generar_informe()