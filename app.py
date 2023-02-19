from flask import Flask, render_template
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request,redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


client = MongoClient('mongodb://localhost:27017/')
db = client['Proiect_preFinal']  # replace with your database name
collection = db['Angajat']  # replace with your collection name

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = []
    for emp in collection.find():
        employees.append({
            'Departament': emp['Departament'],
            'Nume': emp['Nume'],
            'Functie': emp['Functie'],
            'Data_Angajarii': emp['Data_Angajarii'],
            'Salariu': emp['Salariu']
        })
    return render_template('employees.html', employees=employees)

@app.route('/employees/average-salary', methods=['GET'])
def get_average_salary():
    avg_salary = collection.aggregate([{"$group": {"_id": "", "average_salary": {"$avg": "$Salariu"}}}])
    return jsonify({'Salariul mediu al angajatilor este:': list(avg_salary)[0]['average_salary']})



if __name__ == '__main__':
    app.run(debug=True)
