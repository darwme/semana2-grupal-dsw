from flask import Blueprint, request, jsonify
from model.predio import Predio
from utils.db import db

predio= Blueprint('Predio',__name__)

@predio.route('/predio/v1', methods=['GET'])
def getMensaje():
    result={}
    result["data"]='flask-crud-backend'
    return jsonify(result)


@predio.route('/predio/v1/listar', methods=['GET'])
def getPredios():
    result={}
    predios=Predio.query.all()
    result["data"]=predios
    result["stauts_code"]=200
    result["msg"]="Se recupero los predios sin incovenientes"
    return jsonify(result),200

@predio.route('/predio/v1', methods=['POST'])
def addPredio():
    result={}
    body=request.get_json()
    
    id_tipo_predio=body.get('id_tipo_predio')
    descripcion=body.get('descripcion')
    ruc=body.get('ruc')
    telefono=body.get('telefono')
    correo=body.get('correo')
    direccion=body.get('direccion')
    idubigeo=body.get('idubigeo')
    
    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        result["status_code"]=400
        result["msg"]="Faltan datos..."
        return jsonify(result), 400
    
    predio = Predio(id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo)
    db.session.add(predio)
    db.session.commit()
    result["data"]=predio
    result["status_code"]=201
    result["msg"]="Se agregó correctamente"
    return jsonify(result)
        
    
@predio.route('/predio/v1/<int:id>', methods=['PUT'])
def updateOne(id):
    result={}
    body=request.get_json()
    id_tipo_predio=body.get('id_tipo_predio')
    descripcion=body.get('descripcion')
    ruc=body.get('ruc')
    telefono=body.get('telefono')
    correo=body.get('correo')
    direccion=body.get('direccion')
    idubigeo=body.get('idubigeo')
    
    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        result["status_code"]=400
        result["msg"]="Faltan datos..."
        return jsonify(result), 400
    
    predio = Predio.query.get(id)
    if not predio:
        result["status_code"] = 404
        result["msg"] = "Predio no encontrado"
        return jsonify(result), 404
    
    predio.id_tipo_predio=id_tipo_predio
    predio.descripcion=descripcion
    predio.ruc=ruc
    predio.telefono=telefono
    predio.correo=correo
    predio.direccion=direccion
    predio.idubigeo=idubigeo
    
    db.session.commit()
    
    result["data"] = predio
    result["status_code"] = 200
    result["msg"] = "Predio actualizado correctamente"
    return jsonify(result), 200
    
    
@predio.route('/predio/v1/<int:id>', methods=['DELETE'])
def deleteOne(id):
    result = {}
    
    predio = Predio.query.get(id)
    if not id:
        result["status_code"] = 400
        result["msg"] = "Debe consignar un id valido"
        return jsonify(result), 400
    
    if not predio:
        result["status_code"] = 404
        result["msg"] = "Predio no encontrado"
        return jsonify(result), 404
    
    db.session.delete(predio)
    db.session.commit()
    
    result["data"]=predio
    result["status_code"] = 202
    result["msg"] = "Predio eliminado correctamente"
    return jsonify(result), 202
    
        