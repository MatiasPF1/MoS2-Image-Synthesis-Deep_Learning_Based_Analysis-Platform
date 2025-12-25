from dash import html, dcc


########################################################################################################################
#                                    File Input Panel Component 
#########################################################################################################################


def file_input_panel():
    return html.Div(
        [
            html.H4("Input Files", className="section-title"),
            html.P("Select XYZ, Parameter and Batch files for STEM generation", className="section-subtitle"),
            html.Div(
                [
                    # XYZ File Input
                    html.Div(
                        [
                            html.Label("XYZ File"),
                            dcc.Upload(
                                id="xyz-file-upload",
                                children=html.Div([
                                    html.I(className="fas fa-cloud-upload-alt", style={"marginRight": "8px"}),
                                    "Drag & Drop or Click to Select"
                                ]),
                                className="file-upload-box", # CSS class for styling
                                multiple=False # Single file upload
                            ),
                            html.Div(id="xyz-file-name", className="file-name-display")
                        ],
                        className="file-input-group" 
                    ),

                    # Params File Input
                    html.Div(
                        [
                            html.Label("Params File"),
                            dcc.Upload(
                                id="params-file-upload",
                                children=html.Div([
                                    html.I(className="fas fa-cloud-upload-alt", style={"marginRight": "8px"}),
                                    "Drag & Drop or Click to Select"
                                ]),
                                className="file-upload-box", # CSS class for styling
                                multiple=False # Single file upload
                            ),
                            html.Div(id="params-file-name", className="file-name-display")
                        ],
                        className="file-input-group"
                    ),
                    
                    
                    # Batch Input
                    html.Div(
                        [
                            html.Label("Batch File (.bat)"),
                            dcc.Upload(
                                id="batch-file-upload",
                                children=html.Div([
                                    html.I(className="fas fa-cloud-upload-alt", style={"marginRight": "8px"}),
                                    "Drag & Drop or Click to Select"
                                ]),
                                className="file-upload-box", # CSS class for styling
                                multiple=False # Single file upload
                            ),
                            html.Div(id="batch-file-name", className="file-name-display")
                        ],
                        className="file-input-group"
                    ),
                    
                    # Generate STEM Button
                    html.Div(
                        [
                            html.Button(
                                [
                                    html.I(className="fas fa-play", style={"marginRight": "8px"}),
                                    "Generate STEM Images"
                                ],
                                id="generate-stem-btn",
                                className="generate-btn",
                                n_clicks=0
                            )
                        ],
                        className="button-container",
                        style={"marginTop": "5px"}
                    ),
                    
                ],
                className="file-inputs-container"
            )
        ],
        id="file-input-panel",
        className="material-panel"
    )
