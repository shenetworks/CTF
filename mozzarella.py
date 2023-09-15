import os

# Get list of files in the current directory
file_list = os.listdir()

#Known bad hashes
hash_baddies = {"e6ca06e9b000933567a8604300094a85", "e62584c9cd15c3fa2b6ed0f3a34688ab", "f5315fb4a654087d30c69c768d80f826", "6d989302166ba1709d66f90066c2fd59", "4bc6cab128f623f34bb97194da21d7b6", "494e65cf21ad559fccf3dacdd69acc94", "a5965b750997dbecec61358d41ac93c7", "4e84b1448cf96fabe88c623b222057c4"}

exclude_file = "mozzarella.py"

for file_name in file_list:
    if file_name == exclude_file:
        continue
    with open(file_name, 'r') as current:
        # Initialize the counter for each file
        hash_count = 0
        for line in current:
            for hash in hash_baddies:
                if hash in line:
                    # Increment the counter when a match is found
                    hash_count += 1
        # Print the total number of hashes matched for the current file
        if hash_count > 0:
            print(f"Found {hash_count} matches in file: {file_name}")