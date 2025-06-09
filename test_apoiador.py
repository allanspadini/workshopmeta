import pytest
from unittest.mock import MagicMock
from apoiador import analisar_requisicao

@pytest.fixture
def mock_llm():
    mock = MagicMock()
    class MockChain:
        def invoke(self, args):
            return {
                "requisitos_funcionais": [
                    "Permitir que o usuário crie uma conta",
                    "Permitir que o usuário faça login",
                    "Permitir que o usuário visualize seu perfil"
                ],
                "atores": ["usuário"],
                "dados_necessarios": ["nome", "email", "senha", "perfil"]
            }
    mock.__or__ = lambda self, other: MockChain()
    return mock

def test_analisar_requisicao_returns_structured_data(monkeypatch, mock_llm):
    from langchain_core.runnables.base import Runnable

    class DummyParser(Runnable):
        def get_format_instructions(self):
            return "formato de exemplo"

        def invoke(self, input, config=None, **kwargs):
            return {
                "requisitos_funcionais": [
                    "Permitir que o usuário crie uma conta",
                    "Permitir que o usuário faça login",
                    "Permitir que o usuário visualize seu perfil"
                ],
                "atores": ["usuário"],
                "dados_necessarios": ["nome", "email", "senha", "perfil"]
            }


    monkeypatch.setattr("apoiador.JsonOutputParser", DummyParser)

    requisicao = "O sistema deve permitir que o usuário crie uma conta, faça login e visualize seu perfil."
    result = analisar_requisicao(requisicao, mock_llm)

    assert isinstance(result, dict)
    assert "requisitos_funcionais" in result
    assert "atores" in result
    assert "dados_necessarios" in result
    assert "Permitir que o usuário crie uma conta" in result["requisitos_funcionais"]
    assert "usuário" in result["atores"]
    assert "nome" in result["dados_necessarios"]
