full_dot = '●'
empty_dot = '○'
def create_character (name, strength, intelligence, charisma):

    if type(name) != str:
        return 'The character name should be a string'

    if len(name) == 0:
        return 'The character should have a name'

    if len(name) > 10:
        return 'The character name is too long'
    
    if ' ' in name:
        return 'The character name should not contain spaces'
    
    if not all(isinstance(s, int) for s in (strength, intelligence, charisma)):
        return 'All stats should be integers'
            
    if any (s < 1 for s in (strength, intelligence, charisma)):
        return 'All stats should be no less than 1'
        
    if any (s > 4 for s in (strength, intelligence, charisma)):
        return 'All stats should be no more than 4'
        
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    
    def stat_line(label, value):
        full = '●' * value
        empty = '○' * (10 - value)
        return f'{label} {full}{empty}'

    result = [
        name,
        stat_line('STR', strength),
        stat_line('INT', intelligence),
        stat_line('CHA', charisma)
    ]

    return '\n'.join(result)

print(create_character('robotlee', 2, 4, 1))