import argparse
from PIL import Image
import os

def resize_and_optimize_image(image, output_size=(240, 240)):
    original_width, original_height = image.size
    target_width, target_height = output_size

    ratio = min(target_width / original_width, target_height / original_height)
    new_size = (int(original_width * ratio), int(original_height * ratio))

    resized_image = image.resize(new_size, Image.Resampling.LANCZOS)
    new_image = Image.new("RGB", output_size, (255, 255, 255))
    new_image.paste(resized_image, ((target_width - new_size[0]) // 2, (target_height - new_size[1]) // 2))

    return new_image

def extract_frames(gif_path, output_dir, frame_count):
    gif = Image.open(gif_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    total_frames = gif.n_frames
    step = max(1, total_frames // frame_count)
    
    frame_index = 0
    extracted_frames = 0
    
    while extracted_frames < frame_count and frame_index < total_frames:
        gif.seek(frame_index)
        frame = gif.copy().convert("RGB")
        optimized_frame = resize_and_optimize_image(frame)
        frame_path = os.path.join(output_dir, f"frame{extracted_frames}.png")
        optimized_frame.save(frame_path, format="PNG", optimize=True)
        extracted_frames += 1
        frame_index += step

    print(f"提取了{extracted_frames}帧图片，保存在{output_dir}目录中")

def main():
    parser = argparse.ArgumentParser(description="Extract frames from a GIF file and resize to 240x240.")
    parser.add_argument("input_gif", help="Path to the input GIF file.")
    parser.add_argument("output_dir", help="Directory to save the extracted frames.")
    parser.add_argument("--frames", type=int, default=10, help="Number of frames to extract.")
    args = parser.parse_args()

    extract_frames(args.input_gif, args.output_dir, args.frames)

if __name__ == "__main__":
    main()