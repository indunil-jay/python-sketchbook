# any () => checks if one is True.

# all () => checks everything is True.


is_connected: bool = True
has_electricity: bool = True
has_paid: bool = True

requirement: list[bool] = [is_connected, has_electricity, has_paid]

has_internet: bool = all(requirement)
has_no_failture: bool = any(requirement)

print(has_internet)

print(has_no_failture)
