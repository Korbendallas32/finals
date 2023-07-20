from app import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()
#Positive

def test_get_api_key_valid_user(email=valid_email, password=valid_password):
    '''Проверяем что код статуса запроса 200 и в переменной result
    содержится слово key'''
    status, result = pf.get_app_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    '''Проверяем код статуса запроса 200 и список всех питомцев не пустой'''
    _, api_key = pf.get_app_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(api_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_pets_with_valid_data(name='Martin', animal_type='cat', age='5', pet_photo='images/CAT_Martin.jpg'):
    '''Проверяем код статуса 200 и что список с добавленными данными не пустой'''
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, api_key = pf.get_app_key(valid_email, valid_password)
    status, result = pf.add_new_pets(api_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


#Negative


def test_get_api_key_with_wrong_password_and_correct_mail(email=valid_email, password=invalid_password):
    '''Проверяем запрос с неверным паролем и с верной почтой.
    Проверяем нет ли ключа в ответе'''
    status, result = pf.get_app_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_api_key_with_wrong_email_and_correct_password(email=invalid_email, password=valid_password):
    '''Проверяем запрос с недействительным паролем и с действительной почтой.
    Проверяем нет ли ключа в ответе'''
    status, result = pf.get_app_key(email, password)
    assert status == 403
    assert 'key' not in result
