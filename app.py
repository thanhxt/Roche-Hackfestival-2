from flask import Flask, request, jsonify, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Mock-Datenbanken
employees_m1 = []

employees_m2 = []

employees_m3 = []

employees_main = []

employees_day2= [
    {'id': 1, 'name': 'John Doe', 'food_choice': 'A', 'distance': 230, 'transport_choice': 'car', 'room_id': '15', 'roomnumber': 2, 'roomduration': 1},
    {'id': 2, 'name': 'Long Han', 'food_choice': 'A', 'distance': 730, 'transport_choice': 'train', 'room_id': '30', 'roomnumber': 10, 'roomduration': 2},
    {'id': 3, 'name': 'Alice Wong', 'food_choice': 'B', 'distance': 120, 'transport_choice': 'bike', 'room_id': '15', 'roomnumber': 5, 'roomduration': 1},
    {'id': 4, 'name': 'Bob Lee', 'food_choice': 'C', 'distance': 450, 'transport_choice': 'car', 'room_id': '30', 'roomnumber': 8, 'roomduration': 3},
    {'id': 5, 'name': 'Chris Kim', 'food_choice': 'D', 'distance': 300, 'transport_choice': 'train', 'room_id': '15', 'roomnumber': 2, 'roomduration': 2},
    {'id': 6, 'name': 'Diana Hu', 'food_choice': 'A', 'distance': 510, 'transport_choice': 'car', 'room_id': '30', 'roomnumber': 10, 'roomduration': 4},
    {'id': 7, 'name': 'Edward Chen', 'food_choice': 'B', 'distance': 95, 'transport_choice': 'walking', 'room_id': '15', 'roomnumber': 3, 'roomduration': 1},
    {'id': 8, 'name': 'Fiona Liu', 'food_choice': 'C', 'distance': 620, 'transport_choice': 'train', 'room_id': '30', 'roomnumber': 12, 'roomduration': 3},
    {'id': 9, 'name': 'George Tang', 'food_choice': 'D', 'distance': 750, 'transport_choice': 'car', 'room_id': '15', 'roomnumber': 6, 'roomduration': 2},
    {'id': 10, 'name': 'Helen Park', 'food_choice': 'A', 'distance': 400, 'transport_choice': 'bike', 'room_id': '30', 'roomnumber': 9, 'roomduration': 1},
    {'id': 11, 'name': 'Ivan Zhao', 'food_choice': 'B', 'distance': 320, 'transport_choice': 'train', 'room_id': '15', 'roomnumber': 4, 'roomduration': 2},
    {'id': 12, 'name': 'Jessica Lin', 'food_choice': 'C', 'distance': 580, 'transport_choice': 'car', 'room_id': '30', 'roomnumber': 10, 'roomduration': 4},
    {'id': 13, 'name': 'Kevin Yang', 'food_choice': 'D', 'distance': 210, 'transport_choice': 'walking', 'room_id': '15', 'roomnumber': 2, 'roomduration': 1},
    {'id': 14, 'name': 'Laura Zhang', 'food_choice': 'A', 'distance': 670, 'transport_choice': 'train', 'room_id': '30', 'roomnumber': 15, 'roomduration': 3},
    {'id': 15, 'name': 'Michael Wu', 'food_choice': 'B', 'distance': 120, 'transport_choice': 'car', 'room_id': '15', 'roomnumber': 4, 'roomduration': 2},
    {'id': 16, 'name': 'Nancy Li', 'food_choice': 'C', 'distance': 250, 'transport_choice': 'bike', 'room_id': '30', 'roomnumber': 7, 'roomduration': 1},
    {'id': 17, 'name': 'Oscar Sun', 'food_choice': 'D', 'distance': 470, 'transport_choice': 'train', 'room_id': '15', 'roomnumber': 3, 'roomduration': 2},
]

employees_day3 = [
    {'id': 1, 'name': 'John Doe', 'food_choice': 'B', 'distance': 300, 'transport_choice': 'bike', 'room_id': '30', 'roomnumber': 3, 'roomduration': 2},
    {'id': 2, 'name': 'Long Han', 'food_choice': 'C', 'distance': 600, 'transport_choice': 'walking', 'room_id': '15', 'roomnumber': 5, 'roomduration': 1},
    {'id': 3, 'name': 'Alice Wong', 'food_choice': 'A', 'distance': 150, 'transport_choice': 'train', 'room_id': '30', 'roomnumber': 6, 'roomduration': 3},
    {'id': 4, 'name': 'Bob Lee', 'food_choice': 'D', 'distance': 500, 'transport_choice': 'car', 'room_id': '15', 'roomnumber': 4, 'roomduration': 2},
    {'id': 5, 'name': 'Chris Kim', 'food_choice': 'B', 'distance': 250, 'transport_choice': 'bike', 'room_id': '30', 'roomnumber': 8, 'roomduration': 1},
    {'id': 6, 'name': 'Diana Hu', 'food_choice': 'C', 'distance': 400, 'transport_choice': 'train', 'room_id': '15', 'roomnumber': 7, 'roomduration': 4},
    {'id': 7, 'name': 'Edward Chen', 'food_choice': 'A', 'distance': 80, 'transport_choice': 'car', 'room_id': '30', 'roomnumber': 9, 'roomduration': 3},
    {'id': 8, 'name': 'Fiona Liu', 'food_choice': 'D', 'distance': 700, 'transport_choice': 'walking', 'room_id': '15', 'roomnumber': 6, 'roomduration': 2},
    {'id': 9, 'name': 'George Tang', 'food_choice': 'C', 'distance': 600, 'transport_choice': 'train', 'room_id': '30', 'roomnumber': 12, 'roomduration': 1},
    {'id': 10, 'name': 'Helen Park', 'food_choice': 'B', 'distance': 350, 'transport_choice': 'bike', 'room_id': '15', 'roomnumber': 4, 'roomduration': 3},
    {'id': 11, 'name': 'Ivan Zhao', 'food_choice': 'D', 'distance': 280, 'transport_choice': 'car', 'room_id': '30', 'roomnumber': 5, 'roomduration': 2},
    {'id': 12, 'name': 'Jessica Lin', 'food_choice': 'A', 'distance': 450, 'transport_choice': 'train', 'room_id': '15', 'roomnumber': 8, 'roomduration': 3},
    {'id': 13, 'name': 'Kevin Yang', 'food_choice': 'C', 'distance': 200, 'transport_choice': 'bike', 'room_id': '30', 'roomnumber': 4, 'roomduration': 1},
    {'id': 14, 'name': 'Laura Zhang', 'food_choice': 'D', 'distance': 800, 'transport_choice': 'walking', 'room_id': '15', 'roomnumber': 7, 'roomduration': 2},
    {'id': 15, 'name': 'Michael Wu', 'food_choice': 'A', 'distance': 130, 'transport_choice': 'train', 'room_id': '30', 'roomnumber': 6, 'roomduration': 3},
    {'id': 16, 'name': 'Nancy Li', 'food_choice': 'B', 'distance': 270, 'transport_choice': 'car', 'room_id': '15', 'roomnumber': 5, 'roomduration': 2},
    {'id': 17, 'name': 'Oscar Sun', 'food_choice': 'C', 'distance': 490, 'transport_choice': 'train', 'room_id': '30', 'roomnumber': 8, 'roomduration': 1},
]

employees_day4 = [
    {'id': 1, 'name': 'John Doe', 'food_choice': 'C', 'distance': 150, 'transport_choice': 'train', 'room_id': '30', 'roomnumber': 4, 'roomduration': 3},
    {'id': 2, 'name': 'Long Han', 'food_choice': 'D', 'distance': 620, 'transport_choice': 'car', 'room_id': '15', 'roomnumber': 6, 'roomduration': 2},
    {'id': 3, 'name': 'Alice Wong', 'food_choice': 'A', 'distance': 280, 'transport_choice': 'bike', 'room_id': '30', 'roomnumber': 5, 'roomduration': 1},
    {'id': 4, 'name': 'Bob Lee', 'food_choice': 'B', 'distance': 500, 'transport_choice': 'walking', 'room_id': '15', 'roomnumber': 3, 'roomduration': 2},
    {'id': 5, 'name': 'Chris Kim', 'food_choice': 'C', 'distance': 350, 'transport_choice': 'train', 'room_id': '30', 'roomnumber': 7, 'roomduration': 4},
    {'id': 6, 'name': 'Diana Hu', 'food_choice': 'D', 'distance': 420, 'transport_choice': 'car', 'room_id': '15', 'roomnumber': 6, 'roomduration': 3},
    {'id': 7, 'name': 'Edward Chen', 'food_choice': 'A', 'distance': 180, 'transport_choice': 'bike', 'room_id': '30', 'roomnumber': 8, 'roomduration': 1},
    {'id': 8, 'name': 'Fiona Liu', 'food_choice': 'B', 'distance': 550, 'transport_choice': 'walking', 'room_id': '15', 'roomnumber': 5, 'roomduration': 2},
    {'id': 9, 'name': 'George Tang', 'food_choice': 'C', 'distance': 700, 'transport_choice': 'car', 'room_id': '30', 'roomnumber': 9, 'roomduration': 3},
    {'id': 10, 'name': 'Helen Park', 'food_choice': 'D', 'distance': 400, 'transport_choice': 'train', 'room_id': '15', 'roomnumber': 4, 'roomduration': 2},
    {'id': 11, 'name': 'Ivan Zhao', 'food_choice': 'A', 'distance': 300, 'transport_choice': 'bike', 'room_id': '30', 'roomnumber': 5, 'roomduration': 4},
    {'id': 12, 'name': 'Jessica Lin', 'food_choice': 'B', 'distance': 450, 'transport_choice': 'walking', 'room_id': '15', 'roomnumber': 7, 'roomduration': 2},
    {'id': 13, 'name': 'Kevin Yang', 'food_choice': 'C', 'distance': 220, 'transport_choice': 'car', 'room_id': '30', 'roomnumber': 6, 'roomduration': 3},
    {'id': 14, 'name': 'Laura Zhang', 'food_choice': 'D', 'distance': 550, 'transport_choice': 'train', 'room_id': '15', 'roomnumber': 8, 'roomduration': 1},
    {'id': 15, 'name': 'Michael Wu', 'food_choice': 'A', 'distance': 170, 'transport_choice': 'bike', 'room_id': '30', 'roomnumber': 4, 'roomduration': 2},
    {'id': 16, 'name': 'Nancy Li', 'food_choice': 'B', 'distance': 290, 'transport_choice': 'car', 'room_id': '15', 'roomnumber': 6, 'roomduration': 3},
    {'id': 17, 'name': 'Oscar Sun', 'food_choice': 'C', 'distance': 460, 'transport_choice': 'train', 'room_id': '30', 'roomnumber': 5, 'roomduration': 1},
]


# Mock-Daten für Emissionen
food_emissions = {
    'A': 100,
    'B': 200,
    'C': 300,
    'D': 400
}

transport_emissions = {
    'car': 112.2,
    'train': 70,
    'bike': 0,
    'walking': 0
}

room_emissions = {
    '15': 5.5,  # Emissionen pro Person für Räume bis 15 m²
    '30': 5.5   # Emissionen pro Person für größere Räume
}

total_emission_main = 0

number_of_employees = 17



# Route, um die Startseite zu bedienen
@app.route('/')
def index():
    return render_template('index.html')

# Funktion zur Berechnung der CO₂-Emissionen basierend auf der Essensauswahl
def calc_emi_byFood(food_choice):
    return food_emissions.get(food_choice, 0)

# Funktion zur Berechnung der CO₂-Emissionen basierend auf dem Transportmittel
def calc_emi_byTransport(distance, transport_choice):
    emission_rate = transport_emissions.get(transport_choice, 0)
    return distance * emission_rate

# Funktion zur Berechnung der CO₂-Emissionen eines Meetingraums
def calc_emi_byRoom(room_id, roomnumber, roomduration):
    emission_per_person = room_emissions.get(room_id, 0)
    return emission_per_person * roomnumber * roomduration


for new_emp in employees_day2:
    food_emission = calc_emi_byFood(new_emp['food_choice'])
    transport_emission = calc_emi_byTransport(new_emp['distance'], new_emp['transport_choice'])
    room_emission = calc_emi_byRoom(new_emp['room_id'], new_emp['roomnumber'], new_emp['roomduration'])
    total_emission = food_emission + transport_emission + room_emission
    total_emission_main = total_emission_main + total_emission

for new_emp in employees_day3:
    food_emission = calc_emi_byFood(new_emp['food_choice'])
    transport_emission = calc_emi_byTransport(new_emp['distance'], new_emp['transport_choice'])
    room_emission = calc_emi_byRoom(new_emp['room_id'], new_emp['roomnumber'], new_emp['roomduration'])
    total_emission = food_emission + transport_emission + room_emission
    total_emission_main = total_emission_main + total_emission
    
for new_emp in employees_day4:
    food_emission = calc_emi_byFood(new_emp['food_choice'])
    transport_emission = calc_emi_byTransport(new_emp['distance'], new_emp['transport_choice'])
    room_emission = calc_emi_byRoom(new_emp['room_id'], new_emp['roomnumber'], new_emp['roomduration'])
    total_emission = food_emission + transport_emission + room_emission
    total_emission_main = total_emission_main + total_emission



# Trigger-Function-Day1
# Route, um die CO₂-Emissionen zu berechnen und in der "Datenbank" zu speichern
@app.route('/calculate', methods=['POST'])
def calculate():
    global employees_m1
    if not employees_m1:
        for new_emp in employees_day2:
        
            # Berechnungen
            food_emission = calc_emi_byFood(new_emp['food_choice'])
            transport_emission = calc_emi_byTransport(new_emp['distance'], new_emp['transport_choice'])
            room_emission = calc_emi_byRoom(new_emp['room_id'], new_emp['roomnumber'], new_emp['roomduration'])
            
            # Gesamtemission berechnen
            total_emission = food_emission + transport_emission + room_emission

            if total_emission < (total_emission_main/number_of_employees):
                percentage = 100-(total_emission / (total_emission_main/number_of_employees)) * 100
                output1 = str(percentage)[0:5] + ' percent less compared to the average'
            else:
                percentage = (total_emission_main/number_of_employees) / total_emission * 100
                output1 = str(percentage)[0:5] + ' percent more compared to the average'
            
            # Füge den berechneten Mitarbeiter zu employees_main hinzu
            new_employee = {
                    'id': len(employees_m1) + 1,
                    'name': new_emp['name'],
                    'transport_emission': transport_emission,
                    'food_emission': food_emission,
                    'room_emi': room_emission,
                    'sum_emi': total_emission,
                    'You use': output1
                }
            employees_m1.append(new_employee)
    employeelist = sorted(employees_m1, key=lambda x: x['sum_emi'])  
    employees_m1 = employeelist
    # employeelist = employees_m1['sum_emi'].sort()
    return jsonify({'status': 'success', 'employees_m1': employeelist})

# Trigger-Function-Day1
# Route, um die CO₂-Emissionen zu berechnen und in der "Datenbank" zu speichern
@app.route('/calculate', methods=['POST'])
def calculate2():
    global employees_m2
    if not employees_m2:
        for new_emp in employees_day3:
        
            # Berechnungen
            food_emission = calc_emi_byFood(new_emp['food_choice'])
            transport_emission = calc_emi_byTransport(new_emp['distance'], new_emp['transport_choice'])
            room_emission = calc_emi_byRoom(new_emp['room_id'], new_emp['roomnumber'], new_emp['roomduration'])
            
            # Gesamtemission berechnen
            total_emission = food_emission + transport_emission + room_emission

            if total_emission < (total_emission_main/number_of_employees):
                percentage = 100-(total_emission / (total_emission_main/number_of_employees)) * 100
                output1 = str(percentage)[0:5] + ' percent less compared to the average'
            else:
                percentage = (total_emission_main/number_of_employees) / total_emission * 100
                output1 = str(percentage)[0:5] + ' percent more compared to the average'
            
            # Füge den berechneten Mitarbeiter zu employees_main hinzu
            new_employee = {
                    'id': len(employees_m2) + 1,
                    'name': new_emp['name'],
                    'transport_emission': transport_emission,
                    'food_emission': food_emission,
                    'room_emi': room_emission,
                    'sum_emi': total_emission,
                    'You use': output1
                }
            employees_m2.append(new_employee)
    employeelist = sorted(employees_m2, key=lambda x: x['sum_emi'])  
    employees_m2 = employeelist
    return jsonify({'status': 'success', 'employees_m2': employeelist})

# Route, um die CO₂-Emissionen zu berechnen und in der "Datenbank" zu speichern
@app.route('/calculate', methods=['POST'])
def calculate3():
    global employees_m3
    if not employees_m3:
        for new_emp in employees_day4:
        
            # Berechnungen
            food_emission = calc_emi_byFood(new_emp['food_choice'])
            transport_emission = calc_emi_byTransport(new_emp['distance'], new_emp['transport_choice'])
            room_emission = calc_emi_byRoom(new_emp['room_id'], new_emp['roomnumber'], new_emp['roomduration'])
            
            # Gesamtemission berechnen
            total_emission = food_emission + transport_emission + room_emission

            if total_emission < (total_emission_main/number_of_employees):
                percentage = 100-(total_emission / (total_emission_main/number_of_employees)) * 100
                output1 = str(percentage)[0:5] + ' percent less compared to the average'
            else:
                percentage = (total_emission_main/number_of_employees) / total_emission * 100
                output1 = str(percentage)[0:5] + ' percent more compared to the average'
            
            # Füge den berechneten Mitarbeiter zu employees_main hinzu
            new_employee = {
                    'id': len(employees_m3) + 1,
                    'name': new_emp['name'],
                    'transport_emission': transport_emission,
                    'food_emission': food_emission,
                    'room_emi': room_emission,
                    'sum_emi': total_emission,
                    'You use': output1
                }
            employees_m3.append(new_employee)
    employeelist = sorted(employees_m3, key=lambda x: x['sum_emi'])  
    employees_m3 = employeelist
    return jsonify({'status': 'success', 'employees_m3': employeelist})


    count_dict = [10][2]
    for emp in employeelist_m1[:10]:
        name = emp['name']
        if name in count_dict:
            count_dict[name] += 1
        else:
            count_dict[name] = 1
            
    count_dict.append([name, count_dict])
    
def calculate4():
    employees_main = employees_m1
    print (employees_main)

    

@app.route('/trigger-function', methods=['POST'])
def trigger_function():
    # Do some backend processing (e.g., update the database, compute emissions)
    calculate()
    calculate2()
    calculate3()
    calculate4()
    return jsonify({
        'name': employees_main,
    })

@app.route('/trigger-function-day1', methods=['POST'])
def trigger_functionDay1():
    # Do some backend processing (e.g., update the database, compute emissions)
    calculate()
    return jsonify({
        'name': employees_m1,
    })


@app.route('/trigger-function-day2', methods=['POST'])
def trigger_functionDay2():
    # Do some backend processing (e.g., update the database, compute emissions)
    calculate2()
    return jsonify({
        'name': employees_m2,
    })

@app.route('/trigger-function-day3', methods=['POST'])
def trigger_functionDay3():
    # Do some backend processing (e.g., update the database, compute emissions)
    calculate3()
    return jsonify({
        'name': employees_m3,
    })



# Route, um alle CO₂-Emissionsdaten der Mitarbeiter abzurufen
@app.route('/employees', methods=['GET'])
def get_employees_main():
    return jsonify(employees_main)


@app.route('/day1', methods=['GET'])
def get_employees_m1():
    return jsonify(employees_m1)

@app.route('/day2', methods=['GET'])
def get_employees_m2():
    return jsonify(employees_m2)

@app.route('/day3', methods=['GET'])
def get_employees_m3():
    return jsonify(employees_m3)



if __name__ == '__main__':
    app.run(debug=True)
