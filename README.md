\# Network Inventory Scanner 🔍



\## 📝 Descrição

Ferramenta desenvolvida em Python para automação de inventário de rede local (LAN). O script identifica dispositivos ativos, mapeia endereços IP/MAC e consulta os fabricantes de hardware.



\## 🛠️ Como Funciona

\* \*\*Protocolo ARP:\*\* Envia requisições de broadcast para descobrir quem está na rede.

\* \*\*Mapeamento de Camada 2:\*\* Identifica o endereço físico (MAC) de cada dispositivo.

\* \*\*Consulta OUI:\*\* Traduz os primeiros bytes do MAC para identificar o fabricante (Ex: Dell, Intel, TP-Link).



\## 📄 Arquivos no Repositório

\* `monitor\_rede.py`: Script principal em Python.

\* `inventário\_final.csv`: Relatório gerado com os dados coletados no estágio.



---

\*Projeto realizado para consolidar conhecimentos de Redes e Automação.\*

