from flask import Flask, request, render_template, send_file
import pandas as pd
import os

app = Flask(__name__)

# Ruta para almacenar el archivo Excel
EXCEL_FILE = 'datos_formulario.xlsx'

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        ciudad = request.form.get('ciudad')
        opinion_poo = request.form.get('opinion_poo')
        calificacion_poo = request.form.get('calificacion_poo')

        # Crear un DataFrame con los datos
        df = pd.DataFrame({
            'Nombre': [nombre],
            'Email': [email],
            'Ciudad': [ciudad],
            'Opinión sobre POO': [opinion_poo],
            'Calificación': [calificacion_poo]
        })

        # Guardar el DataFrame en un archivo Excel
        if os.path.exists(EXCEL_FILE):
            # Si el archivo ya existe, leerlo y agregar los nuevos datos
            existing_df = pd.read_excel(EXCEL_FILE)
            updated_df = pd.concat([existing_df, df], ignore_index=True)
            updated_df.to_excel(EXCEL_FILE, index=False)
        else:
            # Si no existe, crear el archivo y agregar encabezados
            df.to_excel(EXCEL_FILE, index=False)

        # Redirigir a la página de éxito
        return render_template('exito.html', nombre=nombre)

    return render_template('formulario.html')

@app.route('/descargar')
def descargar():
    return send_file(EXCEL_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
