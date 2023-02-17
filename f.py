from flask import Flask, request, render_template, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        title = request.form['title']
        choice = request.form['choice']
        option1 = request.form.get('option1')
        image = generate_image(text,title,option1,choice)
        return send_file(image, mimetype='image/png')
    else:
        return render_template('index.html')

def generate_image(text,title,option1,choice):
    # # Set up the image
    # font = ImageFont.truetype('segoeui.ttf', size=14)
    # lines = text.split('\n')
    # line_height = font.getsize(lines[0])[1]
    ###width = 640
    ###height = 480
    ###img = Image.new('RGB', (width, height), color='#0c0c0d')

    # # Draw the text
    ####draw = ImageDraw.Draw(img)
    # y = 480
    # for line in lines:
    #     w, h = draw.textsize(line, font=font)
    #     x = (width - w) / 2
    #     draw.text((x, y), line, font=font, fill=(0, 0, 0))
    #     y += line_height
    font = ImageFont.truetype('consola.ttf', size=14)
    font_title = ImageFont.truetype('segoeui.ttf', size=12,)
    #---------------------------------------------------------------
    if choice == "large_img":
        bg_img = Image.open('cmd_bg.jpg')
    else:
        bg_img = Image.open('cmd_bg2.jpg')

    img = Image.new('RGB', bg_img.size, color='white')
    img.paste(bg_img)
    draw = ImageDraw.Draw(img)
    #title = r"MY Title"
    # text = r""" hlo sir g
    # """
    text_width, text_height = draw.textsize(text, font)
    title_width, title_height = draw.textsize(title, font_title)
    text_x = 5
    text_y = 40
    title_x = 30
    title_y = 7
    line_height = font.getsize(' ')[1] + 5
    # draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))
    for i, line in enumerate(text.split('\n')):
        draw.text((text_x, text_y + i*line_height), line, font=font, fill=(255, 255, 255))
    draw.text((title_x, title_y), title, font=font_title, fill=(0, 0, 0))
    lat_op = """
the end"""
    if option1 == "True":
        draw.text((text_x, text_y + i*line_height), lat_op, font=font, fill=(255, 255, 255))
        

    #-------------------------------------------------
    # Save the image to a byte buffer
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    return buffer

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
