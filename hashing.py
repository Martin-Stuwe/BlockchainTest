import hashlib


class hashing:
    def get_digest(file_path):
        h = hashlib.sha256()

        with open(file_path, 'rb') as file:
            while True:
                # Reading is buffered, so we can read smaller chunks.
                chunk = file.read(h.block_size)
                if not chunk:
                    break
                h.update(chunk)

        return h.hexdigest()


    #print(get_digest("C:/Users/marti\Desktop/blockchain_ex1/00"))


    #Werte stimmen noch nicht überein mit Beispielblöcken.
