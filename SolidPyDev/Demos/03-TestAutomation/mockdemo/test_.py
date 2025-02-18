import mockdemo.myCode as myCode

def test_build_url(mocker):

    mocker.patch.object(myCode, 'BASE_URL', 'http://localhost/products')

    actual = myCode.build_url(minPrice=100, maxPrice=500, order='desc')
    expected = 'http://localhost/products?minPrice=100&maxPrice=500&order=desc'
    assert expected == actual


def test_get_meaning_of_life(mocker):

    mocker.patch(
        'mockdemo.myCode.calculate_meaning_of_life',
        return_value='wibble'
    )

    actual = myCode.get_meaning_of_life()
    expected = 'The meaning of life is wibble'
    assert expected == actual


def test_get_product(mocker):

    mocker.patch(
        'mockdemo.myCode.DataLoader.load_product',
        lambda self: 'wibble'
    )

    actual = myCode.get_product()

    expected = 'Product is wibble'

    assert expected == actual
