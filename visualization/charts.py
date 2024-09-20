import plotly.graph_objects as go
def create_charts(metrics):
    fig = go.Figure()
    if metrics:
        fig.add_trace(go.Bar(x=['Commits', 'PR Merge Rate'], y=[metrics.get('commit_frequency', 0), metrics.get('pr_merge_rate', 0)]))
    else:
        fig.add_trace(go.Bar(x=['Commits', 'PR Merge Rate'], y=[0, 0])) 
    return fig
