from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/roundup', methods=['POST'])
def roundup():
    try:
        data = request.json
        amount = float(data['amount'])

        # Calculate the roundup amount
        rounded_amount = round(amount + 0.5)
        roundup_value = rounded_amount - amount

        return jsonify({
            "original_amount": amount,
            "rounded_up_amount": rounded_amount,
            "roundup_value": roundup_value
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
