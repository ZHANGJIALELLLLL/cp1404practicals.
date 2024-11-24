class Band:
    """A class to represent a band with musicians."""

    def __init__(self, name=""):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band, listing musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string representing each musician playing their instrument."""
        return "\n".join(musician.play() for musician in self.musicians)