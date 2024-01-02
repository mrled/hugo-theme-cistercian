#!/usr/bin/env python3


import argparse
import json
import os


cistercian_characters_dict = {
    "0": chr(0x100002),
    "1": chr(0x100003),
    "2": chr(0x100004),
    "3": chr(0x100005),
    "4": chr(0x100006),
    "5": chr(0x100007),
    "6": chr(0x100008),
    "7": chr(0x100009),
    "8": chr(0x10000A),
    "9": chr(0x10000B),
    "10": chr(0x10000C),
    "20": chr(0x10000D),
    "30": chr(0x10000E),
    "40": chr(0x10000F),
    "50": chr(0x100010),
    "60": chr(0x100011),
    "70": chr(0x100012),
    "80": chr(0x100013),
    "90": chr(0x100014),
    "100": chr(0x100015),
    "200": chr(0x100016),
    "300": chr(0x100017),
    "400": chr(0x100018),
    "500": chr(0x100019),
    "600": chr(0x10001A),
    "700": chr(0x10001B),
    "800": chr(0x10001C),
    "900": chr(0x10001D),
    "1000": chr(0x10001E),
    "2000": chr(0x10001F),
    "3000": chr(0x100020),
    "4000": chr(0x100021),
    "5000": chr(0x100022),
    "6000": chr(0x100023),
    "7000": chr(0x100024),
    "8000": chr(0x100025),
    "9000": chr(0x100026),
}


def main():
    scriptroot = os.path.dirname(os.path.realpath(__file__))
    dataroot = os.path.join(scriptroot, "data")
    datacistercian = os.path.join(dataroot, "cistercian")
    data_file = os.path.join(datacistercian, "cistercian.json")

    parser = argparse.ArgumentParser(
        description="Generate the Cistercian data file. The result is committed to the repository; we only keep this script for reference. Hugo templates cannot handle characters outside the Basic Multilingual Plane, which happen to be the codepoints that FRBCistercian uses, so we cannot work with the characters directly in the templates. Instead, we save the characters to a JSON data file and look them up by index. This script creates that JSON data file."
    )
    parser.add_argument("--save-data", action="store_true", help=f"Save to {data_file}")
    parser.add_argument(
        "--quiet", action="store_true", help="Don't print the characters"
    )
    parsed = parser.parse_args()

    if not parsed.quiet:
        print("Cistercian characters:")
        # json.dump will encode the characters as UTF-16 Surrogate Pairs, which is fine for printing on the terminal
        print(json.dumps(cistercian_characters_dict, indent=2))
    if parsed.save_data:
        os.makedirs(datacistercian, exist_ok=True)
        with open(data_file, "w", encoding="utf-8") as f:
            # Set ensure_ascii to False to save the characters without encoding them
            json.dump(cistercian_characters_dict, f, indent=2, ensure_ascii=False)
        if not parsed.quiet:
            print(f"Saved to {data_file}")


if __name__ == "__main__":
    main()
