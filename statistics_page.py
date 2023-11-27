import pygame
import matplotlib.pyplot as plt
import os
from datetime import datetime


class StatisticsPage:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = pygame.display.get_surface().get_size()
        self.data = []  # List to store date-based data
        self.dates = []  # List to store dates


        # Load data from a text file
        self.load_data()


    def load_data(self):
        date_value_pairs = []  # List to store tuples of dates and values
        if os.path.exists("data.txt"):
            with open("data.txt", "r") as file:
                for line in file:
                    try:
                        date, value = line.strip().split(",")
                        date = datetime.today().strftime("%m-%Y")
                        date_value_pairs.append((date, float(value)))
                    except ValueError as e:
                        print(f"Error loading data: {e}. Line: {line}")


        # Unpack date_value_pairs into separate lists
        dates, data = zip(*date_value_pairs)


        # Ensure that dates and data are lists
        self.dates = list(dates)
        self.data = list(data)



    def save_data(self, date, value):
        self.dates.append(date)
        self.data.append(value)
        with open("data.txt", "a") as file:
            file.write(f"{date},{value}\n")
        


    def draw_statistics(self):
        # Example line graph code
        plt.figure(figsize=(2.75, 5))
        plt.plot(self.dates, self.data, marker='o', linestyle='-')
        plt.xlabel("Date")
        plt.ylabel("Percent Accuracy")
        plt.title("Percent Accuracy Over Time")
        plt.grid()


        # Save the graph as an image
        plt.savefig("data_history_graph.png")


        # Display the graph on the screen
        graph_image = pygame.image.load("data_history_graph.png")
        self.screen.blit(graph_image, (50, 100))


        pygame.display.update()
