from flask import Flask, render_template, request, redirect, url_for
from config import EstablecerConexion


app = Flask(__name__)


con_db = EstablecerConexion()

# Esta ruta muestra cada una de las personas que se encuetran en la base de datos


@app.route('/')
def index():
    cursor = con_db.cursor()
    sql = """SELECT*FROM personas"""
    cursor.execute(sql)
    personasRegistradas = cursor.fetchall()
    print(personasRegistradas)

    return render_template('index.html', personasRegistradas=personasRegistradas)


# Guardar cada uno de los registros
@app.route('/guardar_personas', methods=['POST'])
def guardar_personas():
    cursor = con_db.cursor()  # coneccion de la abse de datos
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']

    if nombre and apellido and telefono:
        sql = """
        INSERT INTO personas (nombre,apellido,telefono)
        VALUES (%s,%s,%s)
        """
        # % (nombre, apellido, telefono)
        cursor.execute(sql, (nombre, apellido, telefono))
        con_db.commit()  # guradamos los cambios

        return redirect(url_for('index'))
        print('')
    else:
        print('error')


# Editar informacion de las personas
@app.route('/editar_persona/<int:ID>')
def vistaEditar(ID):
    cursor = con_db.cursor()

    sql = f'''
    SELECT * FROM personas WHERE id={ID}
    '''
    cursor.execute(sql)
    informacion_persona = cursor.fetchone()

    return render_template('editInformation.html', informacion_persona=informacion_persona)


@app.route('/editar_persona/<int:ID>', methods=['POST'])
def editar_informacion(ID):
    cursor = con_db.cursor()
    nombre = request.form['edit-nombre']
    apellido = request.form['edit-apellido']
    telefono = request.form['edit-telefono']
    sql = 'UPDATE personas SET nombre=%s, apellido=%s, telefono=%s WHERE id=%s'
    cursor.execute(sql, (nombre, apellido, telefono, int(ID)))
    con_db.commit()

    return redirect(url_for('index'))


@app.route('/EliminarRegistro/<int:ID>')
def eliminar_registro(ID):
    cursor = con_db.cursor()
    sql = f' DELETE FROM personas WHERE id={ID}'
    cursor.execute(sql)
    con_db.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
