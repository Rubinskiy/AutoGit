import os
import datetime
import git
from git import Repo
import time

# Init
current_date = datetime.datetime.now().strftime("%m/%d/%y %H:%M")
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

def commit_and_push(file_path, date_str):
    with open(file_path, "w") as file:
        file.write(date_str)

    repo = Repo(os.getcwd())
    repo.index.add([file_path])
    repo.index.commit(current_date)
    origin = repo.remote(name='origin')
    origin.push()

def is_time_to_commit():
    now = datetime.datetime.now()
    if now.strftime("%H:%M") in times:
        return True
    else:
        return False

def main():
    file_path = "green.txt"
    print("Waiting for the time to commit..")
    while True:
        if is_time_to_commit():
            commit_and_push(file_path, current_date)
            print("New commit pushed to remote, time of commit: " + str(datetime.datetime.now()))
            while is_time_to_commit():
                time.sleep(1)
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()
