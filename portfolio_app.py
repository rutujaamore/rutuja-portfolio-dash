import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

# --- Config ---
# Ensure you have installed dash-bootstrap-components and dash-iconify:
# pip install dash dash-bootstrap-components dash-iconify
external_stylesheets = [dbc.themes.DARKLY]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# --- Navbar ---
navbar = dbc.Navbar(
    dbc.Container([
        # 1. Navbar Brand: Links to Hero Section. VERIFIED: Must be #home.
        dbc.NavbarBrand("Rutuja More - Data Analyst", href="#home"),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(
            html.Div([
                # Desktop Buttons
                html.Div([
                    # Desktop Projects Link. VERIFIED: Must be #projects.
                    html.A("Projects", href="#projects", className="btn btn-outline-light me-2",
                            **{'data-scroll': '#projects', 'role': 'button'}),
                    html.A("About & Contact", href="#about-contact", className="btn btn-outline-light me-2",
                            **{'data-scroll': '#about-contact', 'role': 'button'}),
                    html.A("Resume", href="/assets/Rutuja_More_Resume.pdf", download="Rutuja_More_Resume.pdf",
                            className="btn btn-outline-light me-2", role="button"),
                ], className="d-none d-md-flex ms-auto align-items-center"),
                
                # Mobile Buttons
                dbc.Nav([
                    # Mobile Projects Link. VERIFIED: Must be #projects.
                    dbc.NavLink("Projects", href="#projects"),
                    dbc.NavLink("About & Contact", href="#about-contact"),
                    html.A("Resume", href="/assets/Rutuja_More_Resume.pdf", download="Rutuja_More_Resume.pdf",
                            className="nav-link"),
                ], navbar=True, className="flex-column d-md-none"),
            ], className="w-100 d-md-flex align-items-center justify-content-end"),
            id="navbar-collapse",
            navbar=True,
            is_open=False,
        ),
    ]),
    color="primary",
    dark=True,
    sticky="top",
    className="shadow-lg mb-4 navbar"
)

# --- Hero Section (FINAL: Left-Aligned Content) ---
hero_section = dbc.Container([
    dbc.Row([
        # 1. Text/Logos Column (Placed on the Left)
        dbc.Col([
            html.H1("Hello, I'm Rutuja More", className="display-3 text-white mb-2"),
            html.H2("A Passionate Data Analyst", className="lead text-info mb-4"),
            html.P("I transform unseen patterns into strategic advantage.",
                     className="text-light fs-5"),
            
            # --- Social Links (Aligned Left) ---
            html.Div([
                # LinkedIn Logo. VERIFIED: Correct URL.
                html.A(DashIconify(icon="mdi:linkedin", color="#0a66c2", width=30), 
                       href="https://www.linkedin.com/in/rutujamore888/", 
                       target="_blank", className="me-4 text-decoration-none"), 
                # GitHub Logo. VERIFIED: Correct URL.
                html.A(DashIconify(icon="mdi:github", color="white", width=30), 
                       href="https://github.com/rutujaamore", 
                       target="_blank", className="me-4 text-decoration-none"), 
                # HackerRank Logo. VERIFIED: Correct URL.
                html.A(DashIconify(icon="simple-icons:hackerrank", color="#2ec866", width=30), 
                       href="https://www.hackerrank.com/profile/rutujamore586", 
                       target="_blank", className="text-decoration-none"),
            # Justifies content to the start (left) on medium screens, centered on small screens
            ], className="mt-4 d-flex justify-content-center justify-content-md-start"), 
            # --- End Social Links ---

        # Text aligns to the left edge of its column (md-start)
        ], md=6, className="text-center text-md-start mb-5"), 
        
        # 2. Image Column (Placed on the Right)
        dbc.Col(
            html.Div(
                html.Img(src="/assets/Image.jpeg",
                         className="img-fluid rounded border border-info border-3 shadow-lg",
                         style={"width": "300px", "height": "300px", "objectFit": "cover"}),
                # Centered image placement
                className="d-flex justify-content-center"
            ), md=4, className="mb-5"
        ),
    ], className="align-items-center justify-content-center py-5")
], id="home", fluid=True, className="bg-dark text-white pt-5")

# --- Projects Section ---
projects_section = dbc.Container([
    html.H2("Projects", className="text-center text-info mb-5 display-5"),
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H4("Cafe Sales Dashboard in Excel", className="card-title text-info")),
            dbc.CardBody([
                html.P(
                    "Built an interactive Excel Cafe Sales Dashboard by cleaning raw sales data, creating calculated fields, analyzing trends with PivotTables, and visualizing monthly revenue, top categories, payment mix, and average order value using charts and slicers in a cafe-themed layout."),
                html.A("View", href="/assets/cafe-sales.png", target="_blank", className="btn btn-info mt-2")
            ])
        ], color="secondary", inverse=True, class_name="shadow-lg h-100"), lg=4, md=6, className="mb-4"),

        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H4("Upcoming Project", className="text-primary")),
            dbc.CardBody([
                html.P("This project is currently under development. Stay tuned!"),
                # VERIFIED: Placeholder link, not email.
                html.A("View", href="#", target="_blank", className="btn btn-info mt-2")
            ])
        ], color="secondary", inverse=True, class_name="shadow-lg h-100"), lg=4, md=6, className="mb-4"),

        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H4("Upcoming Project", className="text-primary")),
            dbc.CardBody([
                html.P("This project is currently under development. Stay tuned!"),
                # VERIFIED: Placeholder link, not email.
                html.A("View", href="#", target="_blank", className="btn btn-info mt-2")
            ])
        ], color="secondary", inverse=True, class_name="shadow-lg h-100"), lg=4, md=12, className="mb-4"),
    ], className="g-4")
], id="projects", fluid=True, className="py-5", style={"backgroundColor": "#1e1e2f"})

# --- Education Section ---
education_section = dbc.Container([
    html.H2("Education", className="text-center text-white mb-5 display-5"),
    dbc.Row([
        dbc.Col(dbc.Card([dbc.CardBody([
            html.H4("Master of Science in Data Analytics", className="card-title text-info"),
            html.P("University of Mumbai (2025 - 2027)", className="card-subtitle text-muted"),
            html.Ul([html.Li(
                "Specialization in Time Series Analysis, Machine Learning, Deep Learning, and Data Visualization. Coursework includes Regression, Statistical Methods, Data Mining, and NLP."),
                html.Li("Capstone Project: eMotion: Mood-Based Content Recommendation with Mood Shift.")],
                className="mt-3")
        ])], color="secondary", inverse=True, class_name="shadow-lg h-100"), lg=6, className="mb-4"),

        dbc.Col(dbc.Card([dbc.CardBody([
            html.H4("Bachelor of Technology in Information Technology", className="card-title text-info"),
            html.P("Bhavan's College (2019 - 2022)", className="card-subtitle text-muted"),
            html.Ul([html.Li("Specialization in Information Technology and Software Development."),
                      html.Li("Gained hands-on experience through practical projects and real-world applications.")],
                      className="mt-3")
        ])], color="secondary", inverse=True, class_name="shadow-lg h-100"), lg=6, className="mb-4"),
    ], className="g-4 justify-content-center")
], id="education", fluid=True, className="py-5", style={"backgroundColor": "#1e1e2f"})

# --- Experience Section ---
experience_section = dbc.Container([
    html.H2("Experience", className="text-center text-info mb-5 display-5"),
    dbc.Row([
        dbc.Col(dbc.Card([dbc.CardBody([
            html.H4("Senior Data Analyst", className="card-title text-info"),
            html.P("Skandha Media Services Pvt Ltd. (2023 - 2025)", className="card-subtitle text-muted mb-2"),
            html.Ul([
                html.Li("Led a team of 3 analysts, working with different sports clients using multiple tools, improving project delivery efficiency by 20%."),
                html.Li("Developed real-time dashboards using ELK Stack, Grafana, and Datadog, increasing ad compliance tracking accuracy by 95%."),
                html.Li("Automated reporting processes with Python, reducing manual effort by 40% and improving operational efficiency.")
            ], className="mt-3")
        ])], color="secondary", inverse=True, class_name="shadow-lg h-100"), lg=12, className="mb-4"),
    ], className="g-4 justify-content-center")
], id="experience", fluid=True, className="py-5", style={"backgroundColor": "#1e1e2f"})

# --- Skills Section (FINAL ADJUSTMENT) ---
skills_section = dbc.Container([
    html.H2("Skills", className="text-center text-white mb-5 display-5"),
    dbc.Row([
        # --- Technical Expertise Card (Left Box) ---
        dbc.Col(dbc.Card([dbc.CardBody([
            html.H4("Technical Expertise", className="card-title text-info fs-4 mb-3"),
            html.Div([
                dbc.Badge("Excel", color="success", className="px-3 py-1 fs-5 me-2 mb-3"),
                dbc.Badge("SQL", color="success", className="px-3 py-1 fs-5 me-2 mb-3"),
                dbc.Badge("Power BI", color="success", className="px-3 py-1 fs-5 me-2 mb-3"),
                dbc.Badge("Python (Pandas, NumPy, Matplotlib)", color="success", className="px-3 py-1 fs-5 me-2 mb-3"),
                dbc.Badge("ELK Stack (Elasticsearch, Logstash, Kibana)", color="success", className="px-3 py-1 fs-5 me-2 mb-3"),
                dbc.Badge("Linux (Ubuntu)", color="success", className="px-3 py-1 fs-5 me-2 mb-3"),
                dbc.Badge("Grafana", color="success", className="px-3 py-1 fs-5 me-2 mb-3"),
                dbc.Badge("Datadog", color="success", className="px-3 py-1 fs-5 me-2 mb-3"),
            ], className="d-flex flex-wrap")
        ])], color="secondary", inverse=True, class_name="shadow-lg"), lg=6, className="mb-4"),

        # --- Methodology & Concepts Card (Right Box) ---
        dbc.Col(dbc.Card([dbc.CardBody([
            html.H4("Methodology & Concepts", className="card-title text-info fs-4 mb-3"),
            html.Div([
                dbc.Badge("Data Analysis, Cleaning & Preprocessing", color="warning", className="px-3 py-1 fs-5 me-2 mb-3"),
                dbc.Badge("Statistical & Predictive Modeling", color="warning", className="px-3 py-1 fs-5 me-2 mb-3"),
                dbc.Badge("Machine Learning & Data Mining", color="warning", className="px-3 py-1 fs-5 me-2 mb-3"),
                dbc.Badge("Business Insights & Decision Support", color="warning", className="px-3 py-1 fs-5 me-2 mb-3"),
            ], className="d-flex flex-wrap")
        ])], color="secondary", inverse=True, class_name="shadow-lg"), lg=6, className="mb-4"),
    ], className="g-4 justify-content-center")
], id="skills", fluid=True, className="py-5", style={"backgroundColor": "#1e1e2f"})

# --- About & Contact Section (Updated Contact Details) ---
about_contact_section = dbc.Container([
    html.H2("About Me & Contact", className="text-center text-info mb-5 display-5"),
    dbc.Row([dbc.Col([
        html.H3("About Me", className="text-info mb-3"),
        html.P("Hello, I’m Rutuja More, a passionate Data Analyst with 2+ years of professional experience. During my college days, I was exploring different fields to find my true interest, and in my final year, a subject on Business Intelligence sparked my curiosity. Through practical projects and hands-on work, I discovered my passion for analyzing data and turning it into actionable insights. Since then, I have focused on building my expertise in data analytics, working on real-world projects, and understanding the critical role data plays in decision-making. Currently, I am pursuing a Master of Science in Data Analytics from Mumbai University to further enhance my skills and knowledge in the field.",
                     className="text-light fs-6 mb-4"),
        html.Hr(className="my-4 border-info"),
        html.H3("Contact", className="text-info mb-3"),
        
        # --- Contact Information ---
        html.Div([
            # Mobile Number
            html.P([
                html.Span("📱", className="me-2 text-info fs-4"),
                # VERIFIED: Correct tel: prefix.
                html.A("+91 9082913463", href="tel:+919082913463", className="text-light text-decoration-none fs-6")
            ], className="mb-2"),
            
            # Email
            html.P([
                html.Span("📧", className="me-2 text-info fs-4"),
                # VERIFIED: Correct mailto: prefix.
                html.A("rutujamore586@gmail.com", href="mailto:rutujamore586@gmail.com", className="text-light text-decoration-none fs-6")
            ], className="mb-2"),
            
            # Location
            html.P([
                html.Span("📍", className="me-2 text-info fs-4"),
                html.Span("Mumbai, Maharashtra", className="text-light fs-6")
            ], className="mb-0"),

        ], className="text-center text-md-start"),
        # --- End Contact Information ---
        
        html.P("© Rutuja More. All rights reserved.", className="text-muted mt-5 text-center")
    ], lg=8, className="mx-auto p-5 bg-secondary rounded shadow-xl")])
], id="about-contact", fluid=True, className="py-5", style={"backgroundColor": "#1e1e2f"})

# --- Layout ---
app.layout = html.Div([
    navbar,
    hero_section,
    projects_section,
    education_section,
    experience_section,
    skills_section,
    about_contact_section,
    html.Div(style={'height': '50px'})
], style={'backgroundColor': '#161b22'})

# --- Callback to toggle mobile collapse ---
@app.callback(
    Output("navbar-collapse", "is_open"),
    Input("navbar-toggler", "n_clicks"),
    State("navbar-collapse", "is_open"),
)
def toggle_navbar(n, is_open):
    if n:
        return not is_open
    return is_open

# --- Run App ---
if __name__ == '__main__':
    print("Running portfolio at http://127.0.0.1:8050")
    app.run(debug=True)