import speedtest
import csv
from datetime import datetime
import filepath

speedtester = speedtest.Speedtest()
time = datetime.now().strftime("%b %d, %Y %H:%M")

ping = speedtester.get_best_server()["latency"]
download = round(speedtester.download()/1000000, 2)
upload  = round(speedtester.upload()/1000000, 2)
print(time)
print(f"Ping:\t\t{ping} ms")
print(f"Download:\t{download} Mbps")
print(f"Upload: \t{upload} Mbps")
with open(filepath.resultsfile, "a+") as resultsfile:
    resultswriter = csv.writer(resultsfile)
    resultswriter.writerow([time,ping, download, upload])
