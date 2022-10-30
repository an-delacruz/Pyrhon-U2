from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class ChoferForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()],render_kw={"placeholder": "Nombre"})
    apellido = StringField('Apellido',render_kw={"placeholder": "Apellido"})
    telefono = StringField('Telefono',render_kw={"placeholder": "Telefono"})
    licencia = StringField('Licencia',validators=[DataRequired()],render_kw={"placeholder": "Licencia"})
    enviar = SubmitField('Enviar')

class TractorForm(FlaskForm):
    numero = StringField('Numero',validators=[DataRequired()],render_kw={"placeholder": "Numero"})
    placas = StringField('Placas',validators=[DataRequired()],render_kw={"placeholder": "Placas"})
    marca = StringField('Marca',validators=[DataRequired()],render_kw={"placeholder": "Marca"})
    modelo = StringField('Modelo',render_kw={"placeholder": "Modelo"})
    enviar = SubmitField('Enviar')

class RemolqueForm(FlaskForm):
    numero = StringField('Numero',validators=[DataRequired()],render_kw={"placeholder": "Numero"})
    placas = StringField('Placas',validators=[DataRequired()],render_kw={"placeholder": "Placas"})
    tipo = StringField('Tipo',validators=[DataRequired()],render_kw={"placeholder": "Tipo"})
    enviar = SubmitField('Enviar')