# AutoGit
Simple program to keep your heatmap green.<br>
This program uses Python with a package called `GitPython`.
<img src="https://github.com/Rubinskiy/AutoGit/assets/62457878/f206e44b-f570-4ed3-b9f8-a81d3a7bd590" style="transform: scale(2);">


## Step 1: Create a private dummy repo + Create a text file
Create a private dummy repository. For example, a simple repo with a text file.

## Step 2: Clone the dummy repo
Clone the repo to your desktop. Make sure that text file is there.

## Step 3: Create a virtual environment + Activate it
Create a virtual environment in the repo you cloned. Use the command `python3 -m virtualenv [name]`. Replace `[name]` with the name of your virtual environment. If the package `virtualenv` has not been found, install it using `python3 -m pip install virtualenv`. After creating the virtual environment, you should see a folder in your cloned repository folder.
Now activate your virtual environment using `[name]/scripts/activate` (if you're on Windows).

## Step 4: Install `GitPython`
Use `python3 -m pip install gitpython`. Wait until installed successfully.

## Step 5: Copy and paste the file `autogit.pyw`
Copy and paste the file `autogit.pyw` from this repo to your cloned repository folder on your desktop. You can edit the times of each commit and push for your dummy repo in the file. The default times are:
```
times = [
    "00:01",
    "09:00",
    "11:00",
    "13:00",
    "15:00",
    "17:00",
    "21:00",
    "22:00",
]
```
Edit the name of the text file you kept in the private repo by replacing line 38 from `autogit.pyw`: `file_path = "[name].txt"`.<br>
Keep in mind that <b>your machine needs to be running during this time</b> while connected to a working internet to be able to commit and push.

## Step 6: Auto-launch the program on startup
Hit `Windows Key + R` then type `shell:startup`. This should bring up your startup program folder. Create a new file in the folder called `start.bat`. Copy and paste the contents below to `start.bat`:
```
@echo off
cd /d "C:\PATH\TO\CLONED\REPO\HERE"
call venv/scripts/activate
python autogit.pyw
pause
```
Replace the text `"C:\PATH\TO\CLONED\REPO\HERE"` in line 2 to the path where your cloned repo is located on your desktop.

## Step 7: Run this program by clicking on `start.bat`
A command prompt will pop up. This is the program running, leave this window open. The next time you reboot your computer, the program will run automatically.
