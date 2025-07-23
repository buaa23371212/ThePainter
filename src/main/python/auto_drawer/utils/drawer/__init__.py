from .circle_drawer import select_circle_tool, draw_circle_command
from .ellipse_drawer import select_ellipse_tool, draw_ellipse_command
from .square_drawer import select_square_tool, draw_square_command
from .rectangle_drawer import select_rectangle_tool, draw_rectangle_command
from .polygon_drawer import select_polygon_tool, draw_polygon_command
from .line_drawer import select_line_tool, draw_line_command
from .polyline_drawer import select_polyline_tool, draw_polyline_command
from .curve_drawer import select_curve_tool, draw_curve_command
from .multicurve_drawer import select_multicurve_tool, draw_multicurve_command
from .rounded_rectangle_drawer import select_rounded_rectangle_tool, draw_rounded_rectangle_command

SHAPE_COMMANDS = {
    'circle': (select_circle_tool, draw_circle_command),
    'ellipse': (select_ellipse_tool, draw_ellipse_command),
    'square': (select_square_tool, draw_square_command),
    'rectangle': (select_rectangle_tool, draw_rectangle_command),
    'rounded_rectangle': (select_rounded_rectangle_tool, draw_rounded_rectangle_command),
    'polygon': (select_polygon_tool, draw_polygon_command),
    'line': (select_line_tool, draw_line_command),
    'polyline':(select_polyline_tool, draw_polyline_command),
    'curve': (select_curve_tool, draw_curve_command),
    'multicurve': (select_multicurve_tool, draw_multicurve_command)
}