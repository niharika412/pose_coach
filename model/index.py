import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from app import app
import anal
import shouldershrug
import goddess
from dash.dependencies import Input, Output, State
import dash


content_style={
'background-color':'#f1d3ae',
'color':'#221f1f',
'margin':'15px'
}
nav_item = dbc.NavItem(dbc.NavLink("Link", href="https://github.com/niharika412/pose_coach"))

dropdown = dbc.DropdownMenu(
	children=[
	dbc.DropdownMenuItem("Help"),
	dbc.DropdownMenuItem(divider=True),
	],
	nav=True,
	in_navbar=True,
	label="Menu",
	)

logo = dbc.Navbar(
	dbc.Container(
		[
		html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                	[
                	dbc.Col(html.Img(src='https://github.com/niharika412/pose_coach/blob/master/logo2.png?raw=true', height="100px")),
                	dbc.Col(dbc.NavbarBrand("Analyse", className="ml-2")),
                	],
                	align="center",
                	no_gutters=True,
                	),
                href="/",
                ),
		dbc.NavbarToggler(id="navbar-toggler2"),
		dbc.Collapse(
			dbc.Nav(
				[nav_item, dropdown], className="ml-auto", navbar=True
				),
			id="navbar-collapse2",
			navbar=True,
			),
		]
		),
	color="dark",
	dark=True,
	className="mb-5",
	)

content=html.Div([
	html.Div('Click on a pose for analysis:'),

	html.Hr(),
	dbc.Row(
		[
		dbc.Col(dcc.Link(dbc.Button(html.Img(src='https://github.com/niharika412/pose_coach/blob/master/images/PhotoGrid_Plus_1599472504043.png?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}), color="light",id="warrior2", className="m-1",n_clicks_timestamp=1 ),href='/analyse'),width=2),
		dbc.Col(dcc.Link(dbc.Button(html.Img(src='https://github.com/niharika412/pose_coach/blob/master/images/PhotoGrid_Plus_1599472556491.png?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}), color="light",id="shouldershrug", className="m-1",n_clicks_timestamp=1),href='/shouldershrug'),width=2),
		dbc.Col(dcc.Link(dbc.Button(html.Img(src='https://github.com/niharika412/pose_coach/blob/master/images/PhotoGrid_Plus_1599472446409.png?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}), color="light",id="goddess", className="m-1",n_clicks_timestamp=1),href='/goddess'),width=2),
		],
		justify='center',
		),
	dbc.Row(
		[
		dbc.Col(html.Div("Warrior 2 Pose"), width=2),
		dbc.Col(html.Div("Shoulder Shrug"), width=2),
		dbc.Col(html.Div("Goddess Pose"), width=2),
		],
		justify="center",
		),
	html.Hr(),
	dbc.Row(
		dbc.Col(
			html.Div("more to come..."),
			width={"size": 6, "offset": 5},
			)
		),
	])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])



def display_page(pathname):
    if pathname == '/analyse':
        return anal.layout
    elif pathname == '/shouldershrug':
    	return shouldershrug.layout
    elif pathname == '/goddess':
    	return goddess.layout
    else:
        return content

app.layout= html.Div([
	logo, 
	dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')])


if __name__ == '__main__':
	app.run_server(debug=True)
