import pdfplumber
import pandas

files = ["part1.pdf", "part2.pdf", "part3.pdf"]

parseddata = []


def parsepdf(filename):
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            for line in text.split("\n"):
                if "000" in line:
                    splitline = []
                    arr = line.split(" ", 4)
                    for i in range(3):
                        splitline.append(arr[i])
                    splitline.append(arr[4])
                    parseddata.append(splitline)
                    print(splitline)


for file in files:
    parsepdf(file)

frame = pandas.DataFrame(data=parseddata, columns=["Incident-Exp#", "Alarm Date", "Alarm Time", "Location and "
                                                                                                "Incident type"])

frame.to_csv("output.csv", index=False)
