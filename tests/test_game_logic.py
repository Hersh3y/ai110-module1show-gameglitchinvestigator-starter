from logic_utils import check_guess, get_range_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, message = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, message = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, message = check_guess(40, 50)
    assert result == "Too Low"


# --- Bug fix tests: get_range_for_difficulty ---

def test_difficulty_easy_range():
    # Easy should have the smallest range
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_difficulty_normal_range():
    # Normal should have a range between Easy and Hard
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_difficulty_hard_range():
    # Hard should have the largest range
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_difficulty_ranges_ordered():
    # Easy range < Normal range < Hard range
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high


# --- Bug fix tests: check_guess hint direction ---

def test_too_high_hint_says_go_lower():
    # When guess is higher than secret, hint should say go LOWER
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_hint_says_go_higher():
    # When guess is lower than secret, hint should say go HIGHER
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_correct_guess_returns_win():
    # When guess equals secret, outcome should be Win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


# --- Bug fix tests: update_score ---

def test_win_score_first_attempt():
    # Winning on attempt 1 should give 90 points (100 - 10*1)
    score = update_score(0, "Win", 1)
    assert score == 90

def test_win_score_not_over_penalized():
    # Winning on attempt 3 should give 70 points (100 - 10*3), not less
    score = update_score(0, "Win", 3)
    assert score == 70

def test_win_score_minimum_points():
    # Even on a late attempt, winning should give at least 10 points
    score = update_score(0, "Win", 20)
    assert score == 10

def test_too_high_deducts_points():
    # "Too High" should always deduct points, never add them
    score = update_score(100, "Too High", 2)
    assert score == 95

def test_too_high_deducts_on_odd_attempt():
    # "Too High" should deduct on odd attempts too
    score = update_score(100, "Too High", 3)
    assert score == 95

def test_too_low_deducts_points():
    # "Too Low" should deduct 5 points
    score = update_score(100, "Too Low", 1)
    assert score == 95
