import requests
import pandas as pd
from requests.auth import HTTPBasicAuth
from config import ODK_URL, USERNAME, PASSWORD

def get_form_data(project_id, form_id):

    url = f"{ODK_URL}/v1/projects/{project_id}/forms/{form_id}.svc/Submissions"

    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            headers={"Accept": "application/json"}
        )

        response.raise_for_status()

        data = response.json()["value"]

        df = pd.json_normalize(data)

        return df

    except Exception as e:
        print(e)
        return pd.DataFrame()
