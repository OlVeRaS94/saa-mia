import pdfplumber
import re
import time

# Leer el PDF y extraer el texto
def leer_pdf(pdf_path):
    texto = ""
    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text()
    return texto

# Extraer preguntas numeradas del texto
def extraer_preguntas(texto):
    preguntas = re.findall(r'(\d+\. [^\n]+)', texto)
    return preguntas

# Generar el examen interactivo
def generar_examen(preguntas):
    respuestas_correctas = {
        1: "París",  # Pregunta 1: Respuesta correcta
        2: "Un ciclo es una estructura de control que repite un bloque de código",  # Pregunta 2: Respuesta correcta
        3: "print('Hola Mundo')"  # Pregunta 3: Respuesta correcta
    }

    puntos = 0
    for i, pregunta in enumerate(preguntas, 1):
        print(f"Pregunta {i}: {pregunta}")
        respuesta_usuario = input("Tu respuesta: ")
        
        # Compara la respuesta con la respuesta correcta
        if respuestas_correctas.get(i, "").lower() == respuesta_usuario.lower():
            print("¡Correcto!")
            puntos += 1
        else:
            print("Incorrecto.")
        
        # Tiempo de espera entre preguntas
        time.sleep(1)
    
    # Resultado final
    print(f"\nExamen terminado. Has obtenido {puntos} de {len(preguntas)} puntos.")
    if puntos == len(preguntas):
        print("¡Excelente, todo correcto!")
    elif puntos >= len(preguntas) // 2:
        print("¡Buen trabajo!")
    else:
        print("Necesitas practicar más.")

# Ruta al archivo PDF
pdf_path = "examen.pdf"

# Extraer el texto del PDF
texto_examen = leer_pdf(pdf_path)

# Extraer las preguntas del texto
preguntas = extraer_preguntas(texto_examen)

# Ejecutar el examen
generar_examen(preguntas)
