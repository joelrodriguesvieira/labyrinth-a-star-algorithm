
def podeSacar(saldo, valorSaque, contaAtiva):
    if contaAtiva:
        if valorSaque <= saldo:
            return "Saque autorizado"
        else: 
            return "Saldo insuficiente"
    else:
        "Conta Inativa"
        
resultado = podeSacar(500, 100, True)
print(resultado)


# Tabela de Decisão 
# PodeSacar                Regra 1              Regra 2              Regra 3
# =================================================================================
# contaAtiva               Sim                  Sim                   Não
# valorSaque               Sim                  Não                    -
# =================================================================================
# Resultado Esperado       Saque Autorizado     Saldo Insuficiente    Conta Inativa



# Saldo        Valor do Saque      Conta Ativa?       Resultado Esperado     
# =======================================================================
# 500           100                 true               Saque Autorizado
# 500           600                 true               Saldo Insuficiente
# 500           100                 false              Conta Inativa


def calcular_frete(valor_compra, regiao):
  if valor_compra >= 100:
    return "Frete grátis"
  else:
    if regiao in ["Norte", "Nordeste"]:
      return "Frete: R$ 20,00"
    else:
      return "Frete: R$ 10,00"
    
    
# Valor da Compra             Região         Resultado Esperado
# =============================================================
# 150                         Sul             Frete Grátis
# 80                          Norte           Frete: R$20.00
# 80                          Sul             Frete: R$10.00 