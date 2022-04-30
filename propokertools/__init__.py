from propokertools import network


def run_query(query: str) -> dict[str, str] or Exception:
    """
    Run any given query
    """
    connection = network._check_connection()
    if connection:
        response = network._make_request(query)
        if isinstance(response, int):
            raise Exception(
                "Error in connecting to the server. Status code: {}".format(response))
        else:
            return network._parse_response(response)
    else:
        raise Exception(connection)
