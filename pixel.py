from PIL import Image

def create_pixel_art(input_path, output_path, pixelation_factor=22, num_colors=44):
    try:
        img = Image.open(input_path)
    except FileNotFoundError:
        print(f"错误：找不到文件，请检查路径: {input_path}")
        return

    # 1. 缩小图片
    width, height = img.size
    img_small = img.resize(
        (width // pixelation_factor, height // pixelation_factor),
        resample=Image.BILINEAR
    )

    # 2. Pillow 内置的量化算法
    img_quantized = img_small.quantize(colors=num_colors, method=Image.Quantize.FASTOCTREE)

    # 3. 转换回 RGB 模式
    img_rgb = img_quantized.convert("RGB")

    # 4. 放大图片
    result = img_rgb.resize(img.size, Image.NEAREST)

    # 5. 保存
    result.save(output_path)
    print(f"像素艺术风格图片已保存至 {output_path}")
    print(f"参数: 像素大小={pixelation_factor}, 颜色数={num_colors}")


# 获取，生成
import os
input_path = os.path.expanduser("./IMG_32459.JPG")
output_path = "./pixel_art_final.png" 

create_pixel_art(input_path, output_path, pixelation_factor=22, num_colors=44)
