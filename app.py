from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined responses
faq = {
    "admission": "Admissions are open until June 30, 2025.",
    "courses": "We offer B.Tech in CSE, ECE, ME, Civil, and more.",
    "faculty": "Our faculty includes experienced professors from IITs and NITs.",
    "events": "Upcoming events include TechFest on April 15th and Workshop on May 2nd.",
    "contact": "You can contact us at contact@college.edu or call +91-1234567890."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.json.get('message').lower()
    response = "Sorry, I don't understand. Can you rephrase?"

    for keyword in faq:
        if keyword in user_message:
            response = faq[keyword]
            break

    return jsonify({'reply': response})

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
