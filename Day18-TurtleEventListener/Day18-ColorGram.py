import colorgram

colors = colorgram.extract('hirst.jpg', 7)

list_color = []

def color_split(x):
    r = x.rgb[0]
    g = x.rgb[1]
    b = x.rgb[2]
    
    color = (r, g, b)
    
    return color
    

for i in colors:
    
    list_color.append(color_split(i))


