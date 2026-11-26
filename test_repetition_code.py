from repetition_code import decode, encode, logical_error_rate


def test_encode_repeats_the_bit():
    assert encode(1, 3) == [1, 1, 1]


def test_decode_corrects_a_single_flip():
    assert decode([1, 0, 1]) == 1


def test_no_noise_means_no_errors():
    assert logical_error_rate(p=0.0, n=3, trials=1000) == 0.0


def test_more_repetitions_reduce_errors():
    one = logical_error_rate(p=0.1, n=1, trials=20000)
    three = logical_error_rate(p=0.1, n=3, trials=20000)
    assert three < one