@app.route('/', methods=['GET'])
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Health Calculator API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }
            h1 { color: #2c3e50; text-align: center; margin-bottom: 30px; }
            .calculator { background-color: #f8f9fa; border-radius: 8px; padding: 20px; margin-bottom: 30px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .calculator h2 { color: #17a2b8; border-bottom: 1px solid #dee2e6; padding-bottom: 10px; }
            .form-group { margin-bottom: 15px; }
            label { display: block; margin-bottom: 5px; font-weight: bold; }
            input, select { width: 100%; padding: 8px; border: 1px solid #ced4da; border-radius: 4px; box-sizing: border-box; }
            button { background-color: #17a2b8; color: white; border: none; padding: 10px 15px; border-radius: 4px; cursor: pointer; }
            button:hover { background-color: #138496; }
            .result { margin-top: 20px; padding: 15px; background-color: #e9ecef; border-radius: 4px; display: none; }
            .api-info { text-align: center; margin-top: 30px; color: #6c757d; font-size: 0.9em; }
        </style>
    </head>
    <body>
        <h1>Health Calculator</h1>
        
        <div class="calculator">
            <h2>BMI Calculator</h2>
            <form id="bmi-form">
                <div class="form-group">
                    <label for="bmi-height">Height (meters)</label>
                    <input type="number" id="bmi-height" step="0.01" min="0.1" placeholder="e.g., 1.75" required>
                </div>
                <div class="form-group">
                    <label for="bmi-weight">Weight (kg)</label>
                    <input type="number" id="bmi-weight" step="0.1" min="1" placeholder="e.g., 70" required>
                </div>
                <button type="submit">Calculate BMI</button>
            </form>
            <div id="bmi-result" class="result"></div>
        </div>
        
        <div class="calculator">
            <h2>BMR Calculator</h2>
            <form id="bmr-form">
                <div class="form-group">
                    <label for="bmr-height">Height (cm)</label>
                    <input type="number" id="bmr-height" step="0.1" min="1" placeholder="e.g., 175" required>
                </div>
                <div class="form-group">
                    <label for="bmr-weight">Weight (kg)</label>
                    <input type="number" id="bmr-weight" step="0.1" min="1" placeholder="e.g., 70" required>
                </div>
                <div class="form-group">
                    <label for="bmr-age">Age (years)</label>
                    <input type="number" id="bmr-age" min="1" placeholder="e.g., 30" required>
                </div>
                <div class="form-group">
                    <label for="bmr-gender">Gender</label>
                    <select id="bmr-gender" required>
                        <option value="">Select gender</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                    </select>
                </div>
                <button type="submit">Calculate BMR</button>
            </form>
            <div id="bmr-result" class="result"></div>
        </div>
        
        <div class="api-info">
            <p>Health Calculator API - Version 1.0.0</p>
        </div>
        
        <script>
            document.getElementById('bmi-form').addEventListener('submit', async function(e) {
                e.preventDefault();
                const height = parseFloat(document.getElementById('bmi-height').value);
                const weight = parseFloat(document.getElementById('bmi-weight').value);
                
                try {
                    const response = await fetch('/bmi', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ height, weight }),
                    });
                    
                    const data = await response.json();
                    
                    const resultElement = document.getElementById('bmi-result');
                    if (response.ok) {
                        resultElement.innerHTML = `
                            <p><strong>Your BMI:</strong> ${data.bmi}</p>
                            <p><strong>Category:</strong> ${data.category}</p>
                        `;
                    } else {
                        resultElement.innerHTML = `<p>Error: ${data.error}</p>`;
                    }
                    resultElement.style.display = 'block';
                } catch (error) {
                    console.error('Error:', error);
                }
            });
            
            document.getElementById('bmr-form').addEventListener('submit', async function(e) {
                e.preventDefault();
                const height = parseFloat(document.getElementById('bmr-height').value);
                const weight = parseFloat(document.getElementById('bmr-weight').value);
                const age = parseInt(document.getElementById('bmr-age').value);
                const gender = document.getElementById('bmr-gender').value;
                
                try {
                    const response = await fetch('/bmr', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ height, weight, age, gender }),
                    });
                    
                    const data = await response.json();
                    
                    const resultElement = document.getElementById('bmr-result');
                    if (response.ok) {
                        resultElement.innerHTML = `
                            <p><strong>Your BMR:</strong> ${data.bmr} ${data.unit}</p>
                            <p>This is the number of calories your body needs at rest.</p>
                        `;
                    } else {
                        resultElement.innerHTML = `<p>Error: ${data.error}</p>`;
                    }
                    resultElement.style.display = 'block';
                } catch (error) {
                    console.error('Error:', error);
                }
            });
        </script>
    </body>
    </html>
    """
    return html_content, 200, {'Content-Type': 'text/html'}
