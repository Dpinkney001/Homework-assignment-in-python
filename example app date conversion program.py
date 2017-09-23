#example app: date conversion

dateStr = input("Enter a date (mm/dd/yyyy): ")
monthStr, dayStr, yearStr = dateStr.split("/")

months = ["January",  "Feburary", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
monthStr = months[int(monthStr)-1]
