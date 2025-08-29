from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from datetime import datetime
import os

app = Flask(__name__)

# Configure Flask-Mail (using Gmail with your credentials)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'nagasumukh01@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'madh tqcv tnmw majl'    # Your 16-character App Password
app.config['MAIL_DEFAULT_SENDER'] = 'nagasumukh01@gmail.com'  # Same as username
mail = Mail(app)

# Your resume data as a dynamic Python dict (easy to edit/add)
resume_data = {
    "name": "D Nagasumukh",
    "email": "nagasumukh01@gmail.com",
    "phone": "9448794069",
    "location": "Bangalore, India",
    "dob": "14-07-2005",
    "linkedin": "https://linkedin.com/in/nagasumukh-d-05423934a",
    "github": "https://github.com/nagasumukh01",
    "education": [
        {
            "degree": "B Tech in CSE",
            "institution": "Reva University",
            "duration": "09/2023 – Present",
            "location": "Bangalore, Karnataka, India",
            "gpa": "8.14"
        },
        {
            "degree": "PUC",
            "institution": "Sri Sai Angels Pre University College",
            "duration": "",
            "location": "Chikmagalur, India",
            "gpa": "94.67"
        },
        {
            "degree": "SSLC",
            "institution": "Vasavi Education Society",
            "duration": "",
            "location": "Chikmagalur, India",
            "gpa": "87.68"
        }
    ],
    "internship": {
        "role": "C Program Intern",
        "company": "PINNACLE",
        "duration": "05/2025 – 06/2025",
        "description": "Actively worked as a C program intern at Pinnacle. Made some basic projects to next level projects."
    },
    "courses": [
        "UI/UX Designing using AI",
        "MS Excel",
        "Introduction to Data Science",
        "Introduction to Cloud",
        "Fundamentals of Database-SQL (Simple Learn)",
        "Introduction to Python (Great Learning)"
    ],
    "awards": [
        {
            "title": "UI/UX Design Challenge, IIT Jammu, Anhad'25",
            "description": "As a team member of 'ERROR FUSION', secured winner position in Anhad'25.",
            "image": "IIT_jammu_cert.png"
        }
    ],
    "certificates": [
        {
            "title": "NER Hackathon",
            "description": "Actively participated at Pan India - NER Tech Hackathon 2.0 at Marriott, Bangalore and secured top 14 among 600+ teams.",
            "image": "NER_cert.png"
        }
    ],
    "skills": [  # For animated bars; add more as needed
        {"name": "Python", "level": 80},  # Percentage (0-100)
        {"name": "C Programming", "level": 70},
        {"name": "UI/UX Design", "level": 75},
        {"name": "Data Science Basics", "level": 60},
        {"name": "SQL", "level": 65}
    ]
    # Projects will be added in projects.html template later
}


# Single route for all content (single-page scroll)
@app.route('/', methods=['GET', 'POST'])
def index():
    success = False
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Send email
        msg = Message('New Contact Form Submission',
                      recipients=['nagasumukh01@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}\nTimestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        mail.send(msg)
        success = True
    return render_template('index.html', data=resume_data, success=success)

if __name__ == '__main__':
    app.run(debug=True)