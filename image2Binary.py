from PIL import Image

def threshold_image(input_image_path, output_image_path, threshold_value):
    # Open the input image
    input_image = Image.open(input_image_path)
    
    # Convert the image to grayscale
    grayscale_image = input_image.convert('L')
    
    # Apply thresholding
    thresholded_image = grayscale_image.point(lambda p: p > threshold_value and 255)
    
    # Save the thresholded image
    thresholded_image.save(output_image_path)

# Example usage:
input_image_path = "/workspaces/PixelConvert/static/uploads/WhatsApp Image 2024-03-13 at 8.32.22 AM.jpeg"
output_image_path = "/workspaces/PixelConvert/output/thresholded_image.jpg"
threshold_value = 128  # Adjust this value as needed
threshold_image(input_image_path, output_image_path, threshold_value)
