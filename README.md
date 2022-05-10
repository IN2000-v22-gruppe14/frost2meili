# frost2meili

Et enkelt skript som henter data fra [Metereologisk institutt sitt "Frost" lokasjons-API](https://frost.met.no/api.html#/locations) og indekserer i [Meilisearch](https://github.com/meilisearch/meilisearch).

*Dette forutsetter at man har en kjørende instans av Meilisearch*

## Kom i gang

1. Endre navn på [.env.example](.env.example) til `.env` og fyll inn verdier

   - `CLIENT_ID` og `CLIENT_SECRET` er dine credentials fra Frost-APIet
   - `MEILI_ROOT` er rot-URI til meiliinstansen din.

2. Last ned avhengigheter

```
pip install -r requirements.txt -U
```

3. Kjør skript

```
python main.py
```
