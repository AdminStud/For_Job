import pyAesCrypt
import os

# File decryption function

def decryption(file, password):

    # Setting the buffer size
    buffer_size = 512 * 1024

    # Calling the decryption method
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # For the result, we print the name of the crypted file
    print("[ The file '" + str(os.path.splitext(file)[0]) + "' is encrypted]")

    # Delete the source file
    os.remove(file)

# Directory scanning function
def walking_by_dirs(dir, password):

    # Going through all the directories in the specified directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # If we find a file, we decrypt it
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # If we find a directory, we repeat the cycle in search of files
        else:
            walking_by_dirs(path, password)
path = input("Enter the path file: ")
password = input("Enter the decryption password: ")
walking_by_dirs(path, password)