import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px


DATA_FILE = "data/formatted_output.csv"


# Load formatted sales data
df = pd.read_csv(DATA_FILE)

# Convert Date column to datetime and sort
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Aggregate total sales per day
daily_sales = df.groupby("Date", as_index=False)["Sales"].sum()

# Create line chart
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)


app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Soul Foods Pink Morsel Sales Visualiser"),

        dcc.Graph(
            id="sales-line-chart",
            figure=fig
        )
    ]
)


if __name__ == "__main__":
    app.run(debug=True)