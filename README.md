# Tournament Report File for a chess tournament

## Prerequisites

- Create an account in [ChessManager](https://chessmanager.com/).
- Copy the code of this GitHub repository, select **Code** – Download ZIP.
- [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/), used for running the scripts below.

## Creating a tournament

1. Download the latest `selolista.csv`:

```bash
uv run -m trf --download-ratings
```

2. Create the [Tournament Report File](https://tornelo.com/knowledge-base/trfx-file-format/) based on `tournament.trf`.

3. Create the `players.csv` file that contains the participants:

- One each line.
- Format is `first-name,last-name,club`.

Example:

```csv
Jyrki,Heikkinen,2064
```

4. Verify that all the registrants are found from the ratings list:

```bash
uv run -m trf --players players.csv
```

5. Generate one or more tournament files, and divide players into them:

```bash
uv run -m trf --players players.csv --tournament my_tournament.trf --group_ends 10 24 38
```

6. Create tournaments:

- Log in to ChessManager.
- Select **New Tournament**.
- Select **Import From File**, and choose the generated TRF file.
- Add the club for each player if needed.
