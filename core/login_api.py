import requests

url = "https://spclient.wg.spotify.com/signup/public/v2/account/create"

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7",
    "content-type": "application/json",
    "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://www.spotify.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",  # Add your User-Agent here

}

data = {
    "account_details": {
        "birthdate": "1990-04-21",
        "consent_flags": {
            "eula_agreed": True,
            "send_email": True,
            "third_party_email": False
        },
        "display_name": "Gor",
        "email_and_password_identifier": {
            "email": "gowedsadwr@gmail.com",
            "password": "077108803Gb"
        },
        "gender": 1
    },
    # "callback_uri": "https://www.spotify.com/signup/challenge?forward_url=https%3A%2F%2Faccounts.spotify.c"
    #                 "om%2Fen%2Fstatus%3Fflow_ctx%3Dc9d573b3-b1da-4c29-88c4-e0f8e9c25d63%3A1696803002&locale=us",
    # "client_info": {
    #     "api_key": "a1e486e2729f46d6bb368d6b2bcda326",
    #     "app_version": "v2",
    #     "capabilities": [1],
    #     "installation_id": "85dce335-7a0e-4381-855f-b0e8c37cba44",
    #     "platform": "www"
    # },
    # "tracking": {
    #     "creation_flow": "",
    #     "creation_point": "https://support.spotify.com/us/podcasters/article/setting-up-spotify-payouts/",
    #     "referrer": ""
    # },
    # "recaptcha_token": "03AFcWeA7E2VA47EvOFlnvC21dOzUlMgAXP7suqm_TaKXfh6IsyEyibTbbLQFMOMitT3EszB1AYximudVM"
    #                    "Qs9Bhs8eTuF31nTbAwo1RLo1Alc6DktGHkxOmEq7ZWrYOWd_tdRfAFvVcwwIq8XmiT-Dp0dw2tM94gfLraJGwiolxJBhu"
    #                    "0PWVDs7kNQdG3XB2o1lJYo_4BxTI9l2g4mBZg-PNT8Imtji9pO-cU_EIdBXDxm0Ovtp6SAxX0eK8B-RedlhBMwHMalC1"
    #                    "BLYEZ33xYRf5QgpYCqOewIZ0oZVfl1gqP58Qfcpy3tZVpvM6HpnvMYCsH1nHmtbBx09YWgjGnJUMxYKm-HbPvl448"
    #                    "sPxJ37dN8T7DYgLr0MkzCTL0TyZ_bqGNs9Y5pCNGnLKfj_QH-Kg-dIUHS8b1BFNfFlKwftfigOKhfXUzyXJvNtEm"
    #                    "AFTFQS-Sy8gsTnPsITv1T04JmD-w_xRQLV8BDwyZujan9F_QiWns27juDolXRgt-1IUtIBETFe9qrSGsX5htvb0XLjAQF"
    #                    "Xd5EbU1Jo2fAv"
}

# params = {
#     "submission_id": "2ccf80d5-77a5-4e98-a7a0-bf2db350d99f",
#     "flow_id": "41729ac4-a405-4024-816f-e13385080d94"
# }

response = requests.post(url, json=data, headers=headers)

print(response.content)
