import utils


def test_alterar_case_ma():
    assert utils.mudar_para_maiuscula("julio") == "JULIO"
    assert utils.mudar_para_maiuscula("12julio") == "12JULIO"
    assert utils.mudar_para_maiuscula("_%&julio") == "_%&JULIO"


def test_alterar_case_mi():
    assert utils.mudar_para_minuscula("TESTE1") == "teste1"
    assert utils.mudar_para_minuscula("(-_-)") == "(-_-)"
    assert utils.mudar_para_minuscula("(-_JULIO-)") == "(-_julio-)"
