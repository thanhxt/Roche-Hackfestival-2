from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Hardcoded "database" of employee CO₂ waste
employees = [
    {'id': 1, 'name': 'John Doe', 'co2_waste': 120.5},
    {'id': 2, 'name': 'Jane Smith', 'co2_waste': 95.2},
    # Add more employees here
]

# Route to serve the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Function to calculate CO₂ waste (placeholder)
def calculate_co2_waste(co2_waste):
    return co2_waste * 1  # Placeholder for more complex calculations

# Route to handle CO₂ waste submission and "save" it to the hardcoded database
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    employee_name = data['employeeName']
    co2_waste = float(data['co2Waste'])

    # Calculate waste (this can be more complex)
    calculated_waste = calculate_co2_waste(co2_waste)

    # Simulate saving to "database" by appending to the hardcoded list
    new_employee = {
        'id': len(employees) + 1,  # Auto-incrementing id
        'name': employee_name,
        'co2_waste': calculated_waste
    }
    employees.append(new_employee)

    return jsonify({
        'employeeName': employee_name,
        'calculatedWaste': calculated_waste
    })

# Fetch all employee CO2 waste data
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True)
