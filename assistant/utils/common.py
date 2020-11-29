from django.views.decorators.http import require_GET, require_POST, require_http_methods

require_PUT = require_http_methods(["PUT"])
require_DELETE = require_http_methods(["DELETE"])
