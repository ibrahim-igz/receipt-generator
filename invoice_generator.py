import ast
from PIL import Image, ImageDraw, ImageFont
import random
from random import randint
from datetime import datetime, timedelta


def measure_pixel(font_size, word):
    single_character_pixel = round(0.48 * font_size)
    word_pixels = len(word) * single_character_pixel
    left_starting_point = abs(350 - word_pixels) / 2
    return left_starting_point


def random_mart():
    font = 25
    marts = ['City Cash And Carry', 'City Mega Mart', 'City Mini']
    random.shuffle(marts)
    word_ = random.choice(marts)
    left_space_ = measure_pixel(font, word_)
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
    left_space_ = measure_pixel(font, date_time_)
    return left_space_, date_time_, font


def random_adress():
    font = 12
    addresses = ['Main hameed chowk Faisalabad', 'Susan Road Faisalabad', 'Satyana Road Faisalabad']
    random.shuffle(addresses)
    address_ = random.choice(addresses)
    left_space_ = measure_pixel(font, address_)
    return left_space_, address_, font


def random_ntn():
    font = 12
    NTN = random.randint(12345678, 56789898)
    STRN = random.randint(1234567891234, 9876543219876)
    ntn_and_strn = f"NTN: {str(NTN)[0:-1]}-{str(NTN)[-1]}  STRN: {str(STRN)}"
    left_space_ = measure_pixel(font, ntn_and_strn)
    return left_space_, ntn_and_strn, font


def random_contact():
    font = 12
    ptcl = random.randint(2345678, 6789898)
    STRN = random.randint(1234567, 3219876)
    sim_codes = ['0321-', '0333-', '0304-', '0315-', '0348-']
    random.shuffle(sim_codes)
    random_code = random.choice(sim_codes)
    contact_ = f"PHONE: 041-{str(ptcl)}  WHATSAPP: {random_code}{str(STRN)}"
    left_space_ = measure_pixel(font, contact_)
    return left_space_, contact_, font

def random_pos_num():
    font = 12
    POS = random.randint(123456, 789898)
    pos_num = f"POS NO: {str(POS)}"
    left_space_ = measure_pixel(font, pos_num)
    return left_space_, pos_num, font

def random_invoice_num():
    font = 12
    INV = random.randint(1234, 9898)
    inv_num = f"Invoice NO: {str(INV)}"
    left_space_ = measure_pixel(font, inv_num)
    return left_space_, inv_num, font

file = open('simple.txt', 'r')
data = file.read()
left_space, font_size, word = random_mart()
time_left_space, date_time, time_font_size = random_date_time()
adress_left_space, adress, adress_font_size = random_adress()
ntn_left_space, ntn, ntn_font_size = random_ntn()
contact_left_space, contact, contact_font_size = random_contact()
pos_left_space, pos, pos_font_size = random_pos_num()
inv_left_space, inv, inv_font_size = random_invoice_num()
data = data % (
    left_space, word, font_size, adress_left_space, adress, adress_font_size, ntn_left_space, ntn, ntn_font_size,
    contact_left_space, contact, contact_font_size, pos_left_space, pos, pos_font_size,
    inv_left_space, inv, inv_font_size,
    time_left_space, date_time, time_font_size)
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
