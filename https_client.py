import socket
import ssl
import sys

if len(sys.argv) != 4:
    print("Uso:")
    print(f"python {sys.argv[0]} site recurso arquivo")
    exit()

site = sys.argv[1]
recurso = sys.argv[2]
arquivo = sys.argv[3]

porta = 80
usar_ssl = False

if site.startswith("https://"):
    site = site.replace("https://", "")
    porta = 443
    usar_ssl = True

elif site.startswith("http://"):
    site = site.replace("http://", "")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if usar_ssl:
    contexto = ssl.create_default_context()
    s = contexto.wrap_socket(s, server_hostname=site)

s.connect((site, porta))

pedido = (
    f"GET {recurso} HTTP/1.1\r\n"
    f"Host: {site}\r\n"
    "Connection: close\r\n\r\n"
)

s.sendall(pedido.encode())

resposta = b""

while True:
    parte = s.recv(1024)

    if not parte:
        break

    resposta += parte

s.close()

separador = b"\r\n\r\n"
pos = resposta.find(separador)

if pos == -1:
    print("Erro ao receber resposta")
    exit()

cabecalho = resposta[:pos].decode(errors="ignore")
dados = resposta[pos + 4:]

if "transfer-encoding: chunked" in cabecalho.lower():
    print("Recebendo dados em chunks")

    conteudo = b""
    resto = dados

    while True:
        fim = resto.find(b"\r\n")

        if fim == -1:
            print("Erro ao ler chunk")
            break

        tamanho_hex = resto[:fim].decode()
        tamanho = int(tamanho_hex, 16)

        if tamanho == 0:
            break

        inicio = fim + 2
        final = inicio + tamanho

        conteudo += resto[inicio:final]

        resto = resto[final + 2:]

    dados = conteudo

elif "content-length" in cabecalho.lower():
    print("Content-Length encontrado")

print(cabecalho.split("\r\n")[0])

with open(arquivo, "wb") as f:
    f.write(dados)

print(f"Arquivo salvo: {arquivo}")