from PIL import Image

import enemy_block

img1 = Image.open("data/W.png")
new_img1 = img1.resize((100, 100))
new_img1.save("data/W2.png")
