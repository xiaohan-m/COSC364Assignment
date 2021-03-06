"""
This is the RoutingTable class for the COSC364 Assignment.
"""


class RoutingTable:
    """
    This class is the routing table, it is responsible for storing and maintaining the routes the router knows
    """

    def __init__(self):
        """Initialise starting properties
        Table entry format (destination_id, next_hop_routerID, metric, flag)
        flag
        "a" alive link
        "d" for dead link
        """
        self.table = {}

    def __str__(self):
        """Print format for the Routing Table class"""
        table_string = ""
        for key in self.table.keys():
            table_string += "{}: Next Hop ID {}, Metric: {}, Flag {}\n".format(key, self.table[key][1], self.table[key][2], self.table[key][3])
        return "Routing Table\n" + table_string

    def display_table_changes(self, route_dead, table_changed, change_cause):
        """Prints out the routing table if a change has occurred"""
        if route_dead:
            print("Route Has Died")
        if table_changed:
            print("Change Caused By: " + change_cause)
            print(self)

    def update(self, rip_entries, next_hop_id, link_metric):
        """
        Expected RIP entry format
        (addr_family, destination_id, metric)
        """
        route_dead = False
        table_changed = False
        for entry in rip_entries:
            if str(entry[1]) not in self.table.keys():
                if (entry[2] + link_metric) < 16:
                    self.table[str(entry[1])] = (entry[1], next_hop_id, entry[2] + link_metric, "a")
                    table_changed = True
            elif self.table[str(entry[1])][2] > entry[2] + link_metric:
                self.table[str(entry[1])] = (entry[1], next_hop_id, entry[2] + link_metric, "a")
                table_changed = True
            elif self.table[str(entry[1])][1] == next_hop_id and entry[2] + link_metric != self.table[str(entry[1])][2] \
                    and entry[2] + link_metric < 16:
                self.table[str(entry[1])] = (entry[1], next_hop_id, entry[2] + link_metric, "a")
                table_changed = True
            elif self.table[str(entry[1])][1] == next_hop_id and entry[2] + link_metric >= 16 \
                    and self.table[str(entry[1])][3] != "d":
                self.table[str(entry[1])] = (entry[1], next_hop_id, 16, "d")
                table_changed = True
                route_dead = True
        self.display_table_changes(route_dead, table_changed, str(next_hop_id))
        return route_dead

    def get_entries(self, sending_router_id, receiving_neighbour=None):
        """
        receiving_neighbour, ID of router to apply split horizon poisoned reverse for.
        return entry format (destination_id, metric)
        return entry type list
        Default parameter for initial message sending for unknown links
        """
        rip_entries = [(sending_router_id, 0)]
        if receiving_neighbour is not None:
            for entry in self.table.values():
                if entry[0] != receiving_neighbour:
                    if entry[1] == receiving_neighbour:
                        rip_entries.append((entry[0], 16))
                    else:
                        rip_entries.append((entry[0], entry[2]))
        return rip_entries

    def update_dead_link(self, neighbour_id):
        """
        Updates router entries on death of a neighbour
        """
        for entry in self.table.values():
            if entry[1] == neighbour_id:
                self.table[str(entry[0])] = (entry[0], entry[1], 16, "d")
        self.display_table_changes(True, True, "Neighbour {} died". format(neighbour_id))

    def garbage_collection(self):
        """
        Removes any links marked for garbage collection
        """
        keys = list(self.table.keys())
        for key in keys:
            if self.table[key][3] == "d":
                del self.table[key]
        print("Garbage Collection Completed")
        print(self)


if __name__ == "__main__":
    """
    "Unit" Tests
    """
    routing_table = RoutingTable()
    print("Intial Table:")
    print(routing_table)
    print("First Fill Test")
    test_entries1 = [(None, 1, 5), (None, 3, 10), (None, 4, 15), (None, 5, 1)]
    routing_table.update(test_entries1, 2, 0)
    print(routing_table)
    print("Updating table Test")
    test_entries2 = [(None, 1, 1), (None, 4, 10), (None,5, 5)]
    routing_table.update(test_entries2, 3, 0)
    print(routing_table)
    print("Set Unreachable Test")
    test_entries3 = [(None, 1, 16), (None, 4, 16), (None, 5, 16)]
    routing_table.update(test_entries3, 3, 0)
    print(routing_table)
    test_entries4 = [(None, 1, 1), (None, 4, 3)]
    routing_table.update(test_entries4, 3, 0)
    print(routing_table)
    print("Get entries test no SH needed")
    print(routing_table.get_entries(1, 5))
    print("Get entries test SH needed")
    print(routing_table.get_entries(1, 3))
    print(routing_table)
    print("Testing Marking dead links")
    routing_table.update_dead_link(1, 3)
    print(routing_table)
    print("Testing Removing dead links")
    routing_table.garbage_collection()
    print(routing_table)