from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    
    # Validate input data
    if not data or 'height' not in data or 'weight' not in data:
        return jsonify({'error': 'Missing required parameters. Please provide height (m) and weight (kg)'}), 400
    
    try:
        height = float(data['height'])
        weight = float(data['weight'])
        
        if height <= 0 or weight <= 0:
            return jsonify({'error': 'Height and weight must be positive values'}), 400
        
        bmi_value = calculate_bmi(height, weight)
        
        # Determine BMI category
        category = "Unknown"
        if bmi_value < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi_value < 25:
            category = "Normal weight"
        elif 25 <= bmi_value < 30:
            category = "Overweight"
        else:
            category = "Obese"
            
        result = {
            'bmi': round(bmi_value, 2),
            'category': category
        }
        
        return jsonify(result)
    
    except ValueError:
        return jsonify({'error': 'Invalid input. Height and weight must be numeric values'}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    
    # Validate input data
    required_fields = ['height', 'weight', 'age', 'gender']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing required parameters. Please provide {", ".join(required_fields)}'}), 400
    
    try:
        height = float(data['height'])  # in cm
        weight = float(data['weight'])  # in kg
        age = int(data['age'])
        gender = data['gender'].lower()
        
        if height <= 0 or weight <= 0 or age <= 0:
            return jsonify({'error': 'Height, weight, and age must be positive values'}), 400
        
        if gender not in ['male', 'female']:
            return jsonify({'error': 'Gender must be either "male" or "female"'}), 400
        
        bmr_value = calculate_bmr(height, weight, age, gender)
        
        result = {
            'bmr': round(bmr_value, 2),
            'unit': 'calories/day'
        }
        
        return jsonify(result)
    
    except ValueError:
        return jsonify({'error': 'Invalid input. Height, weight, and age must be numeric values'}), 400

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'service': 'Health Calculator API',
        'endpoints': {
            '/bmi': 'Calculate Body Mass Index (POST)',
            '/bmr': 'Calculate Basal Metabolic Rate (POST)'
        },
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)