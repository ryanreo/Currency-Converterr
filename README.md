# Currency Converter

A minimal single-page currency converter with **real-time exchange rates** powered by the ExchangeRate-API.

## Features

- Convert between **USD, EUR, KES, GBP, INR**
- Live exchange rates fetched from ExchangeRate-API (v6)
- Instant conversion with a single click

## Tech Stack

- Python, Flask
- Server-rendered HTML with vanilla JS
- ExchangeRate-API v6

## Getting Started

```bash
pip install flask requests
python currency.py
```

Opens on `http://localhost:5000`.

## API Endpoint

- `GET /` — converter page
- `POST /convert` — body `{"amount": 100, "from": "USD", "to": "KES"}` → `{"converted_amount": ...}`

## Note

The API key is currently hardcoded in `currency.py` — move it to an environment variable. A `requirements.txt` is also worth adding (`flask`, `requests`).
