# 4. Crie uma lista com 5 strings e exiba a mais longa.

palavras = ['zabbix','grafana','agent','snmp','coca-cola']
maior_palavra = 0 

for i in range (len(palavras)):
    if len(palavras[i]) > maior_palavra:
        maior_palavra=i

print("A maior palavra é %s."%(palavras[maior_palavra]))
