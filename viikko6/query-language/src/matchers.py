class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):    
        return True

class Not:
    def __init__(self,matcher):
        self._matcher = matcher

    def matches(self, player):
        return not self._matcher.matches(player)

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value



class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        
        return False


class QueryBuilder:
    def __init__(self, matcher=None):
        if matcher is None:
            self.matcher = All()
        else:
            self.matcher = matcher

    def build(self):
        return self.matcher

    def playsIn(self, team):
        #return QueryBuilder(PlaysIn(team))
        return QueryBuilder(And(self.matcher, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        #return QueryBuilder(HasAtLeast(value, attr))
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        #return QueryBuilder(HasFewerThan(value, attr))
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attr)))
    



