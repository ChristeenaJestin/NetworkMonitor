import plotly.express as px


def protocol_pie(protocol_counts):

    if not protocol_counts:
        return px.pie(
            names=["No Data"],
            values=[1],
            title="Protocol Distribution"
        )

    fig = px.pie(
        names=list(protocol_counts.keys()),
        values=list(protocol_counts.values()),
        title="Protocol Distribution"
    )

    return fig


def top_ips_bar(top_ips):

    if not top_ips:

        fig = px.bar(
            x=["No Data"],
            y=[0],
            title="Top Source IPs"
        )

        return fig

    fig = px.bar(
        x=list(top_ips.keys()),
        y=list(top_ips.values()),
        labels={
            "x": "Source IP",
            "y": "Packets"
        },
        title="Top Source IPs"
    )

    return fig

def traffic_timeline_chart(df):

    import plotly.express as px

    if df.empty:

        fig = px.line(
            x=[0],
            y=[0],
            title="Traffic Timeline"
        )

        return fig

    fig = px.line(
        df,
        x="timestamp",
        y="packets",
        title="Network Traffic Timeline"
    )

    return fig