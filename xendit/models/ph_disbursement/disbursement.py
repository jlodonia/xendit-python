from typing import List

from .disbursement_bank import DisbursementBank

from xendit.models._base_model import BaseModel

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError


class Disbursement(BaseModel):
    """Disbursement class (API Reference: Disbursement)

    Related Classes:
      - DisbursementBank

    Static Methods:
      - Disbursement.create (API Reference: /Create Disbursement)
      - Disbursement.get (API Reference: /Get Disbursement by ID)
      - Disbursement.get_by_ext_id (API Reference: /Get Disbursement by External ID)
      - Disbursement.get_available_banks (API Reference: /Get Available Banks)

    Attributes:
      - user_id (str)
      - external_id (str)
      - amount (int)
      - bank_code (str)
      - account_holder_name (str)
      - disbursement_description (str)
      - status (str)
      - id (str)

    Optional Attributes:
      - email_to (str[])
      - email_cc (str[])
      - email_bcc (str[])

    """

    reference_id: str
    channel_code: str
    account_number: str
    account_name: str
    disbursement_description: str
    currency: str
    amount: float
    id: str

    # Optional
    beneficiary: dict
    receipt_notification: dict

    # part of receipt_notification
    email_to: List[str]
    email_cc: List[str]
    email_bcc: List[str]

    @staticmethod
    def create(
        *,
        reference_id,
        channel_code,
        account_number,
        account_name,
        description,
        currency,
        amount,
        beneficiary=None,
        receipt_notification=dict,
        x_idempotency_key=None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create Disbursement (API Reference: Disbursement/Create Disbursement)

        Args:
          - reference_id (str)
          - channel_code (str)
          - account_number (str)
          - account_name (str)
          - description (str)
          - currency (str)
          - amount (float)
          - **email_to (str[])
          - **email_cc (str[])
          - **email_bcc (str[])
          - **for_user_id (str)
          - **x_idempotency_key (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          Disbursement

        Raises:
          XenditError

        """
        url = "/disbursements"
        headers, body = _extract_params(
            locals(),
            func_object=Disbursement.create,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            api_source="PH"
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Disbursement(**resp.body)
        else:
            raise XenditError(resp)