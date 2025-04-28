@app.route('/', methods=['GET'])
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Health Calculator API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .form-container { margin-bottom: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
            .form-group { margin-bottom: 10px; }
            label { display: block; margin-bottom: 5px; }
            input, select { width: 100%; padding: 8px; margin-bottom: 10px; box-sizing: border-box; }
            button { background-color: #4CAF50; color: white; padding: 10px 15px; border: none; cursor: pointer; }
            .result { margin-top: 15px; padding: 10px; background-color: #f1f1f1; display: none; }
        </style>
    </head>
    <body>
        <h1>Health Calculator</h1>
        
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
            document.getElementById('bmi-form').addEventListener('submit', function(e) {
                e.preventDefault();
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
                    const resultElement = document.getElementById('bmi-result');
                    if (data.error) {
                        resultElement.innerHTML = `<p>Error: ${data.error}</p>`;
                    } else {
                        resultElement.innerHTML = `
                            <p>Your BMI: ${data.bmi}</p>
                            <p>Category: ${data.category}</p>
                        `;
                    }
                    resultElement.style.display = 'block';
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            });
            
            document.getElementById('bmr-form').addEventListener('submit', function(e) {
                e.preventDefault();
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
                    const resultElement = document.getElementById('bmr-result');
                    if (data.error) {
                        resultElement.innerHTML = `<p>Error: ${data.error}</p>`;
                    } else {
                        resultElement.innerHTML = `
                            <p>Your BMR: ${data.bmr} ${data.unit}</p>
                        `;
                    }
                    resultElement.style.display = 'block';
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            });
        </script>
    </body>
    </html>
    """
    return html_content, 200, {'Content-Type': 'text/html'}
