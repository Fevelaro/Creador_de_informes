import os
import datetime
from jinja2 import Environment, FileSystemLoader

def generar_informe():
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")

    # Datos automáticos (puedes modificarlos para que vengan de una base de datos o archivo)
    ID_Local = "Nombre de Local, N° Local xxx"
    ABSTRACT = "Pequeño resumen"
    ANTECEDENTES = "Se puede agregar algo mas detallado_esto es version demo"

    Numero_de_UPS=3

    VLL=[380, 381, 382]
    VyC_ALIM=[222,225,229,1.5,2.5,3.6]
    PromVLL=round(sum(VLL[0:3])/3)
    Vneutro_tierra=0.5


    VdeUPS=[222,225,229,222,225,229,220.1,220.2,220.1,]

    Vsin_respaldo=[220,221,229,1.5,2.2,3.5]
    Psin_respaldo=[Vsin_respaldo[0]*Vsin_respaldo[3], Vsin_respaldo[1]*Vsin_respaldo[4], Vsin_respaldo[2]*Vsin_respaldo[5]]

    Varianza=abs(380-PromVLL)
    if 380 > PromVLL:
        ALTOoBajo="más bajo"
    elif 380 < PromVLL:
        ALTOoBajo="más alto"
    else:
        ALTOoBajo="igual"
    
    Capacidad_corriente_FaseR=(VyC_ALIM[3]*100)/22.7
    Capacidad_corriente_FaseS=(VyC_ALIM[4]*100)/22.7
    Capacidad_corriente_FaseT=(VyC_ALIM[5]*100)/22.7

    

    # Secciones para completar manualmente
    print("Por favor, complete las siguientes secciones:")
    #observaciones = input("Observaciones:\n")
    #analisis = input("Análisis:\n")
    #conclusiones = input("Conclusiones:\n")
    
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
    
    template = env.get_template('plantilla_Latex_informe.tex')
    output = template.render(
        ID_Local=ID_Local,
        ABSTRACT=ABSTRACT,
        ANTECEDENTES=ANTECEDENTES,
        VLL=VLL,
        VyC_ALIM=VyC_ALIM,
        PromVLL=PromVLL,
        Varianza=Varianza,
        ALTOoBAJO=ALTOoBajo
    )
    
    # Guardar archivo LaTeX
    output_file = f"informe_{fecha}.tex"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"Informe generado en {output_file}")
    print("Compile con pdflatex para generar el PDF.")

if __name__ == "__main__":
    generar_informe()