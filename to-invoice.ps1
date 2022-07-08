$INVOICE_DIR = "G:\マイドライブ\Projects\go\src\github.com\s-ariga\club-invoice"
$INVOICE_INPUT = "G:\マイドライブ\Projects\go\src\github.com\s-ariga\club-invoice\input\全射手一覧.csv"
$DATA_FILE = "..\output\全射手一覧.csv"


Copy-Item $DATA_FILE $INVOICE_INPUT
Set-Location $INVOICE_DIR