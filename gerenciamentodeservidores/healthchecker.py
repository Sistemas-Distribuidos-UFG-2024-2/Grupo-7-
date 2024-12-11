import requests

def check_service_health(url):
    """
    Verifica a saúde de um serviço enviando uma solicitação HTTP GET.

    :param url: URL do serviço a ser verificado.
    :return: Dicionário contendo o status do serviço.
    """
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return {"status": "healthy", "code": response.status_code, "response_time": response.elapsed.total_seconds()}
        else:
            return {"status": "unhealthy", "code": response.status_code, "response_time": response.elapsed.total_seconds()}
    except requests.exceptions.RequestException as e:
        return {"status": "unreachable", "error": str(e)}

# Exemplo de uso
if __name__ == "__main__":
    url_to_check = "https://api.github.com"
    health_status = check_service_health(url_to_check)
    print(f"Health status for {url_to_check}: {health_status}")
