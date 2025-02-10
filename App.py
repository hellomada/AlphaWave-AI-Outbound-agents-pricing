from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Fixed Costs
COST_PER_MINUTE = 0.0018  # 0.18 cents per minute
FIXED_TIME_COST = 100  # $100 of personal time
INTEGRATION_COST = 25  # $25 for integration
TWILIO_BASE_COST = 15  # Twilio monthly base cost (adjustable)
VAPI_BASE_COST = 10  # VAPI estimated cost (adjustable)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        calls_per_day = int(data.get('calls_per_day', 0))
        avg_duration = float(data.get('avg_duration', 3))  # Default 3 minutes
        days_per_month = 22  # Average business days in a month
        
        total_minutes = calls_per_day * avg_duration * days_per_month
        call_cost = total_minutes * COST_PER_MINUTE
        
        total_cost = call_cost + FIXED_TIME_COST + INTEGRATION_COST + TWILIO_BASE_COST + VAPI_BASE_COST
        total_cost = round(total_cost, 2)
        
        return jsonify({"monthly_cost": total_cost})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
