from PIL import Image
from mili.pixels import PixelGrid

def test_pixel_grid_import_file():
    pil_image = Image.open("./tests/test_image.webp").resize((16, 16), Image.Resampling.LANCZOS)
    pg_image  = PixelGrid.from_image("./tests/test_image.webp")

    assert pil_image.getpixel((9, 2)) == pg_image.get_pixel(9, 2).values()

def test_pixel_grid_using_pillow():
    pil_image = Image.open("./tests/test_image.webp").resize((16, 16), Image.Resampling.LANCZOS)
    pg_image  = PixelGrid.from_image(pil_image)
    
    assert pil_image.getpixel((9, 2)) == pg_image.get_pixel(9, 2).values()

def test_pixel_grid_animated():
    pil_image = Image.open("./tests/test_anim.webp").resize((16, 16), Image.Resampling.LANCZOS).convert("RGB")
    pg_image  = PixelGrid.from_image("./tests/test_anim.webp")

    assert pil_image.getpixel((9, 2)) == pg_image[0].get_pixel(9, 2).values()