class BrowserHistory:

    def __init__(self, homepage: str):
         self.history = [homepage]
         self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current + 1]

        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        if self.current - steps < 0 :
            self.current = 0
        else:
            self.current -= steps
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        x = len(self.history)-1
        if self.current + steps > x:
            self.current = x
        else:
            self.current += steps 
        return self.history[self.current]