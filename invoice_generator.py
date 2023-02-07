import ast
from PIL import Image, ImageDraw, ImageFont
import random
from random import randint
from datetime import datetime, timedelta


def disclaimer_text():
    disclaimer_list = ['This receipt serves as a proof of purchase and is not a guarantee or warranty for the goods '
                       'or services rendered. The seller is not responsible for any lost or stolen receipts. The '
                       'customer assumes all responsibility for the safekeeping of the receipt.',
                       'The receipt you have received is for reference purposes only and does not constitute a '
                       'warranty or guarantee of any kind. The seller makes no representations or warranties, '
                       'expressed or implied, regarding the goods or services described on this receipt. This receipt '
                       'is non-transferable and cannot be used for returns or exchanges.']
    disclaimer = random.choice(disclaimer_list)
    leng = 51
    for i in range(1, len(disclaimer) + 1):
        if i == leng:
            disc_list = list(disclaimer)
            disc_list.insert(i, '\n')
            disclaimer = ''.join(disc_list)
            leng += 51
    # print(disclaimer)
    disclaimer_split = disclaimer.split('\n')
    return disclaimer_split


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
    INV = random.randint(1, 9898)
    inv_num = f"Invoice NO: {str(INV)}"
    left_space_ = measure_pixel(font, inv_num)
    return left_space_, inv_num, font


def random_items(random_length):
    final_data = ''
    y_axis_price = 0
    GST_RATE = 17
    items = [{"Name": "Diamond cling wrap", "Price": 132}, {"Name": "Pepsi Coke 500ml", "Price": 50},
             {"Name": "Bonus Surf Red 1kg", "Price": 350}, {"Name": "Dentist care", "Price": 70},
             {"Name": "Lays Red Chilli", "Price": 40}, {"Name": "Pepsi 250ml", "Price": 60},
             {"Name": "Spacer", "Price": 10}, {"Name": "Vinegar 150ml", "Price": 60},
             {"Name": "Everyday 30mg", "Price": 36}, {"Name": "Eclairs", "Price": 5},
             {"Name": "Tuc biscuit", "Price": 25}, {"Name": "Lolipop", "Price": 10},
             {"Name": "Dairy Milk", "Price": 100}, {"Name": "Kurkure", "Price": 5}]

    y_axis = 295
    sub_total = 0
    # random_length = random.randint(1,6)
    for num in range(random_length):
        random_quantity = [2, 1, 3]
        random.shuffle(random_quantity)
        random_qty_number = random.choice(random_quantity)
        item = items[num]
        y_axis_price = y_axis + 20
        item_gst = round((17 / 100) * (item['Price'] * random_qty_number), 2)
        total = (item['Price'] * random_qty_number) + item_gst
        file_ = open('random_item_temp.txt', 'r')
        data_ = file_.read()
        data_ = data_ % (
            y_axis, str(num + 1) + '-   ' + item['Name'], y_axis_price, item['Price'], y_axis_price, GST_RATE,
            y_axis_price, random_qty_number,
            y_axis_price, item_gst, y_axis_price, total)
        file_.close()
        final_data += data_
        sub_total += total
        y_axis += 35
    y_axis_price += 20
    final_data += """{
            "x": 10,
            "y": %s,
            "text": "_________________________________________",
            "font": "arial.ttf",
            "size": 14,
            "color": "#000000"
        },""" % (y_axis_price)
    return sub_total, final_data, y_axis_price


def cash_price_calculations(subtotal):
    sales_tax = round(0.17 * subtotal, 2)
    discount = round(0.05 * subtotal, 2)
    pos_fee = 1
    payable = round((subtotal + sales_tax + pos_fee - discount), 2)
    return [round(subtotal, 2), sales_tax, discount, pos_fee, payable]


def cash_summary(y_axis_position, sub_total):
    final_temp = ''
    x = 210
    y = y_axis_position + 30
    font_size_ = 12
    cash_ = cash_price_calculations(sub_total)
    headings = ['Total Amount:', 'Sales Tax:', 'Discount:', 'Pos fee:', ' Payable:']
    single_character_pixel = round(0.48 * font_size_)
    for i in range(len(headings)):
        word_pixels = len(headings[i]) * single_character_pixel
        amount_pixels = len(str(cash_[i])) * single_character_pixel
        starting_point = abs(x - word_pixels)
        amount_starting_point = abs(335 - amount_pixels)
        print(starting_point, word_pixels, x - starting_point)
        file_ = open('cash_summary.txt', 'r')
        data_ = file_.read()
        data_ = data_ % (starting_point, y, headings[i], amount_starting_point, y, cash_[i])
        file_.close()
        final_temp += data_
        y += 20
    final_temp += """{
                    "x": 10,
                    "y": %s,
                    "text": "_________________________________________",
                    "font": "arial.ttf",
                    "size": 14,
                    "color": "#000000"
                },""" % (y)
    return final_temp, y


def random_disclaimer(y_axis, disclaimer_split):
    final_attachment = ''
    y_axis += 20
    for text in disclaimer_split:
        attachment = """{
                    "x": 10,
                    "y": %s,
                    "text": "%s",
                    "font": "arial.ttf",
                    "size": 14,
                    "color": "#000000"
                },""" % (y_axis, text)
        final_attachment += attachment
        y_axis += 20
    return final_attachment


disclaimer_split = disclaimer_text()
receipt_required = int(input("Enter the number of receipts you want to generate: "))

for receipt in range(1, receipt_required + 1):
    random_length = random.randint(1, 10)
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
        295 + (random_length * 35) + 50 + (25 * 5) + len(disclaimer_split) * 20, str(receipt), left_space, word,
        font_size, adress_left_space,
        adress, adress_font_size, ntn_left_space, ntn, ntn_font_size,
        contact_left_space, contact, contact_font_size, pos_left_space, pos, pos_font_size,
        inv_left_space, inv, inv_font_size,
        time_left_space, date_time, time_font_size)
    sub_total, item_data, y_axis = random_items(random_length)
    print(sub_total)
    data += item_data
    cash_temp, y_ax = cash_summary(y_axis, sub_total)
    data += cash_temp
    diclaimer_template = random_disclaimer(y_ax, disclaimer_split)
    data += diclaimer_template
    last = """]}"""
    data = data + last
    data = ast.literal_eval(data)
    print(data)

    # Create an image with the specified size
    img = Image.new('RGB', (data["width"], data["height"]), color=(255, 255, 255))

    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Add the text to the image
    for element in data["elements"]:
        draw.text((element["x"], element["y"]), element["text"],
                  font=ImageFont.truetype(element["font"], element["size"]),
                  fill=element["color"])

    # Save the image
    img.save("./output_images/" + "sample_receipt_" + str(receipt) + ".jpg")
