from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response
from flask import request, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'addressData'
mysql.init_app(app)

@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Cities Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM addresses')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, addresses=result)


@app.route('/view/<int:address_id>', methods=['GET'])
def record_view(address_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM addresses WHERE id=%s', address_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', city=result[0])


@app.route('/edit/<int:address_id>', methods=['GET'])
def form_edit_get(address_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM addresses WHERE id=%s', address_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', address=result[0])


@app.route('/edit/<int:address_id>', methods=['POST'])
def form_update_post(address_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Fname'), request.form.get('Lname'), request.form.get('Address'),
                 request.form.get('City'), request.form.get('State'),
                 request.form.get('Zip_Code'), address_id)
    sql_update_query = """UPDATE addresses t SET t.Fname = %s, t.Lname = %s, t.Address = %s, t.City = 
    %s, t.State = %s, t.Zip_Code = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/address/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Address Form')


@app.route('/address/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Fname'), request.form.get('Lname'), request.form.get('Address'),
                 request.form.get('City'), request.form.get('State'),
                 request.form.get('Zip_Code'))
    sql_insert_query = """INSERT INTO addresses (Fname,Lname,Address,City,State,Zip_Code) VALUES (%s, %s,%s, %s,%s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/delete/<int:address_id>', methods=['POST'])
def form_delete_post(address_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM addresses WHERE id = %s """
    cursor.execute(sql_delete_query, address_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


# @app.route('/api/v1/cities', methods=['GET'])
# def api_browse() -> str:
#     cursor = mysql.get_db().cursor()
#     cursor.execute('SELECT * FROM tblCitiesImport')
#     result = cursor.fetchall()
#     json_result = json.dumps(result);
#     resp = Response(json_result, status=200, mimetype='application/json')
#     return resp


# @app.route('/api/v1/cities/<int:city_id>', methods=['GET'])
# def api_retrieve(city_id) -> str:
#     cursor = mysql.get_db().cursor()
#     cursor.execute('SELECT * FROM tblCitiesImport WHERE id=%s', city_id)
#     result = cursor.fetchall()
#     json_result = json.dumps(result);
#     resp = Response(json_result, status=200, mimetype='application/json')
#     return resp
#
#
# @app.route('/api/v1/cities/<int:city_id>', methods=['PUT'])
# def api_edit(city_id) -> str:
#     cursor = mysql.get_db().cursor()
#     content = request.json
#     inputData = (content['fldName'], content['fldLat'], content['fldLong'],
#                  content['fldCountry'], content['fldAbbreviation'],
#                  content['fldCapitalStatus'], content['fldPopulation'],city_id)
#     sql_update_query = """UPDATE tblCitiesImport t SET t.fldName = %s, t.fldLat = %s, t.fldLong = %s, t.fldCountry =
#         %s, t.fldAbbreviation = %s, t.fldCapitalStatus = %s, t.fldPopulation = %s WHERE t.id = %s """
#     cursor.execute(sql_update_query, inputData)
#     mysql.get_db().commit()
#     resp = Response(status=200, mimetype='application/json')
#     return resp
#
# @app.route('/api/v1/cities', methods=['POST'])
# def api_add() -> str:
#
#     content = request.json
#
#     cursor = mysql.get_db().cursor()
#     inputData = (content['fldName'], content['fldLat'], content['fldLong'],
#                  content['fldCountry'], content['fldAbbreviation'],
#                  content['fldCapitalStatus'], request.form.get('fldPopulation'))
#     sql_insert_query = """INSERT INTO tblCitiesImport (fldName,fldLat,fldLong,fldCountry,fldAbbreviation,fldCapitalStatus,fldPopulation) VALUES (%s, %s,%s, %s,%s, %s,%s) """
#     cursor.execute(sql_insert_query, inputData)
#     mysql.get_db().commit()
#     resp = Response(status=201, mimetype='application/json')
#     return resp
#
# @app.route('/api/v1/cities/<int:city_id>', methods=['DELETE'])
# def api_delete(city_id) -> str:
#     cursor = mysql.get_db().cursor()
#     sql_delete_query = """DELETE FROM tblCitiesImport WHERE id = %s """
#     cursor.execute(sql_delete_query, city_id)
#     mysql.get_db().commit()
#     resp = Response(status=200, mimetype='application/json')
#     return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')