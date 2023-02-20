from rembg import remove

input_file = 'image.jpg'
output_file = 'new_file.jpg'

with open(input_file,'rb') as f:
    with open(output_file,'wb') as g:
        input = f.read()
        output = remove(input)
        g.write(output)