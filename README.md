- > LAB - Class 06-07
- > Project:Ten A Thousand Game ( Game of greed's )
  - > Authors:
      - Group ONE
  - Students: 
    - Yousef AL Farwan 
    - Mohammad Al shish
    - Shatha Alrayyani
    - Hamad AlDwairi 
> we defined each class then create these methods : 
> - calculate_score : to get score based on the game rules 
> - roll_dice: return tuple of random integers between 1 and 6 
> - Shelf: return temporarily store unbanked points
> - Bank: return the amount of points added to total from shelf.
> - clear_shelf: remove all unbanked points.

>- Lab 07 Requirements
- [x] Application should implement all features from previous version
  - [x] Application should simulate rolling between 1 and 6 dice
  - [x] Application should allow user to set aside dice each roll
  - [x] Application should allow “banking” current score or rolling again.
  - [x] Application should keep track of total score
  - [x] Application should keep track of current round
  - [x] Application should have automated tests to ensure proper operation


>- Lab 08 Requirements
-[x] Application should implement features from versions 1 and 2
  - [x] Should handle setting aside scoring dice and continuing turn with remaining dice.
  - [x] Should handle when cheating occurs
  - [x] Should allow user to continue rolling with 6 new dice when all dice have scored in current turn
  - [x] Handle zilch
  - [x] Must pass provided unit and simulation tests.


>Tests
- How do you run tests?
     - pytest -v
     - All tests PASSED

> Run game 
- python .\ten_thousand\game.py