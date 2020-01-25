from PIL import Image


folder_path = 'C:\\Users\\ccoon\\OneDrive\\Desktop\\EhrhardtForensic\\ImageProcess\\p22_contact_larger_frame\\'
file_name = 'P22_Contact_Images_1877_and_1915_Buccal.tif'
input_file_path = folder_path + file_name

im = Image.open(input_file_path)

# The crop method from the Image module takes four coordinates as input.
# The right can also be represented as (left+width)
# and lower can be represented as (upper+height).
left_upper_x = 3
left_upper_y = 67
right_lower_x = 370
right_lower_y = 434

max_x = 5323
max_y = 2719

x_increment = 381
y_increment = 381

im_ct = 0

row_start_upper_x = left_upper_x
row_start_lower_y = right_lower_x

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