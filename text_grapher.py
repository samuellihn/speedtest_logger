import math

def round_to(x, base):
    return base * round(x / base)

def ceil_to(x, base):
    return base * math.ceil(x/base)
class Grapher:
    def write_graph(self, x_labels, y_numbers, title="",x_axis_label = "", y_axis_label = "",  start_at_0=False,x_ticks=10, x_scale=1, y_ticks=5, y_scale=1):

        if start_at_0:
            data_min = 0
        else:
            data_min = min(y_numbers)
        data_max = max(y_numbers)

        # round min and max to y tick scale
        data_min = round_to(data_min, y_ticks)
        data_max = round_to(data_max, y_ticks)
        data_range = data_max - data_min

        # Turns scale factor into actual multiplication factor
        y_scale = 1/y_scale

        # finds the widest y number to determine y margin width
        y_margin_width = 0
        for x in y_numbers:
            if len(str(x)) > y_margin_width:
                y_margin_width = len(str(x))
        if len(y_axis_label) > y_margin_width:
            y_margin_width = len(y_axis_label)

        y_margin_width = ceil_to(y_margin_width, 2)

        graph_width = 7 + y_margin_width + len(y_numbers)
        
        graph_string = ""
        for x in range(int(data_range / y_scale)):
            # if processed value exceeds target value, tick is applied
            target = round_to((data_max/ y_scale) - x, y_scale)
            # if target is to be put on label
            scanline = "| "
            

            if (target * y_scale) % (y_ticks * y_scale) == 0:
                scanline += str(target * y_scale).rjust(y_margin_width)
            else:
                scanline += "".rjust(y_margin_width)
            scanline += " | "
            for x in y_numbers:
                if x / y_scale > target:
                    scanline += "#"
                else:
                    scanline += " "
            scanline += " |\n"
            graph_string += scanline
        
        # print a horizontal line until the next vertical tick
        distance_until_first_tick = (2 + y_margin_width + 2 + math.floor(x_ticks/2))
        tick_line = ""
        tick_line += "|".ljust(distance_until_first_tick, "-")

        # creates vertical ticks
        for x in range(math.floor(len(y_numbers) / x_ticks)-1):
            tick_line += "|".ljust(x_ticks, "-")
            
        # finds largest x width to determine x labels
        x_label_width = 0
        for label in x_labels:
            if len(label) > x_label_width:
                x_label_width = len(label)
        
        # ends tick line
        tick_line += "|".ljust(math.ceil(x_ticks / 2) + 1, "-") + "-|\n"
        graph_string += tick_line

        
        x_label_width = ceil_to(x_label_width, x_ticks)
        x_label_lines = math.floor(x_label_width / x_ticks)

        x_label_space_req_l = math.floor((x_label_width - 1)/2)
        if x_label_space_req_l > distance_until_first_tick:
            for label in x_labels:
                label = label[0:distance_until_first_tick * 2]
        

        tick_line = tick_line[(y_margin_width + 5):]
        for line in range(x_label_lines):

            spaces = (distance_until_first_tick-1-x_label_space_req_l)
            label_line = "|".ljust(spaces + (x_ticks * line) + 1)

            index_increment = x_ticks * x_label_lines
            label_index = math.floor(x_ticks/2) + (x_ticks * line) -1
            while label_index < len(x_labels):
                label_line += x_labels[label_index].center(x_label_width)
                label_index += index_increment
            label_line = label_line.rstrip()
            if len(label_line)+1 < graph_width:
                label_line += "|".rjust(graph_width-len(label_line))

            graph_string += label_line + "\n"

        if x_axis_label != "":
            graph_string += "|" + ("-" * graph_width - 2) + "|"
            graph_string += "| "
            graph_string += title.center(graph_width - 4)
            graph_string += " |"
        graph_string += "-" * graph_width + "\n"

        # Write header block
        header_string = "-" * graph_width + "\n"
        header_string += "| " + y_axis_label.ljust(y_margin_width) + " | "
        header_string += title.center(graph_width - 7 - y_margin_width) + " |" + "\n"
        header_string += "|" + "-" * (graph_width - 2) + "|" + "\n"
        graph_string = header_string + graph_string

        return graph_string

