# Create chess Tournament Report Files (TRF)

## Prerequisites

- Create an account in [ChessManager](https://chessmanager.com/).
- Copy the code of this GitHub repository, select **Code – Download ZIP**.
- [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/), used for running the scripts below.

> [!TIP]
> Install a browser add-on to show up-to-date results, say, [Easy Auto Refresh](https://chromewebstore.google.com/detail/easy-auto-refresh/aabcgdmkeabbnleenpncegpcngjpnjkc) for Chrome.

## Creating the input data

1. Create your customized **tournament info**:
- Create a file named `data/input/tournament.trf`.
- Reuse the `data/samples/tournament.trf` template if needed.

See the [Tournament Report File format](https://tornelo.com/knowledge-base/trfx-file-format/).

2. Download the **latest ratings** in the `data/input/selolista.csv` file:

```bash
./trfx -d
```

3. Create the **list of participants** (in the `data/input/players.csv` file):

```csv
last-name,first-name,club
Carlsen,Magnus,2823
Heikkinen,Jyrki,2062
```

> [!NOTE]
> The following data in the participants file are ignored:
> - The first line, which should be a header.
> - Extra fields after the `club` field.

For example, if participants are in Google Sheet,
- export them as CSV, and
- verify that the order of fields is correct.

Verify that all the participants are found from the ratings list:

```bash
./trfx
```

Fix the player data manually if needed. The player names are case-insensitive.

## Running tournaments

1. Generate Tournament Report Files, and divide the players into them:

```bash
./trfx -g 10 24 38
```

The numbers after the `g` argument are the **indexes of the last player** in each group.

The files are created in `data/output/tournament-*.trf`.

2. Create tournaments:

- Log in to ChessManager.
- Select **New Tournament**.
- Select **Import From File**, and choose the generated TRF file from the `data/output` directory.

Once the first round has started, add _Club_ for each player if needed.

3. Export results

After a tournament has finished, export its results for rating calculation:
- Select **Dashboard – Basic information – Export – TRF 2026**.

## Other

For all options, see

```bash
trfx --help
```
