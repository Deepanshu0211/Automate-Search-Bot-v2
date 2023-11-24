import tkinter as tk
from tkinter import Entry, Label, Button, StringVar
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random
from threading import Thread

class SearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Search App")

        
        self.root.geometry("400x200")
       
        
        self.root.configure(bg="#a39193")

        self.num_searches_label = Label(root, text="Enter the number of searches:", font=("Agency FB", 20, "bold"), bg="#a39193")
        self.num_searches_label.pack()

        self.num_searches_var = StringVar()
        self.num_searches_entry = Entry(root, textvariable=self.num_searches_var)
        self.num_searches_entry.pack()

        self.start_search_button = Button(root, text="Start Searches", font=("Centaur"), command=self.start_searches, bg="#4caf50", fg="white")  # Change button colors
        self.start_search_button.pack()

    def start_searches(self):
        try:
            num_searches = int(self.num_searches_var.get())
        except ValueError:
            
            print("Please enter a valid number.")
            return

        
        search_thread = Thread(target=self.perform_searches, args=(num_searches,))
        search_thread.start()

    def perform_searches(self, num_searches):
        
        options = webdriver.EdgeOptions()
      
        driver = webdriver.Edge(options=options)

        driver.get("https://www.bing.com")

        
        queries = [
    "Python programming", "Machine learning", "Web development", "Data science", "Artificial intelligence",
    "Cybersecurity", "Blockchain technology", "Cloud computing", "Internet of Things", "Natural language processing",
    "Computer vision", "Robotics", "Augmented reality", "Virtual reality", "Quantum computing",
    "Data visualization", "Big data", "Databases", "Software engineering", "Mobile app development",
    "Front-end development", "Back-end development", "Full-stack development", "DevOps", "Agile methodology",
    "Project management", "UX/UI design", "Responsive web design", "E-commerce", "Social media marketing",
    "Search engine optimization", "Content marketing", "Digital transformation", "Business intelligence",
    "Finance", "Stock market", "Cryptocurrency", "Economics", "Marketing", "Human resources",
    "Leadership", "Time management", "Mindfulness", "Productivity", "Self-improvement",
    "Travel destinations", "Culinary arts", "Photography", "Music", "Film industry",
    "Fitness", "Yoga", "Meditation", "Health and wellness", "DIY projects",
    "Gardening", "Pets", "Parenting", "Education", "Online learning",
    "Book recommendations", "Movie recommendations", "TV shows", "Video games", "Board games",
    "Sports", "Outdoor activities", "Camping", "Hiking", "Fashion trends",
    "Beauty tips", "Skincare", "Home decor", "Interior design", "Sustainable living",
    "Environmental issues", "Climate change", "Renewable energy", "Space exploration", "Astronomy",
    "History", "Ancient civilizations", "Archaeology", "Philosophy", "Psychology",
    "Mind-bending puzzles", "Brain teasers", "Riddles", "Travel hacks", "Budget travel",
    "Language learning", "Cultural diversity", "Volunteering", "Social issues", "Community service",
    "Random trivia", "Fun facts", "Jokes", "Humor", "Inspirational quotes",
    "Motivational speeches", "TED talks", "Podcasts", "Online communities", "Internet memes",
    "Artificial flowers", "Unicorn sightings", "Waldo's location", "Meaning of life", "The Matrix",
    "Is the cake a lie?", "42", "To be or not to be", "Pi to a million places", "Recursion",
    "This statement is false", "Color of the dress", "Yanny or Laurel", "Mandela Effect", "Parallel universes",
    "Time travel", "Aliens", "UFO sightings", "Conspiracy theories", "Secret societies"
]

       
        for _ in range(num_searches):
            
            query = random.choice(queries)

            
            search_box = driver.find_element("name", "q")
            search_box.clear()  
            self.simulate_typing(search_box, query)

            
            search_box.send_keys(Keys.RETURN)

            
            time.sleep(random.uniform(3, 6))  

        
        driver.quit()

    def simulate_typing(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(0.1 * (1 + ord(char) % 3))  

if __name__ == "__main__":
    root = tk.Tk()
    app = SearchApp(root)
    root.mainloop()
