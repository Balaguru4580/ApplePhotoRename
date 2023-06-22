import os
import calendar
import shutil
import re

cwd = os.getcwd()

print("RUNNING")


for foldername in sorted(os.listdir(cwd)):
    if re.match(r"\d{6}_*[a-z]*", foldername):
        year = foldername[:4]
        month = foldername[4:6]
        month_name = calendar.month_name[int(month)]
        new_foldername = f"{month_name} {year}"

        # Move the contents if the folder already exists
        if os.path.exists(new_foldername):
            for filename in os.listdir(foldername):
                source = os.path.join(foldername, filename)
                destination = os.path.join(new_foldername, filename)
                shutil.move(source, destination)
            shutil.rmtree(foldername)
        else:
            # Rename the folder
            os.rename(foldername, new_foldername)

        # Print a message to confirm the rename
        print(f"{foldername} has been renamed to {new_foldername}")
