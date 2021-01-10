# lana-sre-challenge

## Original description

The original description of the challenge, taken from [lana/sre-challenge](https://github.com/lana/sre-challenge).

Lana has come to conclusion that users are very likely to buy awesome Lana merchandising from a physical store that sells the following 3 products:

```
Code         | Name              |  Price
-----------------------------------------------
PEN          | Lana Pen          |   5.00€
TSHIRT       | Lana T-Shirt      |  20.00€
MUG          | Lana Coffee Mug   |   7.50€
```

Various departments have insisted on the following discounts:

 * The sales department thinks a buy 2 get 1 free promotion will work best (buy two of the same product, get one free), and would like this to only apply to `PEN` items.

 * The CFO insists that the best way to increase sales is with discounts on bulk purchases (buying x or more of a product, the price of that product is reduced), and requests that if you buy 3 or more `TSHIRT` items, the price per unit should be reduced by 25%.

Your task is to implement a simple checkout HTTP API.

We'd expect the server to expose the following independent operations:

- Create a new checkout basket
- Add a product to a basket
- Get the total amount in a basket
- Remove the basket

Implement a checkout service that fulfills these requirements.

Examples:

    Items: PEN, TSHIRT, MUG
    Total: 32.50€

    Items: PEN, TSHIRT, PEN
    Total: 25.00€

    Items: TSHIRT, TSHIRT, TSHIRT, PEN, TSHIRT
    Total: 65.00€

    Items: PEN, TSHIRT, PEN, PEN, MUG, TSHIRT, TSHIRT
    Total: 62.50€

**The solution should:**

- Build and execute in a Unix operating system using Docker
- Create a CI pipeline to release the application

**Bonus Points For:**

- Focus on solving the business problem (less boilerplate!)
- Don't include binaries, and use a dependency management tool
- Have a clear structure
- Unit/Functional tests
- Useful comments
- Documentation
- Commit messages (include .git in zip, avoid big bulk changes)
- Enable monitoring on the application
- Curl examples to test the endpoints

## The Solution