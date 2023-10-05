import requests

url = "https://spclient.wg.spotify.com/signup/public/v2/account/create"

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://www.spotify.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 "
                  "Safari/537.36 "
}

data = {
    "account_details": {
        "birthdate": "1990-03-12",
        "consent_flags": {
            "eula_agreed": True,
            "send_email": True,
            "third_party_email": True
        },
        "display_name": "gorfrogleim",
        "email_and_password_identifier": {
            "email": "danacolvin11185@gmail.com",
            "password": "077108803GBH"
        },
        "gender": 1
    },
    "callback_uri": "https://www.spotify.com/signup/challenge?forward_url=https%3A%2F%2Fopen.spotify.com%2F&locale=us",
    "client_info": {
        "api_key": "a1e486e2729f46d6bb368d6b2bcda326",
        "app_version": "v2",
        "capabilities": [1],
        "installation_id": "85dce335-7a0e-4381-855f-b0e8c37cba44",
        "platform": "www"
    },
    "tracking": {
        "creation_flow": "",
        "creation_point": "spotify.com",
        "referrer": ""
    },
    # "recaptcha_token": "03AFcWeA56s"
    #                    "-LEyQXlq6UnBm4xae_z5Hp34qAG8LBU1wUhl5N0IdNNgrasF7Ad5QVujbhsSP0EllrTMOwgwspd98G6ceEThlUrAGde"
    #                    "8dvdXY4PjQV-0vJtNUaAiVg6bhFikbrXtklj3CCIbd67oH-nrm2RM5COCPiH96S6-0E4MEYNU8KclzA2kd3JNAeYgsaVO7"
    #                    "ooUXODjV-9sFij01OLgpsK7nq_bO7RM1VkEKfZozA6UyM0Vt2mx3vaKLsi5iUzpQ4CZg-T1IdThmCc_SnRsDSV-qUd"
    #                    "JKw00UOmankmKYqnmk0Ib9WWNblgK34HwRtfn0RFEStO-7_2Guh0_zFCynEoEIoDE5WhcyIrVkb_jCOcuAfvu9vTZ8ej"
    #                    "Z2hjVixZEGpLJRBdVnLxm_w9gQijYPsoyJ5NsHiKQ6v_SIpe4WSEM3P7Hil0oXrJgIXdQpaEodkgdKT6xiQ5o5ZDLWa1Z"
    #                    "ao_j9TUeXyXjsc_JM7iock-jWVe6FgNTq9BhCGv4abshN9khGDkSmrgU-tEP7a5yvshl8H9b1XdFG3m6J_z_Dn2R9MSki"
    #                    "t8ZRVbMZwkPs_0LIPAMCcc5dGaW29P783KV5AtFrEvPh2P4pVatzNr-qFG7kmykhMnOQKr6HnK1io98eCponkHDGxsbvxR"
    #                    "3AlYGhutgHUc0P_ArqCHWXPW7pk89eiyWj3vstC1Rd3yK62hARRVMuforEpH4K0W0WSPZ7HIc9WSzFs3f6IcKphJZ6Z0fN"
    #                    "AJnO8pxRCtxiqp_qZjYM_aaFXxuX-IKxs9SsXgCWxknlsJ3Lf8Jg4t6lhFTmzj0jJ307Ef-5lkCH4G6FzcWeky1Xe8TZdej"
    #                    "0zqaBAWcmoIrHVsbSieVUznIVZyIr9dnTwu3W2_38UZNlbRX8up71OojGhyJKfwLw_rA8gsBkBN1lLXvuYorCLpvhedgg"
    #                    "r6J2Nf0rnJLjodk5yD11rXggjJMtPwWFlZT75qncMI4mBZIkWCFdTZoayae6SDHuQ4J0B2sXBHe-qvUj84j22d9AnRWKu"
    #                    "lCGXn-epLLZAKo_fpDNOTvlB-GUp9tugcN88Awc1rI7Zf_UXUut3SCdA0Kpt1BZXaaihwIdpNsL3dcScBe8pezHyUO-a"
    #                    "y9AkjnMDghy6FAToP5Cfsw4b9d3OJQOuXsbCLFu3CUfCZ_c2CoXvmg42_54I4HK-iOOvGM3iXrJQHe0GJR_jtaPX9JLR_"
    #                    "q9IXvTKAQ_ISbwPr_geJ1TXtDtoAHRdd1RbRUbh4e1kpUF8zTMOnoi_fyoJPP_Nm539kmydFZtCqxv1rxITwQ-6oXYDD"
    #                    "VmhPVlXfqeP1zueQs-WWiRQCDO21fIBCVy-V19OqMdGTvhyc89p6kpoqjRFk0U8WqNRVwot46tt7zSgG196a7NlYX9_G"
    #                    "5i-hnB-8WQW80JUvXkEYuCFgF6F8BNWZE2K-WFxrAdIp_sT4z0L2AQDmxZmdMbckUuNMss7_MHnwTC5GKhQNrSWJRa0FWJ"
    #                    "hhozRTkZjQnRaPcHQskBJt05RmIT5QOaoFBfsiHywc6MnKOMTnK8ID2WXnGdfG7TShBHOiCuEfrg",
    # "submission_id": "99345965-478b-484f-8f9e-0c2b26dd9c0c",
    "flow_id": "873d4d52-8685-494f-8007-604dab388d2e"
}

response = requests.post(url, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    print("Request was successful.")
    print(response.json())
else:
    print("Request failed with status code:", response.status_code)
    print(response.text)
