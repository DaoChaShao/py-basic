import uuid


def uuid_1_generator(volume):
    """
    uncertainty generator
    Generate a UUID 1 (timestamp-based),
    including mac address and randomness.
    """
    for i in range(volume):
        result = uuid.uuid1()
        print(f"UUID 1 {i + 1:0{len(str(volume))}d}: {result}")
        # print(f"The length of UUID 1: {len(str(result))}")


def uuid_3_generator(volume):
    """
    certainty generator
    Generate a UUID 3 (name-based using MD5 hash),
    including a namespace and a name.
    """
    for i in range(volume):
        result = uuid.uuid3(uuid.NAMESPACE_DNS, "random_name")
        print(f"UUID 3 (MD5) {i + 1:0{len(str(volume))}d}: {result}")
        # print(f"The length of UUID 3: {len(str(result))}")


def uuid_4_generator(volume, mode=""):
    """
    randomness and disordered generator
    Generate a UUID 4 (random),
    including randomness.
    """
    match mode:
        case "":
            for i in range(volume):
                result = uuid.uuid4()  # generate a random UUID
                print(f"UUID 4 {i + 1:0{len(str(volume))}d}: {result}")
                # print(f"The length of UUID 4: {len(str(result))}")
        case "hex":
            for i in range(volume):
                result = uuid.uuid4().hex  # convert UUID to hex string
                print(f"UUID 4 (hex) {i + 1:0{len(str(volume))}d}: {result}")
                # print(f"The length of UUID 4 (hex): {len(str(result))}")
        case _:
            print("Invalid mode. Please choose between 'hex' or leave it blank.")


def uuid_5_generator(volume):
    """
    certainty generator
    Generate a UUID 5 (name-based using SHA-1 hash),
    including a namespace and a name.
    """
    for i in range(volume):
        result = uuid.uuid5(uuid.NAMESPACE_DNS, "random_name")
        print(f"UUID 5 (SHA-1) {i + 1:0{len(str(volume))}d}: {result}")
        # print(f"The length of UUID 5: {len(str(result))}")


def main():
    """ Main function """
    # set the volume of UUIDs to generate
    id_volume = 10
    # call the UUID 1 generator function with the volume as argument
    uuid_1_generator(id_volume)
    print("-" * 50)
    # call the UUID 3 generator function with the volume as argument
    uuid_3_generator(id_volume)
    print("-" * 50)
    # call the UUID 4 generator function with the volume as argument
    uuid_4_generator(id_volume, mode="hex")
    print("-" * 50)
    # call the UUID 5 generator function with the volume as argument
    uuid_5_generator(id_volume)


if __name__ == "__main__":
    main()
