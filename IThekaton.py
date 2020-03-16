
def calculate(example):
    example = example.split(" ")
    try:
        example[0] = int(example[0])
    except:
        return "Invalid WIDTH input data"
    try:
        example[1] = int(example[1])
    except:
        return "Invalid HEIGHT input data"
    max_width = example[0]
    max_height = example[1]
    for pix in range(1, max_width):
        current_width = 0
        current_height = pix
        for word in example[2:]:
            word_width = len(word) * pix
            if current_width + word_width <= max_width and pix <= max_height:
                current_width += word_width
                if current_width != max_width:
                    current_width += pix
            else:
                current_height += pix
                if current_height <= max_height and word_width <= max_width:
                    current_width = word_width
                    if current_width != max_width:
                        current_width += pix
                else:
                    return pix - 1

if __name__ == "__main__":
    f = open("vhodi.txt", "r")
    lines = f.read().strip().split('\n')
    f.close()
    f = open("izhodi.txt", "w")
    for example in lines:
        result = calculate(example)
        f.write(str(result) + "\n")
        print("Example:", example, "| max_pix =", result)
    f.close()