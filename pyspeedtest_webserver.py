import csv
import web
from text_grapher import Grapher

def construct_table():

    result = ""
    result += "--------------------------------------------------------------------------\n"
    result += "| Date and Time            | Ping        | Download      | Upload        |\n"
    result += "|------------------------------------------------------------------------|\n"
    
    with open("speedtestresults.csv", "r") as resultsfile:
        resultsreader = csv.reader(resultsfile)
        for row in resultsreader:
            result += f"| {row[0].ljust(24)} | {row[1].rjust(8)} ms | {row[2].rjust(8)} Mb/s | {row[3].rjust(8)} Mb/s |\n"

    result += "--------------------------------------------------------------------------\n"

    return result

def construct_graph(x_index, y_index, title = "", y_axis_label=""):

        data_array = []
        with open("speedtestresults.csv", "r") as resultsfile:
            resultsreader = csv.reader(resultsfile)
            for row in resultsreader:
                data_array.append(row)
            data_array = data_array[-60:]
            while len(data_array) < 60:
                data_array.insert(0, ["N/A", 0, 0, 0])

        x_array = []
        y_array = []

        for row in data_array:
            x_array.append(row[x_index])
            y_array.append(float(row[y_index]))
        
        grapher = Grapher()
        return grapher.write_graph(x_array, y_array, title=title, y_axis_label=y_axis_label)



class InternetSpeedResults:
    def GET(self):

        result = construct_table()
        result += construct_graph(0, 1,title="Ping", y_axis_label = "Ping (ms)")
        result += construct_graph(0, 2,title="Download", y_axis_label = "Mbps")
        result += construct_graph(0, 3,title="Upload", y_axis_label = "Mbps")

        return result

if __name__ == "__main__":

    urls = (
        "/speedtest", "InternetSpeedResults"
    )
    app = web.application(urls, globals())
    app.run()
