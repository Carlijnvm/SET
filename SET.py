class Card:
    def __init__(self,symbol,number,color,shading):
        self.symbol=symbol
        self.number=number
        self.color=color
        self.shading=shading

    def __str__(self):
        return '%s, %s, %s, %s' % (Card.symbols[self.symbol],
                           Card.numbers[self.number],
                           Card.colors[self.color],
                           Card.shadings[self.shading])

    symbols=["diamond","squiggle","oval",]
    numbers=["1","2","3"]
    colors=["red","green","purple"]
    shadings=["solid","striped","open"]

    


x = Card(1, 0, 1, 1)
print((x))
