import random  # import library


class Die:  # create die class

    def __init__(self, faces):  # create die faces
        self._faces = faces

    def get_faces(self):
        return self._faces

    # create die roll
    def roll_die(self):
        return random.randint(1, self._faces)

