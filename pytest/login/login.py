class RRSS:
    def __init__(self):
        self.accounts = {}
        self.current_online_accounts = 0
        
    def create_account(self, nickname: str, password: str) -> None:
        self.accounts[nickname] = password
    
    def login(self, nickname: str, password: str) -> bool:
        if nickname in self.accounts:
            return password == self.accounts.get(nickname)
        return False