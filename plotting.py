from motion_detection import df
from bokeh.plotting import figure
from bokeh.models import HoverTool,ColumnDataSource
from bokeh.io import output_file,show
cds=ColumnDataSource(df)
p=figure(x_axis_type="datetime",title="Motion Detector")
p.yaxis.minor_tick_line_color=None
p.yaxis[0].ticker.desired_num_ticks=1
hover=HoverTool(tooltips=[("Start", "@Start{%Y-%m-%d %H:%M:%S}"),("End", "@End{%Y-%m-%d %H:%M:%S}")],formatters={"@Start" : "datetime","@End" : "datetime"})
p.add_tools(hover)
q=p.quad(left="Start",right="End",bottom=0,top=1,color='green',source=cds)
output_file("Graph.html")
show(p)
