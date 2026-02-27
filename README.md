# Kupo Dashboard

A minimal dashboard with a sidebar, summary cards, and a data table built with Python 3 and Flask.

## Setup

1. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
kupo/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── README.md
├── templates/
│   ├── base.html           # Base layout with sidebar
│   ├── index.html          # Dashboard overview
│   ├── users.html          # Users table page
│   └── analytics.html      # Analytics page
└── static/
    ├── css/
    │   └── style.css       # Custom styles
    └── js/
        └── main.js         # Client-side scripts
```
