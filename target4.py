dados = {"SP":67836.43, 
         "RJ":36678.66,
         "MG":29229.88,
          "ES":27165.48,
          "outros":19849.53
        }

soma = 0
for i in dados:
    soma = soma + dados[i]
print(soma)



porcentSP = (dados.get("SP")/soma) * 100

porcentRJ = (dados.get("RJ")/soma) * 100

porcentMG = (dados.get("MG")/soma) * 100

porcentES = (dados.get("ES")/soma) * 100

porcentOutros = (dados.get("outros")/soma) * 100

print(f"% SP = {porcentSP:.2f}")
print(f"% RJ = {porcentRJ:.2f}")
print(f"% MG = {porcentMG:.2f}")
print(f"% ES = {porcentES:.2f}")
print(f"% outros = {porcentOutros:.2f}")

print(porcentSP + porcentES + porcentOutros + porcentMG + porcentRJ)