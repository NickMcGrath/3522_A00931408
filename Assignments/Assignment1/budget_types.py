import enum
class BudgetTypes(enum.Enum):
    """Enum of Budget Types."""
    GAMES_AND_ENTERTAINMENT = 1
    CLOTHING_AND_ACCESSORIES = 2
    EATING_OUT = 3
    MISCELLANEOUS = 4

    def __str__(self):
        """Returns budget types in title case without underscores."""
        return self.name.title().replace('_', ' ')