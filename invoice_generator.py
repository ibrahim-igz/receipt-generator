import ast
from PIL import Image, ImageDraw, ImageFont
import random
from datetime import datetime, timedelta


def measure_pixel(font_size, word):
    single_character_pixel = round(0.48 * font_size)
    word_pixels = len(word) * single_character_pixel
    left_starting_point = (600 - word_pixels) / 2
    return left_starting_point


def random_mart():
    font = 25
    marts = ['City Cash And Carry', 'City Mega Mart', 'City Mini']
    random.shuffle(marts)
    word_ = random.choice(marts)
    left_space_ = measure_pixel(font_size, word)
    return left_space_, font, word_


def random_date_time():
    font = 12
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 1, 31)
    random_seconds = int((end_date - start_date).total_seconds() * random.random())
    random_datetime = start_date + timedelta(seconds=random_seconds)
    formatted_datetime = random_datetime.strftime("%Y-%m-%d %I:%M:%S %p")
    split_date_time = formatted_datetime.split(' ')
    date_time_ = f'Date: {split_date_time[0]}  Time: {split_date_time[1]} {split_date_time[-1]}'
    left_space_ = measure_pixel(font_size, date_time)
    return left_space_, date_time_, font


file = open('simple.txt', 'r')
data = file.read()
left_space, font_size, word = random_mart()
time_left_space, date_time, time_font_size = random_date_time()
data = data % (left_space, word, font_size, time_left_space, date_time, time_font_size)
data = ast.literal_eval(data)
print(data)

# Create an image with the specified size
img = Image.new('RGB', (data["width"], data["height"]), color=(255, 255, 255))

# Create a drawing context
draw = ImageDraw.Draw(img)

# Add the text to the image
for element in data["elements"]:
    draw.text((element["x"], element["y"]), element["text"], font=ImageFont.truetype(element["font"], element["size"]),
              fill=element["color"])

# Save the image
img.save("simple_receipt.jpg")
