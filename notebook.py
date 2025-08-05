import pandas as pd
import numpy as np

# Read in csv
marketing = pd.read_csv("bank_marketing.csv")

# Create copies when splitting to avoid view vs copy issues
client = marketing[["client_id", "age", "job", "marital", 
                   "education", "credit_default", "mortgage"]].copy()
campaign = marketing[["client_id", "number_contacts", "month", "day", 
                     "contact_duration", "previous_campaign_contacts", 
                     "previous_outcome", "campaign_outcome"]].copy()
economics = marketing[["client_id", "cons_price_idx", 
                      "euribor_three_months"]].copy()

## Editing the client dataset
# Clean education column
client.loc[:, "education"] = (client["education"]
                             .str.replace(".", "_")
                             .replace("unknown", np.nan))  # Changed to lowercase nan

# Clean job column
client.loc[:, "job"] = client["job"].str.replace(".", "_")

# Clean and convert client columns to bool data type
bool_map = {"yes": True, "no": False, "unknown": False}
for col in ["credit_default", "mortgage"]:
    client.loc[:, col] = client[col].map(bool_map)

## Editing the campaign dataset
# Change outcomes to boolean values directly
campaign.loc[:, "campaign_outcome"] = campaign["campaign_outcome"].map({"yes": True, "no": False})
campaign.loc[:, "previous_outcome"] = campaign["previous_outcome"].map({
    "success": True, 
    "failure": False,
    "nonexistent": False
})

# Create last_contact_date more efficiently
campaign.loc[:, "last_contact_date"] = pd.to_datetime(
    "2022-" + campaign["month"] + "-" + campaign["day"].astype(str),
    format="%Y-%b-%d"
)

# Drop unnecessary columns more cleanly
campaign.drop(columns=["month", "day"], inplace=True)

# Save tables to individual csv files
client.to_csv("client.csv", index=False)
campaign.to_csv("campaign.csv", index=False)
economics.to_csv("economics.csv", index=False)
