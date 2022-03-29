from Utils.miscellaneous import load_image_as_samples

if  __name__ == "__main__":
    samples = load_image_as_samples("thinking_about_thinking.jpg")
    print(samples[0])