# Prova - Forth

Leia os exercícios em [questao-08.md](questao-08.md) e
[questao-09.md](questao-09.md) e implemente as funcionalidades
descritas lá nos arquivos `questao-08.fs` e `questao-09.fs`.


## Testes

Use o próprio forth para testar suas implementações localmente. Depois, confira
se os testes automatizados estão passando usando `pytest`:

```bash
pytest tests/ -v
```

Existem várias opções no pytest que permitem rodar apenas um teste específico,
ou um grupo de testes, apenas os que falharam na última execução, etc. Consulte
a documentação do pytest para mais detalhes. Seguem alguns exemplos mais comuns:


```bash
# Rodar apenas um teste específico (filtra por nome):
pytest -k nome_da_palavra -v

# Rodar apenas testes que falharam na última execução:
pytest --lf

# Limita número de testes erros
pytest --maxfail=1
```

## Entrega

A entrega consiste em copiar e colar o código dos arquivos `questao-08.fs` e
`questao-09.fs` nas caixas de texto das respectivas questões na avaliação do
Moodle. Certifique-se de que o código esteja correto e completo antes de enviar.
