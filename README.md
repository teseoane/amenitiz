# Amenitiz Technical Evaluation

## Objective

Build an application responding to these needs. 

By application, we mean:
- It can be a simple CLI application
- It is usable while remaining as simple as possible
- It is readable
- It is maintainable
- It is easily extendable

## Technical requirements

- Use any of those languages you are comfortable (Ruby, Python, Go, .Net Core)
- Covered by tests
- Following TDD methodology

## Description

### Assumptions 

**Products Registered**
| Product Code | Name | Price |  
|--|--|--|
| GR1 |  Green Tea | 3.11€ |
| SR1 |  Strawberries | 5.00 € |
| CF1 |  Coffee | 11.23 € |

**Special conditions**

- The CEO is a big fan of buy-one-get-one-free offers and green tea. 
He wants us to add a  rule to do this.

- The COO, though, likes low prices and wants people buying strawberries to get a price  discount for bulk purchases. 
If you buy 3 or more strawberries, the price should drop to 4.50€.

- The VP of Engineering is a coffee addict. 
If you buy 3 or more coffees, the price of all coffees should drop to 2/3 of the original price.

Our check-out can scan items in any order, and because the CEO and COO change their minds  often, it needs to be flexible regarding our pricing rules.

**Test data**
| Basket | Total price expected |  
|--|--|
| GR1,GR1 |  3.11€ |
| SR1,SR1,GR1,SR1 |  16.61€ |
| GR1,CF1,SR1,CF1,CF1 |  30.57€ |

## Project SetUp (Python)

1. Clone the repository:
    ```bash
    git clone git@github.com:teseoane/amenitiz.git
    ```
2. Create a virtualenv with python >= 3.6 and activate it:
    ```bash
    cd amenitiz
    pyenv virtualenv 3.10.3 amenitiz
    pyenv activate amenitiz
    ```
3. Run tests:
    ```bash
    python -m unittest tests/*.py
    ```

## Notes:

There are validations and functionalities to be done but I don't think they are the focus of the exercise, like:
- Product fields (code, name and price) validatios (not None, not empty, strings and decimals).
- Cart functionalities like empty cart and remove product.
- Cart validations like prevent remove products if amount equals 0
