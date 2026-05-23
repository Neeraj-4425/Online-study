import os
from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

# Absolute directory path where your downloadable files are stored
FILES_DIRECTORY = os.path.join(app.root_path, 'files')

# Centralized data store for your dynamic course syllabi
COURSES_DATA = {
    "python-programming": {
        "title": "Python Programming",
        "description": "Master Python programming, from basics to advanced data analysis and visualization techniques.",
        "syllabus": [
            "Module 1: Introduction to Python & Syntax",
            "Module 2: Data Structures (Lists, Dictionaries, Tuples)",
            "Module 3: Object-Oriented Programming (OOP)",
            "Module 4: Data Analysis with Pandas and NumPy",
            "Module 5: Final Capstone Project"
        ]
    },
    "web-development": {
        "title": "Web Development",
        "description": "Build modern, responsive websites using HTML, CSS, JavaScript, and React from scratch.",
        "syllabus": [
            "Module 1: HTML5 & CSS3 Essentials",
            "Module 2: Advanced Layouts with Flexbox and Grid",
            "Module 3: JavaScript ES6+ Fundamentals",
            "Module 4: Building Interfaces with React",
            "Module 5: Deployment and Hosting Basics"
        ]
    },
    "uiux-design": {
        "title": "UI/UX Design Masterclass",
        "description": "Discover the principles of user interface and experience design to create stunning digital products.",
        "syllabus": [
            "Module 1: Introduction to UX Research & User Personas",
            "Module 2: Wireframing and Prototyping in Figma",
            "Module 3: Visual Design Principles & Typography",
            "Module 4: Usability Testing and Iteration",
            "Module 5: Portfolio Creation"
        ]
    },
    "cybersecurity": {
        "title": "Cybersecurity Essentials",
        "description": "Protect networks and data from attacks with comprehensive training in security best practices.",
        "syllabus": [
            "Module 1: Fundamentals of Network Security",
            "Module 2: Identifying Threats, Vulnerabilities, and Attacks",
            "Module 3: Cryptography Basics",
            "Module 4: Incident Response and Risk Management",
            "Module 5: Defensive Best Practices"
        ]
    },
    "sql-database": {
        "title": "SQL & Database Management",
        "description": "Learn to manage and query relational databases effectively using standard SQL techniques.",
        "syllabus": [
            "Module 1: Relational Database Concepts",
            "Module 2: Writing Basic SQL Queries (SELECT, WHERE)",
            "Module 3: Joins, Aggregations, and Subqueries",
            "Module 4: Database Design & Normalization",
            "Module 5: Indexing and Performance Tuning"
        ]
    }
}

@app.route('/')
@app.route('/courses')
def courses():
    """Serves the main page showing all available courses."""
    return render_template('index.html')

@app.route('/study-materials')
def study_materials():
    """Serves the page showing free downloadable files."""
    return render_template('materials.html')

@app.route('/course/<course_id>')
def course_detail(course_id):
    """Dynamically loads and renders the syllabus for a specific course."""
    course = COURSES_DATA.get(course_id)
    if not course:
        abort(404)
    return render_template('course_detail.html', course=course)

@app.route('/download/<filename>')
def download_file(filename):
    """Securely downloads files from the server's backend folders."""
    try:
        return send_from_directory(directory=FILES_DIRECTORY, path=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
