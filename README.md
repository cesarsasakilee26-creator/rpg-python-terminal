# RPG Terminal - Sistema Testável com POO

Projeto prático de engenharia de software focado em **arquitetura orientada a objetos**, **testes unitários automatizados** e **encapsulamento avançado**. Desenvolvido como trabalho acadêmico e portfólio de backend para consolidar competências técnicas reais.

## 🎯 Competências Demonstradas
- **Encapsulamento com `@property` e Setters Blindados**: Proteção de invariantes de estado (`vida`, `mana`) com validação automática via getters/setters. [Ver implementação](src/models/personagem.py)
- **Testes Unitários (pytest)**: Validação de edge cases críticos, contratos de comportamento e regras de negócio. [Ver testes](tests/)
- **POO Aplicada**: Herança, polimorfismo e composição em domínio real (Personagens, Habilidades, Itens).
- **Design Orientado a Testes**: Código estruturado para ser testável desde a primeira linha, com injeção de dependências e separação clara de responsabilidades.
- **Padrão Strategy para Habilidades**: Classes abstratas definindo contratos, concretas implementando comportamentos únicos (`GritoDeGuerra`). [Ver habilidades](src/models/habilidades.py)

## 🧪 Executando os Testes
```bash
pip install pytest
pytest tests/ -v --tb=short