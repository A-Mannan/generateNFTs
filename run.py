from avatar_generator import AvatarGenerator


def generate():
    generator = AvatarGenerator(images_path="images")
    print("Generating 100 Random Avatars...")
    generator.generate_avatar(100)



if __name__ == "__main__":
    generate()
