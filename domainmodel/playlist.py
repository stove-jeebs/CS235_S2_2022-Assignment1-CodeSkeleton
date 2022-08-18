from domainmodel.track import Track


class PlayList:
    def __init__(self):
        self.__tracks = []

    @property
    def tracks(self):
        return self.__tracks

    def add_track(self, track):
        if isinstance(track, Track) and track not in self.tracks:
            self.__tracks.append(track)

    def remove_track(self, track):
        if isinstance(track, Track) and track in self.tracks:
            self.__tracks.remove(track)

    def select_track_to_listen(self, index):
        if isinstance(index, int) and 0 <= index <= self.size() - 1:
            return self.tracks[index]
        return None

    def size(self):
        return len(self.tracks)

    def first_track_in_list(self):
        if self.size() != 0:
            return self.tracks[0]
        return None
