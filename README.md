# Adventure Game

## Student Information

- Name: Jigar Chhatrala
- Stevens Login: jchhatra@stevens.edu

## Project Information

- Public GitHub Repo URL: https://github.com/jigargc/Adventure-Game.git
- Estimated Hours Spent: 20 hours

## Testing

I thoroughly tested my code by writing unit tests for each function, as well as manually testing edge cases and
verifying the correctness of the output.

## Known Bugs and Issues

- In some cases, the application might not handle incorrect user input gracefully, causing unexpected behavior.

## Resolving a Difficult Issue

N/A

## Implemented Extensions

1. **Extension 1: drop**
    - New verb: "drop" to drop an item from the player's inventory.
    - To exercise this new verb, use "drop" followed by the item name, e.g., "drop sword."
    - The dropped item will be placed in the current location.
    - If the item is not in the player's inventory, the application will print an error "You don't have a {item_name}".


2. **Extension 2: dropall**
    - New verb: "dropall" to drop all items from the player's inventory.
    - To exercise this new verb, use "dropall"
    - All items in the player's inventory will be dropped in the current location.
    - If the player's inventory is empty, the application will print an error "You're not carrying anything."

3. **Extension 3: getall**
    - New verb: "getall" to get all items from the current location.
    - To exercise this new verb, use "getall"
    - If the current location has no items, the application will print an error "There's nothing to pick up."
