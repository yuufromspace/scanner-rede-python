from scapy.all import ARP, Ether, srp
import urllib.request
import time
import csv
import os

def get_vendor(mac):
    """Tenta descobrir quem fabricou o aparelho pelo MAC."""
    try:
        # Pausa de 1.5s para a API não nos bloquear
        time.sleep(1.5)
        url = f"https://api.macvendors.com/{mac}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.read().decode('utf-8')
    except:
        return "Fabricante Oculto ou Desconhecido"

def inventario_completo():
    pasta_destino = r"C:\projeto"
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    caminho_final = os.path.join(pasta_destino, "inventario_final.csv")
    
    print("--- 🔍 INICIANDO MAPEAMENTO DE REDE ---")
    
    # Escaneando a rede 192.168.0.0/24
    respostas, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.0.0/24"), timeout=3, verbose=False)

    dados = []
    print(f"Encontrados {len(respostas)} dispositivos. Identificando fabricantes...")

    for _, recebido in respostas:
        ip = recebido.psrc
        mac = recebido.hwsrc
        
        # Chamando a função de fabricante
        vendor = get_vendor(mac)
        print(f"✔ Identificado: {ip} | {vendor}")
        
        dados.append([ip, mac, vendor])

    # Salvando os resultados
    try:
        with open(caminho_final, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["IP", "MAC", "FABRICANTE"])
            writer.writerows(dados)
        print(f"\n✅ PROJETO CONCLUÍDO!")
        print(f"Relatório detalhado salvo em: {caminho_final}")
    except Exception as e:
        print(f"\n❌ Erro ao salvar: {e}")

if __name__ == "__main__":
    inventario_completo()