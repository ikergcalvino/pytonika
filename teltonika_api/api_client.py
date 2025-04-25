import requests

from typing import Any, Dict, List, Optional, Tuple, Union


class ApiClient:
    def __init__(self, base_url: str):
        self._api_base_url = base_url.rstrip("/") + "/api"
        self._auth_token: Optional[str] = None
        self._session = requests.Session()

    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        url = f"{self._api_base_url}{endpoint}"

        headers = {"Content-Type": "application/json"}

        if self._auth_token:
            headers["Authorization"] = f"Bearer {self._auth_token}"

        try:
            response = self._session.request(
                method=method.upper(),
                url=url,
                json=data,
                params=params,
                headers=headers,
                timeout=10
            )

            response_data = response.json()

            if response.ok and response_data.get("success", False):
                return True, response_data.get("data", {})
            else:
                return False, response_data.get("errors", [])

        except requests.exceptions.RequestException as e:
            return False, [{"source": "client", "error": str(e), "code": 0}]

        except ValueError as e:
            return False, [{"source": "client", "error": f"Invalid JSON response: {str(e)}", "code": 0}]

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        return self._make_request("GET", endpoint, params=params)

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        return self._make_request("POST", endpoint, data=data)

    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        return self._make_request("PUT", endpoint, data=data)

    def delete(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        return self._make_request("DELETE", endpoint, data=data)
