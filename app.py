from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'thefitstop_secret_key_2026'


@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submission."""
    try:
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        # Validation
        if not name or not email or not message:
            return render_template('index.html', 
                                 message='Please fill in all fields.',
                                 message_type='error')
        
        if len(message) < 10:
            return render_template('index.html',
                                 message='Message must be at least 10 characters long.',
                                 message_type='error')
        
        # Print contact info
        print(f"\n--- New Contact Message ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        print(f"----------------------------\n")
        
        return render_template('index.html',
                             message='Thank you! Your message has been sent successfully.',
                             message_type='success')
    
    except Exception as e:
        return render_template('index.html',
                             message='An error occurred. Please try again later.',
                             message_type='error')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
