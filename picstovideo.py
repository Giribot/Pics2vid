import os
import cv2
from tkinter import Tk, filedialog, simpledialog, messagebox
from PIL import Image
from tqdm import tqdm
import shutil

def check_and_resize_images(image_folder, temp_folder):
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    if not image_files:
        return False, "No images found in the selected folder."

    first_image = Image.open(os.path.join(image_folder, image_files[0]))
    target_size = first_image.size
    first_image.close()

    os.makedirs(temp_folder, exist_ok=True)
    for img_file in image_files:
        img_path = os.path.join(image_folder, img_file)
        with Image.open(img_path) as img:
            if img.size != target_size:
                resized_img = img.resize(target_size)
                resized_img.save(os.path.join(temp_folder, img_file))
            else:
                shutil.copy(img_path, temp_folder)

    return True, target_size

def create_video_from_images(temp_folder, output_file, fps, quality):
    image_files = sorted([f for f in os.listdir(temp_folder) if f.lower().endswith(('png', 'jpg', 'jpeg'))])
    if not image_files:
        return "No valid images to create a video."

    first_image_path = os.path.join(temp_folder, image_files[0])
    first_image = cv2.imread(first_image_path)
    height, width, layers = first_image.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use MP4 codec (compatible without FFmpeg)
    video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    encode_params = [int(cv2.IMWRITE_JPEG_QUALITY), quality]

    progress = tqdm(total=len(image_files), desc="Encoding video")
    for img_file in image_files:
        img_path = os.path.join(temp_folder, img_file)
        frame = cv2.imread(img_path)
        _, encoded_frame = cv2.imencode('.jpg', frame, encode_params)
        decoded_frame = cv2.imdecode(encoded_frame, cv2.IMREAD_COLOR)
        video.write(decoded_frame)
        progress.update(1)

    video.release()
    progress.close()

    return "Video successfully created."

def main():
    Tk().withdraw()  # Hide the root Tkinter window

    # Step 1: Select the folder containing images
    image_folder = filedialog.askdirectory(title="Select Folder Containing Images")
    if not image_folder:
        messagebox.showerror("Error", "No folder selected.")
        return

    # Step 2: Get FPS setting
    try:
        fps = simpledialog.askinteger("FPS", "Enter frames per second:", minvalue=1, maxvalue=60)
        quality = simpledialog.askinteger("Quality", "Enter quality (0-100, default is 90):", minvalue=0, maxvalue=100, initialvalue=90)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
        return

    # Step 3: Choose output file location
    output_file = filedialog.asksaveasfilename(
        title="Save Video As",
        defaultextension=".mp4",
        filetypes=[("MP4 files", "*.mp4")]
    )
    if not output_file:
        messagebox.showerror("Error", "No save location selected.")
        return

    # Step 4: Check and resize images
    temp_folder = os.path.join(image_folder, "temp_resized")
    valid, result = check_and_resize_images(image_folder, temp_folder)
    if not valid:
        messagebox.showerror("Error", result)
        return

    # Step 5: Create video
    if os.path.exists(output_file):
        messagebox.showinfo("File Exists", "A file with the same name already exists. The new video will not overwrite it.")
        return

    result = create_video_from_images(temp_folder, output_file, fps, quality)
    messagebox.showinfo("Info", result)

    # Cleanup temporary folder
    shutil.rmtree(temp_folder)

if __name__ == "__main__":
    main()
