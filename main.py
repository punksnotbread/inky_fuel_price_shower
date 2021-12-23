from typing import Optional

import inkyphat
import requests
from lxml import etree


def show_text(text: str) -> None:
    color = "red"
    inkyphat.set_colour(color)

    # font_file = inkyphat.fonts.FredokaOne
    font_file = "DejaVuSans.ttf"
    font_size = 18
    font = inkyphat.ImageFont.truetype(
        font_file,
        font_size,
        encoding="utf-8",
    )

    w, h = font.getsize(text)
    x = (inkyphat.WIDTH / 2) - (w / 2)
    y = 51 - (h / 2)

    inkyphat.text((x, y), text, inkyphat.BLACK, font=font)
    inkyphat.show()


def format_text(text: str) -> str:
    if "Kaina" in text:
        text = text.split("Kaina")[-1].strip()
        return f"95: {text}"
    return text


def parse_element(html: str, xpath: str) -> Optional[str]:
    tree = etree.HTML(html)
    el = tree.xpath(xpath)
    if el:
        return el[0]


def get_html(url: str) -> Optional[str]:
    response = requests.get(url)
    if response.ok:
        return response.text


def main():
    url = (
        "https://pricer.lt/tyrimai/preke/"
        "pigiausias-a95-oktaninio-skaiciaus-benzinas/53"
    )
    html = get_html(url)
    price_path = './/span[@class="product-price"]/span/text()'
    text = "Failed getting prices"
    if html:
        text = parse_element(html, price_path)
    text = format_text(text)
    show_text(text)


if __name__ == "__main__":
    main()
