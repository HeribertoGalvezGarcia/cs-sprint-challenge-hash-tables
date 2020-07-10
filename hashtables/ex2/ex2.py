from typing import List


#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source: str, destination: str) -> None:
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets: List[Ticket], length: int) -> List[str]:
    tickets = {ticket.source: ticket.destination for ticket in tickets}

    route = [tickets["NONE"]]

    while route[-1] != "NONE":
        route.append(tickets[route[-1]])

    return route
