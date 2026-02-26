trackings =[]

for i in range(1,5):
  tracking_no =int(input("Enter tracking number: "))
  status =input("Enter status: ")
  tracking={
    "tracking_no":tracking_no,
    "status":status
 }
  trackings.append(tracking)
  print(trackings)

add = int(input("How many data updates would you like to make :"))

for a in range(add):
    update_no = int(input("Enter the tracking number you wish to update : "))

    for tracking in trackings:

        if update_no == tracking["tracking_no"]:
         new_status =input("Enter new status: ")
         tracking["status"] = new_status
         print(tracking)
print(trackings)