from PIL import Image, ImageColor

shapes = ['ball', 'casing', 'plate', 'ingot', 'rotor', 'gear', 'gearSmall', 'cylinder', 'stick', 'stickLong', 'bolt', 'ring', 'bottle', 'block']

material_icon_type = input('Select Material Icon Set: ')

# Get color input
color = input('Select Color (format 0xB4B478 OR #B4B478): ')
color = '#' + color.upper()
color = ImageColor.getcolor(color, 'RGB')

for shape in shapes:
        
    picture = Image.open('resources/base/shapes/shape.mold.' + shape + '.png')  
    # Setup output image
    output = picture
    # Size of the image
    width, height = picture.size

    # Modify pixels
    for x in range(width):
        for y in range(height):
                
            # Get Current Pixel Color
            current_color = picture.getpixel((x, y))
            
            # check opacity/ presence pf alpha channel
            if current_color[3]==255:
                # Photoshop Overlay Algorithm
                average = int((current_color[0] + current_color[1] + current_color[2]) / 3)

                if average < 128:
                    r = int((2 * current_color[0] * color[0]) / 255)
                    g = int((2 * current_color[1] * color[1]) / 255)
                    b = int((2 * current_color[2] * color[2]) / 255)
                    loc = (r, g, b)
                else:
                    r = int((1 - (2 * (1 - current_color[0]) * (1 - color[0]))) / 255) * -1
                    g = int((1 - (2 * (1 - current_color[1]) * (1 - color[1]))) / 255) * -1
                    b = int((1 - (2 * (1 - current_color[2]) * (1 - color[2]))) / 255) * -1
                    loc = (r, g, b)

                output.putpixel((x, y), loc)

            else:
                output.putpixel((x, y), color)
            
    # Write File
    output.save('output/shapes/shape_mold_' + shape + '_' + material_icon_type + '.png')
    
    #Write .json model file
    json = '{"parent": "item/generated","textures": {"layer0": "contenttweaker:items/shape_mold_'
    with open('output/shapes/models/item/shape_mold_' + shape + '_' + material_icon_type + '.json', 'w') as model:
        model.write(json + shape + '_' + material_icon_type + '"}}')
