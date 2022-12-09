#mental.py
import datetime, os, json, ast

class Entry:
    def __init__(self):
        self.date = datetime.date.today()
        self.day = str(datetime.date.today()).split("-")[2]
        self.month = str(datetime.datetime.now().strftime("%B"))
        self.monthNum = str(datetime.date.today()).split("-")[1]
        self.year = str(datetime.date.today()).split("-")[0]
        self.weekday = str(datetime.datetime.now().strftime("%A"))
        self.time = str(datetime.datetime.now().strftime("%H-%M-%S"))
        self._root = ""
        self.ratings = []
        self.averageRating = 5
        self.emotions = set()
        self.reason = ""

    def get_ratings(self):
        try:
            print("What would you rate the day on a scale of 0-10? (bad <---> good)")
            rating = int(input(">> "))
            self.ratings.append(rating)
        except:
            self.get_ratings()
        print(f"Ratings: {self.ratings}")
        return self.ratings
    
    def get_average_rating(self):
        return round(sum(self.ratings)/len(self.ratings), 1)
            
    def get_emotion(self):
        userInput = ""
        emotionsDict = {1: "overjoyed", 2: "happy", 3: "energized", 4: "focused", 5: "optimistic", 6: "confident", 7: "love", 8: "content", 9: "neutral", 10: "empty", 
                        11: "heavy", 12: "lonely", 13: "sad", 14: "anxious", 15: "stressed", 16: "overwhelmed", 17: "shy", 18: "unconfident", 19: "unsure", 
                        20: "embarrassed", 21: "anger", 22: "annoyance", 23: "disgust", 24: "lustful", 25: "creative", 26: "tired"}
        print("--What are your primary emotions?--")
        for key, value in emotionsDict.items():
            print(f"{key}) {value}")
        print("--(0 to exit)--")
        while userInput != 0:
            try: 
                userInput = int(input(">> "))
                self.emotions.add(emotionsDict[userInput])
            except:
                pass
        print(f"Emotions: {self.emotions}")
        return self.emotions

    def get_reason(self):
        print("Is there a specific reason? (if not, just hit enter)")
        self.reason = input(">> ")
        if not self.reason:
            self.reason == "N/A"

        return self.reason

    def check_for_data(self):
        if not os.path.exists(f"{self._root}/raw_data/{self.date}.data"):
            return
        else:
            file = open(f"{self._root}/raw_data/{self.date}.data", "r").read()
            fileData = ast.literal_eval(file)

            self.ratings = fileData['ratings']

    def run_all(self):
        self.check_for_data()
        data = {

            'day': self.day,
            'month': self.month,
            'monthNum': self.monthNum,
            'year': self.year,
            'weekday': self.weekday,
            'time': self.time,
            'ratings': self.get_ratings(),
            'average rating': self.get_average_rating(),
            'emotions': self.get_emotion(),
            'reason': self.get_reason()

        }
        self.save_data(raw=data)
        return data

    def save_data(self, raw):
        if not os.path.exists(f"{self._root}/raw_data"):
            os.mkdir(f"{self._root}/raw_data")
        file = open(f"{self._root}/raw_data/{self.date}.data", "w")
        file.write(str(raw))
        file.close()