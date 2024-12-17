from app_test.models import TestTry, Question


def check_answers(
    user_answer: int,
    right_answer: int,
    test_try: TestTry,
    scores: int,
    question: Question,
) -> str | None:
    """Проверяет ответ на правильность если ответ не правильный, возвращает вопрос на который не ответили"""

    question_with_wrong_answer = None
    if user_answer == right_answer:
        test_try.right_answers_quantity += 1
        test_try.points_quantity += scores
        test_try.save()
    else:
        question_with_wrong_answer = question.name

    return question_with_wrong_answer


def check_test_pass(points: int, points_to_pass: int, test_try: TestTry) -> None:
    """ "Проверяет сдан ли тест, сравнивая количество необходимых баллов с набранными"""

    if points >= points_to_pass:
        test_try.is_passed = True
        test_try.save()
