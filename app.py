from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuration de la base de données MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'emploitepms'

mysql = MySQL(app)


# @app.route('/delete/<int:event_id>', methods=['POST'])
# def delete_event(event_id):
#     cur = mysql.connection.cursor()
#     try:
#         # Supprimer l'événement avec l'ID donné de la base de données
#         cur.execute("DELETE FROM emplois_du_temps WHERE id = %s", (event_id,))
#         mysql.connection.commit()
#         return redirect(url_for('index'))
#     except Exception as e:
#         return f"Une erreur s'est produite : {str(e)}"

# # Autres routes et fonctions de votre application Flask...


@app.route('/delete/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    try:
        # Supprimer l'événement avec l'ID donné de la base de données
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM emplois_du_temps WHERE id = %s", (event_id,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"




@app.route('/index')
def index():
    # Récupérer les événements depuis la base de données
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM emplois_du_temps")
    emplois_du_temps = cur.fetchall()
    cur.close()

    return render_template('index.html', emplois_du_temps=emplois_du_temps)



@app.route('/add_event', methods=['POST'])
def add_event():
    if request.method == 'POST':
        name = request.form['name']
        prof = request.form['prof']
        date = request.form['date']
        timedebut = request.form['timedebut']
        timefin = request.form['timefin']
        salle_classe = request.form['salle_classe']
        UE = request.form['UE']
        day = request.form['day']
        nombre_heures = request.form['nombre_heures']

        # Ajouter l'événement à la base de données
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO emplois_du_temps (name,prof,date,timedebut,timefin,salle_classe,UE,day,nombre_heures) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (name,prof,date,timedebut,timefin,salle_classe,UE,day,nombre_heures))
        mysql.connection.commit()
        cur.close()

        return redirect('/')
    
@app.route('/emploi_du_temps')
def emploi_du_temps():
    # Récupérer les événements depuis la base de données
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM emplois_du_temps")
    emplois_du_temps = cur.fetchall()
    cur.close()

    return render_template('emploi_du_temps.html',emplois_du_temps=emplois_du_temps)

@app.route('/edit/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    # Récupérer l'événement à modifier depuis la base de données
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM emplois_du_temps WHERE id = %s", (event_id,))
    emploi_du_temps = cur.fetchone()
    cur.close()

    if request.method == 'POST':
        # Récupérer les nouvelles valeurs du formulaire de modification
        name = request.form['name']
        prof = request.form['prof']
        date = request.form['date']
        timedebut = request.form['timedebut']
        timefin = request.form['timefin']
        salle_classe = request.form['salle_classe']
        UE = request.form['UE']
        day = request.form['day']
        nombre_heures = request.form['nombre_heures']

        # Mettre à jour l'événement dans la base de données
        cur = mysql.connection.cursor()
        cur.execute("UPDATE emplois_du_temps SET name = %s, prof = %s, date = %s, timedebut = %s, timefin = %s, salle_classe = %s, UE = %s, day = %s, nombre_heures = %s WHERE id = %s",
                    (name, prof, date, timedebut, timefin, salle_classe, UE, day, nombre_heures, event_id))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))

    return render_template('edit_event.html', emploi_du_temps=emploi_du_temps)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/validate_login', methods=['POST'])
def validate_login():
    username = request.form.get('username')
    password = request.form.get('password')
    statut = request.form.get('statut')

    # Exemple de validation basique
    if username == 'etudiant' or password == 'password' or statut == 'etudiant':
        # L'utilisateur est un étudiant
        return redirect('/emploi_du_temps')
    elif username == 'professeur' or password == 'profword' or statut == 'professeur':
        # L'utilisateur est un professeur
        return redirect('/index')
    else:
        # Les informations de connexion sont invalides
        return redirect('/login')



if __name__ == '__main__':
    app.run(debug=True)
    
    
