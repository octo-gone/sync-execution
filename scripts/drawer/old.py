from scripts.drawer.config import *
from scripts.constants import *
import math


class NodePNG:
    def __init__(self, **kwargs):

        self.inputs = kwargs.get("inputs", tuple())
        self.separated_inputs = []

        self.outputs = kwargs.get("outputs", tuple())
        self.separated_outputs = []

        self.desc = kwargs.get("desc", None)
        self.user_symbol = kwargs.get("user_symbol", None)

        self.ratio = (kwargs.get("width", 1), max(self.adjust_ratio(self.inputs), self.adjust_ratio(self.outputs)))
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

    def adjust_ratio(self, values):
        sep_values = [[]]
        sep_i = 0
        for value in values:
            if value not in ("sep",):
                sep_values[sep_i].append(value)
            else:
                sep_i += 1
                sep_values.append([])
        sum_height = 0
        for value in sep_values:
            height = 0
            for v in value:
                if v in SMALL + EMPTY:
                    height += 1 / 3
                if v in BIG:
                    height += 2 / 3
            height += 1 / 3
            sum_height += math.ceil(height)

        return sum_height

    def draw_node(self):
        from PIL import Image, ImageDraw, ImageFont

        size = self.ratio[0] * 900, self.ratio[1] * 900
        img = Image.new("RGBA", size, self.bg_color)
        draw = ImageDraw.Draw(img)
        r = 1 / 6

        def draw_connectors(connectors, orientation, connectors_color):
            label_centers = []
            if len(connectors):
                sep_connectors = [[]]
                sep_i = 0
                for value in connectors:
                    if value not in SEPARATORS:
                        sep_connectors[sep_i].append(value)
                    else:
                        sep_i += 1
                        sep_connectors.append([])
                last_height = 0
                actual_counter = 0
                for i, value in enumerate(sep_connectors):
                    height = 0
                    for v in value:
                        if v in SMALL + EMPTY:
                            height += 1 / 3
                        if v in BIG:
                            height += 2 / 3
                    height += 1 / 3
                    offset = (math.ceil(height) - height) / 2 + last_height
                    height = 0
                    for v in value:
                        height += 1 / 3
                        if v not in EMPTY and connectors_color:
                            color = colors[connectors_color[actual_counter]]
                        elif v not in EMPTY:
                            color = colors[v]
                        else:
                            color = self.bg_color
                        if v in BIG + TRIANGLE + SQUARE + CUT_SQUARE:
                            if v in RECTANGLE:
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
                            elif v in CUT_RECTANGLE:
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
                            elif v in SQUARE:
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
                            elif v in CUT_SQUARE:
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
                                              (r * 900, (offset + height) * 900),
                                              (0, (offset + height + r) * 900),
                                              (0, (offset + height - r) * 900))
                                else:
                                    points = ((size[0], (offset + height - r) * 900),
                                              (size[0] - r * 900, (offset + height) * 900),
                                              (size[0], (offset + height + r) * 900),
                                              (size[0], (offset + height - r) * 900))
                            draw.polygon(points, fill=color)
                            draw.line(points, fill=self.border_color, width=self.border_width)
                            for point in points:
                                draw.ellipse((point[0] - self.border_width / 2, point[1] - self.border_width / 2,
                                              point[0] + self.border_width / 2, point[1] + self.border_width / 2),
                                             fill=self.border_color)

                            if v in BIG:
                                height += 1 / 3
                        if v in ROUND:
                            if orientation:
                                bbox = (-r * 900, (-r + offset + height) * 900, r * 900, (r + offset + height) * 900)
                            else:
                                bbox = (size[0] + -r * 900, (-r + offset + height) * 900,
                                        size[0] + r * 900, (r + offset + height) * 900)
                            draw.ellipse(bbox,
                                         fill=colors[v],
                                         outline=self.border_color, width=self.border_width)
                        if v not in EMPTY:
                            label_centers.append((offset + height))
                            actual_counter += 1
                    last_height += math.ceil(height)
            return label_centers

        inputs_label_centers = draw_connectors(self.inputs, True, self.inputs_color)
        outputs_label_centers = draw_connectors(self.outputs, False, self.outputs_color)

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
            pos = (delta[0] - draw.textsize(self.inner, font=font)[0] / 2 + 150,
                   delta[1] - draw.textsize(self.inner, font=font)[1] / 2 + 150 - 8)
            draw.text(pos, self.inner, fill="black", font=font)

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
        # if icon:
        #     img2.crop((delta[0], delta[1],
        #                delta[0]+self.ratio[0]*300-1, delta[1]+self.ratio[1]*300-1)) \
        #         .save(f".\\resources\\nodes\\icons\\{file_name}.png")
        img2.save(f".\\resources\\generated\\png\\{file_name}.png")
        del draw
        del img
        del img2
