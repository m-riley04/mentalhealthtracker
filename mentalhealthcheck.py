import mental, os
def main():
    root = os.getcwd()

    entry = mental.Entry()
    entry._root = root
    raw = entry.run_all()

    check_dirs(root=root, month=entry.month, year=entry.year)
    save(data=raw, file=create_file(entry=entry))

def check_dirs(root, month, year):
    if not os.path.exists(f"{root}/{year}"):
        os.mkdir(f"{root}/{year}")
    if not os.path.exists(f"{root}/{year}/{month}"):
        os.mkdir(f"{root}/{year}/{month}")

def create_file(entry, root=os.getcwd()):
    if not os.path.exists(f"{root}/{entry.year}/{entry.month}/{entry.day}_{entry.weekday}.txt"):
        file = open(f"{root}/{entry.year}/{entry.month}/{entry.day}_{entry.weekday}.txt", "w")
    else:
        file = open(f"{root}/{entry.year}/{entry.month}/{entry.day}_{entry.weekday}.txt", "a")
    return file

def save(data, file):
    file.write(f"\nDate: {data['weekday']} {data['month']} {data['day']}, {data['year']}\n")
    file.write(f"Time: {data['time']}\n")
    file.write(f"Rating: {data['ratings'][-1]}/10\n")
    file.write(f"Emotions:\n")
    for i in data['emotions']:
        file.write(f"\t-) {i}\n")
    file.write("\n")
    file.write(f"--Reason--\n'{data['reason']}'\n\n")
    
    file.write("----Journal----\n\n\n")
    file.write("----------------------------------------\n")

if __name__ == "__main__":
    main()