import pyAesCrypt
import os

# File encryption function

def ecnryption(file, password):

    # Setting the buffer size
    buffer_size = 512 * 1024

    # Calling the encryption method
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # For the result, we print the name of the encrypted file
    print("[ The file '" + str(os.path.splitext(file)[0]) + "' is encrypted]")

    # Delete the source file
    os.remove(file)

# Directory scanning function
def walking_by_dirs(dir, password):

    # Going through all the directories in the specified directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # If we find a file, we encrypt it
        if os.path.isfile(path):
            try:
                ecnryption(path, password)
            except Exception as ex:
                print(ex)
        # If we find a directory, we repeat the cycle in search of files
        else:
            walking_by_dirs(path, password)
path = input("Enter the path file: ")
password = input("Enter the encryption password: ")
walking_by_dirs(path, password)