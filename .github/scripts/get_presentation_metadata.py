#!/usr/bin/env python3
import sys
from pptx import Presentation

def get_presentation_metadata(file_path):
    try:
        prs = Presentation(file_path)
        slides = len(prs.slides)
        date = prs.core_properties.created.strftime("%Y-%m-%d") if prs.core_properties.created else "Unknown"
        print(f"{slides}|{date}")
    except Exception as e:
        print("0|Unknown")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python get_presentation_metadata.py <путь_к_презентации>")
        sys.exit(1)
    get_presentation_metadata(sys.argv[1]) 