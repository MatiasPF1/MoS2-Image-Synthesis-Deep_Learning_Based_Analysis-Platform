from dash import html
import dash_bootstrap_components as dbc


navbar = html.Div(
    [
        dbc.Navbar(
            dbc.NavbarBrand(
                "MoS2-Image-Synthesis-Analysis-Platform", #Name of the Application
                className="navbar-title mx-auto"          #Center the Tittle
            ),
            className="navbar-custom shadow-sm py-3",     #Style of the Navbar
            color="light",                               
            dark=False
        ),
        html.Hr(className="navbar-separator")  # Separator line below navbar
    ]
)