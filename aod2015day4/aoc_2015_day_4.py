import hashlib


def check_has_five_zeros(hash: str) -> bool:
    """Return true if hash starts with five zeros"""
    if len(hash) < 6:
        return False

    return hash.startswith("000000")


def concatenate_input_and_number(input: str, count: int) -> str:
    """Combine input and number"""
    return input + str(count)


def generate_md5_hash(input_and_number: str) -> str:
    """Convert input+number to hash"""
    return hashlib.md5(input_and_number.encode()).hexdigest()


def main(input):
    has_five = False
    count = 0
    while has_five == False:
        count += 1
        concatenated = concatenate_input_and_number(input, count)
        result = generate_md5_hash(concatenated)
        has_five = check_has_five_zeros(result)
        print(count, result, has_five)

    return count


if __name__ == "__main__":
    input = "yzbqklnj"
    result = generate_md5_hash(input)
    print(main(input))
