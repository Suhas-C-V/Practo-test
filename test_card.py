from Card import Card

def test_card():
	x = 79927398713
	instance = Card()
	assert instance.LuhnAlgo(x) == True, "It works"