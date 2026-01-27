# test_studies
## Repositório onde contém estudos sobre testes de software com python, estou usando principalmente a lib pytest

O uso do pytest para testes E2E envolve a criaçao de testes que simulam cenários reais de usuários, validando a funcionalidade completa do aplicativo.

Os testes E2E são particularmente importantes para aplicativos complexos com múltiplos subsistemas interconectados, pois ajudam a identificar problemas que podem não ser evidentes ao testar componentes individuais de forma isolada.

## Tipos de testes e seus propósitos

Testes de Unidade (Base da pirâmide): Testes rápidos e isolados que verificam se funções ou métodos individuais funcionam corretamente. Eles constituem a maioria dos testes devido à sua velocidade e baixo custo de manutenção.

Testes de Integração (Camada do meio): Testes que verificam se as interações entre componentes ou sistemas funcionam corretamente. Esses testes são mais complexos do que os testes de unidade, mas ainda se concentram em integrações específicas.

Testes de Sistema: Valida que todo o sistema atende a requisitos especificados, testando o software completo e integrado.

Testes E2E (Topo da pirâmide): Testes abrangentes que validam todo o fluxo do aplicativo do início ao fim, simulando cenários reais de usuários em todos os sistemas integrados.

# Materiais de estudo:

https://github.com/personalnerd/teste-e2e/blob/main/2.%20Melhores%20pr%C3%A1ticas%20para%20cria%C3%A7%C3%A3o%20e%20automa%C3%A7%C3%A3o%20de%20testes%20E2E.md

https://apidog.com/pt/blog/e2e-testing-pt/

https://docs.pytest.org/en/stable/

https://www.datacamp.com/pt/tutorial/pytest-tutorial-a-hands-on-guide-to-unit-testing

O pytest só reconhece automaticamente marcas como:

skip
xfail
parametrize
slow (em alguns plugins)

## Conceitos sobre JWT
base64 - módulo da biblioteca padrão python para codificação e decodificação Base64

JWT - biblioteca pyJWT para criar, assinar e validar tokens. Funções principais: jwt.encode() - cria token, jwt.decode() - verifica token

Chave - Segredo usado para assinar o JWT

Algoritmo - Algoritmo da assinatura, combina header + payload + chave

jwt.encode(payload, chave, algorithm) - converte payload para JSON, codifica header e payload em Base64 URL-safe, gera assinatura usando a chave, retorna uma string JWT: header.payload.signature