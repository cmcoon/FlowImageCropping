from PIL import Image

# Define folder holding images and destination for processed
folder_path = 'C:\\Users\\ccoon\\OneDrive\\Desktop\\EhrhardtForensic\\ImageProcess\\p22_contact_smaller_frame\\'

# Input file name
file_name = 'p22_contact_smaller_frame.tif'
input_file_path = folder_path + file_name

# Create image object via pillow/PIL
im = Image.open(input_file_path)

# Define pixel values for upper left coordinates and lower right coordinates
left_upper_x = 3
left_upper_y = 67
right_lower_x = 247
right_lower_y = 309

# Define bounds of image, max params
max_x = 5109
max_y = 2868

# For larger frames we increment with these values
x_increment = 256
y_increment = 256

row_start_upper_x = left_upper_x
row_start_lower_y = right_lower_x

im_ct = 0

# Process images until y is out of bounds
while left_upper_y < max_y:
    im_ct += 1
    coord = (left_upper_x, left_upper_y, right_lower_x, right_lower_y)
    print(coord)
    im_crop = im.crop(coord)

    save_file_name = folder_path + str(im_ct) + '_processed_' + file_name
    im_crop.save(save_file_name)

    left_upper_x += x_increment
    right_lower_x += x_increment

    # Decide if we need to reset x's, update at end of loop
    if left_upper_x > max_x:
        left_upper_x = row_start_upper_x
        right_lower_x = row_start_lower_y
        left_upper_y += y_increment
        right_lower_y += y_increment
