# AI-Powered Resume Parser 📄🚀

A full-stack web application that extracts key information (Email, Skills) from PDF resumes and stores them in a PostgreSQL database.

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML5, Bootstrap 5
- **Database:** PostgreSQL
- **Parsing:** pdfplumber & Regular Expressions (Regex)

## 🌟 Features
- Upload PDF resumes via a clean web interface.
- Automatic extraction of email addresses and technical skills.
- Permanent storage of parsed data in a relational database.
- Real-time display of results on a success page.

## 📁 Project Structure
```text
Resume_Parser_Project/
├── app.py              # Main Flask application
├── database.py         # PostgreSQL connection & storage logic
├── parser_logic.py     # PDF text extraction logic
├── templates/          # HTML files (index.html, success.html)
└── uploads/            # Temporary storage for uploaded PDFs
