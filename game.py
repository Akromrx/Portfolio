class Character:
    def __init__(self, damage, health, defense, IDD, name):
        self.ID = IDD
        self.name = name
        self.level = 1
        self.defense = (defense * self.level)
        self.damage = (damage * self.level)
        self.health = (health * self.level)
        self.dead = False
    
    def Attack(self, opp):
        """
        Attack the given opponent

        It attacks the opponent, giving him the damage of "self.damage"

        Increase the self.damage by leveling up
        """
        opp.Defense(self.damage)
        self.level += 0.1
        self.damage = (self.damage * self.level)
    
    def Defense(self, dmg):
        nach = self.health
        self.health -= (dmg / self.defense)
        auch = self.health
        print(f"Damage taken: {nach - auch}")
        if self.health <= 0:
            self.dead = True
    

class Warrior(Character):
    def __init__(self, damage, health, defense, superpower, IDD, name):
        super().__init__(damage, health, defense, IDD, name)
        self.superpower = superpower
    
    def SuperAttack(self, opp):
        for i in range(self.superpower):
            opp.Defense(self.damage)

    def Show(self):
        print(f"Player {self.name} #{self.ID}\n\nHealth: {self.health}\nLevel: {self.level}\nDamage: {self.damage}\n---------------------")

W1: Warrior = Warrior(5, 230, 2, 5, "01", "Cenrol")
W2: Warrior = Warrior(4, 250, 3, 4, "07", "Apolip")

W2.Show()
W1.Show()
W1.Attack(W2)
W2.Show()
W1.Show()
W1.Attack(W2)
W2.Show()
W1.Show()
