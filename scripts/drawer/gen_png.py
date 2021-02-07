from scripts.drawer.config import *
from scripts.constants import *
import math
from PIL import Image, ImageDraw, ImageFont
import os


def adjust_ratio(values):
    sep_values = [[]]
    sep_i = 0
    for v in values:
        if v[0] != SEPARATOR:
            sep_values[sep_i].append(v)
        else:
            sep_i += 1
            sep_values.append([])

    sum_height = 0
    for value in sep_values:
        height = 0
        for variant, *v in value:
            if variant in SINGLE or SMALL in v:
                height += 1 / 3
            else:
                height += 2 / 3
        height += 1 / 3
        sum_height += math.ceil(height)

    return sum_height


class NodePNG:
    def __init__(self, **kwargs):

        self.inputs = kwargs.get("inputs", tuple())
        self.separated_inputs = []

        self.outputs = kwargs.get("outputs", tuple())
        self.separated_outputs = []

        self.desc = kwargs.get("desc", None)
        self.user_symbol = kwargs.get("user_symbol", None)

        self.ratio = (kwargs.get("width", 1), max(adjust_ratio(self.inputs), adjust_ratio(self.outputs)))
        if self.desc:
            self.ratio = (self.ratio[0], max(2, self.ratio[1]))

        self.label = kwargs.get("label", None)
        self.time = kwargs.get("time", None)
        self.inner = kwargs.get("inner", None)

        self.inputs_label = kwargs.get("inputs_label", ())
        self.outputs_label = kwargs.get("outputs_label", ())

        self.icon = kwargs.get("icon", None)

        self.bg_color = kwargs.get("bg_color", (0, 0, 0, 0))
        self.border_color = kwargs.get("border_color", (0, 0, 0))
        self.inputs_color = kwargs.get("inputs_color", ())
        self.outputs_color = kwargs.get("outputs_color", ())
        self.auto_inputs_color = kwargs.get("auto_inputs_color", True)
        self.auto_outputs_color = kwargs.get("auto_outputs_color", True)

        self.border_width = kwargs.get("border_width", 10)

        self.label_size = kwargs.get("label_size", 40)
        self.time_size = kwargs.get("description_size", 30)
        self.inner_size = kwargs.get("inner_size", 60)

    def draw_node(self):

        size = self.ratio[0] * 900, self.ratio[1] * 900
        img = Image.new("RGBA", size, self.bg_color)
        draw = ImageDraw.Draw(img)

        inputs_label_centers = self.draw_connectors(draw, self.inputs, True)
        outputs_label_centers = self.draw_connectors(draw, self.outputs, False)

        draw.rectangle((0, 0, size[0] - 1, size[1] - 1), outline=self.border_color, width=self.border_width)

        resize_size = self.ratio[0] * 300, self.ratio[1] * 300
        img = img.resize(resize_size, Image.LANCZOS)
        img2 = Image.new("RGBA", (600 + resize_size[0], 600 + resize_size[1]), "white")

        delta = ((img2.size[0] - resize_size[0]) // 2, (img2.size[1] - resize_size[1]) // 2)

        img2.paste(img, delta, img)
        draw = ImageDraw.Draw(img2)

        font_path = ".\\resources\\fonts\\courier.ttf"
        font = ImageFont.truetype(font_path, 40)

        for i, center in enumerate(inputs_label_centers):
            if not center:
                continue
            if i < len(self.inputs_label) and self.inputs_label[i]:
                draw.text((50 + (delta[0] - 100) / 2 - draw.textsize(self.inputs_label[i], font=font)[0] / 2,
                           delta[1] + center * 300 - (font.size + 5)), self.inputs_label[i], fill="black", font=font)
            draw.line((50, delta[1] + center * 300,
                       delta[0] - 50, delta[1] + center * 300),
                      fill=self.border_color, width=self.border_width // 3)

        for i, center in enumerate(outputs_label_centers):
            if not center:
                continue
            if i < len(self.outputs_label) and self.outputs_label[i]:
                draw.text((self.ratio[0] * 300 + delta[0] + 50 + (delta[0] - 100) / 2 -
                           draw.textsize(self.outputs_label[i], font=font)[0] / 2,
                           delta[1] + center * 300 - (font.size + 5)), self.outputs_label[i], fill="black", font=font)
            draw.line((self.ratio[0] * 300 + delta[0] + 50, delta[1] + center * 300,
                       self.ratio[0] * 300 + delta[0] + delta[0] - 50, delta[1] + center * 300),
                      fill=self.border_color, width=self.border_width // 3)

        if self.label:
            font = ImageFont.truetype(font_path, self.label_size)
            pos = (img2.size[0] / 2 - draw.textsize(self.label + " node", font=font)[0] / 2, delta[1] - (font.size + 5))
            draw.text(pos, self.label + " node", fill="black", font=font)

        if self.inner:
            font = ImageFont.truetype(font_path, self.inner_size)
            while draw.textsize(self.inner, font=font)[0] > 200:
                self.inner_size -= 1
                font = ImageFont.truetype(font_path, self.inner_size)
            inner_text_size = draw.textsize(self.inner, font=font)
            split_text = self.inner.split("\n")
            row_count = len(split_text)
            y_pos_start = inner_text_size[1]
            for it, text in enumerate(split_text):
                y_pos = y_pos_start - it * (inner_text_size[1] / row_count) * 2
                pos = (delta[0] - draw.textsize(text, font=font)[0] / 2 + 150,
                       delta[1] - y_pos / 2 + 150 - 8)
                draw.text(pos, text, fill="black", font=font)

        if self.time:
            font = ImageFont.truetype(font_path, self.time_size)
            pos = (delta[0] - draw.textsize(self.time, font=font)[0] + self.ratio[0] * 300 - 8,
                   delta[1] - draw.textsize(self.time, font=font)[1] + self.ratio[1] * 300 - 8)
            draw.text(pos, self.time, fill="black", font=font)

        if self.user_symbol:
            font = ImageFont.truetype(font_path, self.time_size)
            pos = (delta[0] - draw.textsize(self.user_symbol, font=font)[0] + self.ratio[0] * 300 - 8,
                   delta[1] + 8)
            draw.text(pos, self.user_symbol, fill="black", font=font)

        file_name = self.label

        path = "./resources/generated/png/"
        try:
            os.makedirs(path)
        except FileExistsError:
            pass

        # if icon:
        #     img2.crop((delta[0], delta[1],
        #                delta[0]+self.ratio[0]*300-1, delta[1]+self.ratio[1]*300-1)) \
        #         .save(f".\\resources\\nodes\\icons\\{file_name}.png")

        img2.save(path + f"{file_name}.png")
        del draw
        del img
        del img2

    def draw_connectors(self, draw, inout, orientation):
        label_centers = []
        size = self.ratio[0] * 900, self.ratio[1] * 900
        r = 1 / 6
        if len(inout):
            sep_connectors = [[]]
            sep_i = 0
            for value in inout:
                if value[0] != SEPARATOR:
                    sep_connectors[sep_i].append(value)
                else:
                    sep_i += 1
                    sep_connectors.append([])

            last_height = 0
            actual_counter = 0
            for value in sep_connectors:
                height = 0
                for variant, *v in value:
                    if variant in SINGLE or SMALL in v:
                        height += 1 / 3
                    else:
                        height += 2 / 3
                height += 1 / 3
                offset = (math.ceil(height) - height) / 2
                height = last_height
                for v in value:
                    variant = v[0]
                    con_type = None
                    other = v[1:]
                    if len(v) > 1:
                        con_type = v[1]
                        other = v[2:]
                        if con_type not in colors:
                            other = v[1:]
                            con_type = None
                    height += 1 / 3
                    if con_type:
                        color = "#%02x%02x%02x" % colors[con_type]
                    else:
                        color = "#%02x%02x%02x" % colors["any"]
                    if (variant == SINGLE and con_type not in ROUND) or variant == MULTIPLE:
                        if variant == SINGLE:
                            if orientation:
                                points = ((0, (offset + height - r) * 900),
                                          (r * 900, (offset + height) * 900),
                                          (0, (offset + height + r) * 900),
                                          (0, (offset + height - r) * 900))
                            else:
                                points = ((size[0], (offset + height - r) * 900),
                                          (size[0] - r * 900, (offset + height) * 900),
                                          (size[0], (offset + height + r) * 900),
                                          (size[0], (offset + height - r) * 900))
                        else:
                            if SMALL in other:
                                if DIRECTED in other:
                                    if orientation:
                                        points = ((0, (offset + height - r) * 900),
                                                  (r * 900, (offset + height + r) * 900),
                                                  (0, (offset + height + r) * 900),
                                                  (0, (offset + height - r) * 900))
                                    else:
                                        points = ((size[0], (offset + height - r) * 900),
                                                  (size[0] - r * 900, (offset + height + r) * 900),
                                                  (size[0], (offset + height + r) * 900),
                                                  (size[0], (offset + height - r) * 900))
                                else:
                                    if orientation:
                                        points = ((0, (offset + height - r) * 900),
                                                  (r * 900, (offset + height - r) * 900),
                                                  (r * 900, (offset + height + r) * 900),
                                                  (0, (offset + height + r) * 900),
                                                  (0, (offset + height - r) * 900))
                                    else:
                                        points = ((size[0], (offset + height - r) * 900),
                                                  (size[0] - r * 900, (offset + height - r) * 900),
                                                  (size[0] - r * 900, (offset + height + r) * 900),
                                                  (size[0], (offset + height + r) * 900),
                                                  (size[0], (offset + height - r) * 900))
                            else:
                                if DIRECTED in other:
                                    if orientation:
                                        points = ((0, (offset + height - r) * 900),
                                                  (r * 900, (offset + height - r) * 900),
                                                  (r * 900, (offset + height + 3 * r) * 900),
                                                  (0, (offset + height + 3 * r) * 900),
                                                  (0, (offset + height - r) * 900))
                                    else:
                                        points = ((size[0], (offset + height - r) * 900),
                                                  (size[0] - r * 900, (offset + height - r) * 900),
                                                  (size[0] - r * 900, (offset + height + 3 * r) * 900),
                                                  (size[0], (offset + height + 3 * r) * 900),
                                                  (size[0], (offset + height - r) * 900))
                                else:
                                    if orientation:
                                        points = ((0, (offset + height - r) * 900),
                                                  (r * 900, (offset + height + 3 * r) * 900),
                                                  (0, (offset + height + 3 * r) * 900),
                                                  (0, (offset + height - r) * 900))
                                    else:
                                        points = ((size[0], (offset + height - r) * 900),
                                                  (size[0] - r * 900, (offset + height + 3 * r) * 900),
                                                  (size[0], (offset + height + 3 * r) * 900),
                                                  (size[0], (offset + height - r) * 900))

                        draw.polygon(points, fill=color)
                        draw.line(points, fill=self.border_color, width=self.border_width)
                        for point in points:
                            draw.ellipse((point[0] - self.border_width / 2, point[1] - self.border_width / 2,
                                          point[0] + self.border_width / 2, point[1] + self.border_width / 2),
                                         fill=self.border_color)

                        if variant == MULTIPLE and SMALL not in other:
                            height += 1 / 3
                    if con_type in ROUND:
                        if orientation:
                            bbox = (-r * 900, (-r + offset + height) * 900, r * 900, (r + offset + height) * 900)
                        else:
                            bbox = (size[0] + -r * 900, (-r + offset + height) * 900,
                                    size[0] + r * 900, (r + offset + height) * 900)
                        draw.ellipse(bbox,
                                     fill=colors[con_type],
                                     outline=self.border_color, width=self.border_width)
                    if variant != EMPTY:
                        label_centers.append((offset + height))
                        actual_counter += 1
                last_height += math.ceil(height)
        return label_centers