from flask import Flask, request, jsonify, render_template_string
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Health Calculator Live</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .form-container { margin-bottom: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
            .form-group { margin-bottom: 10px; }
            label { display: block; margin-bottom: 5px; }
            input, select { width: 100%; padding: 8px; margin-bottom: 10px; box-sizing: border-box; }
            button { background-color: #4CAF50; color: white; padding: 10px 15px; border: none; cursor: pointer; }
            .result { margin-top: 15px; padding: 10px; background-color: #f1f1f1; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>Health Calculator (Live Results)</h1>

        <!-- BMI Form -->
        <div class="form-container">
            <h2>BMI Calculator</h2>
            <form id="bmi-form">
                <div class="form-group">
                    <label for="bmi-height">Height (meters):</label>
                    <input type="number" id="bmi-height" step="0.01" required>
                </div>
                <div class="form-group">
                    <label for="bmi-weight">Weight (kg):</label>
                    <input type="number" id="bmi-weight" step="0.1" required>
                </div>
                <button type="submit">Calculate BMI</button>
            </form>
            <div id="bmi-result" class="result"></div>
        </div>

        <!-- BMR Form -->
        <div class="form-container">
            <h2>BMR Calculator</h2>
            <form id="bmr-form">
                <div class="form-group">
                    <label for="bmr-height">Height (cm):</label>
                    <input type="number" id="bmr-height" required>
                </div>
                <div class="form-group">
                    <label for="bmr-weight">Weight (kg):</label>
                    <input type="number" id="bmr-weight" required>
                </div>
                <div class="form-group">
                    <label for="bmr-age">Age (years):</label>
                    <input type="number" id="bmr-age" required>
                </div>
                <div class="form-group">
                    <label for="bmr-gender">Gender:</label>
                    <select id="bmr-gender" required>
                        <option value="">Select</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                    </select>
                </div>
                <button type="submit">Calculate BMR</button>
            </form>
            <div id="bmr-result" class="result"></div>
        </div>

        <script>
            // Handle BMI form submission
            document.getElementById('bmi-form').addEventListener('submit', function(e) {
                e.preventDefault(); // prevent page reload
                const height = parseFloat(document.getElementById('bmi-height').value);
                const weight = parseFloat(document.getElementById('bmi-weight').value);

                fetch('/bmi', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ height, weight }),
                })
                .then(response => response.json())
                .then(data => {
                    const resultDiv = document.getElementById('bmi-result');
                    if (data.error) {
                        resultDiv.innerHTML = '<p class="error">' + data.error + '</p>';
                    } else {
                        resultDiv.innerHTML = '<p>Your BMI: ' + data.bmi + '</p><p>Category: ' + data.category + '</p>';
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            });

            // Handle BMR form submission
            document.getElementById('bmr-form').addEventListener('submit', function(e) {
                e.preventDefault(); // prevent page reload
                const height = parseFloat(document.getElementById('bmr-height').value);
                const weight = parseFloat(document.getElementById('bmr-weight').value);
                const age = parseInt(document.getElementById('bmr-age').value);
                const gender = document.getElementById('bmr-gender').value;

                fetch('/bmr', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ height, weight, age, gender }),
                })
                .then(response => response.json())
                .then(data => {
                    const resultDiv = document.getElementById('bmr-result');
                    if (data.error) {
                        resultDiv.innerHTML = '<p class="error">' + data.error + '</p>';
                    } else {
                        resultDiv.innerHTML = '<p>Your BMR: ' + data.bmr + ' ' + data.unit + '</p>';
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            });
        </script>

    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    if not data or 'height' not in data or 'weight' not in data:
        return jsonify({'error': 'Missing required parameters. Please provide height and weight.'}), 400

    try:
        height = float(data['height'])
        weight = float(data['weight'])

        if height <= 0 or weight <= 0:
            return jsonify({'error': 'Height and weight must be positive values.'}), 400

        bmi_value = calculate_bmi(height, weight)
        category = "Unknown"
        if bmi_value < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi_value < 25:
            category = "Normal weight"
        elif 25 <= bmi_value < 30:
            category = "Overweight"
        else:
            category = "Obese"

        return jsonify({'bmi': round(bmi_value, 2), 'category': category})

    except ValueError:
        return jsonify({'error': 'Invalid input values.'}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    required_fields = ['height', 'weight', 'age', 'gender']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields.'}), 400

    try:
        height = float(data['height'])
        weight = float(data['weight'])
        age = int(data['age'])
        gender = data['gender'].lower()

        if height <= 0 or weight <= 0 or age <= 0:
            return jsonify({'error': 'Height, weight and age must be positive values.'}), 400

        if gender not in ['male', 'female']:
            return jsonify({'error': 'Gender must be "male" or "female".'}), 400

        bmr_value = calculate_bmr(height, weight, age, gender)

        return jsonify({'bmr': round(bmr_value, 2), 'unit': 'calories/day'})

    except ValueError:
        return jsonify({'error': 'Invalid input values.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
