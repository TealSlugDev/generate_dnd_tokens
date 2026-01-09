# Imports
import argparse
import os
from PIL import Image, ImageDraw, ImageFont
from constants import *

def generate_tokens(token_count):
    # Geometry
    RADIUS = SIZE // 2
    BORDER_INSET = int(SIZE * 0.18)
    SAFE_RADIUS = RADIUS - BORDER_INSET

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    monster_img = Image.open(BASE_IMAGE).convert("RGBA")
    border_img = Image.open(BORDER_IMAGE).convert("RGBA").resize(
        (SIZE, SIZE), Image.LANCZOS
    )

    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # White background circle
    white_bg = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    bg_draw = ImageDraw.Draw(white_bg)
    bg_draw.ellipse((0, 0, SIZE, SIZE), fill=(255, 255, 255, 255))

    # Monster image (zoomed out + shifted up)
    monster_size = int(SIZE * MONSTER_SCALE)
    monster = monster_img.resize((monster_size, monster_size), Image.LANCZOS)

    monster_layer = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    offset_x = (SIZE - monster_size) // 2
    offset_y = (SIZE - monster_size) // 2 + MONSTER_Y_OFFSET

    monster_layer.paste(monster, (offset_x, offset_y), monster)

    # Composite monster over white background
    token_base = white_bg.copy()
    token_base.alpha_composite(monster_layer)

    for i in range(1, token_count + 1):
        token = token_base.copy()
        draw = ImageDraw.Draw(token)

        text = str(i)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]

        # Bottom-right inside safe circle
        x = int(RADIUS + (SAFE_RADIUS - text_w) * 0.65)
        y = int(RADIUS + (SAFE_RADIUS - text_h) * 0.65)

        draw.text((x, y), text, font=font, fill=NUMBER_COLOR)

        # Border
        token.alpha_composite(border_img)

        token.save(os.path.join(OUTPUT_DIR, f"token_{i}.png"))

    print(f"Generated {token_count} tokens in '{OUTPUT_DIR}' directory.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate numbered circular D&D monster tokens"
    )
    parser.add_argument("count", type=int, help="Number of tokens to generate")

    args = parser.parse_args()
    generate_tokens(args.count)
