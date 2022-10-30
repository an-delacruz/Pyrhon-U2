from flask import Flask,request,url_for,render_template,redirect
from database import db
from flask_migrate import Migrate
from forms import ChoferForm, RemolqueForm, TractorForm
from models import Chofer, Remolque, Tractor
import logging

app = Flask(__name__)

logging.basicConfig(filename='error.log',level=logging.DEBUG)


#Configuración de la bD
USER_DB = "postgres"
PASS_DB = "admin"
URL_DB = "localhost"
NAME_DB = "lineaTransportistaBD"
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#Configurar migración
migrate = Migrate()
migrate.init_app(app,db)

#Form
app.config["SECRET_KEY"] = "123"

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    return render_template('index.html')



#Chofer
@app.route("/choferes")
def choferes():
    try:
        choferes = Chofer.query.all()
        app.logger.info("Se obtuvieron los choferes")
        return render_template("/choferes/choferes.html",choferes=choferes)
    except Exception as e:
        app.logger.error(e)
        return render_template("error.html")

@app.route("/choferes/agregar",methods=['GET','POST'])
def agregarChofer():
    try:
        chofer = Chofer()
        choferForm = ChoferForm(obj=chofer)
        if request.method == 'POST':
            if choferForm.validate_on_submit():
                choferForm.populate_obj(chofer)
                db.session.add(chofer)
                db.session.commit()
                logging.info("Se agregó un chofer")
                return redirect(url_for('choferes'))
        return render_template('/choferes/agregarChofer.html',forma=choferForm)
    except Exception as e:
        logging.error(e)
        return render_template("error.html")        

@app.route("/choferes/editar/<int:id>",methods=['GET','POST'])
def editarChofer(id):
    try:
        chofer = Chofer.query.get_or_404(id)
    
        choferForm = ChoferForm(obj=chofer)
        if request.method == 'POST':
            if choferForm.validate_on_submit():
                choferForm.populate_obj(chofer)
                #update
                db.session.commit()
                logging.info("Se editó un chofer")
                return redirect(url_for('choferes'))
        return render_template('/choferes/editarChofer.html',forma=choferForm)

    except Exception as e:
        logging.error(e)
        return render_template("error.html")

@app.route("/choferes/eliminar/<int:id>")
def eliminarChofer(id):
    try:
        chofer = Chofer.query.get_or_404(id)
        db.session.delete(chofer)
        db.session.commit()
        return redirect(url_for('choferes'))
    except Exception as e:
        logging.error(e)
        return render_template("error.html")




#Tractor
@app.route("/tractores")
def tractores():
    try:
        tractores=Tractor.query.all()
        logging.info("Se obtuvieron los tractores")
        return render_template('/tractores/tractores.html',tractores=tractores)
    except Exception as e:
        logging.error(e)
        return render_template("error.html")

@app.route("/tractores/agregar",methods=['GET','POST'])
def agregarTractor():
    try:
        tractor = Tractor()
        tractorForm = TractorForm(obj=tractor)
        if request.method == 'POST':
            if tractorForm.validate_on_submit():
                tractorForm.populate_obj(tractor)
                db.session.add(tractor)
                db.session.commit()
                logging.info("Se agregó un tractor")
                return redirect(url_for('tractores'))
        return render_template('/tractores/agregarTractor.html',forma=tractorForm)
    except Exception as e:
        logging.error(e)
        return render_template("error.html")

@app.route("/tractores/editar/<int:id>",methods=['GET','POST'])
def editarTractor(id):
    try:
        tractor = Tractor.query.get_or_404(id)
        tractorForm = TractorForm(obj=tractor)
        if request.method == 'POST':
            if tractorForm.validate_on_submit():
                tractorForm.populate_obj(tractor)
                #update
                db.session.commit()
                logging.info("Se editó un tractor")
                return redirect(url_for('tractores'))
        return render_template('/tractores/editarTractor.html',forma=tractorForm)
    except Exception as e:
        logging.error(e)
        return render_template("error.html")
    
@app.route("/tractores/eliminar/<int:id>")
def eliminarTractor(id):
    try:
        tractor = Tractor.query.get_or_404(id)
        db.session.delete(tractor)
        db.session.commit()
        logging.info("Se eliminó un tractor")
        return redirect(url_for('tractores'))
    except Exception as e:
        logging.error(e)
        return render_template("error.html")




#Remolque
@app.route("/remolques")
def remolques():
    try:
        remolques = Remolque.query.all()
        logging.info("Se obtuvieron los remolques")
        return render_template('/remolques/remolques.html',remolques=remolques)
    except Exception as e:
        logging.error(e)
        return render_template("error.html")
    
@app.route("/remolques/agregar",methods=['GET','POST'])
def agregarRemolque():
    try:
        remolque = Remolque()
        remolqueForm = RemolqueForm(obj=remolque)
        if request.method == 'POST':
            if remolqueForm.validate_on_submit():
                remolqueForm.populate_obj(remolque)
                db.session.add(remolque)
                db.session.commit()
                logging.info("Se agregó un remolque")
                return redirect(url_for('remolques'))
        return render_template('/remolques/agregarRemolque.html',forma=remolqueForm)
    except Exception as e:
        logging.error(e)
        return render_template("error.html")
    
@app.route("/remolques/editar/<int:id>",methods=['GET','POST'])
def editarRemolque(id):
    try:
        remolque = Remolque.query.get_or_404(id)
        remolqueForm = RemolqueForm(obj=remolque)
        if request.method == 'POST':
            if remolqueForm.validate_on_submit():
                remolqueForm.populate_obj(remolque)
                #update
                db.session.commit()
                logging.info("Se editó un remolque")
                return redirect(url_for('remolques'))
        return render_template('/remolques/editarRemolque.html',forma=remolqueForm)
    except Exception as e:
        logging.error(e)
        return render_template("error.html")
    
@app.route("/remolques/eliminar/<int:id>")
def eliminarRemolque(id):
    try:
        remolque = Remolque.query.get_or_404(id)
        db.session.delete(remolque)
        db.session.commit()
        logging.info("Se eliminó un remolque")
        return redirect(url_for('remolques'))
    except Exception as e:
        logging.error(e)
        return render_template("error.html")
   
@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('404.html',error=error),404
