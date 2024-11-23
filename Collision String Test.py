import hashlib

def compute_hashes(file_path, algorithm):
    """
    Compute hashes for strings in a file using the specified algorithm.
    :param file_path: Path to the text file containing strings.
    :param algorithm: Hashing algorithm (e.g., 'md5', 'sha1', 'sha256').
    :return: A dictionary with hashes as keys and corresponding strings as values.
    """
    hashes = {}
    with open(file_path, 'r') as file:
        for line in file:
            string = line.strip()  # Remove any surrounding whitespace or newline
            hash_value = hashlib.new(algorithm, string.encode()).hexdigest()
            if hash_value in hashes and hashes[hash_value] != string:
                return {
                    "collision_found": True,
                    "string1": hashes[hash_value],
                    "string2": string,
                    "collision_hash": hash_value
                }
            hashes[hash_value] = string
    return {"collision_found": False}

def check_collisions(file_path):
    """
    Check for collisions in a text file using MD5, SHA-1, and SHA-256.
    :param file_path: Path to the text file containing strings.
    """
    algorithms = ['md5', 'sha1', 'sha256']
    for algorithm in algorithms:
        print(f"\nChecking for collisions using {algorithm.upper()}...")
        result = compute_hashes(file_path, algorithm)
        if result["collision_found"]:
            print(f"Collision Found for {algorithm.upper()}!")
            print(f"String 1: {result['string1']}")
            print(f"String 2: {result['string2']}")
            print(f"Collision Hash: {result['collision_hash']}")
        else:
            print(f"No collisions found using {algorithm.upper()}.")

# Path to the text file containing strings
file_path = "dataset.txt"  # Ensure this file exists and contains strings

# Run the collision check
check_collisions(file_path)
