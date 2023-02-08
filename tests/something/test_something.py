import requests
import pytest

from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statuses
from src.baseclasses.response import Response

@pytest.mark.parametrize("status", Statuses.list())
def test_generator_changing(status, get_player_generator):
    """
    Играемся с генератором, который был получен с помощью фикстуры.
    Вы можете попробовать изменить значение, написать новые методы и посмотреть
    как он будет реагировать.
    Playing with generator, that we received from fixture.
    Here you can change values, write some new useful methods and check how
    will it work.
    """
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_deleting_keys_in_object(delete_key, get_player_generator):
    """
    Пример того, как мы в определённом порядке удаляем каждое поле в объекте,
    который нам вернул генератор.
    Example of case when we delete one by one keys in received object.
    """
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    # print(object_to_send)


@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR")
])
def test_updating_localization_in_generator(
        get_player_generator,
        localizations,
        loc
):
    """
    В этом примере мы получаем 2 генератора, один базовый и один, который ниже
    уровнем. Когда мы получили их, изменяем в генераторе локализацию, создаём
    экземпляр и обновляем им наш главный объект.
    In the test we receive two generators, first is main and second is included
    into first. We change localization in generator and update main using
    instance of second.
    """
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization(loc).set_number(15).build()
    ).build()
    print(object_to_send)