@app.route('/', methods=['GET'])
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Health Calculator API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
            h1 { color: #2c3e50; }
            .endpoint { background-color: #f8f9fa; border-left: 4px solid #17a2b8; padding: 15px; margin-bottom: 20px; }
            .method { color: #17a2b8; font-weight: bold; }
            .parameters { color: #6c757d; }
        </style>
    </head>
    <body>
        <h1>Health Calculator API</h1>
        <p>Version: 1.0.0</p>
        
        <div class="endpoint">
            <h2>/bmi</h2>
            <p><span class="method">Method: POST</span></p>
            <p>Calculate Body Mass Index (BMI)</p>
            <p class="parameters">Parameters: height (m), weight (kg)</p>
            <p>Example request body: {"height": 1.75, "weight": 70}</p>
        </div>
        
        <div class="endpoint">
            <h2>/bmr</h2>
            <p><span class="method">Method: POST</span></p>
            <p>Calculate Basal Metabolic Rate (BMR) using Harris-Benedict Equation</p>
            <p class="parameters">Parameters: height (cm), weight (kg), age, gender</p>
            <p>Example request body: {"height": 175, "weight": 70, "age": 30, "gender": "male"}</p>
        </div>
    </body>
    </html>
    """
    return html_content, 200, {'Content-Type': 'text/html'}
