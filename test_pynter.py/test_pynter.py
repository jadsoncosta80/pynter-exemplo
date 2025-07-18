import os
from urllib.request import urlretrieve
from pynter.pynter import generate_captioned

# 1. Baixar imagem de exemplo
img_url = "https://i.imgur.com/XQCKcC9.jpg"
image_path = "image.jpg"
if not os.path.exists(image_path):
    urlretrieve(img_url, image_path)

# 2. Baixar fonte Roboto se ainda não existir
font_folder = "Roboto"
font_path = os.path.join(font_folder, "Roboto-Regular.ttf")
if not os.path.exists(font_folder):
    os.makedirs(font_folder, exist_ok=True)
    urlretrieve(
        "https://github.com/google/fonts/raw/main/apache/roboto/Roboto%5Bwdth%2Cwght%5D.ttf",
        font_path
    )

# 3. Gerar a imagem com legenda
caption = "TESTANDO PYNTER!"
im = generate_captioned(
    text=caption,
    image_path=image_path,
    size=(800, 600),
    font_path=font_path,
    filter_color=(0, 0, 0, 40),
    text_background_color=(0, 0, 0, 180),
)

# 4. Exibir e salvar
im.show()
im.convert("RGB").save("imagem_legendada.jpg")
print("Imagem legendada salva em imagem_legendada.jpg")
