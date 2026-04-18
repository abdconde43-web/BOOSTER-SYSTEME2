import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def run_viewer():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--mute-audio")
    
 # --- LES PROXIES (Rotation Automatique Mondiale) ---
    def get_fresh_proxies():
        url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        try:
            return requests.get(url).text.splitlines()
        except:
            return ["103.152.112.162:80", "185.201.88.128:8080"]

    proxies = get_fresh_proxies()
    proxy = random.choice(proxies)
    chrome_options.add_argument(f'--proxy-server={proxy}')
    print(f"Robot lancé avec l'IP : {proxy}")
        # Ajoute ici tes proxies résidentiels si tu en achètes
    proxy = random.choice(proxies)
    chrome_options.add_argument(f'--proxy-server={proxy}')

    # --- AGENTS UTILISATEURS (Anti-détection) ---
    u_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
    ]
    chrome_options.add_argument(f"user-agent={random.choice(u_agents)}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # --- TA LISTE DE VIDÉOS ---
    mes_videos = [
        "https://www.youtube.com/watch?v=KQf6UWeO1uQ",
        "https://www.youtube.com/watch?v=KQf6UWeO1uQ"
    ]

    try:
        video = random.choice(mes_videos)
        driver.get(video)
        
        # --- RÈGLE DES 40% (Watch Time) ---
        # On reste entre 1 et 3 minutes pour simuler un vrai intérêt
        wait = random.randint(60, 180) 
        print(f"Vue via {proxy} sur {video} pendant {wait}s...")
        time.sleep(wait)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    run_viewer()
