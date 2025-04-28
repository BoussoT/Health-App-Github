from flask import Flask, request, jsonify, render_template_string
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Default message
    bmi_result = None
    bmr_result = None
    
    if request.method == 'POST':
        # Handle BMI Form
        if 'bmi-height' in request.form and 'bmi-weight' in request.form:
            height = float(request.form['bmi-height'])
            weight = float(request.form['bmi-weight'])
            
            if height <= 0 or weight <= 0:
                bmi_result = {'error': 'Height and weight must be positive values'}
            else:
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
                bmi_result = {
                    'bmi': round(bmi_value, 2),
                    'category': category
                }

        # Handle BMR Form
        if 'bmr-height' in request.form and 'bmr-weight' in request.form and 'bmr-age' in request.form and 'bmr-gender' in request.form:
            height = float(request.form['bmr-height'])  # in cm
            weight = float(request.form['bmr-weight'])  # in kg
            age = int(request.form['bmr-age'])
            gender = request.form['bmr-gender'].lower()
            
            if height <= 0 or weight <= 0 or age <= 0:
                bmr_result = {'error': 'Height, weight, and age must be positive values'}
            elif gender not in ['male', 'female']:
                bmr_result = {'error': 'Gender must be either "male" or "female"'}
            else:
                bmr_value = calculate_bmr(height, weight, age, gender)
                bmr_result = {
                    'bmr': round(bmr_value, 2),
                    'unit': 'calories/day'
                }

    # HTML Template for the frontend
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Health Calculator</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .form-container { margin-bottom: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
            .form-group { margin-bottom: 10px; }
            label { display: block; margin-bottom: 5px; }
            input, select { width: 100%; padding: 8px; margin-bottom: 10px; box-sizing: border-box; }
            button { background-color: #4CAF50; color: white; padding: 10px 15px; border: none; cursor: pointer; }
            .result { margin-top: 15px; padding: 10px; background-color: #f1f1f1; display: none; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>Health Calculator</h1>

        <!-- BMI Form -->
        <div class="form-container">
            <h2>BMI Calculator</h2>
            <form method="POST">
                <div class="form-group">
                    <label for="bmi-height">Height (meters):</label>
                    <input type="number" id="bmi-height" name="bmi-height" step="0.01" required>
                </div>
                <div class="form-group">
                    <label for="bmi-weight">Weight (kg):</label>
                    <input type="number" id="bmi-weight" name="bmi-weight" step="0.1" required>
                </div>
                <button type="submit">Calculate BMI</button>
            </form>
            {% if bmi_result %}
                <div class="result">
                    {% if bmi_result.error %}
                        <p class="error">{{ bmi_result.error }}</p>
                    {% else %}
                        <p>Your BMI: {{ bmi_result.bmi }}</p>
                        <p>Category: {{ bmi_result.category }}</p>
                    {% endif %}
                </div>
            {% endif %}
        </div>

        <!-- BMR Form -->
        <div class="form-container">
            <h2>BMR Calculator</h2>
            <form method="POST">
                <div class="form-group">
                    <label for="bmr-height">Height (cm):</label>
                    <input type="number" id="bmr-height" name="bmr-height" required>
                </div>
                <div class="form-group">
                    <label for="bmr-weight">Weight (kg):</label>
                    <input type="number" id="bmr-weight" name="bmr-weight" required>
                </div>
                <div class="form-group">
                    <label for="bmr-age">Age (years):</label>
                    <input type="number" id="bmr-age" name="bmr-age" required>
                </div>
                <div class="form-group">
                    <label for="bmr-gender">Gender:</label>
                    <select id="bmr-gender" name="bmr-gender" required>
                        <option value="">Select</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                    </select>
                </div>
                <button type="submit">Calculate BMR</button>
            </form>
            {% if bmr_result %}
                <div class="result">
                    {% if bmr_result.error %}
                        <p class="error">{{ bmr_result.error }}</p>
                    {% else %}
                        <p>Your BMR: {{ bmr_result.bmr }} {{ bmr_result.unit }}</p>
                    {% endif %}
                </div>
            {% endif %}
        </div>

    </body>
    </html>
    """
    return render_template_string(html_content, bmi_result=bmi_result, bmr_result=bmr_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
