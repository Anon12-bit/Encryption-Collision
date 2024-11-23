import hashlib

def calculate_hash(file_path, algorithm='sha1'):
    """
    Calculate the hash of a file using the specified algorithm.
    :param file_path: Path to the file.
    :param algorithm: Hashing algorithm (e.g., 'md5', 'sha1', 'sha256').
    :return: Hexadecimal hash value as a string.
    """
    with open(file_path, 'rb') as f:
        hash_obj = hashlib.new(algorithm)  # Create hash object for the given algorithm
        while chunk := f.read(8192):  # Read file in chunks
            hash_obj.update(chunk)
        return hash_obj.hexdigest()

def check_collisions(files, algorithms=['md5', 'sha1', 'sha256']):
    """
    Check for collisions in a list of files using specified hash algorithms.
    :param files: List of file paths to check.
    :param algorithms: List of algorithms to use for hashing.
    """
    # Dictionary to store hashes for each algorithm
    hashes = {algo: {} for algo in algorithms}
    
    for algorithm in algorithms:
        print(f"\nChecking for collisions using {algorithm.upper()}...")
        collision_found = False  # Flag to track collisions
        
        for file in files:
            file_hash = calculate_hash(file, algorithm)
            
            if file_hash in hashes[algorithm]:
                # Collision detected
                collision_found = True
                print(f"  Collision Detected!")
                print(f"    File 1: {hashes[algorithm][file_hash]}")
                print(f"    File 2: {file}")
                print(f"    Hash: {file_hash}")
            else:
                hashes[algorithm][file_hash] = file  # Store the hash and file name
        
        if not collision_found:
            print(f"  No collisions detected for {algorithm.upper()}.")

# Example file paths
files = [
    f"file{i}.pdf" for i in range(1, 51)  # Simulating 50 files named file1.pdf to file50.pdf
]

# Run the collision check for MD5, SHA-1, and SHA-256
check_collisions(files)
