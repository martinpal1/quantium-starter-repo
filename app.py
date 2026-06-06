import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px


DATA_FILE = "data/formatted_output.csv"

df = pd.read_csv(DATA_FILE)

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

app = Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#fff5f8",
        "padding": "40px",
        "minHeight": "100vh",
    },
    children=[
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "30px",
                "borderRadius": "16px",
                "boxShadow": "0 4px 18px rgba(0, 0, 0, 0.12)",
                "maxWidth": "1100px",
                "margin": "0 auto",
            },
            children=[
                html.H1(
                    "Soul Foods Pink Morsel Sales Visualiser",
                    style={
                        "textAlign": "center",
                        "color": "#c2185b",
                        "marginBottom": "10px",
                    },
                ),


                html.Div(
                    children=[
                        html.Label(
                            "Filter by region:",
                            style={
                                "fontWeight": "bold",
                                "marginRight": "20px",
                                "fontSize": "16px",
                                "color": "#333",
                            },
                        ),

                        dcc.RadioItems(
                            id="region-filter",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                            ],
                            value="all",
                            inline=True,
                            style={
                                "display": "inline-block",
                                "fontSize": "16px",
                                "color": "#333",
                            },
                            labelStyle={
                                "marginRight": "20px",
                                "cursor": "pointer",
                            },
                        ),
                    ],
                    style={
                        "textAlign": "center",
                        "marginBottom": "30px",
                    },
                ),

                dcc.Graph(
                    id="sales-line-chart",
                    style={
                        "borderRadius": "12px",
                        "overflow": "hidden",
                    },
                ),
            ],
        )
    ],
)


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df.copy()
        chart_title = "Pink Morsel Sales Across All Regions"
    else:
        filtered_df = df[df["Region"] == selected_region]
        chart_title = f"Pink Morsel Sales in the {selected_region.title()} Region"

    daily_sales = filtered_df.groupby("Date", as_index=False)["Sales"].sum()

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=chart_title,
        labels={
            "Date": "Date",
            "Sales": "Total Sales",
        },
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title={
            "x": 0.5,
            "xanchor": "center",
        },
        font={
            "family": "Arial, sans-serif",
            "size": 14,
            "color": "#333",
        },
        xaxis_title="Date",
        yaxis_title="Total Sales",
        hovermode="x unified",
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)