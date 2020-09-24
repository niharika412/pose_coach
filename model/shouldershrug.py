import dash
import datetime
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import cv2
from dash.dependencies import Input, Output, State
from app import app
import numpy as np
import base64 
from pose import *

path='D:/pose_coach/model/assets/'
l=['No image selected']
layout=html.Div([
    html.Div(id='output213'),
    dbc.Button("Submit", outline=False,id='a',n_clicks_timestamp=0,color="warning",block=True),
    ])


fee=['']

def parse_contents(contents, filename, date):
    imgdata = base64.b64decode(contents)
    with open(path+filename, 'wb') as f:
        f.write(imgdata)
    l.append(filename)
    x=imgkeypoints(path+filename)
    fee.append(x)
    return html.Div([

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        html.Img(src=contents,style={'height':'22rem', 'width':'22rem',"bottom": 2})

    ])




@app.callback(Output('output-image-upload1', 'children'),
              [Input('upload-image', 'contents')],
              [State('upload-image', 'filename'),
               State('upload-image', 'last_modified')])


def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
    else:
        return html.Img(src='https://github.com/niharika412/pose_coach/blob/master/images/valentine-scrapbooking-4708008_1920.jpg?raw=true', style={'height':'22rem', 'width':'22rem',"bottom": 2})


@app.callback(
    Output('output213', 'children'),
    [Input('a', 'n_clicks_timestamp')])

def click(a):
    if a>0:
        #print(l)
        x=fee[-1]
        listx=list(x.split('.'))
        #print(x)
        return html.Div([
        dbc.Row(
        [
           dbc.Col(dbc.Button(html.Img(src=app.get_asset_url('shouldershrugo.jpg'), style={'height':'22rem', 'width':'22rem',"bottom": 2}), color="light",id="warriorwew2", className="m-1",n_clicks_timestamp=1),width=5),
            dbc.Col(dbc.Button(html.Img(src=app.get_asset_url(l[-1].replace(".jpg","o.jpg")), style={'height':'22rem', 'width':'22rem',"bottom": 2}), color="light",id="warrior2d", className="m-1",n_clicks_timestamp=1),width=5),    ],
        justify='center'),
        dbc.Row(
                [
                    dbc.Col(html.Div("Instructor's Keypoints"), width=5),
                    dbc.Col(html.Div("Your Keypoints"), width=5),
                ],
                justify="center",
            ),
        dbc.Alert([
            html.Hr(),
            html.H4(x),
            html.Hr()],color="info")
        ])
    else:
        return [dbc.Row(
    [
        dbc.Col(dbc.Button(html.Img(src='https://github.com/niharika412/pose_coach/blob/master/images/shouldershrug.jpg?raw=true', style={'height':'22rem', 'width':'22rem',"bottom": 2}), color="light",id="warrior2", className="m-1",n_clicks_timestamp=1),width=5),
        dbc.Col(dbc.Button(id="output-image-upload1" ,color="light", className="m-1"),width=5),
    ],
    justify='center'),
    dbc.Row(
            [
                dbc.Col(html.Div("Instructor's Image"), width=5),
                dbc.Col(html.Div("Your Image"), width=5),
            ],
            justify="center",
        ),
     dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'background-color':'blue',
            'color': 'white'
        },
        # Allow multiple files to be upload-ed
        multiple=True
    )]