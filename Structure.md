fit-recommender/
├── data/               # Rohdaten und vorverarbeitete Daten
│   ├── raw/            # Ungesäuberte Daten (Fashion-MNIST, Scraped Images, etc.)
│   ├── cleaned/        # Gesäuberte Daten nach der Vorverarbeitung
│   ├── annotations/    # Manuelle Labels und Metadaten
│   ├── processed/      # Vorbereitete Daten für das Training
│   ├── external/       # Zusätzliche Quellen (z. B. Zeitschriften, Pre-trained Models)
├── notebooks/          # Jupyter-Notebooks für Exploration und Prototyping
│   ├── data_analysis.ipynb
│   ├── model_training.ipynb
│   ├── scraping_experiments.ipynb
├── src/                # Hauptcode für das Projekt
│   ├── data_pipeline/  # Code für Datenaufbereitung
│   │   ├── __init__.py
│   │   ├── scrape.py   # Web Scraper
│   │   ├── preprocess.py  # Vorverarbeitung der Bilder
│   │   ├── augment.py  # Datenaugmentation
│   ├── models/         # ML-Modelle
│   │   ├── __init__.py
│   │   ├── cnn_classifier.py  # Klassifikationsmodell
│   │   ├── recommender.py     # Empfehlungsmodell
│   │   ├── feature_extraction.py
│   ├── api/            # API zur Bereitstellung
│   │   ├── __init__.py
│   │   ├── app.py      # FastAPI/Flask App
│   │   ├── routes.py   # API-Endpunkte
│   ├── utils/          # Hilfsfunktionen (z. B. Logging, Configs)
│       ├── __init__.py
│       ├── config.py
│       ├── logging.py
├── tests/              # Unit- und Integrationstests
│   ├── test_data_pipeline.py
│   ├── test_models.py
│   ├── test_api.py
├── docker/             # Docker-Konfiguration
│   ├── Dockerfile
│   ├── docker-compose.yml
├── scripts/            # Hilfsskripte für Entwicklung und Deployment
│   ├── run_scraping.sh
│   ├── start_training.sh
├── requirements.txt    # Python-Abhängigkeiten
├── README.md           # Projektdokumentation
├── .gitignore          # Git Ignore Regeln
└── .env                # Umgebungsvariablen (z. B. API-Schlüssel, DB-Verbindungen)