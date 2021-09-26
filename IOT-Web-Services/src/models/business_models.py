
class JsonResultViewModel():

    def __init__(
            self,
            result=None,
            request_code=None,
            success_message=None,
            error_message=None,
            exception=None):
        self.result = result
        self.request_code = request_code
        self.success_message = success_message
        self.error_message = error_message
        self.exception = exception
