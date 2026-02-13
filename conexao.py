import speedtest

def executar_teste():
    print("Iniciando teste de velocidade... Aguarde.")
    
    try:
        st = speedtest.Speedtest()
        
        # Encontra o melhor servidor baseado no ping
        st.get_best_server()
        
        # Realiza os testes
        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000
        ping = st.results.ping
        
        print("-" * 30)
        print(f"Download: {download:.2f} Mbps")
        print(f"Upload: {upload:.2f} Mbps")
        print(f"Ping: {ping:.2f} ms")
        print("-" * 30)
        
    except Exception as e:
        print(f"Erro ao realizar o teste: {e}")

if __name__ == "__main__":
    executar_teste()