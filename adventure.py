import json
import sys


class GameEngine(object):
    def __init__(self, map_filename):
        self.map_filename = map_filename
        self.current_room_id = 0
        self.inventory = []
        self.rooms = []
        self.load_map()

    def load_map(self):
        try:
            with open(self.map_filename, 'r') as f:
                map_data = json.load(f)
        except FileNotFoundError:
            print(f"Map file '{self.map_filename}' not found.")
            sys.exit()

        for i, room_data in enumerate(map_data):
            if 'name' not in room_data or 'desc' not in room_data or 'exits' not in room_data:
                print(f"Room {i} is missing required fields.")
                sys.exit()

            self.rooms.append({
                'name': room_data['name'],
                'desc': room_data['desc'],
                'exits': room_data['exits'],
                'items': room_data.get('items', []),
            })

        for room in self.rooms:
            for exit_name, exit_id in room['exits'].items():
                if exit_id >= len(self.rooms):
                    print(f"Exit from room {room['name']} to invalid room {exit_id}.")
                    sys.exit()

    def play(self):
        self.look()
        while True:
            try:
                command = input("What would you like to do? ").lower().strip()
            except EOFError:
                print("Use 'quit' to exit.")
                continue

            if not command:
                continue

            parts = command.split()
            verb = parts[0]
            target = ''.join(parts[1:])

            if verb == 'quit':
                print("Goodbye!")
                sys.exit()
            elif verb == 'look':
                self.look()
            elif verb == 'go':
                self.go(target)
            elif verb == 'get':
                self.get(target)
            elif verb == 'getall':
                self.get_all()
            elif verb == 'drop':
                self.drop(target)
            elif verb == 'dropall':
                self.drop_all()
            elif verb == 'inventory':
                self.show_inventory()
            else:
                print(f"Unknown command '{verb}'. Type 'help' for a list of commands.")

    def get(self, item_name):
        room = self.rooms[self.current_room_id]

        if item_name not in room['items']:
            print(f"There's no {item_name} anywhere.")
            return

        print(f"You pick up the {item_name}.")
        self.inventory.append(item_name)
        room['items'].remove(item_name)

    def get_all(self):
        room = self.rooms[self.current_room_id]
        if len(room['items']) == 0:
            print("There's nothing to pick up.")
            return
        for item in room['items']:
            print(f"You pick up the {item}.")
            self.inventory.append(item)
        room['items'].clear()

    def drop(self, item_name):
        room = self.rooms[self.current_room_id]

        if item_name not in self.inventory:
            print(f"You don't have a {item_name}.")
            return
        print(f"You drop the {item_name}.")
        self.inventory.remove(item_name)
        room['items'].append(item_name)

    def drop_all(self):
        room = self.rooms[self.current_room_id]
        if len(self.inventory) == 0:
            print("You're not carrying anything.")
            return
        for item in self.inventory:
            print(f"You drop the {item}.")
            room['items'].append(item)
        self.inventory.clear()

    def show_inventory(self):
        if not self.inventory:
            print("You're not carrying anything.")
            return
        print("Inventory:")
        for item in self.inventory:
            print(f"  {item}")

    def look(self):
        room = self.rooms[self.current_room_id]
        print(f"> {room['name']}\n\n{room['desc']}\n")
        if room['items']:
            print(f"Items: {', '.join(room['items'])}\n")
        print(f"Exits: {' '.join(room['exits'])}\n")

    def go(self, direction):
        if not direction:
            print("Sorry, you need to 'go' somewhere.")
            return
        room = self.rooms[self.current_room_id]
        if direction in room['exits']:
            self.current_room_id = room['exits'][direction]
            print(f"You go {direction}.\n")
            self.look()
        else:
            print(f"There's no way to go {direction}.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python adventure.py [map filename]")
        sys.exit()
    engine = GameEngine(sys.argv[1])
    engine.play()
