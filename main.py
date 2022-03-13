from datetime import datetime
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


def format_text(data: list[dict]) -> str:
    return "\n".join(f"{entry['type']}: {entry['price']}€" for entry in data)


def parse_prices(el: etree.Element) -> dict[str, str]:
    return {
        "type": el.xpath(".//th/text()")[0],
        "price": el.xpath(".//td/b/text()")[0],
    }


def parse_element(html: str, xpath: str) -> list[dict]:
    tree = etree.HTML(html)
    return [parse_prices(element) for element in tree.xpath(xpath)]


def get_html(url: str) -> Optional[str]:
    ua = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    )
    headers = {"user-agent": ua}
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.text
    raise Exception(f"Could not scrape website, response {response}")


def main():
    now = datetime.now()
    url = "https://degalu-kainos.lt/"
    html = get_html(url)
    price_path = './/div[@id="content"]//tr[contains(.//th/text(), "Benz")]'

    text = parse_element(html, price_path)
    text = format_text(text)
    text += f"\n{str(now)[:19]}"
    show_text(text)


if __name__ == "__main__":
    main()
