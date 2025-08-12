import logging

# Configurare logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),                # consolă
        logging.FileHandler("app.log")          # fișier
    ]
)

logger = logging.getLogger(__name__)
