def check_answers(user_answer, right_answer, test_try, scores, question):

    wrong_answer = None
    if user_answer == right_answer:
        test_try.right_answers_quantity += 1
        test_try.points_quantity += scores
        test_try.save()
    else:
        wrong_answer = question.name

    return wrong_answer


def check_test_pass(points, points_to_pass, test_try):

    if points >= points_to_pass:
        test_try.is_passed = True
        test_try.save()