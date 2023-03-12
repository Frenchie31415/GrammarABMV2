def node_accuracy(actual,expected):
    correct = 0
    total = len(expected)

    for elem in actual:
        if elem in expected:
            correct = correct + 1
    
    return round(correct / float(total),3) * 100