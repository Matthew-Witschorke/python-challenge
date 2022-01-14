import csv

csvpath = "Resources/budget_data.csv"

#Declaring Varbiables Needed
totalMonths = 0
totalProfit = 0
totalChange = 0
averageChange = 0
lastMonth = 867884
greatestIncrease = 0
greatestDecrease = 0


with open(csvpath, "r") as file:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(file, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        totalMonths = totalMonths + 1
        totalProfit = totalProfit + int(row[1])
        currentChange = (int(row[1]) - lastMonth)
        totalChange = totalChange + currentChange
        if currentChange > greatestIncrease:
            greatestIncrease = currentChange
            highestMonth = row[0]
            greatestProfit = currentChange
        if currentChange < greatestDecrease:
            greatestDecrease = currentChange
            lowestMonth = row[0]
            lowestProfit = currentChange
        lastMonth = int(row[1])
        lastMonthChange = currentChange
averageChange = format((totalChange/(totalMonths - 1)),".2f")

# create summary string
summary = f"""Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${totalProfit}
Average  Change: ${averageChange}
Greatest Increase in Profits: {highestMonth} (${greatestProfit})
Greatest Decrease in Profits: {lowestMonth} (${lowestProfit})
        """


with open("analysis/Finacial_Anaysis.txt", "w") as text:
    text.write(summary)