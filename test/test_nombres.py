import allure
from animales import obtener_nombres

@allure.description("test que devuelve una lista de animales ")
@allure.feature(" animales ")
@allure.epic(" listas de nombres")
def test_obtener_nombres():
    nombres = obtener_nombres()
    assert isinstance(nombres, list)
