from PIL import Image
im = Image.open("test_Cisplatino.png")
#bg = Image.new("RGB", im.size, (255,255,255))
#bg.paste(im, (0,0), im)
bg = im.convert('RGB')
bg.save("Success.jpg", qualiaty=100)

