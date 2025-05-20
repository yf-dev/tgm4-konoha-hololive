import math
import os
from typing import Literal

from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

from characters import CHARACTER_MAP, Character

character_id_list = [
    "ina",
    "pekora",
    "hajime",
    "korone",
    "ririka",
    "mococo",
    "irys",
    "okayu",
    "calli",
    "towa",
    "flare",
    "ao",
    "bijou",
    "liz",
    "vivi",
    "miko",
    "suisei",
    "kanade",
    "raden",
    "fuwawa",
    "azki",
    "kronii",
    "bae",
    "gigi",
    "mio",
    "subaru",
    "ceci",
    "raora",
    "marine",
    "shiori",
    "sora",
    "kiara",
    "noel",
    "fubuki",
    "watame",
    "roboco",
    "luna",
    "niko",
    "chihaya",
    "kanata",
    "su",
    "riona",
    "nerissa",
    "shion",
    "mumei",
    "fauna",
    "sana",
    "aqua",
    "ame",
    "gura",
]


def generate_name_image(character: Character) -> Image.Image:
    canvas_width = 1280
    canvas_height = 256
    canvas_padding = 32
    canvas_background_color = (0, 0, 0, 0)  # Transparent
    font_path = "NotoSansCJK-VF.otf.ttc"
    base_font_size = 85
    font_color = "#2e2a2c"
    font_weight = 700
    font_stroke = 4
    font_stroke_color = "#ffffff"
    name_spacing = 40  # Adjust this value to increase/decrease spacing between names

    # Create a blank canvas
    canvas = Image.new("RGBA", (canvas_width, canvas_height), canvas_background_color)
    draw = ImageDraw.Draw(canvas)

    name1 = character.name1
    name2 = character.name2

    # Calculate the maximum font size for name1
    max_font_size1 = base_font_size
    name1_font = None
    text1_width = canvas_width + 1
    text1_height = 0

    while text1_width > canvas_width - canvas_padding * 2 and max_font_size1 > 0:
        max_font_size1 -= 1
        name1_font = ImageFont.truetype(font_path, max_font_size1, encoding="utf-8")
        name1_font.set_variation_by_axes([font_weight])
        left1, top1, right1, bottom1 = draw.textbbox((0, 0), name1, font=name1_font)
        text1_height = bottom1 - top1
        text1_width = right1 - left1

    # Calculate the maximum font size for name2
    max_font_size2 = base_font_size
    name2_font = None
    text2_width = canvas_width + 1
    text2_height = 0

    while text2_width > canvas_width - canvas_padding * 2 and max_font_size2 > 0:
        max_font_size2 -= 1
        name2_font = ImageFont.truetype(font_path, max_font_size2, encoding="utf-8")
        name2_font.set_variation_by_axes([font_weight])
        left2, top2, right2, bottom2 = draw.textbbox((0, 0), name2, font=name2_font)
        text2_height = bottom2 - top2
        text2_width = right2 - left2

    # Calculate vertical positioning to properly center both texts
    # Add spacing between the two names
    total_height = text1_height + text2_height + name_spacing
    start_y = (canvas_height - total_height) // 2

    # Get the actual vertical metrics for name1
    left1, top1, right1, bottom1 = draw.textbbox((0, 0), name1, font=name1_font)
    # Adjust the vertical position to account for the text's actual metrics
    adjusted_top1 = start_y - top1

    # Draw name1
    left1 = canvas_padding
    draw.text(
        (left1, adjusted_top1),
        name1,
        font=name1_font,
        fill=font_color,
        stroke_width=font_stroke,
        stroke_fill=font_stroke_color,
    )

    # Get the actual vertical metrics for name2
    left2, top2, right2, bottom2 = draw.textbbox((0, 0), name2, font=name2_font)
    # Calculate correct position for name2 based on name1's size and the adjusted position, plus spacing
    adjusted_top2 = adjusted_top1 + text1_height + name_spacing - top2

    # Draw name2
    left2 = canvas_padding
    draw.text(
        (left2, adjusted_top2),
        name2,
        font=name2_font,
        fill=font_color,
        stroke_width=font_stroke,
        stroke_fill=font_stroke_color,
    )

    return canvas


def generate_girlname_texture(characters: list[Character]) -> list[Image.Image]:
    images = []

    # chunk the characters list into 5 elements each
    for i in tqdm(range(0, len(characters) // 5), desc="Generating girlname textures"):
        chunk_images = []
        for j in range(5):
            index = i * 5 + j
            if index >= len(characters):
                break
            character = characters[index]
            name_image = generate_name_image(character)
            chunk_images.append(name_image)
        # Create a merged image from the chunk, vertically stacked
        chunk_width = 1280
        chunk_height = 1280
        chunk_canvas = Image.new("RGBA", (chunk_width, chunk_height), (0, 0, 0, 0))

        # Paste each image into the chunk canvas
        for idx, img in enumerate(chunk_images):
            y_offset = idx * (chunk_height // 5)
            chunk_canvas.paste(img, (0, y_offset))

        images.append(chunk_canvas)

    return images


def generate_single_icon(
    character: Character, type_: Literal["icon00", "icon01", "icon02"]
) -> Image.Image:
    icon_size = 96
    bg_color = "#2e2a2c"
    padding = 2
    thumb_path = f"characters/{character.id}/thumb.png"
    canvas = Image.new("RGBA", (icon_size, icon_size), bg_color)
    thumb = Image.open(thumb_path).convert("RGBA")
    thumb = thumb.resize(
        (icon_size - padding * 2, icon_size - padding * 2), Image.Resampling.LANCZOS
    )
    thumb_x = (icon_size - thumb.width) // 2
    thumb_y = (icon_size - thumb.height) // 2
    canvas.paste(thumb, (thumb_x, thumb_y), thumb)

    if type_ == "icon00":
        return canvas

    if type_ == "icon01":
        overlay_path = "icon_grad1.png"
    elif type_ == "icon02":
        overlay_path = "icon_grad2.png"

    overlay = Image.open(overlay_path).convert("RGBA")
    overlay_img = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    overlay_img.paste(overlay, (thumb_x, thumb_y), overlay)
    canvas = Image.alpha_composite(canvas, overlay_img)

    return canvas


def generate_icons(characters: list[Character]) -> list[Image.Image]:
    types_ = ["icon00", "icon01", "icon02"]
    results = []
    for type_ in types_:
        icons = []
        for character in tqdm(characters, desc=f"Generating {type_} icons"):
            icon = generate_single_icon(character, type_)
            icons.append(icon)
        # Create a merged image from the icons, 10x5 grid
        icon_size = 96
        grid_width = 960
        grid_height = 480
        grid_canvas = Image.new("RGBA", (grid_width, grid_height), (0, 0, 0, 0))
        for i, icon in enumerate(icons):
            x_offset = (i % 10) * icon_size
            y_offset = (i // 10) * icon_size
            grid_canvas.paste(icon, (x_offset, y_offset), icon)
        results.append(grid_canvas)
    return results


def apply_drop_shadow(
    image: Image.Image, angle: int, distance: int, opacity: float
) -> Image.Image:
    """
    Apply a drop shadow to an image

    Args:
        image: The source image with transparency
        angle: The angle of the shadow in degrees (0-360)
        distance: The distance of the shadow in pixels
        opacity: The opacity of the shadow (0.0-1.0)

    Returns:
        A new image with the drop shadow applied, preserving original size
    """
    # Convert angle to radians and use trigonometry for accurate positioning
    angle_rad = math.radians(angle)
    x_offset = int(distance * math.cos(angle_rad))
    y_offset = int(distance * math.sin(angle_rad))

    # Get original image size
    width, height = image.size

    # Create a result canvas with the SAME size as the original image
    result = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Create the shadow image
    shadow = Image.new("RGBA", image.size, (0, 0, 0, 0))

    # Use the original image as a mask with reduced opacity
    shadow_mask = Image.new("L", image.size, 0)
    shadow_mask.paste(
        Image.new("L", image.size, int(255 * opacity)), (0, 0), image.split()[3]
    )

    # Create black shadow with original image's alpha channel
    black_image = Image.new("RGB", image.size, (0, 0, 0))
    shadow = Image.merge(
        "RGBA",
        (
            black_image.split()[0],
            black_image.split()[1],
            black_image.split()[2],
            shadow_mask,
        ),
    )

    # Create a temporary larger canvas that can hold both the image and shadow
    # This is just for positioning and will be cropped back to original size
    temp_width = width + abs(x_offset)
    temp_height = height + abs(y_offset)
    temp_canvas = Image.new("RGBA", (temp_width, temp_height), (0, 0, 0, 0))

    # Calculate where the shadow should go in the temp canvas
    if x_offset >= 0:
        shadow_x = x_offset
        image_x = 0
    else:
        shadow_x = 0
        image_x = abs(x_offset)

    if y_offset >= 0:
        shadow_y = y_offset
        image_y = 0
    else:
        shadow_y = 0
        image_y = abs(y_offset)

    # Paste the shadow and original image onto the temp canvas
    temp_canvas.paste(shadow, (shadow_x, shadow_y), shadow)
    temp_canvas.paste(image, (image_x, image_y), image)

    # Crop the temp canvas back to the original image size
    # This ensures we maintain the original dimensions
    crop_x = max(0, -x_offset)
    crop_y = max(0, -y_offset)
    result = temp_canvas.crop((crop_x, crop_y, crop_x + width, crop_y + height))

    return result


def generate_egm_image(
    character: Character, type_: Literal[None, "grad1", "grad2"]
) -> Image.Image:
    shadow_angle = 45
    shadow_distance = 45
    shadow_opacity = 0.65

    egm_path = f"characters/{character.id}/egm.png"
    egm_image = Image.open(egm_path).convert("RGBA")

    if type_ == "grad1":
        overlay_path = "egm_grad1.png"
    elif type_ == "grad2":
        overlay_path = "egm_grad2.png"
    else:
        # Apply drop shadow to the original image and return
        return apply_drop_shadow(
            egm_image,
            angle=shadow_angle,
            distance=shadow_distance,
            opacity=shadow_opacity,
        )

    overlay_image = Image.open(overlay_path).convert("RGBA")

    # Resize overlay if needed
    if overlay_image.size != egm_image.size:
        overlay_image = overlay_image.resize(egm_image.size, Image.Resampling.LANCZOS)

    # Create a new blank image
    result = Image.new("RGBA", egm_image.size, (0, 0, 0, 0))

    # Split the images into their RGBA bands
    _, _, _, a_egm = egm_image.split()
    _, _, _, a_overlay = overlay_image.split()

    # Create a composite image that:
    # 1. Uses the overlay RGB values where the overlay is opaque
    # 2. Uses the original egm RGB values where the overlay is transparent
    # 3. Maintains the original egm transparency (alpha channel)

    # Create a new image with the size of egm_image
    result = Image.new("RGBA", egm_image.size, (0, 0, 0, 0))

    # Use composite operation which respects alpha channels
    # This applies the overlay on top of the egm_image where overlay is not transparent
    result = Image.composite(overlay_image, egm_image, a_overlay)

    # Keep the original alpha channel of egm_image
    r, g, b, _ = result.split()
    result = Image.merge("RGBA", (r, g, b, a_egm))

    # Apply drop shadow to the final result
    result = apply_drop_shadow(
        result, angle=shadow_angle, distance=shadow_distance, opacity=shadow_opacity
    )

    return result


def generate_emgs(characters: list[Character]) -> list[Image.Image]:
    images = []
    for character in tqdm(characters, desc="Generating egm images"):
        types_ = ["grad2", "grad1", None]
        for type_ in types_:
            image = generate_egm_image(character, type_)
            images.append(image)
    return images


if __name__ == "__main__":
    characters = [CHARACTER_MAP[character_id] for character_id in character_id_list]
    os.makedirs("extracted_textures/ui", exist_ok=True)
    # images = generate_girlname_texture(characters)
    # for i, img in tqdm(
    #     enumerate(images), total=len(images), desc="Saving girlname textures"
    # ):
    #     filepath = f"extracted_textures/ui/girlname{i}.twx.png"
    #     img.save(filepath, "PNG")
    # icons = generate_icons(characters)
    # for i, icon in tqdm(
    #     enumerate(icons), total=len(icons), desc="Saving icon textures"
    # ):
    #     filepath = f"extracted_textures/ui/icon{i:02}.twx.png"
    #     icon.save(filepath, "PNG")
    os.makedirs("extracted_textures/eff/egm", exist_ok=True)
    emgs = generate_emgs(characters)
    for i, emg in tqdm(enumerate(emgs), total=len(emgs), desc="Saving egm textures"):
        filepath = f"extracted_textures/eff/egm/egm{i:02}.twx.png"
        emg.save(filepath, "PNG")
